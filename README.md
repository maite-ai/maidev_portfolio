# Portfolio de María Fernanda Ríos (Mai) 🚀

Un sitio web portfolio moderno con temática espacial desarrollado con Django + HTMX.

## 🌟 Características

- **Temática Espacial**: Diseño con colores azul oscuro, lila y elementos futuristas
- **Tono Amigable** (Inspirado en el portfolio de [Charles Bruyerre](https://itssharl.ee/))
- **Tecnología Moderna**: Django + HTMX para interacciones dinámicas
- **Responsive**: Adaptado para dispositivos móviles y desktop
- **Glassmorphism**: Efectos de cristal y transparencias
- **Animaciones**: Transiciones suaves y efectos de hover

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.12.9
- pip (actualizado)

### Pasos de Instalación

1. **Crear entorno virtual** (recomendado):

- Usando *venv*:
```bash
python -m venv venv
venv\Scripts\activate # o en Linux: source venv/bin/activate
```

- Usando *pyenv-virtualenv*:
```bash
pyenv virtualenv 3.12.9 portfolio
pyenv local portfolio
```

2. **Instalar Django y dependencias**:
```bash
pip install -r requirements.txt
```

3. **Ejecutar migraciones**:
```bash
python manage.py migrate
```

4. **Ejecutar servidor de desarrollo**:
```bash
python manage.py runserver
```

5. **Abrir en el navegador**: http://127.0.0.1:8000/

## 📁 Estructura del Proyecto

```
mai_portfolio/              # Raíz del repositorio
├── config/                 # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/              # Aplicación principal
│   ├── templates/          # Templates HTML
│   │   └── portfolio/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── about.html
│   │       ├── experience.html
│   │       ├── projects.html
│   │       └── contact.html
│   ├── static/            # Archivos estáticos
│   │   └── portfolio/
│   │       ├── css/
│   │       ├── js/
│   │       └── images/
│   ├── templatetags/      # Filtros personalizados
│   ├── views.py           # Vistas
│   └── urls.py           # URLs de la app
└── manage.py
```

## 🎨 Secciones del Portfolio

### 🏠 Inicio (Home)
- Saludo amigable
- Imagen de perfil temática: espacial /astronauta
- Resumen profesional
- Enlaces rápidos a otras secciones

### 👩‍💻 Sobre Mí (About)
- Habilidades técnicas organizadas por categorías
- Habilidades blandas con iconos
- Idiomas con barras de progreso
- Filosofía personal

### 💼 Experiencia (Experience)
- Timeline de experiencia laboral
- Detalles de educación
- Evolución profesional

### 🚀 Proyectos (Projects)
- Showcase de proyectos principales
- Detalles técnicos y rol en cada proyecto
- Tecnologías utilizadas
- Habilidades desarrolladas

### 📞 Contacto (Contact)
- Información de contacto
- Formulario funcional (con HTMX)
- Disponibilidad y servicios
- Enlaces a redes sociales

## 🛠 Tecnologías Utilizadas

### Backend
- **Django 5.2.8**: Framework web robusto
- **Python 3.12**: Lenguaje de programación

### Frontend
- **HTMX 1.8.5**: Interacciones dinámicas sin JavaScript complejo
- **CSS3**: Glassmorphism, gradientes, animaciones
- **Font Awesome 6.4.0**: Iconografía
- **Google Fonts (Inter)**: Tipografía moderna

### Características Técnicas
- **Responsive Design**: CSS Grid y Flexbox
- **Glassmorphism**: Efectos de cristal y transparencias
- **Animaciones CSS**: Transiciones suaves
- **Template Tags Personalizados**: Filtros para manipulación de datos
- **CSRF Protection**: Seguridad en formularios

## 🎨 Paleta de Colores

```css
:root {
    --space-dark: #0a0a23;          /* Azul muy oscuro */
    --space-blue: #1a1a40;          /* Azul oscuro */
    --space-purple: #2d1b69;        /* Púrpura oscuro */
    --space-light-purple: #3f2a8a;  /* Púrpura medio */
    --space-pink: #9d4edd;          /* Rosa/púrpura brillante */
    --space-cyan: #00f5ff;          /* Cian brillante */
    --text-white: #ffffff;          /* Blanco */
    --text-gray: #b8b8b8;          /* Gris claro */
}
```

## ⚡ Funcionalidades HTMX

- **Navegación Dinámica**: Carga de contenido sin refresco de página
- **Formulario de Contacto**: Envío asíncrono con feedback inmediato
- **Indicadores de Carga**: Spinners durante las transiciones
- **Animaciones de Entrada**: Efectos fade-in para contenido nuevo

## 🔧 Personalización

### Modificar Estilos
- Colores: Variables CSS en `templates/portfolio/base.html`
- Diseño: Archivos CSS en `portfolio/static/portfolio/css/`
- Animaciones: Keyframes en el template base

### Agregar Nuevas Secciones
1. Crear nueva vista en `views.py`
2. Crear template en `templates/portfolio/`
3. Agregar URL en `urls.py`
4. Actualizar navegación en `base.html`

## 🚀 Próximos Pasos

- [ ] **Blog**: Sección de artículos/posts
- [ ] **Multiidioma**: Soporte para switchear entre inglés y español
- [ ] **SEO**: Meta tags y optimización
- [ ] **Analytics**: Google Analytics integration

## 📝 Notas de Desarrollo

- Los archivos estáticos se sirven automáticamente en desarrollo
- Las imágenes de fondo utilizan gradientes CSS para mejor rendimiento
- La navegación conserva el estado activo usando template tags

## 📄 Licencia

Este proyecto es de uso personal para el portfolio de María Fernanda Ríos.
Puedes utilizarlo como *template* para crear el tuyo y adaptarlo a tu gusto con tu estilo.

## 👨‍💻 Desarrollado por
- **Claude Sonnet 4** (Web)

- **María Fernanda Ríos** (Ajustes)

## 👨‍💻 Contacto
- 💼 [Mi perfil en LinkedIn](https://www.linkedin.com/in/mafernandar)
- 🐙 GitHub: Aquí mismo 😉

---

¡Gracias por visitar el Readme de mi portfolio! 🚀✨
