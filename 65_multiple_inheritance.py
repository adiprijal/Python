class Freelancer:
    company="Fiverr"
    level=1

    def upgradeLevel(self):
        self.level=self.level+1

class Internet:
    company="Google"
    post="Executive Head"

class employee(Internet,Freelancer):
    name="Adip"

e=employee()
print("Level",e.level)
e.upgradeLevel()
print('Level',e.level)
print(e.post)
print(e.name)
print(e.company)        # ***company(Internet,Freelancer) ->Internet is used at first