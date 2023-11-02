from passlib.context import CryptContext
psw_context = CryptContext(schemes="bcrypt", deprecated = "auto")

class Hash():
    def bcrypt(password:str):
        return psw_context.hash(password)
    