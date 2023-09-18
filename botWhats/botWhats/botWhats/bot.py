"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
#pd seria o apelido da biblioteca
import pandas as pd

class Bot(DesktopBot):
    def action(self, execution=None):

        # Open whatsApp website
        self.browse("https://web.whatsapp.com")

        # importar a base de dados
        tabela = pd.read_excel("contatos.xlsx")
        #print(tabela)

        # para cada linha da base
        for linha in tabela.index:

            contato = str(tabela.loc[linha, "Contato"])
            msg = tabela.loc[linha, "Msg"]
            arquivo = tabela.loc[linha, "Arquivo"]
            
            if not self.find( "newChat", matching=0.97, waiting_time=10000):
                self.not_found("newChat")
            self.click()
            if not self.find( "colarNumero", matching=0.97, waiting_time=10000):
                self.not_found("colarNumero")
            self.click()
            self.type_keys_with_interval(100, contato)
            self.enter()

            if pd.isna(arquivo):
                self.paste(msg)
                self.enter()
            else:
                self.paste(msg)
                self.enter()
                if not self.find( "anexar", matching=0.97, waiting_time=10000):
                    self.not_found("anexar")
                self.click()
                if not self.find( "documento", matching=0.97, waiting_time=10000):
                    self.not_found("documento")
                self.click()
                if not self.find( "nome", matching=0.97, waiting_time=10000):
                    self.not_found("nome")
                self.paste(arquivo)
                self.enter()
                if not self.find( "enviar", matching=0.97, waiting_time=10000):
                    self.not_found("enviar")
                self.click()

            if self.find( "seta", matching=0.97, waiting_time=10000):
                self.click()
                

            self.wait(2000)

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()














