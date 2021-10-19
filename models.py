import db

from werkzeug.security import generate_password_hash, check_password_hash

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

    def autenticar(self):
        #Este query es inseguro porque puede permitir una inyección SQL
        #sql = "SELECT * FROM usuarios WHERE usuario = '" + self.usuario + "' AND contrasena = '"  + self.contrasena + "';"    
        #Para mitigar usamos comandos SQL parametrizados
        sql = "SELECT * FROM tbl_usuarios WHERE usuario = ?;"
        obj = db.ejecutar_select(sql, [ self.usuario ])
        if obj:
            if len(obj) >0:
                #Agregamos la invocación al metodo check_password_hash
                #para verificar el password digitado contra el hash seguro almacenado en bd.
                if check_password_hash(obj[0]["contrasena"], self.contrasena):
                    return True
        
        return False        

    @classmethod
    def cargar(cls, pusuario):
        sql = "SELECT * FROM tbl_usuarios WHERE usuario = ? ;"
        #sql = "SELECT * FROM tbl_usuarios WHERE usuario = ? AND contrasena = ? AND tipo_usuario=? AND activo='SI';"
        resultado = db.ejecutar_select(sql, [pusuario])
        if resultado:
            if len(resultado)>0:
                return cls(resultado[0]["usuario"], '********', resultado[0]["tipo_usuario"],'SI', resultado[0]["id_usuario"])
                #return cls(pusuario, pcontrasena, ptipo_usuario,'SI', resultado[0]["id_usuario"])
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
                resultado[0]["nombres"], '********',
                resultado[0]["tipo_usuario"], resultado[0]["activo"], resultado[0]["usuario"])
                #Se cambia el campo contraseña para que no la muestre en las consultas
                #En la tabla usuarios se actualiza la logintud máxima permitida a 500
                #return cls(pid_usuario, resultado[0]["documento"], 
                #resultado[0]["nombres"], resultado[0]["contrasena"],
                #resultado[0]["tipo_usuario"], resultado[0]["activo"], resultado[0]["usuario"])
        return None

    def insertar(self):
        sql = "INSERT INTO tbl_usuarios (documento,nombres,contrasena,tipo_usuario,activo,usuario) VALUES (?,?,?,?,?,?);"
        hashed_pwd = generate_password_hash(self.contrasena, method='pbkdf2:sha256', salt_length=32)
        #Se ingresa la sentencia generate_password_hash para cifrar la contraseña que se envía a la base de datos
        afectadas = db.ejecutar_insert(sql, [self.documento, self.nombres, hashed_pwd, self.tipo_usuario, self.activo, self.usuario])
        return ( afectadas > 0 )

    def eliminar(self):
        sql = "DELETE FROM tbl_usuarios WHERE id_usuario = ?;"
        #sql = "DELETE FROM tbl_usuarios WHERE id_usuario = "+self.id_usuario+";"
        afectadas = db.ejecutar_insert(sql, [ self.id_usuario ])
        return ( afectadas > 0 )

    def modificar(self): # Aquí falta hacer un cambio para cifrar la consulta y el ingreso de la contraseña
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
                resultado[0]["nombres"], '********',
                resultado[0]["tipo_usuario"], resultado[0]["activo"], resultado[0]["usuario"])
                #Se cambia el campo contraseña para que no la muestre en las consultas
                #En la tabla usuarios se actualiza la logintud máxima permitida a 500
                #return cls(pid_usuario, resultado[0]["documento"], 
                #resultado[0]["nombres"], resultado[0]["contrasena"],
                #resultado[0]["tipo_usuario"], resultado[0]["activo"], resultado[0]["usuario"])
        return None

    def insertar(self):
        sql = "INSERT INTO tbl_usuarios (documento,nombres,contrasena,tipo_usuario,activo,usuario) VALUES (?,?,?,?,?,?);"
        hashed_pwd = generate_password_hash(self.contrasena, method='pbkdf2:sha256', salt_length=32)
        #Se ingresa la sentencia generate_password_hash para cifrar la contraseña que se envía a la base de datos
        afectadas = db.ejecutar_insert(sql, [self.documento, self.nombres, hashed_pwd, self.tipo_usuario, self.activo, self.usuario])
        return ( afectadas > 0 )

    def eliminar(self): 
        sql = "DELETE FROM tbl_usuarios WHERE id_usuario = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.id_usuario ])
        return ( afectadas > 0 )

    def modificar(self):# Aquí falta hacer un cambio para cifrar la consulta y el ingreso de la contraseña
        sql = "UPDATE tbl_usuarios SET documento = ?, nombres = ?, contrasena = ?, tipo_usuario = ?, activo = ?, usuario = ? WHERE id_usuario = ?;"
        afectadas = db.ejecutar_insert(sql, [ self.documento, self.nombres, self.contrasena, self.tipo_usuario, self.activo, self.usuario , self.id_usuario])
        return ( afectadas > 0 )
    
    @staticmethod
    def listado():
        sql = "SELECT * FROM tbl_usuarios WHERE tipo_usuario='A' ORDER BY id_usuario;"
        return db.ejecutar_select(sql, None)        
# Fin Clase Usuario Administrador  **************************************************************************************************************************

# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS #####################################
