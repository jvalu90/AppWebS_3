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
        sql = "INSERT INTO tbl_reservas (id_habitacion, id_usuario, comentario, fecha_inicial, fecha_final, activo, comentario_restringido) VALUES (?,?,?,?,?,?,?);"
        afectadas = db.ejecutar_insert(sql, [self.id_habitacion, self.id_usuario, self.comentario, self.fecha_inicial, self.fecha_final, self.activo, self.comentario_restringido])
        return ( afectadas > 0 )

    def eliminar(self): 
        sql = "DELETE FROM tbl_reservas WHERE id_reserva = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.id_reserva])
        return ( afectadas > 0 )
    
    def actualizar(self):
        sql = "UPDATE tbl_reservas SET id_habitacion =? , comentario = ?, fecha_inicial = ?, fecha_final = ? WHERE id_reserva = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.id_habitacion, self.comentario, self.fecha_inicial, self.fecha_final, self.id_reserva ])
        return ( afectadas > 0 ) 

    
    # Se utiliza en la vista 0-1-3-4 / app.py modulo_reservas
    def listado(self, pid_habitacion, pfecha_inicial, pfecha_final):
        sql = "SELECT * FROM tbl_reservas WHERE id_habitacion =? AND fecha_inicial >=? AND fecha_final <=?;"
        return db.ejecutar_select(sql, [pid_habitacion, pfecha_inicial, pfecha_final ])

    # Se utiliza en la vista 0-1-3-4, 0-1-3-4-2/ app.py modulo_reservas, modificar reservas
    @staticmethod
    def listado_choices_habitaciones():
        sql = "SELECT * FROM tbl_habitaciones ORDER BY id_habitacion;"
        return db.ejecutar_select(sql, None)
    
    # Se utiliza en la vista 0-1-3-4-1 / app.py crear_reservas
    @staticmethod
    def listado_choices_usuarios():
        sql = "SELECT * FROM tbl_usuarios ORDER BY id_usuario;"
        return db.ejecutar_select(sql, None)

#Si se necesitan más métodos estáticos podría ser en Gestión de Habitaciones Reservadas
    #@staticmethod
    #def listado_habitaciones_reservadas():
        #sql = "SELECT * FROM tbl_reservas ORDER BY id_reservas;"
        #return db.ejecutar_select(sql, None)

# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD RESERVAS #####################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES ##############################

class habitaciones():
    id_habitacion = 0
    codigo_habitacion = ''
    disponible='SI'

   

    def __init__(self,pid_habitacion,pdisponible,pcodigo_habitacion) -> None:

        self.id_habitacion = pid_habitacion
        self.codigo_habitacion= pcodigo_habitacion
        self.disponible= pdisponible

    @classmethod
    def cargar(cls, pid_habitacion):
        sql = "SELECT * FROM tbl_habitaciones WHERE id_habitacion = ?;"
        resultado = db.ejecutar_select(sql, [ pid_habitacion ])
        if resultado:
            if len(resultado)>0:
                return cls(0,resultado[0]["codigo_habitacion"], resultado[0]["disponible"])
                
        
        return None

    # Se utiliza 0-1-1-4-1-nueva_habitacion

    def insertar(self):
        sql = "INSERT INTO  tbl_habitaciones (id_habitacion) VALUES(?);"
        afectadas = db.ejecutar_insert(sql, [ self.id_habitacion])
        return (afectadas >0)
    
    def modificar(self):
        sql = "UPDATE tbl_habitaciones SET codigo_habitacion = ?, disponible = ? WHERE id_habitacion = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.codigo_habitacion, self.disponible,self.id_habitacion])
        return ( afectadas > 0 )


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS ###############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS ##################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD CALIFICACION ##############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD CALIFICACION #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS ##################################

# Inicio Logueo en la aplicacion
class login():
    usuario=''
    contrasena=''
    tipo_usuario=''
    activo=''
    id_usuario=0

    def __init__(self, pusuario, pcontrasena ,ptipo_usuario , pactivo,pid_usuario) -> None:
       self.usuario=pusuario
       self.contrasena=pcontrasena
       self.tipo_usuario=ptipo_usuario
       self.activo=pactivo
       self.id_usuario=pid_usuario     

    @classmethod
    def cargar(cls, pusuario,pcontrasena,ptipo_usuario):
        sql = "SELECT * FROM tbl_usuarios WHERE usuario = ? AND contrasena = ? AND tipo_usuario=? AND activo='SI';"
        resultado = db.ejecutar_select(sql, [pusuario,pcontrasena,ptipo_usuario])
        if resultado:
            if len(resultado)>0:
                return cls(pusuario, pcontrasena, ptipo_usuario,'SI', resultado[0]["id_usuario"])
        return None

    @staticmethod
    def datos_usuario_logueado(id_usuario):
        sql = "SELECT * FROM tbl_usuarios WHERE id_usuario="+str(id_usuario)+";"
        return db.ejecutar_select(sql, None)
    
# Fin Logueo en la aplicacion

# Tipos de Usuario:
# Inicio Clase Usuario Final  *************************************
class usuario_final():
    id_usuario=0
    documento=''
    nombres=''
    contrasena=''
    tipo_usuario='UF'
    activo='SI'
    usuario=''

    def __init__(self, pid_usuario, pdocumento,  pnombres, pcontrasena ,ptipo_usuario , pactivo, pusuario) -> None:
       self.id_usuario=pid_usuario
       self.documento=pdocumento
       self.nombres=pnombres
       self.contrasena=pcontrasena
       self.tipo_usuario=ptipo_usuario
       self.activo=pactivo
       self.usuario=pusuario
    
    @classmethod
    def cargar(cls, pid_usuario):
        sql = "SELECT * FROM tbl_usuarios WHERE id_usuario = ?;"
        resultado = db.ejecutar_select(sql, [ pid_usuario ])
        if resultado:
            if len(resultado)>0:
                return cls(pid_usuario, resultado[0]["documento"], 
                resultado[0]["nombres"], resultado[0]["contrasena"],
                resultado[0]["tipo_usuario"], resultado[0]["activo"], resultado[0]["usuario"])
        return None

    def insertar(self):
        sql = "INSERT INTO tbl_usuarios (documento,nombres,contrasena,tipo_usuario,activo,usuario) VALUES (?,?,?,?,?,?);"
        afectadas = db.ejecutar_insert(sql, [self.documento, self.nombres,self.contrasena, self.tipo_usuario, self.activo, self.usuario])
        return ( afectadas > 0 )

    def eliminar(self):
        sql = "DELETE FROM tbl_usuarios WHERE id_usuario = ?;"
        #sql = "DELETE FROM tbl_usuarios WHERE id_usuario = "+self.id_usuario+";"
        afectadas = db.ejecutar_insert(sql, [ self.id_usuario ])
        return ( afectadas > 0 )

    def modificar(self):
        sql = "UPDATE tbl_usuarios SET documento = ?, nombres = ?, contrasena = ?, tipo_usuario = ?, activo = ?, usuario = ? WHERE id_usuario = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.documento, self.nombres, self.contrasena, self.tipo_usuario, self.activo, self.usuario , self.id_usuario])
        return ( afectadas > 0 )
    
    @staticmethod
    def listado():
        sql = "SELECT * FROM tbl_usuarios WHERE tipo_usuario='UF' ORDER BY id_usuario;"
        return db.ejecutar_select(sql, None)
# Fin Clase Usuario Final  *************************************************************************************************************************************
# Inicio Clase Usuario Administrador  **************************************************************************************************************************
class usuario_administrador():
    id_usuario=0
    documento=''
    nombres=''
    contrasena=''
    tipo_usuario='A'
    activo='SI'
    usuario=''

    def __init__(self, pid_usuario, pdocumento,  pnombres, pcontrasena ,ptipo_usuario , pactivo, pusuario) -> None:
       self.id_usuario=pid_usuario
       self.documento=pdocumento
       self.nombres=pnombres
       self.contrasena=pcontrasena
       self.tipo_usuario=ptipo_usuario
       self.activo=pactivo
       self.usuario=pusuario
    
    @classmethod
    def cargar(cls, pid_usuario):
        sql = "SELECT * FROM tbl_usuarios WHERE id_usuario = ?;"
        resultado = db.ejecutar_select(sql, [ pid_usuario ])
        if resultado:
            if len(resultado)>0:
                return cls(pid_usuario, resultado[0]["documento"], 
                resultado[0]["nombres"], resultado[0]["contrasena"],
                resultado[0]["tipo_usuario"], resultado[0]["activo"], resultado[0]["usuario"])
        return None

    def insertar(self):
        sql = "INSERT INTO tbl_usuarios (documento,nombres,contrasena,tipo_usuario,activo,usuario) VALUES (?,?,?,?,?,?);"
        afectadas = db.ejecutar_insert(sql, [self.documento, self.nombres,self.contrasena, self.tipo_usuario, self.activo, self.usuario])
        return ( afectadas > 0 )

    def eliminar(self):
        sql = "DELETE FROM tbl_usuarios WHERE id_usuario = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.id_usuario ])
        return ( afectadas > 0 )

    def modificar(self):
        sql = "UPDATE tbl_usuarios SET documento = ?, nombres = ?, contrasena = ?, tipo_usuario = ?, activo = ?, usuario = ? WHERE id_usuario = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.documento, self.nombres, self.contrasena, self.tipo_usuario, self.activo, self.usuario , self.id_usuario])
        return ( afectadas > 0 )
    
    @staticmethod
    def listado():
        sql = "SELECT * FROM tbl_usuarios WHERE tipo_usuario='A' ORDER BY id_usuario;"
        return db.ejecutar_select(sql, None)        
# Fin Clase Usuario Administrador  **************************************************************************************************************************

# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS #####################################
