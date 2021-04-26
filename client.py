import requests

class Client():
    def __init__(self):
        self.session = requests.Session()


    def get_user_by_username(self, username) -> dict:
        req = self.session.get('https://ReplREST.lamaqdahodwala.repl.co/api/user/{}'.format(username))
        json = req.json()
        return json        
    def get_board(self, boardname) -> dict:
        req = self.session.get('https://ReplREST.lamaqdahodwala.repl.co/api/board/{}'.format(boardname))
        json = req.json()
        return json
