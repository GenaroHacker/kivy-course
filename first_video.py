import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='Name:'))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        
        self.inside.add_widget(Label(text='Age:'))
        self.age = TextInput(multiline=False)
        self.inside.add_widget(self.age)

        self.inside.add_widget(Label(text='Job:'))
        self.job = TextInput(multiline=False)
        self.inside.add_widget(self.job)

        self.add_widget(self.inside)

        self.submit = Button(text='Submit', font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        print('Name: ' + self.name.text)
        print('Age: ' + self.age.text)
        print('Job: ' + self.job.text)

        self.name.text = ""
        self.age.text = ""
        self.job.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
