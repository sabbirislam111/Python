
class User():
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.email = f"{f_name}.{l_name}@user.com"

    def full_name(self):
        print(f"{self.f_name} {self.l_name}")


mark = User("mark","jukar")
print(mark.f_name)
print(mark.l_name)
print(mark.email)

mark.full_name()