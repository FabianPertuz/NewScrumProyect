🎥 MiniTikMatch
Una mini app de estilo TikTok creada con Python y GUI (Tkinter), donde los usuarios pueden:

Registrarse e iniciar sesión
Ver videos cortos subidos por otros usuarios
Darle like a los videos
Subir sus propios videos
Hacer “match” con otros usuarios si hay likes mutuos
🚀 Objetivo del Proyecto
Crear una versión simple y local de una red social de videos cortos usando solo Python, sin bases de datos complicadas, ideal para programadores en formación.

🧩 Funcionalidades
👤 Registro e Inicio de Sesión
Los usuarios se registran con un nombre de usuario y contraseña.
Los datos se guardan en un archivo users.json.
📹 Subir Video
El usuario puede seleccionar un archivo de video local (.mp4).
El video se copia a la carpeta /videos y se asocia al usuario en el JSON.
🎬 Ver Videos
El usuario puede ver videos de otros usuarios en pantalla.
Cada video tiene botones de:
👍 Like
⏭️ Siguiente
❤️ Dar Like
Al darle like a un video, se guarda el registro en likes.json con:
Usuario que da el like (from)
Dueño del video (to)
Si dos usuarios se han dado like mutuamente, se considera un match.
🔁 Match
Cuando hay un like mutuo, se guarda en matches.json:
{
  "user1": "ana",
  "user2": "juan"
}
