class Account:

    def __init__(self, bank, name, password, email, age, money_compte, human_money):
        
        self.bank = bank
        self.name = name
        self.password = password
        self.email = email
        self.age = age
        self.money_compte = money_compte
        self.human_money = human_money

    def withdraw_money(self, numbers_money):
        money_human = self.human_money
        compte_money = self.money_compte
        if money_human < numbers_money:
            print("Vous n'avez pas assez d'argent !")
        else:
            compte_money = compte_money - numbers_money
            print("Vous venez de retiré " + numbers_money + "€")

    def deposited_money(self, deposit_money):
        money_human = self.human_money
        compte_money = self.money_compte
        compte_money = compte_money + deposit_money
        money_human = money_human - deposit_money
        if money_human < deposit_money:
            print("Vous avez déposé " + deposit_money + "€")
        else:
            print("Vous n'avez pas assez d'argent !") 

    def account_info(self):
        print("Voici plus d'information sur votre compte: ")
        print("Nom:", self.name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Argent sur le compte:", self.money_compte)