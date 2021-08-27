from model.account import Account
from model.bank import Bank

# création des bank

GBA = Bank("GBA")
QBA = Bank("QBA")
IBA = Bank("IBA")
FBA = Bank("FBA")

# Début du programme

print("Bonjour quel bank souhaitait-vous ?")
print("Les bank disponible sont: GBA, QBA, IBA, FBA")
print("Pour créer un compte sur l'une de ces bank, il faut entrer le nom de la bank en question")
print("Entrer le nom de la bank ou vous souhaitait vous créer un compte")

bank_choice = input("")

if bank_choice == "GBA":
    print("Quel est votre nom ?")
    name_user = input("")
    print("Quel est votre age ?")
    age_user = int(input(""))
    print("Quel est votre email ?")
    email_user = input("")
    print("Quel est votre mot de passe ?")
    password_user = input("")
    print("Quel est l'argent que vous avez actuelement ?")
    human_money_user = int(input(""))
    if human_money_user <= 0:
        print("Vous n'avez pas assez d'argent pour créer un compte")
    else:
        user_account = Account("GBA", name_user, password_user, email_user, age_user, human_money_user, 0)

elif bank_choice == "QBA":
    print("Quel est votre nom ?")
    name_user = input("")
    print("Quel est votre age ?")
    age_user = int(input(""))
    print("Quel est votre email ?")
    email_user = input("")
    print("Quel est votre mot de passe ?")
    password_user = input("")
    print("Quel est l'argent que vous avez actuelement ?")
    human_money_user = int(input(""))
    if human_money_user <= 0:
        print("Vous n'avez pas assez d'argent pour créer un compte")
    else:
        user_account = Account("GBA", name_user, password_user, email_user, age_user, human_money_user, 0)
elif bank_choice == "IBA":
    print("Quel est votre nom ?")
    name_user = input("")
    print("Quel est votre age ?")
    age_user = int(input(""))
    print("Quel est votre email ?")
    email_user = input("")
    print("Quel est votre mot de passe ?")
    password_user = input("")
    print("Quel est l'argent que vous avez actuelement ?")
    human_money_user = int(input(""))
    if human_money_user <= 0:
        print("Vous n'avez pas assez d'argent pour créer un compte")
    else:
        user_account = Account("GBA", name_user, password_user, email_user, age_user, human_money_user, 0)
elif bank_choice == "FBA":
    print("Quel est votre nom ?")
    name_user = input("")
    print("Quel est votre age ?")
    age_user = int(input(""))
    print("Quel est votre email ?")
    email_user = input()
    print("Quel est votre mot de passe ?")
    password_user = input("")
    print("Quel est l'argent que vous avez actuelement ?")
    human_money_user = int(input(""))
    if human_money_user <= 0:
        print("Vous n'avez pas assez d'argent pour créer un compte")
    else:
        user_account = Account("GBA", name_user, password_user, email_user, age_user, human_money_user, 0)
else:
    print("Nous ne proposont pas ces bank merci de réessayer le programme")

print("Votre compte chez", user_account.bank, "a bien était créer avec l'addresse email suivante:", user_account.email)
print("Voulez-vous vous connecter a votre compte ?")
print("Si oui merci d'entrer 'yes' ou 'no'")
login_choice = input("")
if login_choice == "yes":
    print("Quel est votre email ?")
    email_login = input("")
    if email_login == user_account.email:
        print("Quel est votre password")
        password_login = input("")
        if password_login == user_account.password:
            print("Vous êtes bien connecter !")
        else:
            print("Le mot de passe insséré n'est pas le bon")
    else:
        print("Aucun compte n'est relié a cette addresse email !")


print("Quel action voulez vous faire ?")
print("Retiré de l'argent: withdraw")
print("déposé de l'argent: deposit")
print("Avoir des information sur votre compte: account_info")

action_account = input("")

if action_account == "withdraw":
    print("Combien voulez vous retiré ?")
    numbers_money = int(input(""))
    user_account.withdraw_money(numbers_money)
elif action_account == "deposit":
    print("Combien souhaitait-vous déposé d'argent ?")
    dep_money = int(input(""))
    user_account.deposited_money(dep_money)
elif action_account == "account_info":
    user_account.account_info()

print("Souhaitait vous faire une autre action ?")
continues = input("")

