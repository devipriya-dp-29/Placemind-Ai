import os
import django
import json

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_system.settings')
django.setup()

from placements.models import MockTest

def populate_mock_tests():
    questions_bank = [
        {
            "id": 1,
            "question": "What is the time complexity of searching an element in a balanced Binary Search Tree?",
            "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
            "correctIndex": 1,
            "skills": ["Data Structures", "Algorithms"]
        },
        {
            "id": 2,
            "question": "Which of the following is NOT a primary principle of Object-Oriented Programming?",
            "options": ["Encapsulation", "Inheritance", "Polymorphism", "Compilation"],
            "correctIndex": 3,
            "skills": ["Java", "OOP", "Python"]
        },
        {
            "id": 3,
            "question": "In React, which hook is used to handle side effects?",
            "options": ["useState", "useContext", "useEffect", "useReducer"],
            "correctIndex": 2,
            "skills": ["React", "JavaScript", "Frontend"]
        },
        {
            "id": 4,
            "question": "What does SQL stand for?",
            "options": ["Structured Query Language", "Simple Query Language", "Statement Query Language", "Sequential Query Language"],
            "correctIndex": 0,
            "skills": ["SQL", "Database"]
        },
        {
            "id": 5,
            "question": "Which HTTP method is typically used to update an existing resource?",
            "options": ["GET", "POST", "PUT", "DELETE"],
            "correctIndex": 2,
            "skills": ["Networking", "Web Development"]
        },
        {
            "id": 6,
            "question": "What is the purpose of the 'git clone' command?",
            "options": ["Create a new branch", "Copy a repository from a remote server", "Commit changes", "Merging branches"],
            "correctIndex": 1,
            "skills": ["Git", "Version Control"]
        },
        {
            "id": 7,
            "question": "Which of these is a Python data type that is immutable?",
            "options": ["List", "Dictionary", "Set", "Tuple"],
            "correctIndex": 3,
            "skills": ["Python"]
        },
        {
            "id": 8,
            "question": "What is a 'Primary Key' in a database table?",
            "options": ["A key that opens the database", "A unique identifier for each record", "A secondary index", "A foreign relationship"],
            "correctIndex": 1,
            "skills": ["Database", "SQL"]
        },
        {
            "id": 9,
            "question": "Which sorting algorithm has the best average time complexity?",
            "options": ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"],
            "correctIndex": 2,
            "skills": ["Algorithms", "Data Structures"]
        },
        {
            "id": 10,
            "question": "What is the result of 10 + '5' in JavaScript?",
            "options": ["15", "105", "Error", "NaN"],
            "correctIndex": 1,
            "skills": ["JavaScript", "Frontend"]
        },
        {
            "id": 11,
            "question": "Which of the following is a NoSQL database?",
            "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"],
            "correctIndex": 2,
            "skills": ["Database", "Backend"]
        },
        {
            "id": 12,
            "question": "What does CSS stand for?",
            "options": ["Creative Style Sheets", "Cascading Style Sheets", "Computer Style Sheets", "Colorful Style Sheets"],
            "correctIndex": 1,
            "skills": ["CSS", "Frontend"]
        },
        {
            "id": 13,
            "question": "Which company developed Java?",
            "options": ["Microsoft", "Sun Microsystems", "Apple", "Google"],
            "correctIndex": 1,
            "skills": ["Java"]
        },
        {
            "id": 14,
            "question": "In Python, how do you start a block of code?",
            "options": ["{", "(", ":", "["],
            "correctIndex": 2,
            "skills": ["Python", "Algorithms"]
        }
    ]

    # Create a general assessment
    test, created = MockTest.objects.get_or_create(
        title="Technical Skill Assessment (AI-Trained)",
        defaults={
            "description": "Comprehensive test covering DS, OOP, React, and SQL based on training datasets.",
            "total_marks": 100,
            "duration_minutes": 30,
            "questions": questions_bank
        }
    )

    if not created:
        test.questions = questions_bank
        test.save()
        print("Updated existing assessment with more questions.")
    else:
        print("Created new technical assessment.")

    # Create an Aptitude test
    aptitude_test, apt_created = MockTest.objects.get_or_create(
        title="Quantitative Aptitude & Reasoning",
        defaults={
            "description": "Evaluate basic math, logic, and problem solving skills.",
            "total_marks": 50,
            "duration_minutes": 20,
            "questions": [
                {
                    "id": 1,
                    "question": "If a train 120m long passes a pole in 6 seconds, what is its speed?",
                    "options": ["72 km/hr", "60 km/hr", "54 km/hr", "45 km/hr"],
                    "correctIndex": 0,
                    "skills": ["Aptitude", "Math"]
                },
                {
                    "id": 2,
                    "question": "What is the next number in the series: 2, 6, 12, 20, 30, ...?",
                    "options": ["40", "42", "44", "48"],
                    "correctIndex": 1,
                    "skills": ["Reasoning", "Pattern"]
                },
                {
                    "id": 3,
                    "question": "If NOIDA is written as OPJEB, then what will be the code for DELHI?",
                    "options": ["EFMID", "EFMIJ", "EFMIK", "EFMIM"],
                    "correctIndex": 1,
                    "skills": ["Reasoning", "Logic"]
                }
            ]
        }
    )
    if apt_created:
        print("Created Quantitative Aptitude assessment.")

    # Create a Frontend assessment
    frontend_test, frontend_created = MockTest.objects.get_or_create(
        title="Frontend Web Development",
        defaults={
            "description": "Assess HTML, CSS, JavaScript, and framework knowledge like React.",
            "total_marks": 60,
            "duration_minutes": 25,
            "questions": [
                {
                    "id": 1,
                    "question": "What does DOM stand for in JavaScript?",
                    "options": ["Document Object Mechanism", "Document Oriented Model", "Document Object Model", "Dynamic Object Model"],
                    "correctIndex": 2,
                    "skills": ["JavaScript", "Frontend"]
                },
                {
                    "id": 2,
                    "question": "In CSS, how to make the text bold?",
                    "options": ["font-weight: bold", "style: bold", "font: bold", "text-style: bold"],
                    "correctIndex": 0,
                    "skills": ["CSS", "Frontend"]
                }
            ]
        }
    )
    if frontend_created:
        print("Created Frontend Web Development assessment.")

if __name__ == "__main__":
    populate_mock_tests()
