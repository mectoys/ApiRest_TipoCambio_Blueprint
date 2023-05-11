
class Email:

    def __init__(self, email , fecharegister=None):
        self.email = email
        self.fecharegister= fecharegister

    def convert_to_JSON(self):
        return{
            'email': self.email,
            'fecharegister': self.fecharegister
        }