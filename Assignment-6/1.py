class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        return None

    def set_password(self,new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False
    
    def is_correct(self,string):
        if(string == self.old_passwords[-1]):
            return True
        else:
            return False

pm = Password_manager()
pm.set_password("Hello123")
print(pm.get_password())
print(pm.set_password("Hello123"))