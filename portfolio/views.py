from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Home page with hero section and overview"""
    context = {
        'name': 'María Fernanda Ríos',
        'nickname': 'Mai',
        'title': 'Python Developer',
        'summary': 'Experienced Python Developer that builds useful company\'s solutions with Python and Data Processing. Strong background in Object Oriented Programming and Web Development.',
        'location': 'Buenos Aires, Argentina',
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
                'title': 'Software Developer',
                'company': 'INECON',
                'type': 'Freelance position',
                'period': 'Mar 2025 - Nov 2025',
                'description': 'Developed an executable application to automate tariff analysis processes, this includes reports generation, consolidation processes covering complex validation steps, reducing the user job by ~95% (1 hour manual analysis vs ~2.5 minutes automated analysis).',
                'technologies': 'CustomTKinter, Pandas, OpenPyXL, SOLID principles, MVC pattern'
            },
            {
                'title': 'Data Science and AI Bootcamp Teacher',
                'company': 'Le Wagon',
                'type': 'Freelance position',
                'period': 'Dec 2023 - Present',
                'description': 'Teached advanced Python programming concepts for data science and machine learning applications. Mentored in end-to-end ML projects, including data preprocessing, model selection, training and evaluation.',
                'technologies': 'Python, Machine Learning, FastAPI, Docker, Google Cloud Platform'
            }
        ],
        'education': [
            {
                'title': 'Data Science & AI Bootcamp',
                'institution': 'Le Wagon',
                'period': 'Jul 2023 - Sep 2023',
                'description': 'Completed intensive 9-week program focused on production-ready ML applications.',
                'technologies': 'Python, Pandas, NumPy, TensorFlow, Docker, FastAPI'
            },
            {
                'title': 'Web Full Stack Development',
                'institution': 'Digital House',
                'period': 'Mar 2021 - Aug 2021',
                'description': 'Completed full-stack web development program with focus on modern technologies.',
                'technologies': 'MERN stack: MySQL, ExpressJs, React, Node.js'
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
                'type': 'Data Science group project (Le Wagon)',
                'period': 'Sep 2023',
                'description': 'Application for gaming content creators powered by a CNN model specialized in Sound Event Detection that improves their workflow by reducing the editing time.',
                'technologies': 'MoviePy, NumPy, Pandas, TensorFlow, Docker, Google Cloud Platform, FastAPI, Streamlit',
                'role': 'Data Scientist and Team Coordinator'
            },
            {
                'title': 'Peritroopers',
                'type': 'Web full stack development group project (Digital House)',
                'period': 'Aug 2021',
                'description': 'Web full stack application for an e-commerce that sells computer devices.',
                'technologies': 'HTML, CSS, NodeJS, MySQL, Bootstrap, ReactJS',
                'role': 'Full Stack Developer and Team Leader'
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
            'phone': '+54(11)7369-6010',
            'location': 'Buenos Aires, Argentina',
            'github': 'Github profile',
            'linkedin': 'LinkedIn profile'
        }
    }
    return render(request, 'portfolio/contact.html', context)

