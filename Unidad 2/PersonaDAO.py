# DAO = DATA ACCESS OUT
from Persona import Cliente
from Conexion2 import *
from CursorPoll import *
from logger_base import *


class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    _SELECCIONAR_ID = "SELECT cliente.id, cliente.nombre FROM cliente where id = %s"
    _INSERTAR = "INSERT INTO cliente (nombre) VALUES (%s)"
    _ACTUALIZAR = "UPDATE cliente set nombre = %s where id = %s"
    _BORRAR = "DELETE FROM cliente where id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                personas.append(Cliente(r[0], r[1]))
            return personas

    @classmethod
    def seleccionar_por_id(cls, id_persona):
        with CursorDelPool() as cursor:
            valores = (id_persona,)
            cursor.execute(cls._SELECCIONAR_ID, valores)
            resultado = cursor.fetchall()  # Obtener el resultado de la consulta
            return resultado

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre,)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return persona

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = persona.id
            cursor.execute(cls._BORRAR, valores)
            return cursor.rowcount

    # end def


if __name__ == "__main__":
    id = "2"
    log.debug(f"{PersonaDAO.seleccionar_por_id(id)}")
