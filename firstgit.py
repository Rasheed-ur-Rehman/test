##class user():
##    def __init__(self,first_name,last_name,gender,email,password):
##        self.first_name=first_name
##        self.last_name=last_name
##        self.gender=gender
##        self.email=email
##        self.password=password
##        self.login_attempts=0
##    def describe_user(self):
##        print(f"User Name Is :{self.first_name}(self.last_name)")
##        print(f"user is {self.gender}by gender")
##        print(f"user email addreee is {self.emsil}")
##    def greet_user(self):
##        if self.gender.lower()=="female":
##            print(f"WelCome Miss {self.first_name} {self.last_name}")
##        else:
##            print(f"WelCome Mr {self.first_name} {self.last_name}")
##    def increment_login(self):
##        self.login_attempts+=1
##    def reset_login():
##        self.login_attempts=0
##
class User():
    def __init__(self,first_name, last_name, gender, email, password):
        self.first_name = first_name
        self.last_name =last_name
        self.gender =gender
        self.email =email
        self.password =password
        self.login_attempts = 0
    def describe_user(self):
        print(f"User name is: {self.first_name} {self.last_name}")
        print(f"User is {self.gender} by gender")
        print(f"User email address is {self.email}")
    def greet_user(self):
        if self.gender.lower()=="female":
            print(f"Welcome Miss {self.first_name} {self.last_name}")
        else:
            print(f"Welcome Mr. {self.first_name} {self.last_name}")
    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self,first_name, last_name, gender, email, password,privileges):
        super().__init__(first_name, last_name, gender, email, password)
        self.privileges=privileges
        
def show_privileges(self):
    print("admin privallige are ")
    for priv in self.privileges:
        print(priv)
def show_admin(self):
    print(f"(self.first_name) (self.last_name)")
    print(f"(self.gender)")
    print(f"(self.email)")
    print(f"(self.password)")
    print(f"(self.privileges)")
Admin1=Admin("abc",'defghij','male',"ras@gmail.com","2342","abc")
print(Admin1.first_name)
print(Admin1.last_name)
print(Admin1.gender)
print(Admin1.email)
print(Admin1.password)


