@echo off
echo 🚀 Iniciando Portfolio de Mai - Python Developer
echo ==================================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
)

REM Activate virtual environment
echo ⚡ Activando entorno virtual...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Instalando dependencias...
pip install -r requirements.txt

REM Run migrations
echo 🗃️ Ejecutando migraciones...
python manage.py migrate

REM Collect static files
echo 📁 Recolectando archivos estáticos...
python manage.py collectstatic --noinput

echo.
echo ✨ ¡Todo listo! El servidor se iniciará en http://127.0.0.1:8000/
echo.
echo 🚀 Iniciando servidor de desarrollo...
echo    Presiona Ctrl+C para detener el servidor
echo.

REM Start development server
python manage.py runserver

pause
