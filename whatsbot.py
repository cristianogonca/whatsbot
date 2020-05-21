from selenium import webdriver
import time

class whatsappbot:
    def __init__(self):
        self.mensagem = "Bom dia Pessoal"
        self.grupos = ["Família!","teste"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')   

def EnviarMensagens(self):
    #<span dir="auto" title="Família! " class="_1wjpf _3NFp9 _3FXB1">Família! <img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="" draggable="false" class="b74 emoji wa _3FXB1" style="background-position: -80px -20px;"></span>
    #<div tabindex="-1" class="_1Plpp">
    #<span data-icon="send" class="">
    self.driver.get('https://web.whatsapp.com')
    time.sleep(30)
    for grupo in self.grupos:
        grupo = self.driver.find_element_by_xpath("//span[@title='{grupos}']")
        time.sleep(10)
        grupo.click()
        chat_box = self.driver.find_elements_by_class_name('_1Plpp')
        time.sleep(3)
        chat_box.click()
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        botao_enviar.click()
        time.sleep(5)

bot = whatsappbot()
bot.Enviarmensagens()







    






