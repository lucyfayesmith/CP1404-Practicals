from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


# class DynamicWidget(App):
#
#     def __int__(self, **kwargs):
#         self.name_list = ["Molly Smith", "Scott Smith", "Lucy Smith"]
#
#     def build(self):
#         self.title = 'List of Names'
#         self.root = Builder.load_file('list_of_names.kv')
#         self.create_widgets()
#
#     def create_widgets(self):
#         for name in self.name_list:
#             temp_button = Button(text=name, id=name)


class NameList(App):
    def __int__(self, **kwargs):
        self.names = ['Molly Smith', 'Scott Smith', 'Lucy Smith']

    def build(self):
        self.title = 'List of Names'
        self.root = Builder.load_file('list_of_names.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.name_label.add_widget(temp_label)


NameList().run()
