import flet as ft
import asyncio
from Engine import Engine

class WithdrawMoneyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Withdraw Money"
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # 1. Use the new Button class instead of ElevatedButton
        self.name_field = ft.TextField(hint_text="Enter account holder name", width=300)
        self.account_field = ft.TextField(hint_text="Enter your account number", width=300)
        self.amount_field = ft.TextField(hint_text="Enter amount to withdraw", width=300)

        self.create_ui()
        self.engine = Engine()

        # 2. Use Flet's run_task to start the background voice sequence
        # This keeps the logic in the same event loop as the UI
        self.page.run_task(self.run_voice_sequence)

    async def run_voice_sequence(self):
        """Sequential logic for voice input using non-blocking calls"""
        await self.getName()
        await self.getAccount()
        await self.getAmount()

    def create_ui(self):
        header = ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(width=36, height=36, border_radius=18, bgcolor="#9cc4ff"),
                        ft.Text("Bank Form Assistance System", size=18, weight="bold"),
                    ]
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        form = ft.Column(
            controls=[
                ft.Text("Withdraw Money", size=34, weight="bold"),
                ft.Column(
                    controls=[
                        ft.Row([ft.Text("👤 Name", width=150), self.name_field]),
                        ft.Row([ft.Text("# Account", width=150), self.account_field]),
                        ft.Row([ft.Text("💰 Amount", width=150), self.amount_field]),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Button("← Back", on_click=self.back_button_clicked),
                        ft.Button("🖨 Print Form", on_click=self.print_form_button_clicked),
                        ft.Button("🖨 Update", on_click=self.update_fields),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.page.add(header, ft.Divider(), form)

    async def back_button_clicked(self, e):
        print("Back button clicked")

    async def print_form_button_clicked(self, e):
        print(f"Printing: {self.name_field.value}")

    async def update_fields(self, e):
        self.name_field.value = "John Doe"
        self.page.update()

    # Voice Engine Logic - Cleaned up
    async def getName(self):
        print("Listening for name...")
        while True:
            # We wrap the blocking engine call in to_thread to keep UI responsive
            if await asyncio.to_thread(self.engine.getName):
                self.name_field.value = self.engine.name
                self.page.update()
                break
            await asyncio.sleep(0.1)

    async def getAccount(self):
        print("Listening for account...")
        while True:
            if await asyncio.to_thread(self.engine.getAccount):
                self.account_field.value = str(self.engine.account) 
                self.page.update()
                break
            await asyncio.sleep(0.1)

    async def getAmount(self):
        print("Listening for amount...")
        while True:
            if await asyncio.to_thread(self.engine.getAmount):
                self.amount_field.value = str(self.engine.amount)
                self.page.update()
                break
            await asyncio.sleep(0.1)

async def main(page: ft.Page):
    WithdrawMoneyApp(page)

if __name__ == "__main__":
    ft.run(main)