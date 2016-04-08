from gi.repository import Gtk

import sqlite3 as dbapi

__author__ = 'dcuerdo'


class Confirmacion(Gtk.Window):
    def __init__(self,label={},cod={}):
        """
        Metodo en el que declaramos la segunda interfaz
        de confirmacion de compra de los productos de
        la base de datos
        """
        Gtk.Window.__init__(self, title="")
        self.set_border_width(20)
        self.set_default_size(100, 100)

        # LayoutBox
        self.box = Gtk.Box(spacing=6)
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # ListBox Iniciamos la lista de Rows
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

        lres = Gtk.Label(label)
        scod=cod

        no = Gtk.Button.new_with_mnemonic(label="No")
        si = Gtk.Button.new_with_mnemonic(label="Si")

        self.v_box1.pack_start(lres, True, True, 1)
        self.v_box2.pack_start(no, True, True, 1)
        self.v_box2.pack_start(si, True, True, 1)

        self.list_box.add(self.row1)
        self.list_box.add(self.row2)


        no.connect("clicked", self.mno)
        si.connect("clicked", self.msi,cod)

    def mno(self,no):
        """
        Metodo que destruye la ventana
        """
        self.destroy()

    def msi(self,si,cod):
        """
        Metodo de confirmacion de existencias
        """
        existencias=0
        bd = dbapi.connect("basefruterias.dat")
        cursor = bd.cursor()
        cursor.execute("select cantidad from frutas  where codigo='"+cod.get_text()+"'")
        for res in cursor:
            existencias=int(res[0])
            bd.commit()
        existencias = existencias-1
        if existencias.isdigit:
            self.correcto = True
        else:
            self.correcto = False

        if (self.correcto):
            cursor.execute("update frutas set cantidad ='"+str(existencias)+"' where codigo='"+cod.get_text()+"'")
            bd.commit()

        self.destroy

confirma = Confirmacion()
confirma.set_position(Gtk.WindowPosition.CENTER)




