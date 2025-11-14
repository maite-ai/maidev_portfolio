#!/bin/bash

echo "🚀 Iniciando Portfolio de Mai - Python Developer"
echo "=================================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "⚡ Activando entorno virtual..."
source venv/bin/activate

# Install dependencies
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# Run migrations
echo "🗃️ Ejecutando migraciones..."
python manage.py migrate

# Collect static files
echo "📁 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo ""
echo "✨ ¡Todo listo! El servidor se iniciará en http://127.0.0.1:8000/"
echo ""
echo "🚀 Iniciando servidor de desarrollo..."
echo "   Presiona Ctrl+C para detener el servidor"
echo ""

# Start development server
python manage.py runserver
