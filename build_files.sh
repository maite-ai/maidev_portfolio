#!/bin/bash

echo "🚀 Initializing Mai portfolio - Python Developer"
echo "=================================================="
echo ""

# Check if virtual environment exists
VIRTUALENV="portfolio"
if [ -d "$HOME/.pyenv/versions/$VIRTUALENV" ]; then
  echo "The '$VIRTUALENV' virtualenv exists"
else
  echo "📦 Creating virtual environment..."
  pyenv virtualenv 3.12.9 mai-portfolio
fi

# Activate virtual environment
echo "⚡ Activating virtual environment..."
pyenv local portfolio

# Build script for Vercel deployment
echo "Building Django project for Vercel..."

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
#echo "🗃️ Executing migrations..."
#python manage.py migrate

# Collect static files
echo "📁 Collecting statics files..."
python manage.py collectstatic --noinput --clear

echo "📁 Preparing static files for Vercel..."
cp -r staticfiles staticfiles_build

echo "✅ Build completed!"
