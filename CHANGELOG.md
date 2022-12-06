# Registro de cambios

### [v0.3.0](https://github.com/Michelzxc/TickeT4x/) 2022/12/07

---

+ CustomTkinter actualizado a 5.0.2
+ Nuevo formato para representar las ventanas del programa, botones en bloque.
+ Estructura de archivos fuente mejor ordenada.

### [v0.2.1](https://github.com/Michelzxc/TickeT4x/tree/bf0972c79b7c79c3b0246ed9b3f514291db192b1) 2022/12/02

---

+ Se creó la clase ConfigurationFrame para el botón de configuración.

### [v0.2.0](https://github.com/Michelzxc/TickeT4x/tree/3b84c97f7e8cc56ddb0d5238c390cd694775e2c8) 2022/12/01

---

+ Módulo /ctk renombrado a /nctk por conflictos.
+ imagebox.py ya no es necesario, clase ya incluida en nueva version de CustomTkinter.
+ CustomTkinter actualizado a la version 5.0.0!!!
+ Debido a la nueva versión de CustomTkinter se debe cambiar parte del código.
+ Agregadas más imágenes, textos y colores.
+ Ventana Acerca de casi terminada.
+ Botones salir y acerca de ya tienen funcionalidad.
+ Función text_loader ahora también carga el tipo de fuente general de la aplicación.

### [v0.1.3](https://github.com/Michelzxc/TickeT4x/tree/42968c1f6a72df04e78071162437ef4ae8adeb80) 2022/11/28

+ Se agragó un fichero con colores en hexadecimal y una función para cargarlos.
+ En la etiqueta versión se agregó una "v" antes del valor de versión.
+ Insertados los textos y colores en el frame MainMenu.
+ Botón salir funciona.
+ Se preparó soporte para agregar los protocolos.
+ MainMenu se se pega arriba y abajo de la ventana.
+ Clase TickeT4x ahora es hija de CTk.

### [v0.1.2](https://github.com/Michelzxc/TickeT4x/tree/7a2578523f1817815aa824f23bbb08cef13efa73) 2022/11/28

---

+ Se movieron los archivos .json a la carpeta json_.
+ Se creó el módulo de menus.
+ Añadida función para cargar y ajustar el tamaño de las imágenes.
+ Función main se remplazó por Clase TickeT4x.
+ Actualizado README, algo más concreto.

### [v0.1.1](https://github.com/Michelzxc/TickeT4x/tree/ee7c86da93de201692082c67b7eda254b18d0990) 2022/11/28

---

+ Todos los textos del programa centralizados en texts.json.
+ Se implementa el módulo loaders.py.
+ Añadido más descripciones a módulos.

### [v0.1.0](https://github.com/Michelzxc/TickeT4x/tree/33a117fa5c8a174323f2c2c48394484e7898797c) 2022/11/27

---

+ Inicio de creación de la interfaz gráfica de usuario basado en CustomTkinter.
+ Comprobación de plataforma de ejecución. TickeT4x se ejecutará en Windows o GNU/Linux.
+ Función para crear el label de versión del programa.
+ Se agregaron imágenes: windows, linux, cuadrados amarillos y negros, csv, python logo, regedit.
+ Nuevo widget CTkImegeBox, inserta una imágen en pantalla, permite adaptar su tamaño y ubicarlo como un botón.
