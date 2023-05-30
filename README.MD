# **Proyecto colaborativo.🐱‍💻**

***
<img src="https://icon-library.com/images/icon-python/icon-python-3.jpg" align="right"
     alt="logo" width="200" height="200">


El repositorio actual tiene la finalidad de integrar de forma colaborativa características que enriquezcan el archivo denominado main.py, de tal forma que este evolucione siendo capaz de lograr cosas maravillosas gracias al bonito lenguaje de programación de python.

## *Algunas ideas a contribuir...*

- Nueva funcionalidad
- Corrección de errores
- Usabilidad en términos de diseño 
- Entre otras posibilidades

***
# Guía para contribuir utilizando nuestro buen amigo Git Bash.

<img src="https://mir-s3-cdn-cf.behance.net/project_modules/hd/3651d537081535.5733bc340f7b2.png" align="right"
     alt="logo" width="200" height="200">

Necesitaremos 2 repositorios en git hub

- Repositorio original al contribuir
- Repositorio con un fork sobre el original que se alojará en nuestra cuenta


Una vez que contamos con estos 2 repositorios: 


1. Abrimos Git bash

2. Clonamos a nuestra máquina el repositorio con el fork

```bash
git clone [Link del repositorio con el fork] 
```

3. Entramos al directorio del clon

```bash
cd [Nombre repositorio] 
```

4. Ahora abriremos el directorio, en este caso se utilizará VS Code

```bash
code .
```

5. Agregamos una conexion con el repositorio original llamado upstream

```bash
git remote add upstream [Link del repositorio original]
```

6. Ahora contamos con 2 repositorios: 

- El repositorio con el fork ( origin )
- El repositorio original ( upstream )

7. Lo comprobamos de la siguente forma

```bash
git remote -v
```

8. Traemos las posibles modificaciones que se hayan realizado en el repositorio original con conexion de nombre upstream

```bash
git fetch upstream
```
```bash
git rebase upstream/main
```

9. Forzamos a traer los cambios de la conexion upstream al origin para que este tenga las ultimas actualizaciones

```bash
git push origin main --force
```

10. Realizamos nuestras aportaciones

11. Realizamos el commit

```bash
git status
```
```bash
git add .
```
```bash
git commit -m "Mi aportación"
```

12. Realizamos el push

```bash 
git push origin main
```


13. Crea finalmente un Pull Request al maestro de python y espera a que acepte tu solicitud de aportación, recuerda que el profe aún rifa 😎.