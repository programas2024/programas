import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from Regitro import Regitro
import random
import string
from Tooltip import Tooltip
import mysql.connector

class Registrarce:



    def mostrar_menu_contextual(self, event):
        self.menu_contextual = tk.Menu(self.master, tearoff=False)
        self.menu_contextual.add_command(label="Pegar", command=self.pegar)
        self.menu_contextual.add_command(label="Copiar", command=self.copiar)
        self.menu_contextual.tk_popup(event.x_root, event.y_root)

    def copiar(self):
        texto_ingresado = self.contrasena_entry.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(texto_ingresado)


    def pegar(self):
        texto_pegado = self.master.clipboard_get()
        self.contrasena_entry.insert(tk.INSERT, texto_pegado)


    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz de Registro")
        self.master.geometry("400x500")
        self.master.configure(bg="white")
        

        self.generating_right_click_event = False

    


        self.imagen_registrar = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\editar.png")
        self.imagen_cancelar = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\rechazado.png")
        self.imagen_generar = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\olvidocontrasena.png")
        self.imagen_ver = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\candado-abierto.png")
       

        self.register_label = tk.Label(master, text="REGISTRARSE",background="white")
        

        self.cedula_label = tk.Label(master, text="Cédula:",background="white")
        self.cedula_entry = tk.Entry(master)
        self.set_placeholder(self.cedula_entry, "Digite su cédula")
        Tooltip(self.cedula_entry,"Digita tu  cedula")
        self.cedula_entry.config(validate="key", validatecommand=(self.master.register(self.validate_numeric_input), '%P'))
        
        self.nombre_label = tk.Label(master, text="Nombre:",background="white")
        self.nombre_entry = tk.Entry(master)
        self.set_placeholder(self.nombre_entry, "Digite su nombre")
        self.nombre_entry.config(validate="key", validatecommand=(self.master.register(self.validate_text_input), '%P'))
        Tooltip(self.nombre_entry,"Digita tu nombre")
        self.apellidos_label = tk.Label(master, text="Apellidos:",background="white")
        self.apellidos_entry = tk.Entry(master)
        self.set_placeholder(self.apellidos_entry, "Digite sus apellidos")
        self.apellidos_entry.config(validate="key", validatecommand=(self.master.register(self.validate_text_input), '%P'))
        Tooltip(self.apellidos_entry,"Digita tu apellido")
        self.pais_label = tk.Label(master, text="País:",background="white")
        self.paises = ["Colombia", "México", "Honduras", "Perú", "Brasil", "EE.UU.", "Guatemala", "Panamá"]
        self.pais_entry = ttk.Combobox(master, values=self.paises, state="readonly")
        self.pais_entry.set("Colombia")
        self.set_placeholder(self.pais_entry, "Digite su Pais")
        Tooltip(self.pais_entry,"Elije tu pais")

        self.correo_label = tk.Label(master, text="Correo:",background="white")
        self.correo_entry = tk.Entry(master)
        self.set_placeholder(self.correo_entry, "Digite su correo")
        Tooltip(self.correo_entry,"Escriba su correo")
        self.usuario_label = tk.Label(master, text="Usuario:",background="white")
        self.usuario_entry = tk.Entry(master)
        self.set_placeholder(self.usuario_entry, "Digite su usuario")
        Tooltip(self.usuario_entry,"Escribe tu usuario ")
        self.contrasena_label = tk.Label(master, text="Contraseña:",background="white")
        self.contrasena_entry = tk.Entry(master, show="*", exportselection=False, insertbackground="white")
        self.contrasena_entry.bind("<Button-3>", self.mostrar_menu_contextual)

        self.set_placeholder(self.contrasena_entry, "Digite su contraseña")
        Tooltip(self.contrasena_entry,"Escriba una contraseña")
        self.registrar_button = tk.Button(master, text="Registrar",image=self.imagen_registrar,background="white", command=self.registrar)
        Tooltip(self.registrar_button,"Registrar")
        self.generar_contrasena_button = tk.Button(master, text="Generar Contraseña",image=self.imagen_generar,background="white", command=self.generar_contrasena)
        Tooltip(self.generar_contrasena_button,"Generar contraseña")
        self.cancelar_button = tk.Button(master, text="Cancelar",background="white",image=self.imagen_cancelar, command=self.cancelar)
        Tooltip(self.cancelar_button,"Salir")
        

        # Instanciar la clase Registro
        self.registro_handler = Regitro(self)

        # Posicionamiento en la ventana
        self.register_label.place(x=60, y=40)

        self.cedula_label.place(x=60, y=70)
        self.cedula_entry.place(x=120, y=70)

        self.nombre_label.place(x=60, y=100)
        self.nombre_entry.place(x=120, y=100)

        self.apellidos_label.place(x=60, y=140)
        self.apellidos_entry.place(x=120, y=140)

        self.pais_label.place(x=60, y=150)
        self.pais_entry.place(x=120, y=150)

        self.pais_label.place(x=60, y=180)
        self.pais_entry.place(x=120, y=180)

        self.correo_label.place(x=60, y=215)
        self.correo_entry.place(x=120, y=215)

        self.usuario_label.place(x=60, y=255)
        self.usuario_entry.place(x=120, y=255)

        self.contrasena_label.place(x=60, y=290)
        self.contrasena_entry.place(x=130, y=290)

        self.registrar_button.place(x=60, y=400, width=90)
        self.generar_contrasena_button.place(x=160, y=400, width=130)
        self.cancelar_button.place(x=290, y=400, width=90)

       


        self.mostrar_contrasena_button = tk.Button(master, text="🔒",image=self.imagen_ver,background="white", command=self.mostrar_contrasena)
        self.mostrar_contrasena_button.bind("<Enter>", lambda event: self.contrasena_entry.config(show=""))
        self.mostrar_contrasena_button.bind("<Leave>", lambda event: self.contrasena_entry.config(show="*"))
        self.mostrar_contrasena_button.place(x=330 ,y=290, width=60, height=40)
        


    
    
    
    def mostrar_contrasena(self, event=None):
        self.contrasena_entry.config(show="")

    def ocultar_contrasena(self, event):
        self.contrasena_entry.config(show="*")

    def set_placeholder(self, entry, text):
        entry.insert(0, text)
        entry.bind("<FocusIn>", lambda event, entry=entry, text=text: self.clear_entry(event, entry, text))
        entry.bind("<FocusOut>", lambda event, entry=entry, text=text: self.restore_entry(event, entry, text))

    def clear_entry(self, event, entry, text):
        if entry.get() == text:
            entry.delete(0, tk.END)

    def restore_entry(self, event, entry, text):
        if not entry.get():
            entry.insert(0, text)

    def validate_text_input(self, text):
        return all(char.isalpha() or char.isspace() for char in text)
    
    def validate_numeric_input(self, text):
        return text.isdigit() or text == ""

    
    def select_country(self, event):
        # Obtener el índice del país seleccionado en el Listbox
        index = self.pais_listbox.curselection()
        if index:
            # Obtener el valor del país seleccionado
            selected_country = self.paises[index[0]]
            # Actualizar el valor seleccionado en el Combobox
            self.pais_entry.set(selected_country)


    def generar_contrasena(self):
        longitud = 10
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
        self.contrasena_entry.delete(0, tk.END)
        self.contrasena_entry.insert(0, contrasena)

    def registrar(self):
        # Verifica si todos los campos están llenos correctamente
        if (not self.nombre_entry.get().isalpha() or
                not self.apellidos_entry.get().isalpha() or
                not self.pais_entry.get().isalpha() or
                not self.correo_entry.get().endswith((".com", ".org", ".net")) or
                not self.usuario_entry.get().isalnum() or
                not self.contrasena_entry.get()):
            messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")
            return

        try:
            # Establece la conexión con la base de datos
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )

            # Crea un cursor para ejecutar consultas SQL
            cursor = connection.cursor()

            # Verificar si la tabla existe, y si no, crearla
            cursor.execute("SHOW TABLES LIKE 'registros'")
            table_exists = cursor.fetchone()
            if not table_exists:
                # Si la tabla no existe, la creamos
                cursor.execute("""
                    CREATE TABLE registros (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(255),
                        apellidos VARCHAR(255),
                        pais VARCHAR(100),
                        correo VARCHAR(255),
                        usuario VARCHAR(100),
                        contrasena VARCHAR(255),
                        fecha_registro DATETIME
                    )
                """)
                connection.commit()

            # Prepara la consulta SQL para insertar los datos
            query = "INSERT INTO registros (nombre, apellidos, pais, correo, usuario, contrasena, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            ahora = datetime.now()
            fecha_registro = ahora.strftime("%Y-%m-%d %H:%M:%S")
            data = (
                self.nombre_entry.get(),
                self.apellidos_entry.get(),
                self.pais_entry.get(),
                self.correo_entry.get(),
                self.usuario_entry.get(),
                self.contrasena_entry.get(),
                fecha_registro
            )

            # Ejecuta la consulta SQL para insertar los datos
            cursor.execute(query, data)

            # Realiza los cambios en la base de datos
            connection.commit()

            # Cierra el cursor y la conexión
            cursor.close()
            connection.close()

            messagebox.showinfo("Registro Exitoso", "Los datos se han registrado correctamente en la base de datos.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo realizar el registro en la base de datos: {error}")

    def cancelar(self):
        self.master.destroy()


