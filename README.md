
# Tu nevera

Proyecto de grados que trata de buscar recetas de comida entre los distintos ingredientes de las recetas que suben los usuarios.



## Caracteristicas

- Buscador en general de usuarios
- Buscador en general de recetas
- Buscador de recetas mediante seleccion de ingredientes ( pantalla de "vamos a cocinar!")

## Caracteristicas sin funcionar 
Las siguiente caracteristicas estan fuera de servicio o sin funcionar debido a que este proyecto fue realizado a mediados del 2018 por lo tanto muchas de las dependencias estan desactualizadas o debido a que se mantuvieron sin funcionar para poder deployarlo en el hosting de Render.

- Usuarios seguidos
- Configuracion de cuenta
- Mi perfil
- Subir receta
- Registrarse





## Instalacion y ejecucion

#### Migraciones

```bash
python manage.py migrate
```

#### Inserccion de datos
Abrir un gestor sql, dbeaver u otro para tomar el contenido del archivo `respaldo.sql` y ejecutar las insercciones de los datos a la base de datos sqlite

#### Ejecucion del proyecto

```bash
python manage.py runserver
```

#### Ejecucion del proyecto con gunicorn

```bash
gunicorn pruebasubir.wsgi 
```


## Usuario para ingresar:

```bash
User: root_default
Pass: root123456789
```


## Demo

https://tu-nevera.onrender.com/usuario/login/


## Authors

- [@AntonioAMPY](https://github.com/AntonioAMPY)
- [@Jpvillegas](https://github.com/Jpvillegas)

