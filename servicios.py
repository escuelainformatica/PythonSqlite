from modelo.Peliculas import Peliculas


class PeliculasServicio:
    # un funcion dentro una clase se llama metodo, y necesita un argumento inicial (usualmente es self)
    def menu(self) -> None:
        print("Menu:")
        print("ingrese 1 para ingresar una pelicula")
        print("ingrese 2 para listar las peliculas ingresadas")

    def ingresar_pelicula(self, pel: Peliculas) -> None:
        pel.titulo = input("Ingresa titulo")
        pel.genero = input("Ingresa genero")
        pel.duracion = int(input("Ingresa duracion"))

        # listar.append[titulo, genero, duracion]

    def listar_peliculas(self, peliculas: list) -> None:
        for peli in peliculas:
            print(peli.titulo, '|', peli.genero, '|', peli.duracion)
