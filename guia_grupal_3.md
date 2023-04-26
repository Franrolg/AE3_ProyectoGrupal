## Importar el modelo de usuario

- El primer paso es importar el modelo de usuario en el archivo `views.py` de la siguiente manera:

   ```
   from django.contrib.auth.models import User
   ```

   Esto permite acceder al modelo de usuario predefinido de Django.

## Crear una vista

- El siguiente paso es crear una vista en el archivo `views.py` que lea los datos de la base de datos SQLite3 y los muestre en una página web. Por ejemplo, si se quisiera mostrar todos los usuarios almacenados en la base de datos, se podría crear una vista de la siguiente manera:

   ```
   from django.shortcuts import render
   from django.contrib.auth.models import User

   def user_list(request):
       users = User.objects.all()
       return render(request, 'user_list.html', {'users': users})
   ```

   En este ejemplo, se ha creado una vista `user_list` que utiliza el método `all()` para obtener todos los usuarios almacenados en la base de datos y los almacena en una variable `users`. A continuación, la vista renderiza el archivo `user_list.html` y pasa la variable `users` como contexto.

## Crear una plantilla HTML

- El siguiente paso es crear una plantilla HTML que muestre los datos obtenidos por la vista. Por ejemplo, se podría crear una plantilla `user_list.html` de la siguiente manera:

   ```
   <h1>Lista de usuarios</h1>
   <ul>
   {% for user in users %}
       <li>{{ user.username }} (email: {{ user.email }})</li>
   {% endfor %}
   </ul>
   ```

   En este ejemplo, se ha creado una plantilla HTML que utiliza un bucle `for` para iterar sobre cada usuario en la lista `users` y mostrar su nombre de usuario y correo electrónico.

## Configurar la URL

- El último paso es configurar una URL en el archivo `urls.py` que apunte a la vista creada. Por ejemplo, se podría crear una URL de la siguiente manera:

   ```
   from django.urls import path
   from .views import user_list

   urlpatterns = [
       path('users/', user_list, name='user_list'),
   ]
   ```

   En este ejemplo, se ha creado una URL que apunta a la vista `user_list` y se ha asignado un nombre `user_list` para que pueda ser referenciado en otras partes de la aplicación.

Con estos cuatro pasos, se ha creado una aplicación web Django que muestra contenido dinámico desde la base de datos SQLite3 utilizando el modelo de usuario predefinido de Django. Ahora, cuando se visite la URL `/users/` en el navegador web, se mostrará una lista de todos los usuarios almacenados en la base de datos.