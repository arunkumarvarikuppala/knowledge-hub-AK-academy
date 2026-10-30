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

# Additional general practice tests; teacher review recommended.
# These do not claim complete official ICSE syllabus coverage.
EXAMS.update({'Class 6 Mathematics — Practice Test 1': {'class': 'Class 6',
                                           'subject': 'Mathematics',
                                           'duration_minutes': 20,
                                           'questions': [{'question': 'What is the place value of 7 in '
                                                                      '47,305?',
                                                          'options': ['7', '70', '700', '7,000'],
                                                          'answer': '7,000',
                                                          'explanation': 'The digit 7 is in the '
                                                                         'thousands place: 7 × 1,000 = '
                                                                         '7,000.'},
                                                         {'question': 'Which of these numbers is prime?',
                                                          'options': ['21', '29', '35', '39'],
                                                          'answer': '29',
                                                          'explanation': '29 has exactly two positive '
                                                                         'factors: 1 and 29.'},
                                                         {'question': 'What is the HCF of 18 and 24?',
                                                          'options': ['3', '6', '12', '72'],
                                                          'answer': '6',
                                                          'explanation': 'Their common factors are 1, '
                                                                         '2, 3 and 6; the highest is '
                                                                         '6.'},
                                                         {'question': 'What is the LCM of 4 and 6?',
                                                          'options': ['2', '10', '12', '24'],
                                                          'answer': '12',
                                                          'explanation': '12 is the smallest positive '
                                                                         'number divisible by both 4 '
                                                                         'and 6.'},
                                                         {'question': 'Simplify 12/18 to its lowest '
                                                                      'terms.',
                                                          'options': ['2/3', '3/2', '6/9', '4/9'],
                                                          'answer': '2/3',
                                                          'explanation': 'Divide numerator and '
                                                                         'denominator by their HCF, 6, '
                                                                         'to get 2/3.'},
                                                         {'question': 'Calculate 3/4 + 1/8.',
                                                          'options': ['4/12', '1/2', '5/8', '7/8'],
                                                          'answer': '7/8',
                                                          'explanation': '3/4 = 6/8, and 6/8 + 1/8 = '
                                                                         '7/8.'},
                                                         {'question': 'Calculate 2.5 + 0.75.',
                                                          'options': ['2.125', '3.25', '3.75', '2.75'],
                                                          'answer': '3.25',
                                                          'explanation': 'Align the decimal points: '
                                                                         '2.50 + 0.75 = 3.25.'},
                                                         {'question': 'What is the perimeter of a '
                                                                      'rectangle of length 8 cm and '
                                                                      'width 5 cm?',
                                                          'options': ['13 cm',
                                                                      '26 cm',
                                                                      '40 cm',
                                                                      '80 cm'],
                                                          'answer': '26 cm',
                                                          'explanation': 'Perimeter = 2 × (length + '
                                                                         'width) = 2 × 13 = 26 cm.'},
                                                         {'question': 'What is the area of a square of '
                                                                      'side 6 cm?',
                                                          'options': ['12 cm²',
                                                                      '24 cm²',
                                                                      '36 cm²',
                                                                      '18 cm²'],
                                                          'answer': '36 cm²',
                                                          'explanation': 'Area = side × side = 6 × 6 = '
                                                                         '36 cm².'},
                                                         {'question': 'What is the size of a right '
                                                                      'angle?',
                                                          'options': ['45°', '90°', '180°', '360°'],
                                                          'answer': '90°',
                                                          'explanation': 'A right angle measures 90 '
                                                                         'degrees.'}],
                                           'written_questions': [{'question': 'Find the HCF and LCM of '
                                                                              '12 and 18. Show your '
                                                                              'method.',
                                                                  'reference_answer': '12 = 2² × 3 and '
                                                                                      '18 = 2 × 3². HCF '
                                                                                      '= 2 × 3 = 6. LCM '
                                                                                      '= 2² × 3² = 36.'},
                                                                 {'question': 'A ribbon is 5/6 m long. '
                                                                              'You cut off 1/3 m. How '
                                                                              'much remains? Show your '
                                                                              'steps.',
                                                                  'reference_answer': '1/3 = 2/6. '
                                                                                      'Remaining length '
                                                                                      '= 5/6 − 2/6 = '
                                                                                      '3/6 = 1/2 m.'},
                                                                 {'question': 'Find the area and '
                                                                              'perimeter of a rectangle '
                                                                              '9 cm long and 4 cm wide.',
                                                                  'reference_answer': 'Area = 9 × 4 = '
                                                                                      '36 cm². '
                                                                                      'Perimeter = 2 × '
                                                                                      '(9 + 4) = 26 '
                                                                                      'cm.'}]},
 'Class 7 Mathematics — Practice Test 1': {'class': 'Class 7',
                                           'subject': 'Mathematics',
                                           'duration_minutes': 20,
                                           'questions': [{'question': 'Calculate −8 + 13.',
                                                          'options': ['−21', '−5', '5', '21'],
                                                          'answer': '5',
                                                          'explanation': 'Starting at −8 and moving 13 '
                                                                         'units to the right gives 5.'},
                                                         {'question': 'Calculate (−6) × (−4).',
                                                          'options': ['−24', '24', '−10', '10'],
                                                          'answer': '24',
                                                          'explanation': 'The product of two negative '
                                                                         'numbers is positive: 6 × 4 = '
                                                                         '24.'},
                                                         {'question': 'Calculate 3/5 ÷ 9/10.',
                                                          'options': ['27/50', '2/3', '3/2', '1/6'],
                                                          'answer': '2/3',
                                                          'explanation': 'Multiply by the reciprocal: '
                                                                         '3/5 × 10/9 = 30/45 = 2/3.'},
                                                         {'question': 'Simplify the ratio 18:24.',
                                                          'options': ['2:3', '3:4', '4:3', '6:8'],
                                                          'answer': '3:4',
                                                          'explanation': 'Divide both terms by 6: 18:24 '
                                                                         '= 3:4.'},
                                                         {'question': 'What is 15% of 200?',
                                                          'options': ['15', '20', '30', '40'],
                                                          'answer': '30',
                                                          'explanation': '15/100 × 200 = 30.'},
                                                         {'question': 'Solve 3x + 5 = 20.',
                                                          'options': ['5', '15', '25/3', '3'],
                                                          'answer': '5',
                                                          'explanation': 'Subtract 5: 3x = 15. Divide '
                                                                         'by 3: x = 5.'},
                                                         {'question': 'Simplify 4a + 3a − 2a.',
                                                          'options': ['9a', '5a', '5a²', '6a'],
                                                          'answer': '5a',
                                                          'explanation': 'Combine the coefficients: (4 '
                                                                         '+ 3 − 2)a = 5a.'},
                                                         {'question': 'Two angles of a triangle are 50° '
                                                                      'and 60°. Find the third angle.',
                                                          'options': ['60°', '70°', '110°', '130°'],
                                                          'answer': '70°',
                                                          'explanation': 'Angles of a triangle sum to '
                                                                         '180°: 180 − 50 − 60 = 70°.'},
                                                         {'question': 'Find the mean of 4, 6, 8 and 10.',
                                                          'options': ['6', '7', '8', '28'],
                                                          'answer': '7',
                                                          'explanation': 'Mean = (4 + 6 + 8 + 10)/4 = '
                                                                         '28/4 = 7.'},
                                                         {'question': 'Find the simple interest on '
                                                                      '₹1,000 at 5% per year for 2 '
                                                                      'years.',
                                                          'options': ['₹50', '₹100', '₹150', '₹1,100'],
                                                          'answer': '₹100',
                                                          'explanation': 'Simple interest = PRT/100 = '
                                                                         '1,000 × 5 × 2/100 = ₹100.'}],
                                           'written_questions': [{'question': 'Solve 5x − 7 = 18 and '
                                                                              'check your answer.',
                                                                  'reference_answer': '5x = 25, so x = '
                                                                                      '5. Check: 5 × 5 '
                                                                                      '− 7 = 18.'},
                                                                 {'question': 'A book marked ₹400 is '
                                                                              'sold at a 10% discount. '
                                                                              'Find the discount and '
                                                                              'selling price.',
                                                                  'reference_answer': 'Discount = '
                                                                                      '10/100 × 400 = '
                                                                                      '₹40. Selling '
                                                                                      'price = 400 − 40 '
                                                                                      '= ₹360.'},
                                                                 {'question': 'The angles of a triangle '
                                                                              'are in the ratio 2:3:4. '
                                                                              'Find all three angles.',
                                                                  'reference_answer': 'There are 9 '
                                                                                      'equal parts. '
                                                                                      'Each part = '
                                                                                      '180°/9 = 20°. '
                                                                                      'The angles are '
                                                                                      '40°, 60° and '
                                                                                      '80°.'}]},
 'Class 8 Mathematics — Practice Test 1': {'class': 'Class 8',
                                           'subject': 'Mathematics',
                                           'duration_minutes': 20,
                                           'questions': [{'question': 'Simplify 2³ × 2⁴.',
                                                          'options': ['2⁷', '2¹²', '4⁷', '2¹'],
                                                          'answer': '2⁷',
                                                          'explanation': 'When multiplying powers with '
                                                                         'the same base, add exponents: '
                                                                         '3 + 4 = 7.'},
                                                         {'question': 'Find √144.',
                                                          'options': ['11', '12', '14', '72'],
                                                          'answer': '12',
                                                          'explanation': '12 × 12 = 144, so the '
                                                                         'principal square root is 12.'},
                                                         {'question': 'Expand (x + 3)².',
                                                          'options': ['x² + 9',
                                                                      'x² + 3x + 9',
                                                                      'x² + 6x + 9',
                                                                      '2x + 6'],
                                                          'answer': 'x² + 6x + 9',
                                                          'explanation': 'Using (a + b)² = a² + 2ab + '
                                                                         'b² gives x² + 6x + 9.'},
                                                         {'question': 'Factorise x² − 9.',
                                                          'options': ['(x − 3)²',
                                                                      '(x − 9)(x + 1)',
                                                                      '(x − 3)(x + 3)',
                                                                      '(x + 3)²'],
                                                          'answer': '(x − 3)(x + 3)',
                                                          'explanation': 'Use a² − b² = (a − b)(a + b), '
                                                                         'with a = x and b = 3.'},
                                                         {'question': 'Solve 2(x − 3) = 10.',
                                                          'options': ['2', '5', '8', '13'],
                                                          'answer': '8',
                                                          'explanation': 'Divide by 2: x − 3 = 5. Add '
                                                                         '3: x = 8.'},
                                                         {'question': 'An item costs ₹500 and sells for '
                                                                      '₹600. Find the profit percentage '
                                                                      'on cost price.',
                                                          'options': ['10%', '16⅔%', '20%', '25%'],
                                                          'answer': '20%',
                                                          'explanation': 'Profit = ₹100. Profit '
                                                                         'percentage = 100/500 × 100 = '
                                                                         '20%.'},
                                                         {'question': 'Find the amount on ₹1,000 at 10% '
                                                                      'annual compound interest after 2 '
                                                                      'years.',
                                                          'options': ['₹1,100',
                                                                      '₹1,200',
                                                                      '₹1,210',
                                                                      '₹210'],
                                                          'answer': '₹1,210',
                                                          'explanation': 'Amount = 1,000 × 1.1² = '
                                                                         '₹1,210. ₹210 is the interest, '
                                                                         'not the amount.'},
                                                         {'question': 'Find the area of a trapezium '
                                                                      'with parallel sides 6 cm and 10 '
                                                                      'cm and perpendicular height 4 '
                                                                      'cm.',
                                                          'options': ['24 cm²',
                                                                      '32 cm²',
                                                                      '40 cm²',
                                                                      '64 cm²'],
                                                          'answer': '32 cm²',
                                                          'explanation': 'Area = ½ × (6 + 10) × 4 = 32 '
                                                                         'cm².'},
                                                         {'question': 'Find the volume of a cube of '
                                                                      'side 3 cm.',
                                                          'options': ['9 cm³',
                                                                      '18 cm³',
                                                                      '27 cm³',
                                                                      '54 cm³'],
                                                          'answer': '27 cm³',
                                                          'explanation': 'Volume = side³ = 3³ = 27 '
                                                                         'cm³.'},
                                                         {'question': 'A fair six-sided die is rolled '
                                                                      'once. What is the probability of '
                                                                      'an even number?',
                                                          'options': ['1/6', '1/3', '1/2', '2/3'],
                                                          'answer': '1/2',
                                                          'explanation': 'The even outcomes are 2, 4 '
                                                                         'and 6: probability = 3/6 = '
                                                                         '1/2.'}],
                                           'written_questions': [{'question': 'Expand (2x + 5)² and '
                                                                              'state the identity used.',
                                                                  'reference_answer': 'Use (a + b)² = '
                                                                                      'a² + 2ab + b². '
                                                                                      'Therefore (2x + '
                                                                                      '5)² = 4x² + 20x '
                                                                                      '+ 25.'},
                                                                 {'question': 'A cuboid is 8 cm long, 5 '
                                                                              'cm wide and 3 cm high. '
                                                                              'Find its volume and '
                                                                              'total surface area.',
                                                                  'reference_answer': 'Volume = 8 × 5 × '
                                                                                      '3 = 120 cm³. '
                                                                                      'Total surface '
                                                                                      'area = 2(lw + wh '
                                                                                      '+ hl) = 2(40 + '
                                                                                      '15 + 24) = 158 '
                                                                                      'cm².'},
                                                                 {'question': 'Find the compound '
                                                                              'interest on ₹2,000 at '
                                                                              '10% per year for 2 '
                                                                              'years, compounded '
                                                                              'annually.',
                                                                  'reference_answer': 'Amount = 2,000 × '
                                                                                      '(1 + 10/100)² = '
                                                                                      '₹2,420. Compound '
                                                                                      'interest = 2,420 '
                                                                                      '− 2,000 = '
                                                                                      '₹420.'}]}})
