import db

# Aquí se desarrollan todas las funciones que tienen que ver con la conexión de la base de datos
# Es necesario sectorizar por tipo CRUD

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD RESERVAS ##################################

class reservas():
    id_reserva = 0
    id_habitacion =''
    id_usuario = ''
    comentario =''
    calificacion = ''
    fecha_inicial = ''
    fecha_final = ''
    activo =''
    comentario_restringido = ''

    def __init__(self, pid_reserva, pid_habitacion, pid_usuario,
                 pcomentario,pcalificacion,pfecha_inicial,pfecha_final,
                 pactivo, pcomentario_restringido):

        self.id_reserva = pid_reserva
        self.id_habitacion = pid_habitacion
        self.id_usuario = pid_usuario
        self.comentario = pcomentario
        self.calificacion = pcalificacion
        self.fecha_inicial = pfecha_inicial
        self.fecha_final = pfecha_final
        self.activo = pactivo
        self.comentario_restringido = pcomentario_restringido

# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD RESERVAS #####################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES ##############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS ###############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS ##################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD CALIFICACION ##############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD CALIFICACION #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS ##################################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS #####################################