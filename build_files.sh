#!/bin/bash

echo "🚀 Initializing Mai portfolio - Python Developer"
echo "=================================================="
echo ""

# Activate virtual environment
echo "⚡ Activating virtual environment..."
python -m venv venv
source venv/bin/activate

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
