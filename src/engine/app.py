import flet as ft
import asyncio
from Engine import Engine
from PdfGen import generate_filled_cheque
from datetime import datetime
from Facerecogination.reco import Facerecogination

class BankAssistantApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Bank Form Assistance System"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.engine = Engine()

        self.faceRecogination = Facerecogination()

        # Define reusable TextFields
        self.name_field = ft.TextField(label="Account Holder Name", width=300)
        self.account_field = ft.TextField(label="Account Number", width=300)
        self.amount_field = ft.TextField(label="Amount", width=300)

        # Route Handling
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

        # Task to destroy when user is not on a FORM INPUT page
        self.form_input_task = None
        self.page.go( "/")

    def home_view(self):
        navbar = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("Bank Form Assistance System", size=20, weight="bold", color=ft.Colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor="#5c6bc0",
            padding=20,
        )

        # to resolve the error await can only be use in a async function
        # created this function and called it in button clicks
        async def push_route_withdraw(e):
            await self.page.push_route("/withdraw")
        async def push_route_deposit(e):
            await self.page.push_route("/deposit")

        content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Main Menu", size=28, weight="bold", color="#333333"),
                ft.FilledButton(
                    content=ft.Row([ft.Text("💵"), ft.Text("Withdraw Money")], alignment=ft.MainAxisAlignment.CENTER),
                    on_click= push_route_withdraw,
                    width=300, height=50
                ),
                ft.FilledButton(
                    content=ft.Row([ft.Text("🧾"), ft.Text("Deposit Money")], alignment=ft.MainAxisAlignment.CENTER),
                    on_click= push_route_deposit,
                    width=300, height=50,
                ),
            ],
            spacing=20,
        )

        return ft.View(
            route="/",
            controls=[navbar, content],
            bgcolor="#f0f2f5",
            padding=0
        )

    def transaction_ui(self, mode="Withdraw"):
        return ft.View(
            route=f"/{mode.lower()}",
            controls=[
                ft.AppBar(title=ft.Text(f"{mode} Service"), bgcolor="#5c6bc0", color="white"),
                ft.Container(
                    padding=40,
                    content=ft.Column([
                        ft.Text(f"{mode} Form", size=24, weight="bold"),
                        self.name_field,
                        self.account_field,
                        self.amount_field,
                        ft.Row([
                            ft.OutlinedButton("← Menu", on_click=lambda _: self.page.go("/")),
                            ft.FilledButton("🔄 Reset", on_click=self.reset_fields),
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
                )
            ]
        )


    async def route_change(self, e):
        self.page.views.clear()

        if self.page.route == "/":

            # Capture and recognize immediately
            self.faceRecogination.capture()
            name = self.faceRecogination.faceReco()

            if name:
                self.engine.name = name
                self.engine.speak(f"नमस्ते {name} जी, आपका स्वागत है")

            self.page.views.append(self.home_view())
            self.page.run_task(self.run_voice_intent_input)

        elif self.page.route == "/withdraw":
            self.engine.intent = self.engine.WITHDRAW
            self.page.views.append(self.transaction_ui("Withdraw"))
            self.form_input_task = self.page.run_task(self.run_voice_sequence_form_input)

        elif self.page.route == "/deposit":
            self.engine.intent = self.engine.DEPOSIT
            self.page.views.append(self.transaction_ui("Deposit"))
            self.form_input_task = self.page.run_task(self.run_voice_sequence_form_input)

        self.page.update()


    def faceReco(self):
        self.engine.name = self.faceRecogination.faceReco()

    async def view_pop(self, e):
        if len(self.page.views) > 1:
            self.page.views.pop()
            top_view = self.page.views[-1]
            self.page.go(top_view.route)

    async def reset_fields(self, e):
        self.name_field.value = ""
        self.account_field.value = ""
        self.amount_field.value = ""
        self.page.update() # REMOVED AWAIT

    # --- VOICE LOGIC ---

    async def run_voice_intent_input(self):
        await self.getIntent()


    async def run_voice_sequence_form_input(self):

        # If already recognized
        if self.engine.name:
            self.engine.speak(f"नमस्ते {self.engine.name} जी")

        else:
            # New user flow
            await self.getName()

            # Capture face AFTER getting name
            self.faceRecogination.capture()

            # Save new user
            self.faceRecogination.saveUser(self.engine.name)

        await self.getAccount()
        await self.getAmount()

        self.genPdf()
        await self.reset_fields(None)
        await self.page.push_route("/")


        

    async def getIntent(self):
        intent = ""
        while self.page.route == "/":
            # to_thread prevents the Vosk model from freezing the GUI
            if await asyncio.to_thread(self.engine.getIntent):
                intent = self.engine.intent
                break
            await asyncio.sleep(0.1)
        
        if (intent == self.engine.WITHDRAW): await self.page.push_route("/withdraw")
        elif (intent == self.engine.DEPOSIT): await self.page.push_route("/deposit")
        



    async def getName(self):

        while self.page.route != "/":
            if await asyncio.to_thread(self.engine.getName):

                self.name_field.value = self.engine.name
                self.page.update()
                break

            await asyncio.sleep(0.1)


    async def getAccount(self):
        while self.page.route != "/":
            if await asyncio.to_thread(self.engine.getAccount):
                self.account_field.value = str(self.engine.account)
                self.page.update()
                break
            await asyncio.sleep(0.1)

    async def getAmount(self):
        while self.page.route != "/":
            if await asyncio.to_thread(self.engine.getAmount, ):
                self.amount_field.value = str(self.engine.amount)
                self.page.update()
                break
            await asyncio.sleep(0.1)

    def genPdf(self):
        generate_filled_cheque(
            name=self.engine.name,
            amount_num=int(str(self.engine.amount).replace(" ", "")),
            amount_words=self.engine.word_amount,
            acc_num=str(self.engine.account),
            date_val=datetime.now().strftime("%d/%m/%Y")
        )


    

# --- ENTRY POINT ---

async def main(page: ft.Page):
    app = BankAssistantApp(page)
    await app.route_change(None)

if __name__ == "__main__":
    ft.run(main)














































