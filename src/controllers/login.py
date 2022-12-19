from src.models.login import LoginModel

loginModel = LoginModel()

class LoginController():
    def validateLogin(self, username):
        return loginModel.validateLogin(username)

    def validateAccount(self, email):
        return loginModel.validateAccount(email)

    def createAccount(self, username, password, email):
        loginModel.createAccount(username, password, email)

    def profileAccount(self, idu):
        return loginModel.profileAccount(idu)