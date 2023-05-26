# **Proyecto colaborativo.🐱‍💻**


<img src="https://icon-library.com/images/icon-python/icon-python-3.jpg" align="right"
     alt="logo" width="200" height="200">


El repositorio actual tiene la finalidad de integrar de forma colaborativa características que enriquezcan el archivo denominado main.py, de tal forma que este evolucione siendo capaz de lograr cosas maravillosas gracias al bonito lenguaje de programación de python.

## *Algunas ideas a contribuir...*

- Nueva funcionalidad
- Corrección de errores
- Usabilidad en terminos de diseño 
- Entre otras posibilidades

***
# Guía para contribuir utilizando nuestro buen amigo Git Bash.

<img src="https://mir-s3-cdn-cf.behance.net/project_modules/hd/3651d537081535.5733bc340f7b2.png" align="right"
     alt="logo" width="200" height="200">

Necesitaremos 2 repositorios en git hub

- Repositorio original al contribuir
- Repositorio con un fork sobre el original que se alojará en nuestra cuenta


Una vez que contamos con estos 2 repositorios 


1. Abrimos Git bash

2. Clonamos a nuestra maquina el repositorio con con el fork

~~~
git clone [Link del repositorio con el fork] 
~~~

3. Entramos al directorio del clon

~~~
cd [Nombre repositorio] 
~~~

4. Ahora abriremos el directorio, en este caso se utilizará VS Code

~~~
code .
~~~

5. Agregamos una conexion con el repositorio original llamado upstream

~~~
git remote add upstream [Link del repositorio original]
~~~

6. Ahora contamos con 2 repositorios: 

- El repositorio con el fork ( origin )
- El repositorio original ( upstream )

7. Lo comprobamos de la siguente forma

~~~
git remote -v
~~~

8. Traemos las posibles modificaciones que se hayan realizado en el repositorio original con conexion de nombre upstream

~~~
git fetch upstream
~~~
~~~
git rebase upstream/main
~~~

9. Forzamos a traer los cambios de la conexion upstream al origin para que este tenga las ultimas actualizaciones

~~~
git push origin main --force
~~~

10. Realizamos nuestras aportaciones

11. Realizamos el commit

~~~
git status
~~~
~~~
git add .
~~~
~~~
git commit -m "Mi aportación"
~~~

12. Realizamos el push

~~~
git push origin main
~~~

