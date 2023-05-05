import os
import sys
import tempfile
import time
from PyQt5 import QtWidgets, uic, QtGui

app = QtWidgets.QApplication(sys.argv)

temp_dir = getattr(sys, "_MEIPASS", tempfile.gettempdir())
ui_file = os.path.join(temp_dir, "resources", "tela.ui")
icon_file = os.path.join(temp_dir, "resources", "icone.ico")

if os.path.exists(ui_file):
    tela = uic.loadUi(ui_file)
else:
    tela = uic.loadUi("tela.ui")

if os.path.exists(icon_file):
    tela.setWindowIcon(QtGui.QIcon(icon_file))
else:
    tela.setWindowIcon(QtGui.QIcon('rebate.ico'))

# Adiciona a imagem "logo2.png" à QLabel "imagem_label" presente na interface
imagem_path = os.path.join(temp_dir, "resources", "logo2.png")
if os.path.exists(imagem_path):
    imagem = QtGui.QPixmap(imagem_path)
    tela.imagem_label.setPixmap(imagem)
else:
    print("A imagem não pôde ser encontrada.")

def instalar():
    tela.setEnabled(False)
    tela.BotaoStatus.setText("Aguarde a reinstalação...")
    QtWidgets.QApplication.processEvents()

    os.system("taskkill /f /im teamviewer.exe")
    os.system("""powershell.exe -command "& {(new-object System.Net.WebClient).DownloadFile('https://download.teamviewer.com/download/version_13x/TeamViewer_Setup.exe','C:\SCL\ieam13.exe')}""")
    os.system("""powershell.exe -Command "& {$Install = Start-Process 'C:\SCL\ieam13.exe' -ArgumentList '/S' -PassThru}""")

    time.sleep(20)

    tela.BotaoStatus.setText("Team Viewer reinstalado com sucesso!!!")
    tela.setEnabled(True)

tela.BotaoInstalar.clicked.connect(instalar)
tela.show()
sys.exit(app.exec_())


#script usado para compactar o arquivo

#pyinstaller --onefile --windowed --add-data "tela.ui;resources" --add-data "icone.ico;resources" --add-data "logo2.png;resources" --ico=icone.ico teste.py
