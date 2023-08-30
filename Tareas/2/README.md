# **(Par. 2) Otras herramientas para el manejar errores **
En esta parte del tema se mostrara un ejemplo de las exepciones para el manejo de errores pero en el lenguaje C++

Como ya vimos, las excepciones en C++ se asemejan a las de lenguajes como C# y Java. 

En el bloque try, si se produce una excepción, la detectará el primer bloque catch asociado cuyo tipo coincida con el de la excepción. 

En otras palabras, la ejecución salta de la instrucción throw a la instrucción catch. 
Si no se encuentra ningún bloque catch utilizable, se invoca std::terminate y se cierra el programa. 

> [!Note]
> El código de _ **ejemplo.cpp**_ ilustra cómo usar excepciones para manejar casos en los que los valores pasados a una función están fuera de los límites esperados. 
En este caso, si un valor demasiado grande se pasa a MyFunc, se lanza una excepción que se captura en la función main, lo que permite al programa manejar el error de manera controlada.

En C++, se puede producir cualquier tipo; sin embargo, se recomienda iniciar un tipo que derive directa o indirectamente de std::exception. En el ejemplo anterior, el tipo de excepción, 
invalid_argument, se define en la biblioteca estándar del archivo de encabezado <stdexcept>. 

C++ no proporciona ni requiere un bloque finally 
para asegurarse de que todos los recursos se liberan si se produce una excepción. La adquisición de recursos es la expresión de inicialización (RAII), 
que usa punteros inteligentes, que proporciona la funcionalidad necesaria para la limpieza de recursos. Para más información, consulte Diseño de la seguridad de excepciones. 
