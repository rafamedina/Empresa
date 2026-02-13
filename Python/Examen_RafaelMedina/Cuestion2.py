class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def calcularNotaMedia(self):
        suma_notas = 0 
        nNotas = 0
        
        for nota in self.notas:
            suma_notas += nota
            nNotas += 1
            
        if nNotas == 0:
            return 0
            
        media = suma_notas / nNotas
        return media  # <--- AQUÍ FALTABA EL RETURN

    def mostrar_estado(self):
        media = self.calcularNotaMedia()
        
        # Ahora media ya es un número y la comparación funciona
        estado = "Aprobado" if media >= 5 else "Suspenso"
        print(f"Alumno: {self.nombre} | Media: {media:.2f} | Estado: {estado}")


lista_alumnos = []
lista_alumnos.append(Alumno("Rafa", [4, 5, 3]))      
lista_alumnos.append(Alumno("Iker", [9, 8, 10]))    
lista_alumnos.append(Alumno("Marcos", [5, 6, 5]))      

print("--- LISTA DE ALUMNOS ---")
for alumno in lista_alumnos:
    alumno.mostrar_estado()


mejor_alumno = None
mejor_media = -1  

for alumno in lista_alumnos:
    media_actual = alumno.calcularNotaMedia()
    
    if media_actual > mejor_media:
        mejor_media = media_actual
        mejor_alumno = alumno

print("\n--- MEJOR ALUMNO ---")
if mejor_alumno:
    print(f"El mejor alumno es {mejor_alumno.nombre} con una media de {mejor_media:.2f}")