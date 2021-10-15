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

    @classmethod
    def cargar(cls, pid_reserva):
        sql = "SELECT * FROM tbl_reservas WHERE id_reserva = ?;"
        resultado = db.ejecutar_select(sql, [ pid_reserva ])
        if resultado:
            if len(resultado)>0:
                return cls(pid_reserva, resultado[0]["id_habitacion"], 
                resultado[0]["id_usuario"], resultado[0]["comentario"],
                resultado[0]["calificacion"], resultado[0]["fecha_inicial"],
                resultado[0]["fecha_final"], resultado[0]["activo"],
                resultado[0]["comentario_restringido"])
        
        return None

    def insertar(self):
        sql = "INSERT INTO tbl_reservas (comentario, calificacion, fecha_inicial,fecha_final, activo, comentario_restringido) VALUES (?,?,?,?,?,?);"
        afectadas = db.ejecutar_insert(sql, [self.comentario, self.calificacion, self.fecha_inicial, self.fecha_final, self.activo, self.comentario_restringido])
        return ( afectadas > 0 )

    def eliminar(self):
        sql = "DELETE tbl_reservas WHERE id_reserva = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.id_reserva])
        return ( afectadas > 0 )

    
    def listado(self):
        sql = "SELECT * FROM tbl_reservas WHERE fecha_inicial =? and fecha_final =?;"
        return db.ejecutar_select(sql, [self.fecha_inicial, self.fecha_final ])

    #def actualizar(self):
        #Pendiente desarrollar 

# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD RESERVAS #####################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES ##############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS ###############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS ##################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD CALIFICACION ##############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD CALIFICACION #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS ##################################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS #####################################