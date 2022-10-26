# Actividad grupal: Resolución de un problema mediante búsqueda heurística

- Objetivos de la actividad.
  - Implementar la estrategia de búsqueda heurística A* para la resolución de un problema real.
  
## Descripción de la actividad y pautas de elaboración.

La empresa Amazon desea utilizar un robot para ordenar el inventario de su almacén. Amazon cuenta con tres inventarios (mesa con suministros para vender) localizados en unas posiciones específicas del almacén. El robot se debe encargar de mover los tres inventarios a una posición objetivo.

El robot puede moverse horizontal y verticalmente, y cargar o descargar un inventario. Un ejemplo del robot, moviendo el inventario, se puede observar [en vídeo](https://youtu.be/UtBa9yVZBJM).

## FHS

- La carpeta `writing` contiene el algoritmo seguido a mano.
- Los archivos con nombre `mexmiart04t6actgr` contiene el reporte de la actividad en distintos formatos. El archivo fuente es `mexmiart04t6actgr.org`, desde él se puede incluso ejecutar el código fuente si la configuración de Org-babel es correcta. Se recomienda `mexmiart04t6actgr.pdf` para la lectura.
- `a-star.lisp` contiene el programa hecho en Common Lisp.
- `a-star.out` contiene un log de la ejecución completa del programa.

## Replicar el ejercicio

### Instalación

#### En un sisitema *nix like (GNU/Linux, FreeBSD, MacOS, etc)

1. Instalar desde el gestor de paquetes de su preferencia una implementación de Lisp, por ejemplo SBCL o CLisp. Ejemplo:

	   apt install sbcl

2. Instalar Quicklisp tal cual indica su [página de instalación](https://www.quicklisp.org/beta/)

	   curl -O https://beta.quicklisp.org/quicklisp.lisp
	   sbcl --load quicklisp.lisp
	
Y dentro de sbcl:

	(quicklisp-quickstart:install)

3. (Opcional) Instalar Emacs, configurar la variable `inferior-lisp-program`. Presione las teclas **Alt - :**, verá en la parte inferior de la pantalla el texto **Eval:** y presione:

	(setq inferior-lisp-program "sbcl")
	
	- Abrir el archivo `a-star.lisp`. Presione las teclas **Ctrl - x** seguido de  **Ctrl - f**, al seleccionar el archivo presione **Enter** y verá su contenido.
	
	- Podrá dividir en dos la pantalla (**Ctrl - x 3**) y ejecutar el intérprete de Lisp (**Ctrl - c** y luego **Ctrl - z**).
		
	- Coloque el cursor sobre el nombre de cada instrucción del archivo de Lisp y presione **Ctrl - c** seguido de **Ctrl - e** para ejecutarlo. Verá el nombre de la instrucción reflejada en el intérprete, lo cual indicará que se ha ejecutado correctamente. Un ejemplo de ejecución puede ser visto en `a-star.out`.

4. (Opcional) Copie y pegue dentro del intérprete de Lisp cada bloque de código. Si se ejecuta correctamente debería ver el nombre del bloque en mayúsculas.

### En un sistema Windows

1. Instalar desde la pagina de http://www.sbcl.org/ el instalador de windows (32 y 64), hay algunas veces que la pagina no esta disponible asi que se cuenta con un repositorio de respaldo en https://github.com/sbcl/sbcl

2. Ejecutar el archivo descargado e instalar como cualquier aplicacion de windows. Cuando termine la instalacion, se tiene que agregar en las variables de entorno (variables del sistema - Variables de entorno - seleccionar Patch y editar - Nuevo - agregamos las iniciales sbcl. Agregada la variable de entorno, en la ventana de Editar variable de Entorno, le ponemos en examinar y buscamos donde quedo instalado Steel Bank Common Lisp . Por ultimo damos click en Aceptar en todas las ventanas

3. Cerrar la Terminal y volverla a abrir para que los cambios en el Patch tengan efecto

4. Abrimos la terminal de Windows Power Shell y escribimos sbcl, para confirmar que fue instalado de forma correcta 

5. Instalamos QuickLisp para poder abrir archivos de Lisp. QuickLisp se instala de https://www.quicklisp.org/beta/ donde vienen todas las instrucciones paso a paso para instalarlo en la terminal 

6.     $ **curl -O [https://beta.quicklisp.org/quicklisp.lisp]
       % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
       100 49843  100 49843    0     0  33639      0  0:00:01  0:00:01 --:--:-- 50397
       
       $ **curl -O [https://beta.quicklisp.org/quicklisp.lisp.asc]

       $ **gpg --verify quicklisp.lisp.asc quicklisp.lisp**
       gpg: Signature made Sat Feb  1 09:25:28 2014 EST using RSA key ID 028B5FF7
       gpg: Good signature from "Quicklisp Release Signing Key
       
       $ sbcl --load quicklisp.lisp
       
	   This is SBCL 1.0.42.52, an implementation of ANSI Common Lisp.
       More information about SBCL is available at <http://www.sbcl.org/>.
       SBCL is free software, provided as is, with absolutely no warranty.
       It is mostly in the public domain; some portions are provided under
       BSD-style licenses.  See the CREDITS and COPYING files in the
       distribution for more information.
       
       ==== quicklisp quickstart loaded ====

       To continue, evaluate: (quicklisp-quickstart:install)
       
       * (quicklisp-quickstart:install)

		
	   Fetching #<URL "http://beta.quicklisp.org/dist/quicklisp/2010-10-07/systems.txt">
	   45.30KB
       ==================================================
       46,386 bytes in 0.50 seconds (89.70KB/sec)
       Fetching #<URL "http://beta.quicklisp.org/dist/quicklisp/2010-10-07/releases.txt">
       83.49KB
       ==================================================
       85,490 bytes in 0.53 seconds (157.22KB/sec)
       #<SYSTEM cl-vectors / cl-vectors-20101006-git / quicklisp 2010-10-07>
       #<SYSTEM lispbuilder-sdl-cl-vectors / lispbuilder-20101006-svn / quicklisp 2010-10-       
       #<SYSTEM lispbuilder-sdl-cl-vectors-examples / lispbuilder-20101006-svn / quicklisp   
       #<SYSTEM lispbuilder-sdl-vecto / lispbuilder-20101006-svn / quicklisp 2010-10-07>
       #<SYSTEM lispbuilder-sdl-vecto-examples / lispbuilder-20101006-svn / quicklisp  
       #<SYSTEM static-vectors / static-vectors-20101006-git / quicklisp 2010-10-07>
       #<SYSTEM vecto / vecto-1.4.3 / quicklisp 2010-10-07>
       NIL


       * (ql:quickload "vecto")
       To load "vecto":
       Install 5 Quicklisp releases:
       cl-vectors salza2 vecto zpb-ttf zpng
       Fetching #<URL "http://beta.quicklisp.org/archive/salza2/2010-10-06/salza2- 2.0.7.tgz">
       14.84KB
       ==================================================
       15,197 bytes in 0.12 seconds (125.77KB/sec)
       Fetching #<URL "http://beta.quicklisp.org/archive/zpng/2010-10-06/zpng-1.2.tgz">
       38.59KB
       ==================================================
       39,521 bytes in 0.37 seconds (103.47KB/sec)
       Fetching #<URL "http://beta.quicklisp.org/archive/zpb-ttf/2010-10-06/zpb-ttf-1.0.tgz">
       42.59KB
       ==================================================
       43,611 bytes in 0.39 seconds (110.33KB/sec)
       Fetching #<URL "http://beta.quicklisp.org/archive/cl-vectors/2010-10-06/cl-vectors-20101006-git.tgz">
       40.40KB
       ==================================================
       41,374 bytes in 0.37 seconds (109.20KB/sec)
       Fetching #<URL "http://beta.quicklisp.org/archive/vecto/2010-10-06/vecto-1.4.3.tgz">
       75.71KB
       ==================================================
       77,526 bytes in 0.49 seconds (153.57KB/sec)
       Loading "vecto"
       ..................................................
       [package zpb-ttf].................................
       [package salza2]..................................
       [package zpng]....................................
       [package net.tuxee.paths].........................
       [package net.tuxee.aa]............................
       [package net.tuxee.aa-bin]........................
       [package net.tuxee.vectors].......................
       [package vecto]........
       ("vecto")
       * (ql:add-to-init-file)
       I will append the following lines to #P"/Users/quicklisp/.sbclrc":

       ;;; The following lines added by ql:add-to-init-file:
        #-quicklisp
        (let ((quicklisp-init (merge-pathnames "quicklisp/setup.lisp"
                                         (user-homedir-pathname))))
       (when (probe-file quicklisp-init)
         (load quicklisp-init)))

        Press Enter to continue.

       #P"/Users/quicklisp/.sbclrc"
       (quit)
       $ 
7. Se tiene ya QuicLisp instalado

8. Los archivos Lisp pueden ejecutarse directamente desde la terminal, usando AutoCad o LispWorks.

Se recomienda ver un [video tutorial](https://www.youtube.com/watch?v=Egg0IkWDpwY) para seguir el proceso de instalación.

## Licencia
This repo is part of Actividades escolares UNIR

Copyright (C) 2021, Edgar Uriel Domínguez Espinoza, Aldo Alberto Bernal Castillo , Maria Inés Calderón Zetter

Actividades escolares UNIR is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Actividades escolares UNIR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Actividades escolares UNIR; if not, see <http://www.gnu.org/licenses/> or write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
