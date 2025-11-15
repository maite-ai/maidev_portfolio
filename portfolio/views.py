from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Home page with hero section and overview"""
    context = {
        'name': 'María Fernanda Ríos',
        'nickname': 'Mai',
        'title': 'Python Developer | Data Science & AI teacher',
        'summary': 'Experienced Python Developer that builds useful company\'s solutions with Python and Data Processing. Strong background in Object Oriented Programming and Web Development.',
        'location': 'Ciudad Autónoma de Buenos Aires, Argentina',
        'email': 'mariafernandarios89@gmail.com',
        'phone': '+54(11)7369-6010'
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """About section with detailed information"""
    context = {
        'skills': {
            'technical': [
                'Python frameworks: FastAPI',
                'Relational Databases: SQLite, MySQL',
                'Advanced Linux user with bash script knowledge',
                'DevOps: Docker, GCP (Google Cloud Platform)',
                'Other relevant skills: Clean code and good coding practices, Unit testing, Java & JavaScript, OOP, MVC design pattern, Data processing, Machine Learning, OpenPyXL'
            ],
            'soft': [
                'Self-taught learning', 'Collaboration', 'Flexibility', 'Initiative',
                'Good Communication and active listening', 'Problem-solving and decision-making in challenging scenarios',
                'Result oriented', 'Attention to detail', 'Deadline-driven environments'
            ]
        },
        'languages': [
            {'name': 'Spanish', 'level': 'Native'},
            {'name': 'English', 'level': 'C1'}
        ]
    }
    return render(request, 'portfolio/about.html', context)

def experience(request):
    """Experience and education section"""
    context = {
        'work_experience': [
            {
                'title': 'IT Consultant - Software Developer',
                'company': 'INECON',
                'type': 'Posición freelance',
                'period': 'Mar 2025 - Nov 2025',
                'description': 'Desarrollé íntegramente una aplicación ejecutable para automatizar procesos de análisis tarifario. Esto incluyó generación de reportes, consolidación de hojas de cálculo cubriendo varios y complejos pasos de validación de la información, reduciendo el trabajo del usuario en un ~95.',
                'technologies': 'CustomTKinter, Pandas, Openpyxl, Principios SOLID, Patrón de diseño MVC, Cadena de validación con estados, Documentación'
            },
            {
                'title': 'Profesora de bootcamps de Data Science & AI',
                'company': 'Le Wagon',
                'type': 'Posición freelance',
                'period': 'Dic 2023 - Presente',
                'description': 'Enseñé conceptos avanzados de programación en Python para aplicaciones de Data Science y Machine Learning. Brindé mentorías en la realización integral de proyectos finales que involucraba el procesamiento de los datos, la elección del modelo, entrenamiento y evaluación jugando un papel importante en el éxito de sus presentaciones.',
                'technologies': 'Python, Machine Learning, FastAPI, Docker, Google Cloud Platform'
            },
            {
                'title': 'Administrativo - ex-Personal Militar',
                'company': 'Armada Argentina',
                'type': 'Relación de dependencia',
                'period': 'Feb 2009 - Dic 2021',
                'description': 'Me desempeñé como operadora de radio, asistente administrativo, entre otras, pasando por jefaturas, estaciones de comunicaciones y buques militares. Participé en la campaña sanitaria de 2012, en la búsqueda del Submarino ARA San Juan y en el rescate de un herido del buque pesquero Praia do Santa Cruz',
                'technologies': 'N/A'
            }
        ],
        'education': [
            {
                'title': 'Data Science & AI Bootcamp',
                'institution': 'Le Wagon',
                'period': 'Jul 2023 - Sep 2023',
                'description': 'Completé el programa intensivo de 9 semanas enfocado en aplicaciones production-ready.',
                'technologies': 'Python, BeautifulSoup, Pandas, Seaborn, SciPy, Scikit-Learn, TensorFlow, Docker, FastAPI, GCP, Prefect, ML Flow, Streamlit'
            },
            {
                'title': 'Desarrollo Web Full Stack',
                'institution': 'Digital House',
                'period': 'Mar 2021 - Ago 2021',
                'description': 'Completé el curso de Desarrollo Web Full Stack con enfoque en el stack MERN.',
                'technologies': 'HTML & CSS, JavaScript, MySQL, ExpressJs, React, Node.js, Bootstrap'
            },
            {
                'title': 'Ingeniería de Sistemas de la Información (Abandonado)',
                'institution': 'CRUC - Instituto Universitario Aeronáutico',
                'period': 'Mar 2016 - Dic 2020',
                'description': 'Cursé la carrera y aprobé materias de los primeros años pero lo abandoné por razones laborales.',
                'technologies': 'Programación Orientada a Objetos (Java), Desarrollo de Aplicaciones Web, Matemáticas, Diseño y Administración de Bases de Datos (MySQL), Física, Administración de empresas, Arquitectura de Computadoras (Assembly)'
            }
        ]
    }
    return render(request, 'portfolio/experience.html', context)

def projects(request):
    """Projects showcase section"""
    context = {
        'projects': [
            {
                'title': 'Gameplay Video Auto Edit',
                'type': 'Proyecto grupal de Data Science (Le Wagon)',
                'period': 'Sep 2023',
                'description': 'Aplicación para creadores de contenido de gameplay que mejora su flujo de trabajo al reducir en un ~75% el tiempo de edición.',
                'technologies': 'Pandas, MoviePy, NumPy, TensorFlow, Docker, Google Cloud Platform, FastAPI, Streamlit',
                'role': 'Data Scientist trainee y Coordinadora de equipo'
            },
            {
                'title': 'Peritroopers',
                'type': 'Proyecto grupal de desarrollo web full stack (Digital House)',
                'period': 'Ago 2021',
                'description': 'Aplicación web para e-commerce que se dedica a la venta de dispositivos periféricos.',
                'technologies': 'HTML, CSS, NodeJS, MySQL, Bootstrap, ReactJS, Express.js',
                'role': 'Desarrolladora web trainee y Líder de equipo'
            }
        ]
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    """Contact information and form"""
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Here you could add email sending functionality
        # For now, just return a success message
        success_message = f"""
        <div style="background: rgba(0, 245, 255, 0.1); border: 1px solid rgba(0, 245, 255, 0.3); padding: 1rem; border-radius: 10px; text-align: center;">
            <i class="fas fa-check-circle" style="color: var(--space-cyan); margin-right: 0.5rem;"></i>
            <span style="color: var(--space-cyan);">¡Gracias {name}! Tu mensaje ha sido enviado. Te contactaré pronto.</span>
        </div>
        """
        return HttpResponse(success_message)

    context = {
        'contact_info': {
            'email': 'mariafernandarios89@gmail.com',
            'phone': '888888',
            'location': 'Ciudad Autónoma de Buenos Aires, Argentina',
            'github': 'https://github.com/maite-ai',
            'linkedin': 'https://www.linkedin.com/in/mafernandar'
        }
    }
    return render(request, 'portfolio/contact.html', context)
