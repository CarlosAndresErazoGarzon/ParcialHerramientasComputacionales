## ParcialHerramientasComputacionales
### Problema
Una universidad desea realizar descuentos a la comunidad estudiantil a partir de si el cliente es estudiante o profesor aplicando porcentajes de descuento distintos.
### Modelo computacional
Se realiza una solución al problema en el lenguaje de programación Python aplicando las guías y estilos de programación vistas en la clase.
### Entradas
- Cédula.
- Rol ("0" para estudiante o "1" para profesor).
- Código de producto.
- Cantidad del producto.
- Precio del producto.
### Salidas
- Se presentan los productos comprados por un estudiante o profesor con una cédula específica a manera de tabla.
- Se muestra el total a pagar
### Cálculos
- Para obtener el total entre la cantidad de un producto y su valor: `total = cant*precio` (Linea 59).
- Para aplicar el descuento dependiendo del rol:
  - Rol de profesor: `total*0.20` (línea 63).
  - Rol de estudiante: `total*0.50` (línea 67).
- Para obtener el valor acumulado de la compra (línea 86-88):
~~~
for n in lista:
    ...
    total_final += n[1]
~~~

## Contenido del repositorio
- **main.py:** Archivo con el algoritmo correspondiente a la solución.
- **Errores.txt:** Archivo donde se enlistan los errores que se pudieron haber presentado a la hora de realizar la solución.
