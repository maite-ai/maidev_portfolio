#!/bin/bash

echo "🚀 Initializing Mai portfolio - Python Developer"
echo "=================================================="
echo ""

# Activate virtual environment
echo "⚡ Activating virtual environment..."
python -m venv venv
source venv/bin/activate
echo ""

# Build script for Vercel deployment
echo "Building Django project for Vercel..."
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt
echo ""

# Run migrations
#echo "🗃️ Executing migrations..."
echo "⚡ Skipping database migrations (portfolio doesn't use database)"

# Collect static files
echo "📁 Collecting statics files..."
python manage.py collectstatic --noinput --clear
echo ""

# Debug: list what was collected
echo "🔍 Files collected in staticfiles:"
ls -la staticfiles/
echo "🔍 Portfolio static files:"
ls -la staticfiles/portfolio/ 2>/dev/null || echo "No 'portfolio' folder fouund"
echo "🔍 Images in statictfiles:"
find staticfiles/ -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" 2>/dev/null || echo "No images found"
echo ""

# Copy staticfiles to the directory that Vercel expects
echo "📁 Preparing static files for Vercel..."
cp -r staticfiles staticfiles_build

# Debug: Verify copu worked
echo "🔍 Files in staticfiles_build:"
ls -la staticfiles_build/
echo "🔍 Images in statictfiles_build:"
find staticfiles_build/ -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" 2>/dev/null || echo "No images found"
echo ""

echo "✅ Build completed!"
