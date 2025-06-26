# 🛢️ Blog Petrolero - Proyecto Final Django

Bienvenidos al **Blog Petrolero**, un sitio web desarrollado como proyecto final individual para el curso de Python con Django de **CODERHOUSE**.

Este blog tiene como objetivo ser un espacio técnico en el que se puedan **publicar artículos, compartir documentación y experiencias** relacionadas con la **industria del petróleo**. 
Fue creado por **Manuel Vera Carrillo**, ingeniero en petróleo con más de 5 años de experiencia en sistemas de extracción y producción tanto en la operacion, como en la rama Ingenieril.

---

## 📌 ¿Qué ofrece este proyecto?

La aplicación web incluye todas las funciones esenciales de un blog técnico profesional, y está desarrollada en Python con el framework Django.

### ✔️ Funcionalidades principales:

- ✅ Registro y login de usuarios
- ✅ Perfil de usuario básico
- ✅ Creación, lectura y eliminación de publicaciones técnicas
- ✅ Vista general de blogs con filtros de búsqueda
- ✅ Subida y descarga de archivos técnicos (PDF, DOC, etc.)
- ✅ Página de "Acerca de mí"
- ✅ Estilo visual responsive con Bootstrap 5
- ✅ Navegación fluida sin usar la barra del navegador

---

## 🧠 ¿Cómo está estructurado?

El proyecto está dividido en dos aplicaciones:

### 1. `usuarios/`
- Registro de nuevos usuarios
- Login y logout
- Página personalizada de “Acerca de mí”
- Redirección automática tras login y logout

### 2. `pages/`
- Gestión de publicaciones técnicas (con título, autor, fecha y contenido)
- Filtro de búsqueda por título o autor
- Subida de archivos técnicos en múltiples formatos
- Listado de archivos subidos por los usuarios

---

## 🖼️ Diseño general

### Barra de navegación

- **Logo** del blog a la izquierda
- Botones de navegación visibles:  
  - `Inicio`  
  - `Blogs`  
  - `Documentos`  
  - `Acerca de mí`  
  - `Iniciar sesión / Registrarse` (o `Cerrar sesión` si ya estás logueado)

### Página principal (`/`)

- Banner con imagen petrolera
- Bienvenida al visitante
- Botón de acceso directo a las publicaciones

### Página de Blogs (`/pages/`)

- Muestra una lista de publicaciones técnicas
- Filtro de búsqueda por título o autor
- Cada entrada tiene:
  - Título
  - Resumen (contenido truncado)
  - Autor y fecha
  - Botón “Leer más” para acceder al detalle
- Si el usuario está logueado, también verá el botón “Nueva publicación”

### Página de carga de archivos (`/pages/archivos/`)

- Muestra los documentos técnicos subidos por los usuarios
- Botón para “Subir nuevo archivo” (visible solo para usuarios logueados)
- Cada archivo muestra:
  - Título y descripción
  - Autor
  - Fecha de subida
  - Botón de descarga

---

## 👨‍🔧 Tecnologías utilizadas

- Python 3.13
- Django 5.2
- Bootstrap 5 (CDN)
- Bootstrap Icons
- SQLite (por defecto)
- HTML, CSS
- Sistema de archivos para medios (MEDIA)

---

## 🚀 ¿Cómo correr este proyecto?

### 1. Clonar el repositorio

```bash
git clone https://github.com/ManoloVC/Entrega_Final-VeraCarrillo.git
cd Entrega_Final-VeraCarrillo
