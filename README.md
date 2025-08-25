# 🎬 Movie Reviews Project  

Una aplicación web desarrollada con **Django** que le permite a los usuarios explorar películas, consultar detalles como título, género, año y descripción, además de acceder a noticias y estadísticas visuales del mundo del cine.  

---

## ✨ Características principales  

- 🔍 **Buscador de películas**  
  Permite encontrar películas ingresando su nombre, mostrando información como imagen, descripción, género, año y enlace externo.  

- 📰 **Sección de noticias**  
  Muestra noticias destacadas relacionadas con cine y actualidad, presentadas en un diseño adaptable para distintos dispositivos.  

- 📊 **Estadísticas visuales**  
  Gráficas interactivas de:  
  - Cantidad de películas por año.  
  - Cantidad de películas por género (considerando solo el primer género).  

- 📩 **Formulario de suscripción**  
  Los usuarios pueden registrar su correo electrónico para recibir actualizaciones.  

---

## 🛠️ Tecnologías utilizadas  

- **Python 3.12.3**  
- **Django Framework**  
- **SQLite** como base de datos por defecto  
- **HTML5**  
- **Bootstrap 5** para el diseño responsivo  
- **Matplotlib** para las gráficas  

---

## 🚀 Cómo ejecutar el proyecto  

1. Clonar el repositorio:  
   git clone https://github.com/JeanArdila711/TallerP1
2. Crear un entorno virtual:
    python -m venv env
    2.1 Activar el entorno virtual:
        .\env\Scripts\activate
3. Instalar depedencias:
    pip install -r requirements.txt
4. Aplicar migraciones:
    python manage.py migrate
5. Ejecutar servidor:
    python manage.py runserver
6. Acceder en el navegador:     
    http://127.0.0.1:8000
    

## 📌 Autor

👤 Jean Carlo Ardila