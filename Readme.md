# Big Data Aplicado
## UD 6 - Apache Hadoop
### Práctica 2 MapReduce

> Para los siguientes ejercicios, copia el comando y/o haz una captura de pantalla donde se muestre el resultado de cada acción
> Debes entregar los correspondientes comandos y capturas.
> Recuerda que tienes que tener correctamente configurado Apache Hadoop (HDFS, MapReduce y Yarn). Si no es así, consulta la documentación del módulo

1. Cálcula el del número π, con 16 maps y 10000000 muestras.
   
2. Cambia el cálculo con 4 maps y las mismas muestras
   
3. Compara los resultados estudiando cada "Jobs" en Yarn a través de su WebUI y analiza las diferencias. ¿Qué conclusiones obtienes? (Añade las correspondientes capuras)

4. Resuelve el siguiente sudoku

```
8 5 ? 3 9 ? ? ? ?
? ? 2 ? ? ? ? ? ?
? ? 6 ? 1 ? ? ? 2
? ? 4 ? ? 3 ? 5 9
? ? 8 9 ? 1 4 ? ?
3 2 ? 4 ? ? 8 ? ?
9 ? ? ? 8 ? 5 ? ?
? ? ? ? ? ? 2 ? ?
? ? ? ? 4 5 ? 7 8
```

5. Usando un fichero de texto de gran volumen, realiza el cálculo de la media, mediana y desviación estándar del tamaño de las palabras del texto. Compara los jobs de cada uno de ellos observando su coste en recursos, rendimiento y tiempo. Detalla la conclusión que puedes sacar de estos datos.

6. Vamos a seguir utilizando los ejemplos que nos facilita MapReduce. Para ello vamos a usar un conjunto de 3 aplicaciones(teragen, terasort y teravalidate). Estos se basan en la implementación de MapReduce desarrolladas por Owen O'Malley y Arun Murthy. Estas aplicaciones ganaron el estándar de comparación anual de ordenación de terabytes de uso general ("Daytona") en 2009 con una velocidad de 0,578 TB/min (100 TB en 173 minutos). Para obtener más información sobre este y otros estándares de comparación de ordenación, consulte el sitio [Sort Benchmark](https://sortbenchmark.org/).

Este ejemplo utiliza tres conjuntos de programas de MapReduce:

- TeraGen: programa de MapReduce que genera filas de datos que se van a ordenar.

- TeraSort: toma una muestra de los datos de entrada y usa MapReduce para ordenar los datos de manera absoluta.

    TeraSort es una ordenación MapReduce estándar, salvo por el particionador personalizado. El particionador usa una lista ordenada de N-1 claves de muestra que definen el intervalo de claves para cada reducción. En concreto, todas las claves, como esa sample[i-1] <= key < sample[i] se envían para reducir i. Esta particionador garantiza que las salidas de la reducción i sean todas menores que la salida de la reducción i+1.

- TeraValidate: programa de MapReduce que valida que la salida se ordene de manera global.

    Crea una asignación por archivo en el directorio de salida y cada asignación asegura que cada clave es menor o igual que la anterior. La función de asignación genera registros de la primera y última clave de cada archivo. La función de reducción se asegura de que la primera clave del archivo i es mayor que la última clave del archivo i-1. Los problemas se notifican como una salida de la fase de reducción con las claves que no están en orden.


7. Crea un fichero a través de la aplicación `Teragen` de 2GB _(Observa primero si tienes espacio suficiente en el cluster (al menos 10GB) [http://bda-iesgrancapitan:9870/](http://bda-iesgrancapitan:9870/). Puedes hacerlo con menos para el ejercicio)_. El formato del fichero debe ser `Apellido1Nombre_teragen`

8. Muestra el fichero generado incluyendo permisos y tamaño en formato de GB. Indica que observas

9. Ejecuta la siguiente aplicación `terasort` para ordenar los datos generados anteriormente. _Ponte cómodo, dependiendo de tu máquina, tardará un ratito ;p_. Observa en la WebUI de Yarn el correspondiente _JOB_ y en HDFS como se añaden los datos(bloques), y el espacio ocupado. El formato del fichero debe ser `Apellido1Nombre_terasort`

10. Una vez finalizado, observa y compara el resultado. El formato del fichero debe ser `Apellido1Nombre_teravalidate`

11. Finalmente, valida el resultado obtenido con `testvalidate`

13. Busca el checksum resultante de la operación e indica cuál es y donde lo has encontrado

14. Investiga el ejemplo `pentomino`. Deberás explicar [cómo funciona](https://es.wikipedia.org/wiki/Pentomin%C3%B3), realizar un ejemplo con él y explicarlo de forma detallada.

>Entrega la tarea en el siguiente repositorio: https://classroom.github.com/a/qWUMrzog