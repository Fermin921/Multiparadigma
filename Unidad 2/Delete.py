import psycopg2
from logger_base import log

conexion = psycopg2.connect(
    user="postgres",
    password="19100209",
    host="127.0.0.1",
    port="5432",
    database="postgres",
)
# Codigo para eliminar un registro de la base de datos
try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    id_a_eliminar = 1  # Supongamos que quieres eliminar el registro con id=1
    sentencia = "DELETE FROM cliente WHERE id = %s"
    valores = (id_a_eliminar,)  # Recuerda incluir la coma para crear una tupla
    cursor.execute(sentencia, valores)
    conexion.commit()
    log.debug(f"Registro: {valores} eliminado correctamente")
except Exception as e:
    conexion.rollback()
    log.error(e)
