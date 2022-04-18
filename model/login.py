from controller.webdriver import Element

####################################################################################################################
#                                                  CHECK                                                           #
####################################################################################################################
def check_page_welcome(driver):
    """
    Checa se o navegador está na página.
    :param driver: webdriver
    :return: boolean
    """
    p = Element(driver, 'Tela Welcome')
    p.as_2_class = 'our-story-card-title'
    return p.findBy_Class()

def check_page_login(driver):
    """
    Checa se o navegador está na página.
    :param driver: webdriver
    :return: boolean
    """
    p = Element(driver, 'Tela Login')
    p.as_2_class = 'hybrid-login-form-main'
    return p.findBy_Class()

def check_page_profiles(driver):
    """
    Checa se o navegador está na página.
    :param driver: webdriver
    :return: boolean
    """
    p = Element(driver, 'Tela de Perfis')
    p.as_2_class = 'profile-gate-label'
    return p.findBy_Class()

def check_error_userInvalid(driver):
    """
    Checa se a mensagem de erro é apresentada.
    :param driver: webdriver
    :return: boolean
    """
    e = Element(driver, 'create a new account')
    e.as_5_text = 'create a new account'
    return e.find_by_text()

def check_error_passwordInvalid(driver):
    """
    Checa se a mensagem de erro é apresentada.
    :param driver: webdriver
    :return: boolean
    """
    e = Element(driver, 'reset your password')
    e.as_5_text = 'reset your password'
    return e.find_by_text()

####################################################################################################################
#                                                Click                                                             #
####################################################################################################################

def click_signin_welcome(driver):
    """
    Clica no botão Sign In da tela Welcome
    :param driver: webdriver
    :return: boolean
    """
    s = Element(driver, 'botão sign in de Welcome')
    s.as_5_text = 'Sign In'
    return s.click_by_text()

def click_signin_login(driver):
    """
    Clica no botão Sign In da tela Login
    :param driver: webdriver
    :return: boolean
    """
    s = Element(driver, 'botão sign in de Login')
    s.as_2_class = 'login-button'
    return s.click_by_class()

####################################################################################################################
#                                                  SET                                                             #
####################################################################################################################

def set_email(driver, email_or_number):
    """
    Insere o email ou telefone
    :param driver: webdriver
    :param email_or_number: e-mail ou número
    :return: boolean
    """
    e = Element(driver, 'email')
    e.as_1_id = 'id_userLoginId'
    return e.set_by_id(email_or_number)

def set_password(driver, password):
    """
    Insere senha
    :param driver: webdriver
    :param password: senha
    :return: boolean
    """
    p = Element(driver, 'password')
    p.as_1_id = 'id_password'
    return p.set_by_id(password)
