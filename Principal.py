__author__ = 'dcuerdo'

from gi.repository import Gtk

from gi.repository import Gtk
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

import sqlite3 as dbapi




class Principal(Gtk.Window):
    def __init__(self):
        """
        En el constructor principal, creamos la interfaz con Gtk
        Creamos la conexion a la base de datos
        Creamos el Listbox, y iniciamos la lista de rows
        Creamos la cantidad de rows necesarias, labels, botones y entrys
        """
        self.condicion = bool
        self.bd = dbapi.connect("basefruterias.dat")
        self.cursor = self.bd.cursor()
        self.elementos = []

        Gtk.Window.__init__(self, title="Fruteria")
        self.set_border_width(20)
        self.set_default_size(500, 100)

        self.box = Gtk.Box(spacing=6)
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        print(self.list_box.get_selection_mode())
        self.box.pack_start(self.list_box, True, True, 0)

        # Row1
        self.row1 = Gtk.ListBoxRow()
        self.hor_box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row1.add(self.hor_box1)
        self.v_box1 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box1.pack_start(self.v_box1, True, True, 1)

        # Row2
        self.row2 = Gtk.ListBoxRow()
        self.hor_box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row2.add(self.hor_box2)
        self.v_box2 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box2.pack_start(self.v_box2, True, True, 1)

        # Row3
        self.row3 = Gtk.ListBoxRow()
        self.hor_box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row3.add(self.hor_box3)
        self.v_box3 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box3.pack_start(self.v_box3, True, True, 1)

        # Row4
        self.row4 = Gtk.ListBoxRow()
        self.hor_box4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row4.add(self.hor_box4)
        self.v_box4 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box4.pack_start(self.v_box4, True, True, 1)

        # Row5
        self.row5 = Gtk.ListBoxRow()
        self.hor_box5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row5.add(self.hor_box5)
        self.v_box5 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box5.pack_start(self.v_box5, True, True, 1)

        # Row6
        self.row6 = Gtk.ListBoxRow()
        self.hor_box6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.row6.add(self.hor_box6)
        self.v_box6 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box6.pack_start(self.v_box6, True, True, 1)

        self.preciot=0
        self.cantidadcompra=0

        self.lcodigo = Gtk.Label("Codigo -->")
        self.lfruta = Gtk.Label("Fruta -->")
        self.ltotal = Gtk.Label("Existencias -->")
        self.lprecio = Gtk.Label("Precio -->")
        self.lres = Gtk.Label(" ")

        self.ecodigo = Gtk.Entry()
        self.efruta = Gtk.Entry()
        self.etotal = Gtk.Entry()
        self.eprecio = Gtk.Entry()

        self.btodas = Gtk.Button.new_with_mnemonic(label="Mostrar todas")
        self.bbuscar = Gtk.Button.new_with_mnemonic(label="Buscar")
        self.binsertar = Gtk.Button.new_with_mnemonic(label="Insertar nueva")
        self.beliminar = Gtk.Button.new_with_mnemonic(label="Eliminar")
        self.bcomprar = Gtk.Button.new_with_mnemonic(label="Comprar cesta")
        self.bimprimir = Gtk.Button.new_with_mnemonic(label="Imprimir base")
        self.binformacion=Gtk.Button.new_with_mnemonic(label="Informacion")


        self.v_box1.pack_start(self.lcodigo, True, True, 1)
        self.v_box1.pack_start(self.ecodigo, True, True, 1)
        self.v_box1.pack_start(self.bbuscar, True, True, 1)
        self.v_box2.pack_start(self.lfruta, True, True, 1)
        self.v_box2.pack_start(self.efruta, True, True, 1)
        self.v_box2.pack_start(self.bcomprar, True, True, 1)
        self.v_box3.pack_start(self.ltotal, True, True, 1)
        self.v_box3.pack_start(self.etotal, True, True, 1)
        self.v_box3.pack_start(self.binformacion, True, True, 1)
        self.v_box4.pack_start(self.lprecio, True, True, 1)
        self.v_box4.pack_start(self.eprecio, True, True, 1)
        self.v_box4.pack_start(self.bimprimir, True, True, 1)
        self.v_box5.pack_start(self.lres, True, True, 1)
        self.v_box6.pack_start(self.btodas, True, True, 1)
        self.v_box6.pack_start(self.binsertar, True, True, 1)
        self.v_box6.pack_start(self.beliminar, True, True, 1)

        self.list_box.add(self.row1)
        self.list_box.add(self.row2)
        self.list_box.add(self.row3)
        self.list_box.add(self.row4)
        self.list_box.add(self.row5)
        self.list_box.add(self.row6)


        self.btodas.connect("clicked", self.ctodas)
        self.bbuscar.connect("clicked", self.mbuscar)
        self.binsertar.connect("clicked", self.minsertar)
        self.beliminar.connect("clicked", self.mborrar)
        self.bcomprar.connect("clicked", self.mcomprar)
        self.bimprimir.connect("clicked",self.cimprimir)
        self.binformacion.connect("clicked",self.cinformacion)

    def ctodas(self,widget):
        """
        Metodo que muestra todas las
        frutas en la interfaz
        """
        fruta=""

        self.cursor.execute("select * from frutas")
        for res in self.cursor:
                fruta=fruta+("codigo: " + str(res[0]) + ", nombre: " + str(res[1]) + ", cantidad " + str(res[2]) + ", precio: " + str(res[3]) + "\n")
        self.bd.commit()
        self.lres.set_text(fruta)

    def mbuscar(self,widget):
        """
        Metodo que busca una fruta a traves del codigo
        """
        fruta=""
        cod= self.ecodigo.get_text()
        if cod.isdigit:
            self.condicion=True
            self.cursor.execute("select * from frutas where codigo='"+cod+"'")
            for res in self.cursor:
                 fruta=fruta+(   "codigo: " + str(res[0]) + ", nombre: " + str(res[1]) + ", cantidad " + str( res[2]) + ", precio: " + str(res[3]) + "\n")
            self.vemergente(fruta)
            self.bd.commit()
        else:
            self.vemergente("Revise los datos")
            self.condicion=False

    def cinformacion(self,widget):
        """
        Metodo que simplemente informa
        de como funciona el programa
        """
        self.vemergente("Informacion al usuario")

    def mcomprar(self,widget):
        """
        Metodo que muestra todas las inserciones que hay en la base de datos
        """
        frutac=""
        cod = self.ecodigo.get_text()
        if cod.isdigit:
            self.cursor.execute("select * from frutas  where codigo='"+cod+"'")
            for res in self.cursor:
                frutac=frutac+("Va a comprar\n " + str(res[1]) + ", Precio:\n " + str(res[3]) + "\n ESTAS SEGURO?")
            self.bd.commit()
        else:
            self.vemergente("Codigo invalido")

        from Cesta import Confirmacion
        abrir=Confirmacion(frutac, cod)
        abrir.set_position(Gtk.WindowPosition.CENTER)
        abrir.show_all()

    def mborrar(self,widget):
        """
        Metodo que borra una fila de la base de datos
        """
        cod=self.ecodigo.get_text()
        if cod.isdigit:
            self.cursor.execute("delete from frutas where cod='"+cod+"' ")
            self.bd.commit()
            self.vemergente("Insertado")
        else:
            self.vemergente("Codigo invalido")

    def minsertar(self,widget):
        """
        Metodo para insertar en la base de datos
        """
        cod = str(self.ecodigo.get_text())
        nombre = str(self.efruta.get_text())
        cantidad = str(self.etotal.get_text())
        precio = str(self.eprecio.get_text())

        if cod.isdigit and nombre.isalpha and cantidad.isdigit and precio.isdigit:
            self.condicion = True
        else:
            self.vemergente("Revise los datos")
            self.condicion = False

        if (self.condicion):
            try:
                self.cursor.execute("insert into frutas values('"+cod+"','"+nombre+"','"+cantidad+"','"+precio+"')")
                self.bd.commit()
                self.vemergente("Insertado")
            except dbapi.IntegrityError:
                self.vemergente("Codigo repetido")

    def vdestruir(self, widget):
        """"
        Destruye la ventana vemergente
        """
        widget.destroy()

    def vemergente(self, texto):
        """
        ventena usanda como ventana emergente
        para todos los metodos
        """
        window = Gtk.Window(title="Advertencia")
        label = Gtk.Label(texto)
        label.set_padding(10, 10)
        window.add(label)
        window.connect("delete-event", self.vdestruir)
        window.set_position(Gtk.PositionType.RIGHT)
        window.show_all()

    def cimprimir(self,widget):
        """
        Metodo imprimir que imprime un pdf con la base de datos

        """
        pdf = "Frutas_.pdf"
        c = canvas.Canvas(pdf, pagesize=A4)
        c.drawString(20, 800, "Impresion de la Base de Datos")
        frutas = list(self.cursor.execute("select * from frutas"))
        title = [["CODIGO", "NOMBRE", "CANTIDAD", "PRECIO"]]

        fruta = title + frutas
        tabla = Table(fruta)

        tabla.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 2, colors.white),
                                   ('BACKGROUND', (0, 1), (-1, -1), colors.yellow),
                                   ('BACKGROUND', (0, 0), (-1, 0), colors.black)]))

        tabla.wrapOn(c, 20, 30)
        tabla.drawOn(c, 20, 600)
        c.save()
        self.vemergente("PDF Generado")

ventana = Principal()
ventana.set_position(Gtk.WindowPosition.CENTER)
ventana.set_resizable(False)
ventana.connect("delete-event", Gtk.main_quit)
ventana.show_all()
Gtk.main()



