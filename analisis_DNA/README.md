# Analisis de una secuencia de DNA

Este es un paquete de Python diseñado para leer un archivo FASTA que contenga una secuencia de un genoma y contar todas "A", "T", "G" y "C" que tenga dicha secuencia, calcular la frecuencia de aparición de cada codón, transcribirla a RNA y traducir a aminoácidos.
El script principal del paquete se encuentra dentro del subpaquete scripts.

## Uso

El script principal acepta que se introduzca el nombre del archivo para poder abrirlo, también solicita, si el usuario quiere, un nucleótido específico para contar y el marco de lectura FORWARD a usar.

```
parser = argparse.ArgumentParser(
    description="El siguiente script sirve para analizar una secuencia de DNA, incluye distintas funcionalidades")

parser.add_argument("Input_file",
                    help="El nombre o la ruta al archivo FASTA que se quiera procesar",
                    type=str)

parser.add_argument("-n", "--Nucleotidos",
                    help="El nucleótido para calcular cuántas veces aparece, por defecto son los 4 (A T G C)",
                    type=str,
                    default="ATCG",
                    choices=["A", "T", "G", "C"],
                    required=False)

parser.add_argument("-m", "--Marco_lectura",
                    help="El marco de lectura a elegir, solo se puede FORWARD, inserte 0 para el mc 1, 1 para mc 2 o 2 para mc 3",
                    type=int,
                    default=0,
                    choices=[0, 1, 2],
                    required=False)

args = parser.parse_args()
```


## Salida

El script principal imprime en pantalla la veces que aparece en la secuencia el nucleótido elejido, en caso de que no se elijiera, se van a imprimir
los 4 nucleótidos.
Al igual, imprime en pantalla la frecuencia de aparición de cada codón en la secuencia, los codones se sacan apartir del primer marco de lectura.
Por último, imprime en pantalla la transcripción a RNA y la traducción a aminoácidos de la secuencia de DNA, para ambas se puede elegir el marco de lectura FORWARD que se quiera para hacer la funcionalidad.

## Control de errores

Si el archivo proporcionado no existe, el script generará un mensaje de error. 
Del mismo modo, si el archivo tiene algun error, el script generará un error o si el archivo FASTA esta vacio lo va a notificar.
De igual manera, si el archivo FASTA no tiene cabecera se levatara un error para avisar que esta vacio.

## Pruebas

El paquete incluye un subpaquete llamado tests, con pruebas unitarias para los modulos de los subpaquetes utils, operations y scripts.

## Datos

El paquete esta diseñado para trabajar con un archivo FASTA, no importa la longitud de las secuencias ni su orden.

## Metadatos y documentacion

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script.

## Codigo fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Terminos de uso

Este script está disponible bajo la licencia APACHE-2.0. Consulte el archivo LICENSE para obtener más detalles sobre la licencia.

## Como citar

Si utiliza este script en su trabajo, por favor citelo.

## Contactenos

Frida Galán Hernández

Carlos García González

email: <fridagh@lcg.unam.mx>

email: <carlosgg@lcg.unam.mx>