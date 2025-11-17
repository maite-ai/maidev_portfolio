#!/bin/bash

# Build script for Vercel deployment
echo "Building Django project for Vercel..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

echo "📁 Preparing static files for Vercel..."
cp -r staticfiles staticfiles_build

echo "✅ Build completed!"
