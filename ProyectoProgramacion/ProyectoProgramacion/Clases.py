from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import json
import smtplib
from email.message import EmailMessage
import pandas as pd
from PIL import Image, ImageTk

class Ventana():
    def __init__(self, geometria, color, titulo):
        self.geometria = geometria
        self.color = color
        self.titulo = titulo

        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.config(background=self.color)
        self.ventana.title(self.titulo)
        self.ventana.geometry(self.geometria)

    
        self.header_image = PhotoImage(file="Imagenes/headeer.png")
        self.header = Label(self.ventana, image=self.header_image, background="white")
        self.header.place(x=0, y=0)

        self.footer_logo = PhotoImage(file="Imagenes/footer.png")
        self.footer = Label(self.ventana, image=self.footer_logo)
        self.footer.place(x=0, y=510)

        self.frame_creditos = Frame(self.ventana, height=438, width=898, background="white")

   
        self.inicio_sesion = Frame(self.ventana, height=438, width=898, background="white")
        self.formulario_inicio = Label(self.inicio_sesion, background="white", height=15, width=50)
        self.bienvenida_logo = PhotoImage(file="Imagenes/bienvenida.png")
        self.bienvenida = Label(self.inicio_sesion, background="white", image=self.bienvenida_logo)
        self.bienvenida.place(x=240, y=40)

        self.usuario_inicio = Entry(self.formulario_inicio, font=("Arial", 12), width=15)
        self.contrasena_inicio = Entry(self.formulario_inicio, font=("Arial", 12), width=15, show="*")

        self.texto1_inicio = Label(self.formulario_inicio, text="Usuario: ", background="white")
        self.texto2_inicio = Label(self.formulario_inicio, text="Contraseña: ", background="white")

        self.boton_recovery = Button(self.formulario_inicio, text="¿Olvidaste tu Contraseña?", font=("Arial", 7),
                                     background="white", border=False, command=self.olvidar_contraseña)
        self.boton_inicio_sesion = Button(self.formulario_inicio, text="Iniciar Sesión", font=("Arial", 10),
                                          background="white", command=self.iniciar_sesion)


        self.texto2_inicio.place(x=90, y=78)
        self.texto1_inicio.place(x=90, y=18)
        self.usuario_inicio.place(x=90, y=40)
        self.contrasena_inicio.place(x=90, y=100)

        self.boton_recovery.place(x=87, y=100)
        self.boton_inicio_sesion.place(x=120, y=130)

        
        self.frame_correo = Frame(self.ventana, height=240, width=231, background="white")
        self.frame_validacion = Frame(background="white", height=30, width=175)
        self.frame_perfil = Frame(self.ventana, height=438, width=898, background="white")
        self.frame_perfil.grid_propagate(False)

        self.frame_horas = Frame(self.ventana, height=400, width=898, background="white")
        self.frame_creditos = Frame(self.ventana, height=400, width=898, background="white")

        self.frame_noticias = Frame(self.ventana, height=400, width=898, background="white")
        self.frame_noticias.grid_propagate(False)

        self.materias = {} 

        self.mostrar_inicio_sesion()
        self.crear_foro()

    def crear_foro(self):
        for widget in self.frame_perfil.winfo_children():
            widget.destroy()
        Label(self.frame_perfil, text="Foro", font=("Arial", 16), background="white").place(x=500, y=40)

        for i in range(1):
            frame_post = Frame(self.frame_perfil, background="white", padx=10, pady=10, relief="groove", bd=1)
            frame_post.place(x=500,y=80)

            titulo = Label(frame_post, text=f"Título del Post {i+1}", font=("Arial", 12, "bold"), background="white")
            titulo.pack(anchor="w")

            contenido = Label(
                frame_post,
                text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                font=("Arial", 10),
                background="white",
                wraplength=600,
                justify="left"
            )
            contenido.pack(anchor="w")

            img = Image.new("RGB", (150, 100), color="gray")
            img_tk = ImageTk.PhotoImage(img)
            imagen = Label(frame_post, image=img_tk, background="white")
            imagen.image = img_tk
            imagen.pack(anchor="w", pady=5)

    def mostrar_inicio_sesion(self):
        self.inicio_sesion.place(x=0, y=73)
        self.formulario_inicio.place(x=270, y=200)
        self.bienvenida.place(x=240, y=40)
        for widget in self.frame_perfil.winfo_children():
            widget.destroy()
    
        self.boton_inicio_sesion.place(x=120, y=190)
        self.boton_recovery.place(x=87, y=170)
    def buscar_contrasena(self, correo):
    
        with open("usuarios.json", "r") as archivo_json:
            usuarios = json.load(archivo_json)
            for usuario in usuarios:
    
                if usuario.get("correo") == correo:
                    return usuario.get("contrasena")
        return None 


    def enviar_correo(self):
        correo_ingresado = self.correo.get() 
        contrasena = self.buscar_contrasena(correo_ingresado)  
        if contrasena: 
            servidor = "smtp.gmail.com"
            puerto = 587
            usuario = "p31recovery31@gmail.com"
            contrasena_correo = "zcez vcsz ytju zbug"  

            mensaje = EmailMessage()
            mensaje["Subject"] = "Recuperación de Contraseña"
            mensaje["From"] = usuario
            mensaje["To"] = correo_ingresado
            mensaje.set_content(f"Tu contraseña es: {contrasena}")

            try:
                with smtplib.SMTP(servidor, puerto) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(usuario, contrasena_correo)
                    smtp.send_message(mensaje)
                    print("Correo enviado exitosamente.")
            except Exception as e:
                print(f"Ocurrió un error al enviar el correo: {e}")
        else:
            print("No se encontró el correo en la base de datos.")



    def mostrar_noticias(self):
        self.mostrar_boton_regresar()
        self.frame_noticias.place(x=0, y=72)

        # Limpiar el frame para evitar contenido duplicado
        for widget in self.frame_noticias.winfo_children():
            widget.destroy()

        # Crear un Canvas con Scrollbar
        canvas = Canvas(self.frame_noticias, width=600, height=400)  # Ajusta el tamaño visible
        scrollbar = Scrollbar(self.frame_noticias, orient="vertical", command=canvas.yview, background="white")
        contenido_frame = Frame(canvas)

        # Configurar el Canvas y la Scrollbar
        contenido_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=contenido_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Plantilla para las noticias
        noticias = [
            {
                "titulo": "Pruebas de informática para estudiantes continuos, de programas en modalidad presencial (viernes 29 de noviembre de 2024)",
                "contenido": 
                
                '''
Están abiertas las inscripciones para las pruebas de Informática. Las pruebas se realizarán de forma presencial el viernes 29 de noviembre, de 7:00 a. m. a 7:00 p. m. en el Campus Central.

Fecha límite para inscripción y pago: martes 26 de noviembre.

El proceso es el siguiente:

Cancele $50.000 por cada prueba a presentar
Ingrese a miportalu.unab.edu.co
Seleccione en el menú superior Servicio para Estudiantes
En la sección Pago de Servicios Estudiantiles, seleccione la opción Servicios Académicos
En el menú desplegable seleccione Pruebas
Seleccione el botón Cargar Servicios
Del recuadro Prueba de informática básica pregrado, seleccione Pagar Servicio
Guarde la imagen del comprobante de pago (si paga más de una prueba debe repetir los pasos anteriores por cada pago y únalos en un archivo .pdf)
Inscríbase en el siguiente enlace (una sola inscripción por el total de pruebas a presentar): Inscripción pruebas de Informática (debe tener la imagen del comprobante de pago e ingresar a su cuenta de correo de UNAB antes de hacer clic en el enlace).
NOTA: Si por algún motivo no presentó las pruebas en el proceso de inducción, puede redactar un documento solicitando la presentación de las pruebas sin cobro y anexarlo en formato pdf como comprobante de pago.

El jueves 28 de noviembre se enviará a su correo UNAB, el aula y la hora en que debe presentar las pruebas.

El día de la prueba debe presentar su carné de estudiante UNAB o su documento de identidad con foto (cédula de ciudadanía o tarjeta de identidad).   
______________________________________________________________________________


''',
                "imagen": "Imagenes/pruebas-informatica.png"
            },
            {
                "titulo": "Información para presentar la prueba de homologación institucional TEP",
                "contenido": 
                '''

El Departamento de Lenguas informa que las pruebas de homologación TEP I, TEP II y TEP III que se aplicarán el viernes 8 de noviembre 2024, serán presenciales (Edificio ingeniería segundo piso aula de informática L21, campus el Jardín).

Inscripciones y pago: 28 de octubre al 5 de noviembre 2024

Los estudiantes interesados en presentar su prueba de homologación institucional pueden inscribirse y realizar el pago a partir del 28 de octubre hasta el 5 de noviembre 5:00 p.m. al correo lenguas@unab.edu.co con los siguientes datos: nombre completo, ID, programa, correo UNAB. En el asunto del mensaje escribir: Inscripción prueba de homologación TEP I (con un puntaje mínimo de 70 %, homologa los niveles A1, A2.1 y A2.2), TEP II (con un puntaje mínimo de 70%, homologa los niveles A1, A2.1, A2.2, B1.1 y B1.2) o TEP III (con un puntaje mínimo de 61%, homologa todos los niveles  A1,A2.1, A2.2, B1.1, B1.2, B2.1 y B2.2). Sólo debe pagar UNA sola prueba, la que necesita presentar.

El costo de la prueba es de $1.040.000

Para el pago directamente debe ingresar a este enlace.

Se encuentra disponible un servicio para el pago en línea de pruebas de homologación de inglés.

Una vez realice el pago hasta las 5:00 p. m. del 5 de noviembre de 2024, enviar al correo: lenguas@unab.edu.co su nombre completo, el ID, programa, correo UNAB y adjuntar la evidencia del soporte de pago generado por la plataforma ecollect.

Se enviará citación al correo institucional.

Día de la prueba: viernes 8 de noviembre de 2024 a las 7:45 a.m. (Disponibilidad toda la jornada de la mañana). Edificio Ingeniería segundo piso, aula de informática L21, campus el Jardín.

Tenga en cuenta que:

1.  La presentación de la prueba es individual y personal, está prohibido el uso de cualquier ayuda tecnológica, impresa o manuscrita; la tenencia de: celular, manos libres, audífonos, papeles, fotocopias etc., será considerada un intento de copia.

2.  Debe contar con su documento de identidad o carnet institucional. El profesor encargado de la prueba solicitará cualquiera de estos documentos con el fin de verificar la identidad.

3. El incumplimiento de las recomendaciones anteriores puede conducir a acciones disciplinarias por parte de la Universidad.
______________________________________________________________________________

                ''',
                "imagen": "Imagenes/noticia.png"
            },
            {
                "titulo": "Examen diagnóstico de inglés para estudiantes pregrado profesional",
                "contenido": '''
                
El Departamento de Lenguas tiene el gusto de informar que la prueba de diagnóstico de inglés está dirigida a estudiantes pregrado profesional que no han presentado su prueba.

Inscripciones:

Los estudiantes que nunca han presentado su prueba de diagnóstico de inglés, pueden inscribirse hasta el miércoles 30 de octubre 2024 al correo lenguas@unab.edu.co con los siguientes datos: nombre completo, ID, programa, correo institucional. En el asunto del mensaje escribir: Inscripción prueba de diagnóstico. Esta prueba será presentada por una única vez durante toda la carrera y no tiene costo (reglamento estudiantil, capítulo primero, artículo 7, pag. 7).

Día de la prueba: viernes 1 de noviembre de 2024 a las 8:00 am en el aula de informática B13 AINF, campus el Jardín edificio de Biblioteca. Con disponibilidad jornada de la mañana.

Tenga en cuenta que:

1.  La presentación de la prueba es individual y personal, está prohibido el uso de cualquier ayuda tecnológica, impresa o manuscrita; la tenencia de: celular, manos libres, audífonos, papeles, fotocopias etc., será considerada un intento de copia.

2.  Debe contar con su documento de identidad o carnet institucional. El profesor encargado de la prueba solicitará cualquiera de estos documentos con el fin de verificar la identidad.

3. El incumplimiento de las recomendaciones anteriores puede conducir a acciones disciplinarias por parte de la Universidad.

4. Si ya presentó la prueba de diagnóstico en la UNAB en algún semestre anterior, NO es necesario que presente la prueba nuevamente.

5.  Traer lapicero.
    ''',
                "imagen": "Imagenes/noticia2.png"
            }
        ]

        # Mostrar cada noticia en el contenido_frame dentro del Canvas
        for i, noticia in enumerate(noticias):
            # Título de la noticia
            titulo_label = Label(contenido_frame, text=noticia["titulo"], font=("Arial", 14, "bold"), wraplength=400, justify="left", background="white")
            titulo_label.grid(row=i*3, column=0, sticky="w", padx=10, pady=(10, 0))

            # Contenido de la noticia
            contenido_label = Label(contenido_frame, text=noticia["contenido"], wraplength=400, justify="left", background="white")
            contenido_label.grid(row=i*3 + 1, column=0, sticky="w", padx=10, pady=5)

            # Imagen de la noticia
            try:
                imagen = PhotoImage(file=noticia["imagen"])
                imagen_label = Label(contenido_frame, image=imagen)
                imagen_label.image = imagen  # Referencia para evitar que se elimine la imagen
                imagen_label.grid(row=i*3, column=1, rowspan=2, padx=10, pady=10)
            except Exception as e:
                print(f"Error al cargar la imagen: {noticia['imagen']}. Error: {e}")

    def olvidar_contraseña(self):
        self.inicio_sesion.place_forget()  
        self.frame_correo_texto = Label(self.frame_correo, text="Introduce tu correo: ", background="white")
        self.frame_correo_texto.place(x=48, y=78)
        self.frame_correo.place(x=330, y=150)

        self.correo = Entry(self.frame_correo, width=21)
        self.correo.place(x=50, y=100)

     
        self.boton_enviar_correo = Button(self.frame_correo, text="Enviar Contraseña", background="white",
                                        command=self.enviar_correo)
        self.boton_enviar_correo.place(x=50, y=130)

     
        self.boton_regresar = Button(self.frame_correo, text="Regresar", command=self.regresar)
        self.boton_regresar.place(x=75, y=160)

    def iniciar_sesion(self):
        ruta_json = 'usuarios.json'

       
        if hasattr(self, 'texto_validacion'):
            self.texto_validacion.destroy()

        try:
            with open(ruta_json, 'r', encoding="utf8") as archivo:
                usuarios = json.load(archivo)

            usuario = self.usuario_inicio.get()
            contrasena = self.contrasena_inicio.get()

            for u in usuarios:
                if isinstance(u, dict):
                    if u['usuario'] == usuario and u['contrasena'] == contrasena:
                        if u['rol'] == "Estudiante":
                          
                            if 'carrera' in u and 'creditos' in u:
                                self.mostrar_bienvenida(u['nombre'], u['usuario'], u['carrera'])


                                self.inicio_sesion.place_forget()  
                            else:
                       
                                self.mostrar_bienvenida(u['nombre'], u['usuario'], u["carrera"])
                                self.inicio_sesion.place_forget()

                        elif u['rol'] == "Admin":
                            self.mostrar_panel_admin()

                        self.frame_perfil.place(x=0, y=73)

                        if hasattr(self, 'frame_registro'):
                            self.frame_registro.place_forget()

                        return

          
            self.texto_validacion = Label(self.frame_validacion, text="Credenciales Incorrectas", font=("Arial", 12),
                                        background="white", fg="red")
            self.frame_validacion.place(x=350, y=180)
            self.texto_validacion.place(x=0, y=50)

        except FileNotFoundError:
            print("El archivo de usuarios no se encontró.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")

    def mostrar_bienvenida(self, nombre, usuario, carrera):
        mensaje_bienvenida = f"Bienvenido {nombre}"
        mensaje_carrera = f"Programa: {carrera}"
        self.mensaje_bienvenida_label = Label(self.frame_perfil, text=mensaje_bienvenida, font=("Arial", 16), background="white")
        self.mensaje_bienvenida_label.place(x=40, y=80)
        self.mensaje_carrera_label = Label(self.frame_perfil, text=mensaje_carrera, font=("Arial", 14), background="white")
        self.mensaje_carrera_label.place(x=40, y=120)


        self.Mostrar_noticias = Button(self.frame_perfil, text="Ver Noticias", command=lambda: self.mostrar_noticias())
        self.Mostrar_creditos = Button(self.frame_perfil, command=lambda: self.mostrar_creditos_faltantes(usuario), text="Creditos")
        self.Mostrar_horas = Button(self.frame_perfil, command=lambda: self.mostrar_horas_libres_faltantes(usuario), text="Horas Libres")
        self.Mostrar_horas.place(x=180, y=200)
        self.Mostrar_creditos.place(x=40,y=200)
        self.Mostrar_noticias.place(x=100, y=200)
        self.mostrar_boton_regresar()

    def mostrar_boton_regresar(self):
        if not hasattr(self, 'boton_regresar'):
            self.boton_regresar = Button(self.ventana, text="Regresar", background="white", command=self.regresar)
        self.boton_regresar.place(x=10, y=10)

    def regresar(self):
     
        if hasattr(self, 'frame_correo'):
            self.frame_correo.place_forget()
        if hasattr(self, 'frame_registro'):
            self.frame_registro.place_forget()
        if hasattr(self, 'frame_admin'):
            self.frame_admin.place_forget()
        if hasattr(self, 'frame_perfil'):
            self.frame_perfil.place_forget()
        if hasattr(self, 'frame_horas'):
            self.frame_horas.place_forget()
        if hasattr(self, 'frame_creditos'):
            self.frame_creditos.place_forget()
        if hasattr(self,"frame_noticias"):
            self.frame_noticias.place_forget()
        
        self.inicio_sesion.place(x=20, y=73)
    
    def mostrar_panel_admin(self):
 
        self.frame_admin = Frame(self.ventana, background="white")
        self.frame_admin.place(x=0, y=73, width=898, height=438)

     
        self.boton_ver_usuarios = Button(self.frame_admin, text="Ver Usuarios", command=self.ver_usuarios)
        self.boton_ver_usuarios.pack(pady=10)

        self.boton_registrar_usuario = Button(self.frame_admin, text="Registrar Usuario", command=self.mostrar_registro)
        self.boton_registrar_usuario.pack(pady=10)

        self.boton_eliminar_usuario = Button(self.frame_admin, text="Eliminar Usuario", command=self.mostrar_eliminar_usuario)
        self.boton_eliminar_usuario.pack(pady=10)

       
        self.boton_registrar_a_materia = Button(self.frame_admin, text="Registrar a Materia", command=self.registrar_a_materia)
        self.boton_registrar_a_materia.pack(pady=10)

        self.boton_exportar_excel = Button(self.frame_admin, text="Exportar Usuarios a Excel", command=self.exportar_usuarios)
        self.boton_exportar_excel.pack(pady=10)

        self.boton_horas_libres = Button(self.frame_admin, text="Registrar Horas Libres", command=self.mostrar_horas_libres)
        self.boton_horas_libres.pack(pady=10) 


        self.boton_regresar = Button(self.frame_admin, text="Regresar", command=self.regresar)
        self.boton_regresar.pack(pady=10)
    
    def registrar_a_materia(self):
     
        for widget in self.frame_admin.winfo_children():
            widget.destroy()

 
        self.label_seleccionar_estudiante = Label(self.frame_admin, text="Seleccionar Estudiante:", background="white")
        self.label_seleccionar_estudiante.pack(pady=10)

        self.lista_estudiantes = [] 
        ruta_json_usuarios = 'usuarios.json'
        try:
            with open(ruta_json_usuarios, 'r', encoding="utf8") as archivo:
                usuarios = json.load(archivo)

            self.lista_estudiantes = [u['usuario'] for u in usuarios if u['rol'] == 'Estudiante']

            self.combo_estudiantes = ttk.Combobox(self.frame_admin, values=self.lista_estudiantes)
            self.combo_estudiantes.pack(pady=10)

        except FileNotFoundError:
            print("El archivo de usuarios no se encontró.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")

        self.label_seleccionar_carrera = Label(self.frame_admin, text="Seleccionar Carrera:", background="white")
        self.label_seleccionar_carrera.pack(pady=10)


        self.carreras = []
        ruta_json_carreras = 'carreras.json'
        try:
            with open(ruta_json_carreras, 'r', encoding="utf8") as archivo:
                carreras = json.load(archivo)

            self.carreras = list(carreras.keys())
            self.combo_carreras = ttk.Combobox(self.frame_admin, values=self.carreras)
            self.combo_carreras.pack(pady=10)

        except FileNotFoundError:
            print("El archivo de carreras no se encontró.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")

        self.label_seleccionar_semestre = Label(self.frame_admin, text="Seleccionar Semestre:", background="white")
        self.label_seleccionar_semestre.pack(pady=10)

        self.combo_semestre = ttk.Combobox(self.frame_admin, state="disabled")
        self.combo_semestre.pack(pady=10)

   
        self.combo_carreras.bind("<<ComboboxSelected>>", self.actualizar_semestres)

        self.label_seleccionar_materia = Label(self.frame_admin, text="Seleccionar Materia:", background="white")
        self.label_seleccionar_materia.pack(pady=10)

        self.combo_materias = ttk.Combobox(self.frame_admin, state="disabled")
        self.combo_materias.pack(pady=10)

        self.boton_registrar = Button(self.frame_admin, text="Registrar en Materia", command=self.confirmar_registro)
        self.boton_registrar.pack(pady=10)

        self.boton_regresar = Button(self.frame_admin, text="Regresar", command=self.regresar)
        self.boton_regresar.pack(pady=10)
    
    def mostrar_horas_libres(self):
 
        Label(self.frame_admin, text="Nombre del estudiante:").place(x=10, y=10)
        Label(self.frame_admin, text="Horas libres:").place(x=10, y=50)

  
        self.entry_nombre = Entry(self.frame_admin)
        self.entry_nombre.place(x=150, y=10, width=200)

        self.entry_horas = Entry(self.frame_admin)
        self.entry_horas.place(x=150, y=50, width=200)


        boton_registrar = Button(self.frame_admin, text="Registrar horas libres",
                                 command=self.registrar_horas_libres_entry)
        boton_registrar.place(x=100, y=100)

    def mostrar_horas_libres_faltantes(self, usuario):
        self.frame_horas.place(x=0, y=100)
 
        horas_libres_totales = 90

    
        try:
            with open('usuarios.json', 'r', encoding='utf8') as archivo_usuarios:
                usuarios = json.load(archivo_usuarios)
        except FileNotFoundError:
            print("El archivo de usuarios no se encontró.")
            return
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON de usuarios.")
            return

        usuario_encontrado = None
        for u in usuarios:
            if u['usuario'] == usuario:
                usuario_encontrado = u
                break

        if usuario_encontrado is None:
            print(f"Error: No se encontró el usuario '{usuario}'.")
            return

      
        horas_libres_actuales = usuario_encontrado.get("horas_libres", 0)

 
        horas_faltantes = max(0, horas_libres_totales - horas_libres_actuales)

        porcentaje_completado = (horas_libres_actuales / horas_libres_totales) * 100

     
        if hasattr(self, 'label_horas_faltantes'):
            self.label_horas_faltantes.config(
                text=f"Al estudiante le faltan {horas_faltantes} horas libres para completar las 90 horas requeridas.", background="white"
            )
        else:
            self.label_horas_faltantes = Label(
                self.frame_horas, 
                text=f"Al estudiante le faltan {horas_faltantes} horas libres para completar las 90 horas requeridas.",
                font=("Arial", 12),
                fg="black", background="white"
            )
            self.label_horas_faltantes.place(x=250, y=80)  

        if hasattr(self, 'barra_progreso'):
            self.barra_progreso['value'] = porcentaje_completado
        else:
            self.barra_progreso = Progressbar(
                self.frame_horas, 
                orient=HORIZONTAL, 
                length=300, 
                mode='determinate', 
                maximum=100,
                
            )
            self.barra_progreso.place(x=320, y=120) 


        if hasattr(self, 'label_porcentaje'):
            self.label_porcentaje.config(
                text=f"{int(porcentaje_completado)}%"
            )
        else:
            self.label_porcentaje = Label(
                self.frame_horas, 
                text=f"{int(porcentaje_completado)}%", 
                font=("Arial", 10),
                fg="black"
            )
            self.label_porcentaje.place(x=630, y=120)


    def registrar_horas_libres_entry(self):
        nombre_estudiante = self.entry_nombre.get()
        horas_libres = self.entry_horas.get()

        try:
            horas_libres = float(horas_libres)
        except ValueError:
            print("Error: Las horas deben ser un número.")
            return

   
        try:
            with open("usuarios.json", "r") as archivo:
                usuarios = json.load(archivo)
        except FileNotFoundError:
            print("Error: El archivo 'usuarios.json' no existe.")
            return

        usuario_encontrado = False
        for usuario in usuarios:
            if usuario.get("usuario") == nombre_estudiante:
                usuario["horas_libres"] = horas_libres
                usuario_encontrado = True
                break

        if not usuario_encontrado:
            print(f"Error: No se encontró el usuario '{nombre_estudiante}'.")
            return

     
        with open("usuarios.json", "w") as archivo:
            json.dump(usuarios, archivo, indent=4)

        print(f"Horas libres para {nombre_estudiante} registradas correctamente.")
    
    def actualizar_materias(self, event):
        carrera_seleccionada = self.combo_carreras.get()
        semestre_seleccionado = self.combo_semestre.get()

        if not carrera_seleccionada or not semestre_seleccionado:
            return

        ruta_json_carreras = 'carreras.json'
        try:
            with open(ruta_json_carreras, 'r', encoding="utf8") as archivo:
                carreras = json.load(archivo)

            materias = carreras[carrera_seleccionada][semestre_seleccionado]
            self.combo_materias.config(state="normal", values=[materia['Materia'] for materia in materias])

        except FileNotFoundError:
            print("El archivo de carreras no se encontró.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")
    def actualizar_semestres(self, event):
        carrera_seleccionada = self.combo_carreras.get()
        if not carrera_seleccionada:
            return

        ruta_json_carreras = 'carreras.json'
        try:
            with open(ruta_json_carreras, 'r', encoding="utf8") as archivo:
                carreras = json.load(archivo)

            semestres = list(carreras[carrera_seleccionada].keys())
            self.combo_semestre.config(state="normal", values=semestres)


            self.combo_materias.config(state="disabled", values=[])

      
            self.combo_semestre.bind("<<ComboboxSelected>>", self.actualizar_materias)

        except FileNotFoundError:
            print("El archivo de carreras no se encontró.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")
    

    def confirmar_registro(self):
        estudiante_seleccionado = self.combo_estudiantes.get()
        carrera_seleccionada = self.combo_carreras.get()
        semestre_seleccionado = self.combo_semestre.get()
        materia_seleccionada = self.combo_materias.get()

        if not estudiante_seleccionado or not carrera_seleccionada or not semestre_seleccionado or not materia_seleccionada:
            print("Debe seleccionar un estudiante, carrera, semestre y materia.")
            return

        ruta_json_usuarios = 'usuarios.json'
        ruta_json_carreras = 'carreras.json'

        try:
            with open(ruta_json_usuarios, 'r', encoding="utf8") as archivo:
                usuarios = json.load(archivo)


            for usuario in usuarios:
                if usuario['usuario'] == estudiante_seleccionado and usuario['rol'] == 'Estudiante':

                    if 'creditos_completados' not in usuario:
                        usuario['creditos_completados'] = 0


                    with open(ruta_json_carreras, 'r', encoding="utf8") as archivo_carreras:
                        carreras = json.load(archivo_carreras)
                        materias = carreras[carrera_seleccionada][semestre_seleccionado]

                        for materia in materias:
                            if materia['Materia'] == materia_seleccionada:
                                usuario['creditos_completados'] += materia['Creditos']
                                print(f"{estudiante_seleccionado} ha sido registrado en {materia_seleccionada}.")
                                

                                with open(ruta_json_usuarios, 'w', encoding="utf8") as archivo_usuarios:
                                    json.dump(usuarios, archivo_usuarios, ensure_ascii=False, indent=4)
                                break
                    break

        except FileNotFoundError:
            print("El archivo de usuarios o carreras no se encontró.")
        except json.JSONDecodeError:
            print("Error al leer los archivos JSON.")

    def mostrar_eliminar_usuario(self):

        for widget in self.frame_admin.winfo_children():
            widget.destroy()

        self.label_usuario_a_eliminar = Label(self.frame_admin, text="Usuario a eliminar:", background="white")
        self.label_usuario_a_eliminar.pack(pady=10)

        self.entry_usuario_a_eliminar = Entry(self.frame_admin)
        self.entry_usuario_a_eliminar.pack(pady=10)

        self.boton_confirmar_eliminacion = Button(self.frame_admin, text="Eliminar", command=self.eliminar_usuario)
        self.boton_confirmar_eliminacion.pack(pady=10)

        self.boton_regresar = Button(self.frame_admin, text="Regresar", command=self.regresar)
        self.boton_regresar.pack(pady=10)


    def ver_usuarios(self):
        
        for widget in self.frame_admin.winfo_children():
            widget.destroy()


        ruta_json = 'usuarios.json'
        try:
            with open(ruta_json, 'r', encoding="utf8") as archivo:
                usuarios = json.load(archivo)

            for index, usuario in enumerate(usuarios):
                texto_usuario = f"{index + 1}. {usuario['nombre']} - {usuario['usuario']} - {usuario['correo']} - {usuario['rol']}"
                label_usuario = Label(self.frame_admin, text=texto_usuario, background="white")
                label_usuario.pack(anchor="w")
            

        except FileNotFoundError:
            print("El archivo de usuarios no se encontró.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")
        self.boton_regresar = Button(self.frame_admin, text="Regresar", command=self.regresar)
        self.boton_regresar.pack()
    def exportar_usuarios(self):
        ruta_json = 'usuarios.json'
        try:
            with open(ruta_json, 'r', encoding="utf8") as archivo:
                usuarios = json.load(archivo)

            df = pd.DataFrame(usuarios)
            df.to_excel('usuarios.xlsx', index=False)

            print("Exportado a usuarios.xlsx con éxito.")
        except Exception as e:
            print(f"Ocurrió un error al exportar: {e}")


    def mostrar_registro(self):
       
        self.frame_admin.place_forget()

       
        self.frame_registro = Frame(self.ventana, background="white")
        self.frame_registro.place(x=0, y=73, width=898, height=438)

        self.label_nombre = Label(self.frame_registro, text="Nombre:", background="white")
        self.label_nombre.place(x=10, y=60)
        self.entry_nombre = Entry(self.frame_registro)
        self.entry_nombre.place(x=10, y=80)

        self.label_usuario = Label(self.frame_registro, text="Usuario:", background="white")
        self.label_usuario.place(x=10, y=100)
        self.entry_usuario = Entry(self.frame_registro)
        self.entry_usuario.place(x=10, y=120)

        self.label_contrasena = Label(self.frame_registro, text="Contraseña:", background="white")
        self.label_contrasena.place(x=10, y=140)
        self.entry_contrasena = Entry(self.frame_registro, show="*")
        self.entry_contrasena.place(x=10, y=160)

        self.label_correo = Label(self.frame_registro, text="Correo:", background="white")
        self.label_correo.place(x=10, y=180)
        self.entry_correo = Entry(self.frame_registro)
        self.entry_correo.place(x=10, y=200)

        self.label_rol = Label(self.frame_registro, text="Rol:", background="white")
        self.label_rol.place(x=10, y=220)

        self.var_rol = StringVar(value="Estudiante")
        self.checkbox_estudiante = Radiobutton(self.frame_registro, text="Estudiante", variable=self.var_rol, value="Estudiante", background="white")
        self.checkbox_admin = Radiobutton(self.frame_registro, text="Admin", variable=self.var_rol, value="Admin", background="white")
        self.checkbox_estudiante.place(x=10, y=240)
        self.checkbox_admin.place(x=100, y=240)

        self.label_carrera = Label(self.frame_registro, text="Carrera:", background="white")
        self.label_carrera.place(x=10, y=260)
        self.carreras = {
            "Ingenieria Biomedica": 153,
            "Ingenieria de Sistemas": 151,
            "Ingenieria en Energia y Sostenibilidad": 154,
            "Ingenieria Financiera": 153,
            "Ingenieria Industrial": 137,
            "Ingenieria Mecatronica": 154
        }
        self.combo_carrera = ttk.Combobox(self.frame_registro, values=list(self.carreras.keys()))
        self.combo_carrera.place(x=10, y=280)

        self.boton_registrar = Button(self.frame_registro, text="Registrar Usuario", command=self.registrar_usuario)
        self.boton_registrar.place(x=10, y=320)


        self.boton_regresar_registro = Button(self.frame_registro, text="Regresar", command=self.regresar)
        self.boton_regresar_registro.place(x=10, y=20)


    def mostrar_creditos_faltantes(self, usuario):

        self.frame_creditos.place(x=0, y=100)
        try:
            with open('usuarios.json', 'r', encoding='utf8') as archivo_usuarios:
                usuarios = json.load(archivo_usuarios)
        except FileNotFoundError:
            print("El archivo de usuarios no se encontró.")
            return
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON de usuarios.")
            return


        usuario_encontrado = None
        for u in usuarios:
            if u['usuario'] == usuario:
                usuario_encontrado = u
                break

        if usuario_encontrado is None:
            print(f"Error: No se encontró el usuario '{usuario}'.")
            return


        carrera = usuario_encontrado['carrera']


        try:
            with open('carreras.json', 'r', encoding='utf8') as archivo_carreras:
                carreras = json.load(archivo_carreras)
        except FileNotFoundError:
            print("El archivo de carreras no se encontró.")
            return
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON de carreras.")
            return

        if not isinstance(carreras, dict):
            print("Error: El archivo de carreras debe contener un diccionario.")
            return

        if carrera not in carreras:
            print(f"Error: La carrera '{carrera}' no está en el archivo de carreras.")
            return


        creditos_totales = 0
        for semestre, datos in carreras[carrera].items():
            if semestre.startswith("creditos totales"):
                creditos_totales += datos

        creditos_actuales = usuario_encontrado.get("creditos_completados", 0)

        creditos_faltantes = creditos_totales - creditos_actuales


        if hasattr(self, 'label_creditos_faltantes'):
            self.label_creditos_faltantes.config(
                text=f"El estudiante necesita {creditos_faltantes} créditos para completar la carrera de {carrera}.", background="white"
            )
        else:
            self.label_creditos_faltantes = Label(
                self.frame_creditos, 
                text=f"El estudiante necesita {creditos_faltantes} créditos para completar la carrera de {carrera}.",
                font=("Arial", 12),
                fg="black", background="white"
            )
            self.label_creditos_faltantes.place(x=10, y=10)  


    def registrar_usuario(self):
        carrera = self.combo_carrera.get()
        if self.var_rol.get() == "Estudiante" and carrera not in self.carreras:
            print("Por favor, selecciona una carrera válida.")
            return


        creditos_completados = 0


        nuevo_usuario = {
            'nombre': self.entry_nombre.get(),
            'usuario': self.entry_usuario.get(),
            'contrasena': self.entry_contrasena.get(),
            'correo': self.entry_correo.get(),
            'rol': self.var_rol.get(),
            'carrera': carrera,
            'creditos': self.carreras[carrera] if carrera else 0,
            'creditos_completados': creditos_completados  
        }

        ruta_json = 'usuarios.json'
        try:
            with open(ruta_json, 'r', encoding='utf-8') as archivo:
                usuarios = json.load(archivo)


            if any(u['usuario'] == nuevo_usuario['usuario'] for u in usuarios):
                print("El usuario ya existe.")
                return

            usuarios.append(nuevo_usuario)

        except FileNotFoundError:
            usuarios = [nuevo_usuario] 
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")

        with open(ruta_json, 'w', encoding='utf-8') as archivo:
            json.dump(usuarios, archivo, ensure_ascii=False, indent=4)

        print("Usuario registrado exitosamente.")
        self.regresar()
    def eliminar_usuario(self):
        ruta_json = 'usuarios.json'
        usuario_a_eliminar = self.entry_usuario_a_eliminar.get() 

        try:
            with open(ruta_json, 'r', encoding='utf8') as archivo:
                usuarios = json.load(archivo)

 
            usuarios_filtrados = [u for u in usuarios if u['usuario'] != usuario_a_eliminar]

            if len(usuarios_filtrados) < len(usuarios):
                with open(ruta_json, 'w', encoding='utf8') as archivo:
                    json.dump(usuarios_filtrados, archivo, ensure_ascii=False, indent=4)
                print(f"Usuario {usuario_a_eliminar} eliminado exitosamente.")
            else:
                print("Usuario no encontrado.")

        except FileNotFoundError:
            print("El archivo de usuarios no se encontró.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")




ventana = Ventana("898x550", "white", "Sistema de Gestión de Usuarios")
ventana.ventana.mainloop()
