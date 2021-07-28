# quiero agregar todas las funciones de la base de datos

# esta clase repo tiene una gracia: usualmente es igual.

from modelo.Peliculas import Peliculas


class AutoRepo:
    def listar_todo(self,con) -> list:
        #  peliculas = []  # lista vacia
        cursor = con.cursor()  # recordset (o command)
        cursor.execute("select titulo,genero,duracion from repo")
        # for fila in cursor:
        #    print(fila[0])

        tuples_peliculas = cursor.fetchall()  # listado de tuples.
        peliculas = []
        for tup in tuples_peliculas:
            # *tup = desempaqueta un tuple, es decir, lo transforma en 3 argumentos.
            pelicula = Peliculas(*tup)  # tup[0],tup[1],tup[2]
            peliculas.append(pelicula)  # listado de Peliculas
        cursor.close()
        return peliculas

    def insertar(self,pel:Peliculas,con):
        cursor=con.cursor()

        # prepared statement (consulta preparada)
        # es segura
        # evita las inyeccion sql
        cursor.execute("insert into repo(titulo,genero,duracion) values(?,?,?)"
                       ,(pel.titulo,pel.genero,pel.duracion))
        con.commit()  # aprobar la operacion (cierra la transaccion)
        cursor.close()