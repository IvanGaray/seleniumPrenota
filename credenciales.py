chat_id = "" #Your chat Id in telegram between you and your bot
message = "hello from your telegram bot"

class loginPrenota:
    def __init__(self, email:str, password:str):
        self.email = email
        self.password = password

usuario = loginPrenota('yourMail','yourPass')

TOKEN = '' #Your token
hayTurno = "¡Pudes sacar turno!" 
noHayTurno = "No hay turnos todavía." 