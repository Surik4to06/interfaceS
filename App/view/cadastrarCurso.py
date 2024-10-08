from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer

class CadastrarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroCurso.ui',self)

    def getCadastroCurso(self):
        area = self.campoArea.currentText().strip()
        nome = self.nomeCurso.text().strip()
        oferta = self.ofertaCurso.text().strip()
        periodo = self.periodoCurso.currentText().strip()
        carga = self.cargaCurso.text().strip()
        horas = self.horasPorDia.text().strip()
        alunos = self.quantidadeAlunos.text().strip()
        
        return(area, nome, oferta, periodo, carga, horas, alunos)

    def validandoDados(self):
        self.respostaCadastrando.setText('CADASTRANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastrando))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.respostaCadastroIncompleto.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastroIncompleto))

    def limparCampos(self, campo):
        campo.clear()


