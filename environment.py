# acest fisier ne ajuta la rularea testelor
#importam toate clasele pe care ne ajuta sa interactionam cu paginile, din folderul de "pages" si Browser ul

from browser import Browser
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from pages.test3_page import Test3


# met care va fi apelata inainte de exe tuturor testelor
# context = paramentru care o sa fie initializat cu clasa noastra de pagini & cea de browser
#daca o sa mai adaugam fisiere in pages atunci trebuie sa le adaugam si aici
def before_all(context):
    context.browser = Browser() ## obj de tip browser
    context.login_page = LoginPage()
    context.signup_page = SignUpPage()
    context.test3_page = Test3()


#dupa exe toate testele, vrem sa inchidem browser ul respectiv
def after_all(context):
    context.browser.close()