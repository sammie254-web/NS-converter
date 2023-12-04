from kivymd.app import App
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.menu import MDDropdownMenu

class Number_systems(GridLayout):
    def dropdown_from(self):
        self.menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": "Binary",
                "on_release": lambda x = "Binary" : self.binary_from()

            },
            {
                "viewclass": "OneLineListItem",
                "text": "Octal",
                "on_release": lambda x="Binary": self.octal_from()

            },
            {
                "viewclass": "OneLineListItem",
                "text": "Decimal",
                "on_release": lambda x="Binary": self.decimal_from()

            },
            {
                "viewclass": "OneLineListItem",
                "text": "Hexadecimal",
                "on_release": lambda x="Binary": self.hexadecimal_from()

            }
        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.menu_from,
            items=self.menu_list,
            width_mult = 4
        )
        self.menu.open()

    def binary_from(self):
        from_value = "binary"
        self.from_values = from_value
        from_v = self.from_values
    def octal_from(self):
        from_value = "octal"
        self.from_values = from_value

    def decimal_from(self):
        from_value = "decimal"
        self.from_values = from_value

    def hexadecimal_from(self):
        from_value = "hexadecimal"
        self.from_values = from_value

    def dropdown_to(self):
        self.menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": "Binary",
                "on_release": lambda x = "Binary" : self.binary_to()

            },
            {
                "viewclass": "OneLineListItem",
                "text": "Octal",
                "on_release": lambda x="Binary": self.octal_to()

            },
            {
                "viewclass": "OneLineListItem",
                "text": "Decimal",
                "on_release": lambda x="Binary": self.decimal_to()

            },
            {
                "viewclass": "OneLineListItem",
                "text": "Hexadecimal",
                "on_release": lambda x="Binary": self.hexadecimal_to()

            }
        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.menu_to,
            items=self.menu_list,
            width_mult = 4
        )
        self.menu.open()

    def binary_to(self):
        to_value = "binary"
        self.to = to_value


    def octal_to(self):
        to_value = "octal"
        self.to = to_value

    def decimal_to(self):
        to_value = "decimal"
        self.to = to_value

    def hexadecimal_to(self):
        to_value = "hexadecimal"
        self.to = to_value

    def convert(self):

        from_v = ""
        to_v = ""
        try:
            from_v = self.from_values
        except:
            pass
        try:
            to_v = self.to
        except:
            pass

        number_system = ""
        try:
            number_system = self.ids.value.text
        except:
            pass

        if from_v == "binary" and to_v == "octal":
            decimal = ""
            answer =""
            try:
                decimal = int(self.ids.value.text,2)
                answer = oct(decimal)
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "binary" and to_v == "decimal":
            answer = ""
            try:
                answer = int(self.ids.value.text,2)
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "binary" and to_v == "hexadecimal":
            answer = ""
            decimal = ""
            try:
                decimal = int(self.ids.value.text,2)
                answer = hex(decimal)
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "octal" and to_v == "binary":
            answer = ""
            decimal = ""
            try:
                decimal = int(self.ids.value.text, 8)
                answer = bin(decimal)
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "octal" and to_v == "decimal":
            answer = ""
            try:
                answer = int(self.ids.value.text, 8)
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "octal" and to_v == "hexadecimal":
            answer = ""
            decimal = ""
            try:
                decimal = int(self.ids.value.text, 8)
                answer = hex(decimal)
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "decimal" and to_v == "binary":
            answer = ""
            try:
                answer = bin(int(self.ids.value.text))
            except:
                print("error")
            self.ids.result_label.text = str(answer)

        if from_v == "decimal" and to_v == "octal":
            answer = ""
            try:
                answer = oct(int(self.ids.value.text))
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "decimal" and to_v == "hexadecimal":
            answer = ""
            try:
                answer = hex(int(self.ids.value.text))
            except:
                pass
            self.ids.result_label.text = str(answer)


        if from_v == "hexadecimal" and to_v == "binary":
            answer = ""
            decimal = ""
            try:
                decimal = int(self.ids.value.text, 16)
                answer = bin(decimal)
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "hexadecimal" and to_v == "octal":
            answer = ""
            decimal = ""
            try:
                decimal = int(self.ids.value.text, 16)
                answer = oct(decimal)
            except:
                pass
            self.ids.result_label.text = str(answer)

        if from_v == "hexadecimal" and to_v == "decimal":
            answer = ""
            try:
                answer = int(self.ids.value.text, 16)
            except:
                pass
            self.ids.result_label.text = str(answer)


class numbersApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"

numbersApp().run()