# coding=utf-8
__author__ = 'Jeferson de Souza'
Version = '2.4'

import webbrowser
import esky
import sys

from Tkinter import *
import tkFileDialog
import tkMessageBox
import Tkconstants
from face import *


class MyApp:
    def __init__(self, myParent):
        self.app = myParent
        self.app.title('Gerador de Analises')

        # Criar um menu
        self.menubar = Menu(self.app)
        self.app.config(menu=self.menubar)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Config')
        self.filemenu.add_command(label='Salvar', command=self.gerar_calculos)

        self.filemenu.add_separator()

        self.filemenu.add_command(label='Sair', command=self.app.quit)
        self.menubar.add_cascade(label='Arquivo', menu=self.filemenu)

        # -----
        #Menu editar

        self.editar = Menu(self.menubar, tearoff=0)
        self.editar.add_command(label='FC')
        self.editar.add_command(label='Calculos')

        self.menubar.add_cascade(label='Editar', menu=self.editar)

        # Help

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.help)
        self.helpmenu.add_command(label="Check Update", command=self.nova)




        #frame
        '''
        self.fexibir = Frame(self.app, bg="gray").pack()
        self.fzero = Frame(self.app, bg="gray").pack()
        self.fum = Frame(self.app, bg="gray").pack()
        self.fdois = Frame(self.app, bg="gray").pack()
        self.ftreis = Frame(self.app, bg="gray").pack()
        self.fquatro = Frame(self.app, bg="gray").pack()
        self.fcinco = Frame(self.app, bg="gray").pack()
'''
        #-----------------------
        #entrada de quantidade do Acido
        self.qt_ac = Entry(font='{MS Sans Serif} 10')
        self.qt_ac.insert(0, '0')  #inserindo a quantidade padrao
        self.qt_ac.place(relx=0.04, rely=0.20, relwidth=0.12, relheight=0.07)
        self.value_qtac = self.qt_ac.get()

        self.l_acido = Label(text='Acido', justify=LEFT)
        self.l_acido.place(relx=0.18, rely=0.20, relwidth=0.17, relheight=0.07)

        self.ac_minimo = Entry(font='{MS Sans Serif} 10')
        self.ac_minimo.insert(0, '0')
        self.ac_minimo.place(relx=0.40, rely=0.20, relwidth=0.12, relheight=0.07)

        self.ac_max = Entry(font='{MS Sans Serif} 10')
        self.ac_max.insert(0, '0')
        self.ac_max.place(relx=0.60, rely=0.20, relwidth=0.12, relheight=0.07)
        #--------------------------------------------------------------------------

        #Entrada Nitrato
        self.qt_nitrato = Entry(font='{MS Sans Serif} 10')
        self.qt_nitrato.insert(0, '0')
        self.qt_nitrato.place(relx=0.04, rely=0.30, relwidth=0.12, relheight=0.07)

        self.l_nitrato = Label(text='Nitrato')
        self.l_nitrato.place(relx=0.18, rely=0.30, relwidth=0.17, relheight=0.07)

        self.min_nitrato = Entry(font='{MS Sans Serif} 10')
        self.min_nitrato.insert(0, '0')
        self.min_nitrato.place(relx=0.40, rely=0.30, relwidth=0.12, relheight=0.07)

        self.max_nitrato = Entry(font='{MS Sans Serif} 10')
        self.max_nitrato.insert(0, '0')
        self.max_nitrato.place(relx=0.60, rely=0.30, relwidth=0.12, relheight=0.07)
        #------------------------------------------------------------------

        #Entrada Carbonato

        self.qt_carbonato = Entry(font='{MS Sans Serif} 10')
        self.qt_carbonato.insert(0, '0')
        self.qt_carbonato.place(relx=0.04, rely=0.40, relwidth=0.12, relheight=0.07)

        self.l_carbonato = Label(text='Carbonato')
        self.l_carbonato.place(relx=0.18, rely=0.40, relwidth=0.17, relheight=0.07)

        self.min_carbonato = Entry(font='{MS Sans Serif} 10')
        self.min_carbonato.insert(0, '0')
        self.min_carbonato.place(relx=0.40, rely=0.40, relwidth=0.12, relheight=0.07)

        self.max_carbonato = Entry(font='{MS Sans Serif} 10')
        self.max_carbonato.insert(0, '0')
        self.max_carbonato.place(relx=0.60, rely=0.40, relwidth=0.12, relheight=0.07)
        #----------------------------------------------

        #Entrada Talco

        self.qt_talco = Entry(font='{MS Sans Serif} 10')
        self.qt_talco.insert(0, '0')
        self.qt_talco.place(relx=0.04, rely=0.50, relwidth=0.12, relheight=0.07)

        self.l_talco = Label(text='Talco', justify=LEFT)
        self.l_talco.place(relx=0.18, rely=0.50, relwidth=0.17, relheight=0.07)

        self.min_talco = Entry(font='{MS Sans Serif} 10')
        self.min_talco.insert(0, '0')
        self.min_talco.place(relx=0.40, rely=0.50, relwidth=0.12, relheight=0.07)

        self.max_talco = Entry(font='{MS Sans Serif} 10')
        self.max_talco.insert(0, '0')
        self.max_talco.place(relx=0.60, rely=0.50, relwidth=0.12, relheight=0.07)
        #---------------------------------------------------------

        #Entrada Composto

        self.qt_composto = Entry(font='{MS Sans Serif} 10')
        self.qt_composto.insert(0, '0')
        self.qt_composto.place(relx=0.04, rely=0.60, relwidth=0.12, relheight=0.07)

        self.l_composto = Label(text='Composto')
        self.l_composto.place(relx=0.18, rely=0.60, relwidth=0.17, relheight=0.07)

        self.min_composto = Entry(font='{MS Sans Serif} 10')
        self.min_composto.insert(0, '0')
        self.min_composto.place(relx=0.40, rely=0.60, relwidth=0.12, relheight=0.07)

        self.max_composto = Entry(font='{MS Sans Serif} 10')
        self.max_composto.insert(0, '0')
        self.max_composto.place(relx=0.60, rely=0.60, relwidth=0.12, relheight=0.07)
        #---------------------------------------------------------

        self.minimo = Label(text='Minimo')
        self.minimo.place(relx=0.40, rely=0.10, relwidth=0.12, relheight=0.07)

        self.maximo = Label(text='Maximo')
        self.maximo.place(relx=0.60, rely=0.10, relwidth=0.12, relheight=0.07)

        self.quantidade = Label(text='Quantidade')
        self.quantidade.place(relx=0.01, rely=0.10, relwidth=0.20, relheight=0.07)

        self.parametros = Label(text='Parametros')
        self.parametros.place(relx=0.46, rely=0.02, relwidth=0.20, relheight=0.07)
        #------------------------------------------------------------------------

        #Botoes

        #button_opt = {'fill': Tkconstants.BOTH, 'padx':1, 'pady':4}
        #self.buton = Button(text='Salvar', command=self.salvar)

        self.buton1 = Button(text='Gerar', command=self.gerar_calculos)
        self.buton1.place(relx=0.40, rely=0.80, relwidth=0.30, relheight=0.10)

        #self.buton.pack(side=BOTTOM, **button_opt)

        #define as op

        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'Calculos.txt'
        options['parent'] = root
        options['title'] = 'Salvar como..'


    def salvar(self, texto=''):

        f = tkFileDialog.asksaveasfile(mode='w', **self.file_opt)
        if f is None:
            return
        # texto = str(texto.get(1.0, END))
        f.write(texto)
        f.close()

    def gerar_calculos(self):
        # acido valores
        try:
            qt_ac = int(self.qt_ac.get())
            min_ac = float(self.ac_minimo.get())
            max_ac = float(self.ac_max.get())

            #Nitrato
            qt_nitrato = int(self.qt_nitrato.get())
            min_nitrato = float(self.min_nitrato.get())
            max_nitrato = float(self.max_nitrato.get())

            #Carbonato
            qt_carbonat = int(self.qt_carbonato.get())
            min_carbonat = float(self.min_carbonato.get())
            max_carbonato = float(self.max_carbonato.get())

            # Talco
            qt_talco = int(self.qt_talco.get())
            min_talco = float(self.min_talco.get())
            max_talco = float(self.max_talco.get())

            #composto
            qt_composto = int(self.qt_composto.get())
            min_composto = float(self.min_composto.get())
            max_composto = float(self.max_composto.get())

            resultado_acido = ''
            resultado_nitrato = ''
            resultado_carbonato = ''
            resulado_talco = ''
            resultado_composto = ''

            for i in range(qt_ac):
                resultado_acido += calculo_acido(max_ac, min_ac)
            for i in range(qt_nitrato):
                resultado_nitrato += calc_nitrato(min_nitrato, max_nitrato)
            for i in range(qt_carbonat):
                resultado_carbonato += calculo_carbonato(max_carbonato, min_carbonat)
            for i in range(qt_talco):
                resulado_talco += calculo_solucao(max_talco, min_talco)
            for i in range(qt_composto):
                resultado_composto += calculo_solucao(max_composto, min_composto)

            string_unica = 'Acido \n' + resultado_acido + '\n Nitrato \n' + resultado_nitrato + '\n Carbonato \n' + resultado_carbonato + '\n Talco \n' + resulado_talco + '\n Composto \n' + resultado_composto

            self.salvar(string_unica)
        except:
            tkMessageBox.showwarning('Atencão', 'Nenum campo deve ficar em branco..\n Preencha com ZEROs.')


    def help(self):
        msg = '''
        Fake-Lab. - 1.0.10
        Power by: open source
        Author - Jeferson Souza
        Email - mp_bra_nco@hotmail.com
         '''
        t = tkMessageBox.showinfo('Sobre', msg)

        return t


    # --- Função para busca de atualização *Recurso de update ----
    def nova(self):
        janela = Tk()
        janela.geometry('290x100')
        janela.wm_title('UPDATE')
        lab = Label(janela, text='', font=('Helvetica', 13))
        lab.pack()

        bt = Button(janela, text='SAIR', command=janela.destroy, width=30).pack(side=BOTTOM)

        if getattr(sys, "frozen", False):
            #app = esky.Esky(sys.executable, "http://hunterdell1.hol.es/update/")
            #app = esky.Esky(sys.executable, "http://127.0.0.1:8000/")
            app = esky.Esky(sys.executable, "http://jeferson1925.bugs3.com/update.fake_lab/")

            try:
                if app.find_update() is not None:
                    link = Label(janela, text="Nova versão disponivel", fg="Blue", cursor="hand2",
                                 font=('Helvetica', 13))
                    link.pack()
                    link.bind("<Button-1>", self.google_link_callback)

                else:
                    lab['text'] = 'Usando a versão mais recente: ' + app.active_version
            except:
                lab['text'] = 'Impossivel conectar com o servidor'


    def teste(self):
        lbl_google_link = Label(self.app, text="Nova versão", fg="Blue", cursor="hand2")
        lbl_google_link.pack()
        lbl_google_link.bind("<Button-1>", self.google_link_callback)

    def google_link_callback(self, event):
        #webbrowser.open_new(r"http://127.0.0.1:8000/")
        webbrowser.open_new(r"http://jeferson1925.bugs3.com/update.fake_lab/")


root = Tk()
root.geometry("365x230+100+100")
root.resizable(width=FALSE, height=FALSE)
# root.wm_iconbitmap('quimica.ico')
myapp = MyApp(root)
root.mainloop()