#!/bin/bash

echo "🚀 Iniciando Portfolio de Mai - Python Developer"
echo "=================================================="
echo ""

# Check if virtual environment exists
VIRTUALENV="portfolio"
if [ -d "$HOME/.pyenv/versions/$VIRTUALENV" ]; then
  echo "El entorno virtual '$VIRTUALENV' existe"
else
  echo "📦 Creando entorno virtual..."
  pyenv virtualenv 3.12.9 mai-portfolio
fi

# Activate virtual environment
echo "⚡ Activando entorno virtual..."
pyenv local portfolio

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

# Start development server
python manage.py runserver

echo "🚀 Iniciando servidor..."
echo "   (Presiona Ctrl+C para detenerlo)"
