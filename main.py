import sqlite3

from PeliculaRepositorio import PeliculaRepositorio
from modelo.Peliculas import Peliculas
from servicios import PeliculasServicio
from EjemploBasico import EjemploBasico

tup=(20,"hola")

obj=EjemploBasico(*tup)  # EjemploBasico(20,"hola")

# cuando tengo un argumento en una definicion de una funcion, metodo o constructor
# sirve para empaquetar, es decir, transformar todos los argumentos en un tuple.
def funcionempaquetar(*paquete):
    print(paquete)


funcionempaquetar(1,2,3,4,5)


con = sqlite3.connect('base.db')  # va a crear un archivo base.db



# listas []    [20,30]
# tuples ()   (20,30) <-- rapidos, solamente lectura
# diccionarios {campo=20,campo2=2}



repo=PeliculaRepositorio()

peliculas=repo.listar_todo(con)

servicio = PeliculasServicio()

menuv = 0

while menuv == 0:
    servicio.menu()
    op = int(input("Ingresa opcion"))

    if op == 1:
        pel = Peliculas()  # crear una memoria con los datos que estan en la clase Peliculas
        peli = pel  # instancia peli apunta donde apunta pel
        servicio.ingresar_pelicula(pel)
        peliculas.append(pel)
        # sql:
        # insert into peliculas(titulo,genero,duracion) values('aa','bbb',222)
        repo.insertar(pel,con)


    elif op == 2:
        servicio.listar_peliculas(peliculas)



con.close()