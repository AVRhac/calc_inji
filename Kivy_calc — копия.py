from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):   
        main_layout=BoxLayout(orientation="vertical")
        self.solution=TextInput(font_size=40)
        main_layout.add_widget(self.solution)
        button_plus=["+"]

        for i in button_plus:
            h_layout=BoxLayout()
            for label in i:
                button= Button(text='+')
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        eq_button=Button(text='=')
        eq_button.bind(on_press=self.on_solution)
        main_layout.add_widget(eq_button)
        return main_layout
    def on_button_press(self, instance):
        cur=self.solution.text
        button_text=instance.text
        new_text=cur+button_text
        self.solution.text=new_text
        
        self.last_button=button_text
    def on_solution(self, instance):
        text=self.solution.text
        if text:
            solution=str(eval(self.solution.text))
            self.solution.text=solution
if __name__=='__main__':
    app=MainApp()
    app.run()
                    

