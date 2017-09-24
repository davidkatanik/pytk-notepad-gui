#Projekt URO David Katanik / KAT0013

#importy
from tkinter import *
from tkinter import tix, ttk, font
from tkinter import Tk, messagebox


#init

class App(Frame):
  def __init__(self, master= None):
    Frame.__init__(self, master, bd=2, relief=GROOVE)
    root.minsize(1200,700)
    self.pack(expand=1, fill=BOTH)
    self.initVariables()
    self.createFrames()
    self.createMenu(master)
    self.createToolbar()
    self.createComponents()
  
  #init variables
  def initVariables(self):
    self.numofwords = IntVar()
    self.numofwords.set(0)
    self.encoding = StringVar()
    self.encoding.set("UTF-8")
    self.status = StringVar()
    self.status.set("Online")
    self.pages = IntVar()
    self.pages.set(1)
    self.listofpages = StringVar()
    self.copies = IntVar()
    self.copies.set(1)
    self.icon = BooleanVar()
    self.complete = BooleanVar()
    self.sb1 = IntVar()
    self.sb1.set(1)
    self.sb2 = IntVar()
    self.sb2.set(1)
    self.sb3 = IntVar()
    self.sb3.set(1)
  
  #frames  
  def createFrames(self):
    self.toolbar = Frame(self, bd=2, relief=RAISED, height=30, pady=2, padx=1)
    self.root = Frame(self, bd=2, relief=SUNKEN, width=20)
    self.statusbar = Frame(self, bd=1, relief=RAISED, height=20)
    
    self.toolbar.pack(side='top', expand = 0, fill =X, padx = 3)
    self.root.pack(side='top',fill=BOTH, expand=1)
    self.statusbar.pack(side='bottom',fill=X)
    
    self.scrollFrame = Frame(self.root)
    self.scrollFrame.pack(fill=BOTH,expand=1)
    
    self.leftRowCount = Frame(self.scrollFrame, bd=2, relief=SUNKEN, width=20)
    self.textFrame = Frame(self.scrollFrame, bd=2, relief=RIDGE)
    
    self.leftRowCount.pack(side='left',fill=Y)
    self.textFrame.pack(side='left',expand = 1 , fill=BOTH)
  
  
  #menu
  def createMenu(self,master):
    self.menuBar = Menu(master)
    master.config(menu=self.menuBar)
    self.breakRows = BooleanVar()
    self.breakRows.set(True)    
    
    #fileMenu    
    self.fileMenu = Menu(self.menuBar, tearoff = 0)
    self.fileMenu.add_command(label = "Nový", accelerator="Ctrl+N")
    self.fileMenu.add_command(label = "Otevřít...", accelerator="Ctrl+O")
    self.fileMenu.add_command(label = "Uložit", accelerator="Ctrl+S")
    self.fileMenu.add_command(label = "Uložit jako...")
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label = "Vzhled stránky...")
    self.fileMenu.add_command(label = "Tisk", accelerator="Ctrl+P", command=self.printdialog)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label = "Konec")

    #editMenu
    self.editMenu = Menu(self.menuBar, tearoff = 0)
    self.editMenu.add_command(label = "Zpět", accelerator="Ctrl+Z")
    self.editMenu.add_separator()
    self.editMenu.add_command(label = "Vyjmout", accelerator="Ctrl+X")
    self.editMenu.add_command(label = "Kopírovat", accelerator="Ctrl+C")
    self.editMenu.add_command(label = "Odstranit", accelerator="Del")
    self.editMenu.add_separator()
    self.editMenu.add_command(label = "Najít...", accelerator="Ctrl+F")
    self.editMenu.add_command(label = "Najít další", accelerator="F3")
    self.editMenu.add_command(label = "Nahradit...", accelerator="Ctrl+H")
    self.editMenu.add_command(label = "Přejít...", accelerator="Ctrl+G")
    self.editMenu.add_separator()
    self.editMenu.add_command(label = "Vybrat vše", accelerator="Ctrl+A")
    self.editMenu.add_command(label = "Čas a datum", accelerator="F5")

    #formatMenu
    self.formatMenu = Menu(self.menuBar, tearoff = 0)
    self.formatMenu.add_checkbutton(label = "Zalamování řádků", variable=self.breakRows)
    self.formatMenu.add_command(label = "Písmo...",command=self.fontdialog)
    
    #showMenu
    self.showMenu = Menu(self.menuBar, tearoff = 0)
    self.showMenu.add_command(label = "Stavový řádek")
    
    #helpMenu
    self.helpMenu = Menu(self.menuBar, tearoff = 0)
    self.helpMenu.add_command(label = "Zobrazit nápovědu")
    self.helpMenu.add_separator()
    self.helpMenu.add_command(label = "O programu poznámkový blok", command=self.help)


    #addMenu
    self.menuBar.add_cascade(label = "Soubor", menu=self.fileMenu)
    self.menuBar.add_cascade(label = "Úpravy", menu=self.editMenu)
    self.menuBar.add_cascade(label = "Formát", menu=self.formatMenu)
    self.menuBar.add_cascade(label = "Zobrazení", menu=self.showMenu)
    self.menuBar.add_cascade(label = "Nápověda", menu=self.helpMenu)
    
  #toolbar  
  def createToolbar(self):
    self.load = Button(self.toolbar)
    self.icon_load= PhotoImage(file="icons/load.png")
    self.load.config(image=self.icon_load,width="20",height="20")
    self.load.pack(side = "left",padx=1)  

    self.save = Button(self.toolbar)
    self.icon_save= PhotoImage(file="icons/save.png")
    self.save.config(image=self.icon_save,width="20",height="20")
    self.save.pack(side = "left",padx=1) 
    
    self.lock = Button(self.toolbar)
    self.icon_lock= PhotoImage(file="icons/lock.png")
    self.lock.config(image=self.icon_lock,width="20",height="20")
    self.lock.pack(side = "left",padx=1) 
    
    self.setting = Button(self.toolbar)
    self.icon_setting= PhotoImage(file="icons/setting.png")
    self.setting.config(image=self.icon_setting,width="20",height="20")
    self.setting.pack(side = "left",padx=1) 
    
    self.undo = Button(self.toolbar)
    self.icon_undo= PhotoImage(file="icons/undo.png")
    self.undo.config(image=self.icon_undo,width="20",height="20")
    self.undo.pack(side = "left",padx=1) 
    
    self.repeat = Button(self.toolbar)
    self.icon_repeat= PhotoImage(file="icons/repeat.png")
    self.repeat.config(image=self.icon_repeat,width="20",height="20")
    self.repeat.pack(side = "left",padx=1) 
    
    Label(self.toolbar, width=1).pack(side= "left")
    
    self.left_align = Button(self.toolbar)
    self.icon_left_align= PhotoImage(file="icons/left_align.png")
    self.left_align.config(image=self.icon_left_align,width="20",height="20")
    self.left_align.pack(side = "left",padx=1)
    
    self.justify_align = Button(self.toolbar)
    self.icon_justify_align= PhotoImage(file="icons/justify_align.png")
    self.justify_align.config(image=self.icon_justify_align,width="20",height="20")
    self.justify_align.pack(side = "left",padx=1)
    
    self.right_align = Button(self.toolbar)
    self.icon_right_align= PhotoImage(file="icons/right_align.png")
    self.right_align.config(image=self.icon_right_align,width="20",height="20")
    self.right_align.pack(side = "left",padx=1)
    
    Label(self.toolbar, width=1).pack(side= "left")
    
    self.style = ttk.Combobox(self.toolbar,width=20)
    fonts=list(font.families())
    fonts.sort()
    self.style['values'] = fonts
    self.style.current(335)
    self.style.pack(side = "left",padx=1) 
    
    self.bold = Button(self.toolbar)
    self.icon_bold= PhotoImage(file="icons/bold.png")
    self.bold.config(image=self.icon_bold,width="20",height="20")
    self.bold.pack(side = "left",padx=1)   
    
    self.italic = Button(self.toolbar)
    self.icon_italic= PhotoImage(file="icons/italic.gif")
    self.italic.config(image=self.icon_italic,width="20",height="20")
    self.italic.pack(side = "left",padx=1)   
    
    self.underline = Button(self.toolbar)
    self.icon_underline= PhotoImage(file="icons/underline.gif")
    self.underline.config(image=self.icon_underline,width="20",height="20")
    self.underline.pack(side = "left",padx=1) 
    
    self.strike_throught = Button(self.toolbar)
    self.icon_strike_throught= PhotoImage(file="icons/strike_throught.gif")
    self.strike_throught.config(image=self.icon_strike_throught,width="20",height="20")
    self.strike_throught.pack(side = "left",padx=1)
    
    self.size = ttk.Combobox(self.toolbar,width=2)
    sizes=[8,9,10,11,12,14,16,18,20,22,24,26,28,36,48,72]
    self.size['values'] = sizes
    self.size.current(3)
    self.size.pack(side = "left",padx=1)      
    
    Label(self.toolbar, width=1).pack(side= "left")
    
    self.list = Button(self.toolbar)
    self.icon_list= PhotoImage(file="icons/list.png")
    self.list.config(image=self.icon_list,width="20",height="20")
    self.list.pack(side = "left",padx=1)
    
    self.num_list = Button(self.toolbar)
    self.icon_num_list= PhotoImage(file="icons/num_list.png")
    self.num_list.config(image=self.icon_num_list,width="20",height="20")
    self.num_list.pack(side = "left",padx=1)
  
    Label(self.toolbar, width=1).pack(side= "left")
    
    self.btnPrint = Button(self.toolbar, command=self.printdialog)
    self.icon_btnPrint= PhotoImage(file="icons/print.png")
    self.btnPrint.config(image=self.icon_btnPrint,width="20",height="20")
    self.btnPrint.pack(side = "left",padx=1)
    
    self.function = Button(self.toolbar)
    self.icon_function= PhotoImage(file="icons/function.gif")
    self.function.config(image=self.icon_function,width="20",height="20")
    self.function.pack(side = "left",padx=1)
    
    self.image = Button(self.toolbar)
    self.icon_image= PhotoImage(file="icons/img.png")
    self.image.config(image=self.icon_image,width="20",height="20")
    self.image.pack(side = "left",padx=1)
    
    self.smile = Button(self.toolbar)
    self.icon_smile= PhotoImage(file="icons/smile.png")
    self.smile.config(image=self.icon_smile,width="20",height="20")
    self.smile.pack(side = "left",padx=1)
    
    self.searchFrame = Frame(self.toolbar, bd = 2, relief=GROOVE)
    self.searchFrame.pack(side = "left",padx=1)
  
    self.entrysearch = Entry(self.searchFrame, width=30)
    self.entrysearch.pack(side="left", expand=1)
  
    self.search = Button(self.searchFrame)
    self.icon_search= PhotoImage(file="icons/search.png")
    self.search.config(image=self.icon_search,width="20",height="20")
    self.search.pack(side = "left",padx=1)
    
    self.zoomin = Button(self.toolbar)
    self.icon_zoomin= PhotoImage(file="icons/zoomin.png")
    self.zoomin.config(image=self.icon_zoomin,width="20",height="20")
    self.zoomin.pack(side = "left",padx=1)
    
    self.zoomout = Button(self.toolbar)
    self.icon_zoomout= PhotoImage(file="icons/zoomout.png")
    self.zoomout.config(image=self.icon_zoomout,width="20",height="20")
    self.zoomout.pack(side = "left",padx=1)
    
  def createComponents(self):
    self.textField = Text(self.textFrame)
    self.textField.pack(side='top',expand=1, fill=BOTH)
    
    self.leftTextField = Text(self.leftRowCount, width=4)
    self.leftTextField.pack(expand=1, fill=Y)
    
    self.updateRowCount('<Key>')
    self.textField.bind('<BackSpace>', self.updateRowCount)
    self.textField.bind('<Return>', self.updateRowCount) 
                                             
    #scrollBar                                         
    self.leftTextField.config(state=DISABLED)
    self.scrollbarYText = Scrollbar(self.scrollFrame)
    self.scrollbarYText.pack(side=RIGHT, fill=Y)


    self.textField.bind("<MouseWheel>", self.onMouseWheel)
    self.leftTextField.bind("<MouseWheel>", self.onMouseWheel)
    self.textField.config(yscrollcommand=self.scrollbarYText.set)
    self.leftTextField.config(yscrollcommand=self.scrollbarYText.set)
    self.scrollbarYText.config(command=self.yView)
    
    #pocet slov
    Label(self.statusbar, text="Počet slov: ").pack(side='left')
    self.lblnumofwords = Label(self.statusbar, textvariable=self.numofwords)
    self.lblnumofwords.pack(side='left')
    
    #kodovani
    self.lblencoding = Label(self.statusbar, textvariable=self.encoding)
    self.lblencoding.pack(side='right')
    Label(self.statusbar, text="kódování: ").pack(side='right') 
    

  #Print dialog
  def printdialog(self):
    self.pdialog = Toplevel(self)
    self.pdialog.wm_title("Tisk")
    self.pdialog.minsize(600, 400)
    self.pdialog.resizable(False, False)
    
    self.printframe = Frame(self.pdialog, padx=4, pady=4)
    self.printframe.pack(fill=BOTH, expand=1)
    
    self.btnframe = Frame(self.pdialog, padx=4, pady=4)
    self.btnframe.pack(fill=X ,side ='bottom')
    

    self.ntbprint = tix.NoteBook(self.printframe)
    self.ntbprint.add("page1", label="Obecné")
    self.p1 = self.ntbprint.subwidget_list["page1"]
    self.ntbprint.pack(side='top', expand=1, fill=BOTH)
            
    
    #tlacitka v printdialogu
    btnConfigPrint = Button(self.btnframe, text="Použij",width=15)
    btnConfigPrint.pack(side=RIGHT, padx=20)
    btnCancelPrint = Button(self.btnframe, text="Storno", width=15,command=self.pdialog.destroy)
    btnCancelPrint.pack(side=RIGHT, padx=20)
    btnPrint = Button(self.btnframe, text="Tiskni", width=15)
    btnPrint.pack(side=RIGHT, padx=20)
    
    btnConfigPrint.config(state=DISABLED)
    
    
    #labelframy v printdialogu
    
    #vyber tiskarny
    self.lblfrprinter = LabelFrame(self.p1, text="Výběr tiskárny")
    self.lblfrprinter.pack(side=TOP,fill=BOTH,expand=1, padx=10, pady=10)
    
    self.liboxprinter = Listbox(self.lblfrprinter,selectmode=SINGLE)
    self.liboxprinter.pack(side=TOP, fill=BOTH, expand=1)
    
    scrollbarY = Scrollbar(self.liboxprinter)
    scrollbarY.pack(side=RIGHT, fill=Y)
    self.liboxprinter.config(yscrollcommand=scrollbarY.set)
    scrollbarY.config(command=self.liboxprinter.yview)
    
    self.liboxprinter.insert(END, u"FAX", u"Microsoft XPS Document Writer", u"Samsung CLX-3180 Series", u"Send to OneNote", u"Síťová tiskárna", u"PDF writer")
    self.liboxprinter.select_set(0)
    
    self.liboxprinterframe = Frame(self.liboxprinter)
    self.liboxprinterframe.pack(side=BOTTOM, padx=10, pady=10)
    
    Label(self.lblfrprinter,text="Stav: ").pack(side=LEFT)
    Label(self.lblfrprinter,textvariable=self.status).pack(side=LEFT)
    
    Button(self.lblfrprinter,text="Předvolby").pack(side=RIGHT, padx=10, pady=10)
    
    #frame pro rozsah stranek a pocet kopii
    self.subPrintFrame = Frame(self.p1)
    self.subPrintFrame.pack(side=TOP,fill=BOTH,expand=1)
    
    #rozsah stranek
    self.lblfrpages = LabelFrame(self.subPrintFrame, text="Rozsah stránek")
    self.lblfrpages.pack(side=LEFT,fill=BOTH,expand=1, padx=10, pady=10)
    
    Radiobutton(self.lblfrpages, text="Vše", variable=self.pages, value=1).pack(anchor=W, padx=10) 
    Radiobutton(self.lblfrpages, text="Výběr", variable=self.pages, value=2).pack(anchor=W, padx=10)
    Radiobutton(self.lblfrpages, text="Stránky", variable=self.pages, value=3).pack(anchor=W, padx=10)
    Entry(self.lblfrpages, textvariable=self.listofpages).pack(anchor=W, padx=10, pady=10, fill=X)
        
    #pocet kopii
    self.lblfrcopies = LabelFrame(self.subPrintFrame, text="Kopií")
    self.lblfrcopies.pack(side=RIGHT,fill=BOTH,expand=1, padx=10, pady=10)
    
    self.tmpFr1=Frame(self.lblfrcopies)
    self.tmpFr1.pack(side=TOP, fill=BOTH, expand=1, padx=5, pady=5)
    Label(self.tmpFr1, text="Počet kopií").pack(side=LEFT)
  
    self.spboxCopies = Spinbox(self.tmpFr1, from_=1, to=99,textvariable=self.copies)
    self.spboxCopies.pack(side=RIGHT)
    
    self.tmpFr2=Frame(self.lblfrcopies)
    self.tmpFr2.pack(side=BOTTOM, fill=BOTH, expand=1, padx=5, pady=5)
    
    
    self.icon.set(1)
    self.page=Label(self.tmpFr2)
    self.icon_up= PhotoImage(file="icons/page_up.png")
    self.icon_down= PhotoImage(file="icons/page_down.png")
    
    self.tmpFr3 = Frame(self.tmpFr2)
    self.tmpFr3.pack(side=RIGHT)
    Checkbutton(self.tmpFr3, text="Na výšku", variable=self.icon ,onvalue=True, offvalue=False, command=self.showicon).pack(side=TOP, anchor = W) 
    self.showicon() 
    self.page.pack(side=LEFT)
    
    Checkbutton(self.tmpFr3, text="Kompletovat", variable=self.complete ,onvalue=True, offvalue=False).pack(side=TOP, anchor = W) 
    self.pdialog.grab_set()
    root.wait_window(self.pdialog)
    
  def showicon(self):
    if self.icon.get() == 1:
      self.page.config(image=self.icon_up,width="48",height="48")
    else :
      self.page.config(image=self.icon_down,width="48",height="48")       
  #font dialog
  def fontdialog(self):
    self.fdialog = Toplevel(self)
    self.fdialog.wm_title("Písmo")
    self.fdialog.minsize(600, 400)
    self.fdialog.resizable(False, False)  
    
    #buttons in fontdialog
    btnFrame = Frame(self.fdialog)
    btnFrame.pack(side=BOTTOM, fill=X)
    btnCancelPrint = Button(btnFrame, text="Storno",width=15,command=self.fdialog.destroy)
    btnCancelPrint.pack(side=RIGHT, padx=20,pady=2)
    btnokPrint = Button(btnFrame, text="OK", width=15)
    btnokPrint.pack(side=RIGHT, padx=20,pady=2)
    
    self.ntbfont = tix.NoteBook(self.fdialog)
    self.ntbfont.add("page1", label="Písmo")
    self.ntbfont.add("page2", label="Upřesnit")
    self.p1 = self.ntbfont.subwidget_list["page1"]
    self.p2 = self.ntbfont.subwidget_list["page2"]
    self.ntbfont.pack(side='top', expand=1, fill=BOTH, padx=5, pady=5) 
    
    #help frames
    self.liboxFrame = Frame(self.p1)
    self.liboxFrame.pack(side=TOP,expand=1, fill=BOTH)
    
    self.otherFrame = Frame(self.p1)
    self.otherFrame.pack(side=BOTTOM,expand=1, fill=BOTH)
    
    #font family  
    self.liboxfamily = Listbox(self.liboxFrame, selectmode=SINGLE,exportselection=0)
    self.liboxfamily.pack(side=LEFT, fill=BOTH, expand=1, padx=4,pady=4)
    
    scrollbarY = Scrollbar(self.liboxfamily)
    scrollbarY.pack(side=RIGHT, fill=Y)
    self.liboxfamily.config(yscrollcommand=scrollbarY.set)
    scrollbarY.config(command=self.liboxfamily.yview)
    
    fonts=list(font.families())
    fonts.sort()

    for i in fonts:
      self.liboxfamily.insert(END, i) 
    self.liboxfamily.select_set(335) 
       
    #font style  
    self.liboxstyle = Listbox(self.liboxFrame, selectmode=SINGLE,exportselection=0)
    self.liboxstyle.pack(side=LEFT, fill=BOTH, expand=1, padx=4,pady=4)
    
    scrollbarY2 = Scrollbar(self.liboxstyle)
    scrollbarY2.pack(side=RIGHT, fill=Y)
    self.liboxstyle.config(yscrollcommand=scrollbarY2.set)
    scrollbarY2.config(command=self.liboxstyle.yview)
    
    for i in ['Normální','Kurzíva','Tučené','Tučené Kurzíva']:
      self.liboxstyle.insert(END, i) 
    self.liboxstyle.select_set(0)
    
    #font size  
    self.liboxsize = Listbox(self.liboxFrame, selectmode=SINGLE,exportselection=0)
    self.liboxsize.pack(side=LEFT, fill=BOTH, expand=1, padx=4,pady=4)
    
    scrollbarY3 = Scrollbar(self.liboxsize)
    scrollbarY3.pack(side=RIGHT, fill=Y)
    self.liboxsize.config(yscrollcommand=scrollbarY3.set)
    scrollbarY3.config(command=self.liboxsize.yview)
    
    for i in [8,9,10,11,12,14,16,18,20,22,24,26,28,36,48,72]:
      self.liboxsize.insert(END, i) 
    self.liboxsize.select_set(0)
      
    self.lblfrExample = LabelFrame(self.otherFrame, text="Ukázka")
    self.lblfrExample.pack(side=LEFT, expand=1, fill=BOTH,padx=20,pady=20)
    
    self.lblExample = Label(self.lblfrExample, text="AaBbYy")
    self.lblExample.pack(expand=1,fill=BOTH,padx=2,pady=2)
    
    
    localFrame = Frame(self.otherFrame)
    localFrame.pack(side=RIGHT, expand=1, fill=BOTH,padx=2,pady=2)
    Label(localFrame,text="Skript:").pack(anchor=N, padx=4,pady=4)
    
    self.cboxEncoding = ttk.Combobox(localFrame, state='readonly')
    self.cboxEncoding['values'] = ['Středoevropské','Západní','Řecké','Turecké','Pobaltské','Cyrilice','Vietnamské']
    self.cboxEncoding.current(0)
    self.cboxEncoding.pack(anchor=N, padx=4,pady=4)
    
    #config frame
  
    lblframeChars = LabelFrame(self.p2,text="Proložení znaků")
    lblframeChars.pack(side=TOP, expand=1, fill=BOTH,padx=10,pady=10)
    
    frame1=Frame(lblframeChars)
    frame1.pack(side=LEFT,expand=1,fill=BOTH,padx=10,pady=10)
    
    frame2=Frame(lblframeChars)
    frame2.pack(side=RIGHT,expand=1,fill=BOTH,padx=10,pady=10)
    
    Label(frame1,text="Měřítko").grid(column=0,row=0, padx=2, pady=2)
    Label(frame1,text="Mezery").grid(column=0,row=1, padx=2, pady=2)
    Label(frame1,text="Umístění").grid(column=0,row=2, padx=2, pady=2)
    
    Checkbutton(frame1, text="Prokládání písem velikostí").grid(column=0,row=3, columnspan=2, padx=2, pady=2) 
    
    cb1 = ttk.Combobox(frame1, values=('100%','150%','200%','50%','33%'),width=15, state='readonly')
    cb1.grid(column=1,row=0, padx=2, pady=2)
    cb1.current(0)
    
    cb2 = ttk.Combobox(frame1, values=('Normální','Rozšířené','Zúžené'),width=15, state='readonly')
    cb2.grid(column=1,row=1, padx=2, pady=2)
    cb2.current(0)
    
    cb3 = ttk.Combobox(frame1, values=('Normální','Zvýšené','Snížené'),width=15, state='readonly')
    cb3.grid(column=1,row=2, padx=2, pady=2) 
    cb3.current(0)
    
    Label(frame2,text="").grid(column=0,row=0, padx=2, pady=2)
    Label(frame2,text="O kolik").grid(column=0,row=1, padx=2, pady=2)
    Label(frame2,text="O kolik").grid(column=0,row=2, padx=2, pady=2)
    
    Spinbox(frame2, from_=1, to=99, width=10,textvariable=self.sb1).grid(column=1,row=1, padx=2, pady=2)
    Spinbox(frame2, from_=1, to=99, width=10,textvariable=self.sb2).grid(column=1,row=2, padx=2, pady=2)
    
    Spinbox(frame2, from_=1, to=99, width=5,textvariable=self.sb3).grid(column=0,row=3, padx=2, pady=2)
    Label(frame2,text="Bodů a více").grid(column=1,row=3, padx=2, pady=2)
    
    
    #second part of congif frame
    self.otherFrame2 = Frame(self.p2)
    self.otherFrame2.pack(side=BOTTOM,expand=1, fill=BOTH)
    
    self.lblfrExample2 = LabelFrame(self.otherFrame2, text="Ukázka")
    self.lblfrExample2.pack(side=LEFT, expand=1, fill=BOTH, padx=20,pady=20)
    
    self.lblExample2 = Label(self.lblfrExample2, text="AaBbYy")
    self.lblExample2.pack(expand=1,fill=BOTH)
    
    localFrame2 = Frame(self.otherFrame2)
    localFrame2.pack(side=RIGHT, expand=1, fill=BOTH,padx=2,pady=2)
    
    localFrame3 = Frame(localFrame2)
    localFrame3.pack(side=TOP, expand=1, fill=BOTH,padx=2,pady=2)
    
    localLblFrame = Frame(localFrame3)
    localLblFrame.pack(side=LEFT,expand=1, fill=BOTH,pady=2)
    
    localCBFrame = Frame(localFrame3)
    localCBFrame.pack(side=RIGHT,expand=1, fill=BOTH,padx=2,pady=2)
    
    Label(localLblFrame,text="Ligatury").pack(side=TOP,expand=1, fill=Y, anchor=W,padx=2,pady=2)
    Label(localLblFrame,text="Mez. mezi čísly").pack(side=TOP,expand=1, fill=Y, anchor=W,padx=2,pady=2)
    Label(localLblFrame,text="Číselné tvary").pack(side=TOP,expand=1, fill=Y, anchor=W,padx=2,pady=2)
    Label(localLblFrame,text="Stylistické sady").pack(side=TOP,expand=1, fill=Y, anchor=W,padx=2,pady=2)
    
    cboxLig = ttk.Combobox(localCBFrame, values=('Žádné','Pouze standardní','Standardní a kotextové','Historické a volitelné','Všechny'), width=20, state='readonly')
    cboxLig.current(0)
    cboxLig.pack(side=TOP,expand=1, anchor=E,padx=2,pady=2)
    
    cboxMMC = ttk.Combobox(localCBFrame, values=('Výchozí','Proporční','Tabulkové'), width=20, state='readonly')
    cboxMMC.current(0)
    cboxMMC.pack(side=TOP,expand=1, anchor=E,padx=2,pady=2)
    
    cboxCT = ttk.Combobox(localCBFrame, values=('Výchozí','Vyrovnané','Starodávné'), width=20, state='readonly')
    cboxCT.current(0)
    cboxCT.pack(side=TOP,expand=1, anchor=E,padx=2,pady=2)
    
    cboxSS = ttk.Combobox(localCBFrame, values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), width=20, state='readonly')
    cboxSS.current(0)
    cboxSS.pack(side=TOP,expand=1, anchor=E,padx=2,pady=2)
    
    cbtnPKA = Checkbutton(localFrame2, text="Používat kontextové alternativy") 
    cbtnPKA.pack(side=BOTTOM,fill=Y,anchor=W,padx=2,pady=2)
    
    self.fdialog.grab_set()
    root.wait_window(self.fdialog)
    
  def help(self):
    messagebox.showinfo("O aplikaci","Toto je projekt od Davida Katanika do předmětu Uživatelské rozhraní - URO ")   
    
  def yView(self, *args):
    self.textField.yview(*args)
    self.leftTextField.yview(*args)

  def onMouseWheel(self, event):
    if event.delta < 0:
      e = 1
    else:
      e = -1
    self.textField.yview("scroll", 0, 'units')
    self.leftTextField.yview("scroll", e, 'units')
    
  def updateRowCount(self, key):
    self.leftTextField.config(state=NORMAL)
    a = int(self.textField.index('end').split('.')[0])
    self.leftTextField.delete(float(0), END) 
    for x in range(1,a):
      self.leftTextField.insert(float(x),str(x)+'\n')
    self.leftTextField.config(state=DISABLED)       
    self.textField.update() 
    
root = tix.Tk()
root.wm_title("Poznámkový blok")
app = App(root)
root.mainloop()