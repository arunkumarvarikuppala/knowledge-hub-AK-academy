# Starter question bank for Knowledge Hub mock examinations.
# Add and teacher-verify questions before using these tests for formal assessment.

EXAMS = {
    "Class 9 Mathematics — Practice Test 1": {
        "class": "Class 9",
        "subject": "Mathematics",
        "duration_minutes": 15,
        "questions": [
            {
                "question": "Which of the following is an irrational number?",
                "options": ["1/2", "0.25", "√2", "4"],
                "answer": "√2",
                "explanation": "√2 cannot be expressed as a ratio of two integers."
            },
            {
                "question": "What is the degree of 3x² + 2x + 5?",
                "options": ["1", "2", "3", "5"],
                "answer": "2",
                "explanation": "The highest power of x is 2, so the degree is 2."
            },
            {
                "question": "Solve: x + 5 = 12.",
                "options": ["5", "6", "7", "17"],
                "answer": "7",
                "explanation": "Subtract 5 from both sides: x = 12 - 5 = 7."
            },
            {
                "question": "Which number is a whole number?",
                "options": ["-2", "0", "1/3", "√3"],
                "answer": "0",
                "explanation": "Whole numbers include 0 and the positive integers."
            },
            {
                "question": "Solve: 2x = 18.",
                "options": ["8", "9", "16", "20"],
                "answer": "9",
                "explanation": "Divide both sides by 2: x = 9."
            },
        ],
        "written_questions": [
            {
                "question": "Explain the difference between rational and irrational numbers.",
                "reference_answer": "A rational number can be written as p/q for integers p and q with q ≠ 0. An irrational number cannot be written in that form."
            },
            {
                "question": "Solve 3x + 4 = 16 and show your steps.",
                "reference_answer": "Subtract 4 from both sides: 3x = 12. Divide by 3: x = 4."
            },
        ],
    },
    "Class 10 Mathematics — Practice Test 1": {
        "class": "Class 10",
        "subject": "Mathematics",
        "duration_minutes": 15,
        "questions": [
            {
                "question": "Which is the standard form of a quadratic equation?",
                "options": ["ax + b = 0", "ax² + bx + c = 0, a ≠ 0", "ax³ + b = 0", "x + y = 0"],
                "answer": "ax² + bx + c = 0, a ≠ 0",
                "explanation": "A quadratic equation has highest power 2 and a non-zero coefficient of x²."
            },
            {
                "question": "Factorise x² - 5x + 6.",
                "options": ["(x - 1)(x - 6)", "(x + 2)(x + 3)", "(x - 2)(x - 3)", "(x + 1)(x - 6)"],
                "answer": "(x - 2)(x - 3)",
                "explanation": "The numbers -2 and -3 multiply to 6 and add to -5."
            },
            {
                "question": "Find the common difference of 2, 5, 8, 11, ...",
                "options": ["2", "3", "5", "8"],
                "answer": "3",
                "explanation": "Subtract consecutive terms: 5 - 2 = 3."
            },
            {
                "question": "What is the 5th term of the AP 4, 9, 14, 19, ...?",
                "options": ["19", "20", "24", "25"],
                "answer": "24",
                "explanation": "The sequence increases by 5; the 5th term is 24."
            },
            {
                "question": "What is the discriminant of x² - 4x + 4 = 0?",
                "options": ["0", "4", "8", "16"],
                "answer": "0",
                "explanation": "D = b² - 4ac = (-4)² - 4(1)(4) = 16 - 16 = 0."
            },
        ],
        "written_questions": [
            {
                "question": "Solve x² - 7x + 12 = 0 by factorisation.",
                "reference_answer": "x² - 7x + 12 = (x - 3)(x - 4) = 0, so x = 3 or x = 4."
            },
            {
                "question": "Write the nth-term formula for an arithmetic progression and explain its symbols.",
                "reference_answer": "aₙ = a + (n - 1)d, where a is the first term, d is the common difference, and n is the term number."
            },
        ],
    },
    "Class 10 Physics — Practice Test 1": {
        "class": "Class 10",
        "subject": "Physics",
        "duration_minutes": 15,
        "questions": [
            {
                "question": "What is the SI unit of work?",
                "options": ["Newton", "Watt", "Joule", "Pascal"],
                "answer": "Joule",
                "explanation": "Work is measured in joules (J)."
            },
            {
                "question": "Work done when force and displacement are in the same direction is:",
                "options": ["F/s", "F × s", "s/F", "F + s"],
                "answer": "F × s",
                "explanation": "For parallel force and displacement, W = F × s."
            },
            {
                "question": "The SI unit of force is:",
                "options": ["Joule", "Newton", "Watt", "Metre"],
                "answer": "Newton",
                "explanation": "Force is measured in newtons (N)."
            },
            {
                "question": "If displacement is zero, the work done by a constant force is:",
                "options": ["Zero", "Always 1 J", "Always negative", "Infinite"],
                "answer": "Zero",
                "explanation": "W = F × s × cos(θ); if displacement s is zero, work is zero."
            },
            {
                "question": "Which quantity is measured in joules?",
                "options": ["Force", "Distance", "Work", "Acceleration"],
                "answer": "Work",
                "explanation": "The joule is the SI unit of work and energy."
            },
        ],
        "written_questions": [
            {
                "question": "Define work done and write its formula.",
                "reference_answer": "Work is done when a force causes displacement. W = F × s × cos(θ); when force and displacement are in the same direction, W = F × s."
            },
            {
                "question": "Calculate work done by a 10 N force moving an object 3 m in the same direction.",
                "reference_answer": "W = F × s = 10 × 3 = 30 J."
            },
        ],
    },
}
