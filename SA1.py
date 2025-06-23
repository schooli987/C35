#firebase configuration, write into the database and change to dashboard screen

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner

import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


signedin_user=""
signedin_name=""


# --- Color Theme ---
Window.clearcolor = (0.01, 0.09, 0.17, 1)  # Dark Navy Blue

PRIMARY_COLOR = (0.2, 0.6, 0.8, 1)  # Teal Blue
SECONDARY_COLOR = (0.1, 0.4, 0.6, 1)
TEXT_COLOR = (1, 1, 1, 1)
BUTTON_TEXT_COLOR = (1, 1, 1, 1)

# --- Globals ---S
sm = ScreenManager()
sm.transition = SlideTransition()

user_data = {
    "otp": "",
    "email": "",
    "password": "",
    "name": ""
}

email_input_signup = None
otp_input_signup = None


# --- Popup ---
def show_popup(title, message):
    popup = Popup(title=title, content=Label(text=message, color=TEXT_COLOR),
                  size_hint=(None, None), size=(300, 200),
                  background_color=SECONDARY_COLOR)
    popup.open()

# --- Navigation ---
def go_to_signup(instance):
    sm.transition.direction = 'left'
    sm.current = 'signup'

def go_to_login(instance):
    sm.transition.direction = 'right'
    sm.current = 'login'

# --- OTP Verification ---

def verify_otp(instance):
    global otp_input_signup
    user_data["email"]
    entered_otp = otp_input_signup.text.strip()
    if entered_otp == user_data["otp"]:
        show_popup("Success", "OTP verified! You are signed up.")
        sm.current = "dashboard"
        user_data["name"] = name_input_signup.text.strip()
        user_data["password"] = password_input.text.strip()
        user_data["email"]=email_input_signup.text.strip()
        email = user_data["email"]
        password = user_data["password"]
        name = user_data["name"]
       
    else:
        show_popup("Error", "Invalid OTP. Please try again.")
    

# --- Send OTP Email ---
def send_otp(instance):
    global email_input_signup
    email = email_input_signup.text.strip()
    if not email:
        show_popup("Error", "Please enter a valid email.")
        return

    otp = str(random.randint(100000, 999999))
    user_data["otp"] = otp
    user_data["email"] = email

    sender_email = "sehar627@gmail.com"
    sender_password = "ssssjookrehsrjzj"  # App password (not your regular one)
    subject = "Your OTP Code"
    body = f"Your One-Time Password (OTP) is: {otp}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        show_popup("Success", f"OTP sent to {email}")
    except Exception as e:
        show_popup("Error", f"Failed to send email: {str(e)}")

# --- Login Screen ---
def build_login_screen():
    layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
    layout.add_widget(Label(text='[b]Login[/b]', markup=True, font_size=36,
                            size_hint=(1, None), height=60, color=TEXT_COLOR))

    float_layout = FloatLayout(size_hint=(1, 1))

    email_input = TextInput(hint_text='Email', multiline=False,
                            size_hint=(0.6, None), height=50,
                            pos_hint={'center_x': 0.5, 'center_y': 0.7},
                            background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    password_input = TextInput(hint_text='Password', password=True, multiline=False,
                               size_hint=(0.6, None), height=50,
                               pos_hint={'center_x': 0.5, 'center_y': 0.55},
                               background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    submit_btn = Button(text='Login', size_hint=(0.4, None), height=50,
                        pos_hint={'center_x': 0.5, 'center_y': 0.4},
                        background_color=PRIMARY_COLOR, color=BUTTON_TEXT_COLOR)

    float_layout.add_widget(email_input)
    float_layout.add_widget(password_input)
    float_layout.add_widget(submit_btn)

    layout.add_widget(float_layout)

    switch_btn = Button(text='New User? Go to Signup', size_hint=(1, None), height=50,
                        background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR)
    switch_btn.bind(on_press=go_to_signup)
    layout.add_widget(switch_btn)

    return layout

# --- Signup Screen ---
def build_signup_screen():
    global email_input_signup, otp_input_signup,name_input_signup,password_input

    layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
    layout.add_widget(Label(text='[b]Signup[/b]', markup=True, font_size=36,
                            size_hint=(1, None), height=60, color=TEXT_COLOR))

    float_layout = FloatLayout(size_hint=(1, 1))

    name_input_signup= TextInput(hint_text='Name', multiline=False,
                           size_hint=(0.6, None), height=50,
                           pos_hint={'center_x': 0.5, 'center_y': 0.85},
                           background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    email_input_signup = TextInput(hint_text='Email', multiline=False,
                                   size_hint=(0.6, None), height=50,
                                   pos_hint={'center_x': 0.5, 'center_y': 0.70},
                                   background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    password_input = TextInput(hint_text='Password', password=True, multiline=False,
                               size_hint=(0.6, None), height=50,
                               pos_hint={'center_x': 0.5, 'center_y': 0.55},
                               background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    generate_otp_btn = Button(text='Generate OTP', size_hint=(0.4, None), height=40,
                              pos_hint={'center_x': 0.5, 'center_y': 0.40},
                              background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR)
    generate_otp_btn.bind(on_press=send_otp)

    otp_input_signup = TextInput(hint_text='Enter OTP', multiline=False,
                                 size_hint=(0.6, None), height=50,
                                 pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                 background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    verify_btn = Button(text='Verify OTP', size_hint=(0.4, None), height=50,
                        pos_hint={'center_x': 0.5, 'center_y': 0.10},
                        background_color=PRIMARY_COLOR, color=BUTTON_TEXT_COLOR, on_press=verify_otp)


    float_layout.add_widget(name_input_signup)
    float_layout.add_widget(email_input_signup)
    float_layout.add_widget(password_input)
    float_layout.add_widget(generate_otp_btn)
    float_layout.add_widget(otp_input_signup)
    float_layout.add_widget(verify_btn)

    layout.add_widget(float_layout)

    switch_btn = Button(text='Already a user? Go to Login', size_hint=(1, None), height=50,
                        background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR)
    switch_btn.bind(on_press=go_to_login)
    layout.add_widget(switch_btn)

    return layout
def build_dashboard_screen():
    layout = FloatLayout(size_hint=(1, 1))

    welcome_label = Label(
        text='Welcome to the dashboard!',
        size_hint=(None, None), size=(300, 30),
        pos_hint={'center_x': 0.5, 'top': 0.98},
        color=TEXT_COLOR
    )
    layout.add_widget(welcome_label)

    # Info center box as FloatLayout
    info_float = FloatLayout(size_hint=(None, None), size=(600, 90),
                             pos_hint={'center_x': 0.5, 'top': 0.88})

    group_members_spinner = Spinner(
        text='Group Members',
        values=["member1", "member2"],
        size_hint=(None, None), size=(180, 40),
        pos_hint={'x': 0, 'center_y': 0.5},
        background_color=SECONDARY_COLOR,
        color=BUTTON_TEXT_COLOR
    )
    info_float.add_widget(group_members_spinner)

    owe_float = FloatLayout(size_hint=(None, None), size=(120, 60),
                            pos_hint={'x': 0.35, 'center_y': 0.5})
    owe_label = Label(
        text='You Owe', font_size=18,
        size_hint=(1, None), height=25,
        pos_hint={'center_x': 0.5, 'top': 1},
        color=TEXT_COLOR
    )

    owe_float.add_widget(owe_label)
    owe_amount_label = Label(
        text='0', font_size=24,
        size_hint=(1, None), height=35,
        pos_hint={'center_x': 0.5, 'y': 0},
        color=TEXT_COLOR
    )
    owe_float.add_widget(owe_amount_label)
    info_float.add_widget(owe_float)

    other_owe_float = FloatLayout(size_hint=(None, None), size=(150, 60),
                                  pos_hint={'x': 0.65, 'center_y': 0.5})
    other_owe_label = Label(
        text='Other Owe You', font_size=18,
        size_hint=(1, None), height=25,
        pos_hint={'center_x': 0.5, 'top': 1},
        color=TEXT_COLOR
    )
    other_owe_amount_label = Label(
        text='₹0', font_size=24,
        size_hint=(1, None), height=35,
        pos_hint={'center_x': 0.5, 'y': 0},
        color=TEXT_COLOR
    )
    other_owe_float.add_widget(other_owe_label)
    other_owe_float.add_widget(other_owe_amount_label)
    info_float.add_widget(other_owe_float)

    layout.add_widget(info_float)

    # Dummy label for spacing (optional)
    layout.add_widget(Label(size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0}))

    #num_of_col=4+len(group_members)
    table = GridLayout(cols=6, size_hint=(1, None), height=400)
    headers = ['Date', 'Description', 'Paid By', 'Amount','member1','member2'] 
   
    for col in headers:
        table.add_widget(Label(text=col, bold=True, color=TEXT_COLOR))
    layout.add_widget(table)

    btn_layout = BoxLayout(
        orientation='horizontal',
        size_hint=(1, None), height=60, spacing=20, padding=[0, 0, 0, 10]
    )
    add_expense_btn = Button(
       text='Add Expense', size_hint=(0.5, 1)
    ) 

    add_group_members_btn = Button(
       text='Add Group Members', size_hint=(0.5, 1)
    )

    btn_layout.add_widget(add_expense_btn)
    btn_layout.add_widget(add_group_members_btn)
    layout.add_widget(btn_layout)

    return layout
# --- Screens ---
login_screen = Screen(name='login')
login_screen.add_widget(build_login_screen())

signup_screen = Screen(name='signup')
signup_screen.add_widget(build_signup_screen())

dashboard_screen = Screen(name='dashboard')
dashboard_screen.add_widget(build_dashboard_screen())

sm.add_widget(login_screen)
sm.add_widget(signup_screen)
sm.add_widget(dashboard_screen)
# --- App ---
class MyApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyApp().run()
