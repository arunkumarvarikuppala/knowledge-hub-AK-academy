# Knowledge Hub: starter foundation practice for Classes 6–10.
# 66 exams: at least two for every subject in the current app catalogue.
# Existing tests are preserved. Adjacent classes share some foundation questions.
# Not a complete syllabus bank or an official/teacher-verified examination set.
# Literature uses original passages, not the prescribed works.
# The app saves MCQ scores; written responses remain session-only.

EXAMS = {'Class 9 Mathematics — Practice Test 1': {'class': 'Class 9',
                                           'subject': 'Mathematics',
                                           'duration_minutes': 15,
                                           'questions': [{'question': 'Which of the following is an '
                                                                      'irrational number?',
                                                          'options': ['1/2', '0.25', '√2', '4'],
                                                          'answer': '√2',
                                                          'explanation': '√2 cannot be expressed as a ratio '
                                                                         'of two integers.'},
                                                         {'question': 'What is the degree of 3x² + 2x + 5?',
                                                          'options': ['1', '2', '3', '5'],
                                                          'answer': '2',
                                                          'explanation': 'The highest power of x is 2, so '
                                                                         'the degree is 2.'},
                                                         {'question': 'Solve: x + 5 = 12.',
                                                          'options': ['5', '6', '7', '17'],
                                                          'answer': '7',
                                                          'explanation': 'Subtract 5 from both sides: x = 12 '
                                                                         '- 5 = 7.'},
                                                         {'question': 'Which number is a whole number?',
                                                          'options': ['-2', '0', '1/3', '√3'],
                                                          'answer': '0',
                                                          'explanation': 'Whole numbers include 0 and the '
                                                                         'positive integers.'},
                                                         {'question': 'Solve: 2x = 18.',
                                                          'options': ['8', '9', '16', '20'],
                                                          'answer': '9',
                                                          'explanation': 'Divide both sides by 2: x = 9.'}],
                                           'written_questions': [{'question': 'Explain the difference '
                                                                              'between rational and '
                                                                              'irrational numbers.',
                                                                  'reference_answer': 'A rational number can '
                                                                                      'be written as p/q for '
                                                                                      'integers p and q with '
                                                                                      'q ≠ 0. An irrational '
                                                                                      'number cannot be '
                                                                                      'written in that '
                                                                                      'form.'},
                                                                 {'question': 'Solve 3x + 4 = 16 and show '
                                                                              'your steps.',
                                                                  'reference_answer': 'Subtract 4 from both '
                                                                                      'sides: 3x = 12. '
                                                                                      'Divide by 3: x = '
                                                                                      '4.'}]},
 'Class 10 Mathematics — Practice Test 1': {'class': 'Class 10',
                                            'subject': 'Mathematics',
                                            'duration_minutes': 15,
                                            'questions': [{'question': 'Which is the standard form of a '
                                                                       'quadratic equation?',
                                                           'options': ['ax + b = 0',
                                                                       'ax² + bx + c = 0, a ≠ 0',
                                                                       'ax³ + b = 0',
                                                                       'x + y = 0'],
                                                           'answer': 'ax² + bx + c = 0, a ≠ 0',
                                                           'explanation': 'A quadratic equation has highest '
                                                                          'power 2 and a non-zero '
                                                                          'coefficient of x².'},
                                                          {'question': 'Factorise x² - 5x + 6.',
                                                           'options': ['(x - 1)(x - 6)',
                                                                       '(x + 2)(x + 3)',
                                                                       '(x - 2)(x - 3)',
                                                                       '(x + 1)(x - 6)'],
                                                           'answer': '(x - 2)(x - 3)',
                                                           'explanation': 'The numbers -2 and -3 multiply to '
                                                                          '6 and add to -5.'},
                                                          {'question': 'Find the common difference of 2, 5, '
                                                                       '8, 11, ...',
                                                           'options': ['2', '3', '5', '8'],
                                                           'answer': '3',
                                                           'explanation': 'Subtract consecutive terms: 5 - 2 '
                                                                          '= 3.'},
                                                          {'question': 'What is the 5th term of the AP 4, 9, '
                                                                       '14, 19, ...?',
                                                           'options': ['19', '20', '24', '25'],
                                                           'answer': '24',
                                                           'explanation': 'The sequence increases by 5; the '
                                                                          '5th term is 24.'},
                                                          {'question': 'What is the discriminant of x² - 4x '
                                                                       '+ 4 = 0?',
                                                           'options': ['0', '4', '8', '16'],
                                                           'answer': '0',
                                                           'explanation': 'D = b² - 4ac = (-4)² - 4(1)(4) = '
                                                                          '16 - 16 = 0.'}],
                                            'written_questions': [{'question': 'Solve x² - 7x + 12 = 0 by '
                                                                               'factorisation.',
                                                                   'reference_answer': 'x² - 7x + 12 = (x - '
                                                                                       '3)(x - 4) = 0, so x '
                                                                                       '= 3 or x = 4.'},
                                                                  {'question': 'Write the nth-term formula '
                                                                               'for an arithmetic '
                                                                               'progression and explain its '
                                                                               'symbols.',
                                                                   'reference_answer': 'aₙ = a + (n - 1)d, '
                                                                                       'where a is the first '
                                                                                       'term, d is the '
                                                                                       'common difference, '
                                                                                       'and n is the term '
                                                                                       'number.'}]},
 'Class 10 Physics — Practice Test 1': {'class': 'Class 10',
                                        'subject': 'Physics',
                                        'duration_minutes': 15,
                                        'questions': [{'question': 'What is the SI unit of work?',
                                                       'options': ['Newton', 'Watt', 'Joule', 'Pascal'],
                                                       'answer': 'Joule',
                                                       'explanation': 'Work is measured in joules (J).'},
                                                      {'question': 'Work done when force and displacement '
                                                                   'are in the same direction is:',
                                                       'options': ['F/s', 'F × s', 's/F', 'F + s'],
                                                       'answer': 'F × s',
                                                       'explanation': 'For parallel force and displacement, '
                                                                      'W = F × s.'},
                                                      {'question': 'The SI unit of force is:',
                                                       'options': ['Joule', 'Newton', 'Watt', 'Metre'],
                                                       'answer': 'Newton',
                                                       'explanation': 'Force is measured in newtons (N).'},
                                                      {'question': 'If displacement is zero, the work done '
                                                                   'by a constant force is:',
                                                       'options': ['Zero',
                                                                   'Always 1 J',
                                                                   'Always negative',
                                                                   'Infinite'],
                                                       'answer': 'Zero',
                                                       'explanation': 'W = F × s × cos(θ); if displacement s '
                                                                      'is zero, work is zero.'},
                                                      {'question': 'Which quantity is measured in joules?',
                                                       'options': ['Force',
                                                                   'Distance',
                                                                   'Work',
                                                                   'Acceleration'],
                                                       'answer': 'Work',
                                                       'explanation': 'The joule is the SI unit of work and '
                                                                      'energy.'}],
                                        'written_questions': [{'question': 'Define work done and write its '
                                                                           'formula.',
                                                               'reference_answer': 'Work is done when a '
                                                                                   'force causes '
                                                                                   'displacement. W = F × s '
                                                                                   '× cos(θ); when force and '
                                                                                   'displacement are in the '
                                                                                   'same direction, W = F × '
                                                                                   's.'},
                                                              {'question': 'Calculate work done by a 10 N '
                                                                           'force moving an object 3 m in '
                                                                           'the same direction.',
                                                               'reference_answer': 'W = F × s = 10 × 3 = 30 '
                                                                                   'J.'}]},
 'Class 6 Mathematics — Practice Test 1': {'class': 'Class 6',
                                           'subject': 'Mathematics',
                                           'duration_minutes': 20,
                                           'questions': [{'question': 'What is the place value of 7 in '
                                                                      '47,305?',
                                                          'options': ['7', '70', '700', '7,000'],
                                                          'answer': '7,000',
                                                          'explanation': 'The digit 7 is in the thousands '
                                                                         'place: 7 × 1,000 = 7,000.'},
                                                         {'question': 'Which of these numbers is prime?',
                                                          'options': ['21', '29', '35', '39'],
                                                          'answer': '29',
                                                          'explanation': '29 has exactly two positive '
                                                                         'factors: 1 and 29.'},
                                                         {'question': 'What is the HCF of 18 and 24?',
                                                          'options': ['3', '6', '12', '72'],
                                                          'answer': '6',
                                                          'explanation': 'Their common factors are 1, 2, 3 '
                                                                         'and 6; the highest is 6.'},
                                                         {'question': 'What is the LCM of 4 and 6?',
                                                          'options': ['2', '10', '12', '24'],
                                                          'answer': '12',
                                                          'explanation': '12 is the smallest positive number '
                                                                         'divisible by both 4 and 6.'},
                                                         {'question': 'Simplify 12/18 to its lowest terms.',
                                                          'options': ['2/3', '3/2', '6/9', '4/9'],
                                                          'answer': '2/3',
                                                          'explanation': 'Divide numerator and denominator '
                                                                         'by their HCF, 6, to get 2/3.'},
                                                         {'question': 'Calculate 3/4 + 1/8.',
                                                          'options': ['4/12', '1/2', '5/8', '7/8'],
                                                          'answer': '7/8',
                                                          'explanation': '3/4 = 6/8, and 6/8 + 1/8 = 7/8.'},
                                                         {'question': 'Calculate 2.5 + 0.75.',
                                                          'options': ['2.125', '3.25', '3.75', '2.75'],
                                                          'answer': '3.25',
                                                          'explanation': 'Align the decimal points: 2.50 + '
                                                                         '0.75 = 3.25.'},
                                                         {'question': 'What is the perimeter of a rectangle '
                                                                      'of length 8 cm and width 5 cm?',
                                                          'options': ['13 cm', '26 cm', '40 cm', '80 cm'],
                                                          'answer': '26 cm',
                                                          'explanation': 'Perimeter = 2 × (length + width) = '
                                                                         '2 × 13 = 26 cm.'},
                                                         {'question': 'What is the area of a square of side '
                                                                      '6 cm?',
                                                          'options': ['12 cm²', '24 cm²', '36 cm²', '18 cm²'],
                                                          'answer': '36 cm²',
                                                          'explanation': 'Area = side × side = 6 × 6 = 36 '
                                                                         'cm².'},
                                                         {'question': 'What is the size of a right angle?',
                                                          'options': ['45°', '90°', '180°', '360°'],
                                                          'answer': '90°',
                                                          'explanation': 'A right angle measures 90 '
                                                                         'degrees.'}],
                                           'written_questions': [{'question': 'Find the HCF and LCM of 12 '
                                                                              'and 18. Show your method.',
                                                                  'reference_answer': '12 = 2² × 3 and 18 = '
                                                                                      '2 × 3². HCF = 2 × 3 = '
                                                                                      '6. LCM = 2² × 3² = '
                                                                                      '36.'},
                                                                 {'question': 'A ribbon is 5/6 m long. You '
                                                                              'cut off 1/3 m. How much '
                                                                              'remains? Show your steps.',
                                                                  'reference_answer': '1/3 = 2/6. Remaining '
                                                                                      'length = 5/6 − 2/6 = '
                                                                                      '3/6 = 1/2 m.'},
                                                                 {'question': 'Find the area and perimeter '
                                                                              'of a rectangle 9 cm long and '
                                                                              '4 cm wide.',
                                                                  'reference_answer': 'Area = 9 × 4 = 36 '
                                                                                      'cm². Perimeter = 2 × '
                                                                                      '(9 + 4) = 26 cm.'}]},
 'Class 7 Mathematics — Practice Test 1': {'class': 'Class 7',
                                           'subject': 'Mathematics',
                                           'duration_minutes': 20,
                                           'questions': [{'question': 'Calculate −8 + 13.',
                                                          'options': ['−21', '−5', '5', '21'],
                                                          'answer': '5',
                                                          'explanation': 'Starting at −8 and moving 13 units '
                                                                         'to the right gives 5.'},
                                                         {'question': 'Calculate (−6) × (−4).',
                                                          'options': ['−24', '24', '−10', '10'],
                                                          'answer': '24',
                                                          'explanation': 'The product of two negative '
                                                                         'numbers is positive: 6 × 4 = 24.'},
                                                         {'question': 'Calculate 3/5 ÷ 9/10.',
                                                          'options': ['27/50', '2/3', '3/2', '1/6'],
                                                          'answer': '2/3',
                                                          'explanation': 'Multiply by the reciprocal: 3/5 × '
                                                                         '10/9 = 30/45 = 2/3.'},
                                                         {'question': 'Simplify the ratio 18:24.',
                                                          'options': ['2:3', '3:4', '4:3', '6:8'],
                                                          'answer': '3:4',
                                                          'explanation': 'Divide both terms by 6: 18:24 = '
                                                                         '3:4.'},
                                                         {'question': 'What is 15% of 200?',
                                                          'options': ['15', '20', '30', '40'],
                                                          'answer': '30',
                                                          'explanation': '15/100 × 200 = 30.'},
                                                         {'question': 'Solve 3x + 5 = 20.',
                                                          'options': ['5', '15', '25/3', '3'],
                                                          'answer': '5',
                                                          'explanation': 'Subtract 5: 3x = 15. Divide by 3: '
                                                                         'x = 5.'},
                                                         {'question': 'Simplify 4a + 3a − 2a.',
                                                          'options': ['9a', '5a', '5a²', '6a'],
                                                          'answer': '5a',
                                                          'explanation': 'Combine the coefficients: (4 + 3 − '
                                                                         '2)a = 5a.'},
                                                         {'question': 'Two angles of a triangle are 50° and '
                                                                      '60°. Find the third angle.',
                                                          'options': ['60°', '70°', '110°', '130°'],
                                                          'answer': '70°',
                                                          'explanation': 'Angles of a triangle sum to 180°: '
                                                                         '180 − 50 − 60 = 70°.'},
                                                         {'question': 'Find the mean of 4, 6, 8 and 10.',
                                                          'options': ['6', '7', '8', '28'],
                                                          'answer': '7',
                                                          'explanation': 'Mean = (4 + 6 + 8 + 10)/4 = 28/4 = '
                                                                         '7.'},
                                                         {'question': 'Find the simple interest on ₹1,000 at '
                                                                      '5% per year for 2 years.',
                                                          'options': ['₹50', '₹100', '₹150', '₹1,100'],
                                                          'answer': '₹100',
                                                          'explanation': 'Simple interest = PRT/100 = 1,000 '
                                                                         '× 5 × 2/100 = ₹100.'}],
                                           'written_questions': [{'question': 'Solve 5x − 7 = 18 and check '
                                                                              'your answer.',
                                                                  'reference_answer': '5x = 25, so x = 5. '
                                                                                      'Check: 5 × 5 − 7 = '
                                                                                      '18.'},
                                                                 {'question': 'A book marked ₹400 is sold at '
                                                                              'a 10% discount. Find the '
                                                                              'discount and selling price.',
                                                                  'reference_answer': 'Discount = 10/100 × '
                                                                                      '400 = ₹40. Selling '
                                                                                      'price = 400 − 40 = '
                                                                                      '₹360.'},
                                                                 {'question': 'The angles of a triangle are '
                                                                              'in the ratio 2:3:4. Find all '
                                                                              'three angles.',
                                                                  'reference_answer': 'There are 9 equal '
                                                                                      'parts. Each part = '
                                                                                      '180°/9 = 20°. The '
                                                                                      'angles are 40°, 60° '
                                                                                      'and 80°.'}]},
 'Class 8 Mathematics — Practice Test 1': {'class': 'Class 8',
                                           'subject': 'Mathematics',
                                           'duration_minutes': 20,
                                           'questions': [{'question': 'Simplify 2³ × 2⁴.',
                                                          'options': ['2⁷', '2¹²', '4⁷', '2¹'],
                                                          'answer': '2⁷',
                                                          'explanation': 'When multiplying powers with the '
                                                                         'same base, add exponents: 3 + 4 = '
                                                                         '7.'},
                                                         {'question': 'Find √144.',
                                                          'options': ['11', '12', '14', '72'],
                                                          'answer': '12',
                                                          'explanation': '12 × 12 = 144, so the principal '
                                                                         'square root is 12.'},
                                                         {'question': 'Expand (x + 3)².',
                                                          'options': ['x² + 9',
                                                                      'x² + 3x + 9',
                                                                      'x² + 6x + 9',
                                                                      '2x + 6'],
                                                          'answer': 'x² + 6x + 9',
                                                          'explanation': 'Using (a + b)² = a² + 2ab + b² '
                                                                         'gives x² + 6x + 9.'},
                                                         {'question': 'Factorise x² − 9.',
                                                          'options': ['(x − 3)²',
                                                                      '(x − 9)(x + 1)',
                                                                      '(x − 3)(x + 3)',
                                                                      '(x + 3)²'],
                                                          'answer': '(x − 3)(x + 3)',
                                                          'explanation': 'Use a² − b² = (a − b)(a + b), with '
                                                                         'a = x and b = 3.'},
                                                         {'question': 'Solve 2(x − 3) = 10.',
                                                          'options': ['2', '5', '8', '13'],
                                                          'answer': '8',
                                                          'explanation': 'Divide by 2: x − 3 = 5. Add 3: x = '
                                                                         '8.'},
                                                         {'question': 'An item costs ₹500 and sells for '
                                                                      '₹600. Find the profit percentage on '
                                                                      'cost price.',
                                                          'options': ['10%', '16⅔%', '20%', '25%'],
                                                          'answer': '20%',
                                                          'explanation': 'Profit = ₹100. Profit percentage = '
                                                                         '100/500 × 100 = 20%.'},
                                                         {'question': 'Find the amount on ₹1,000 at 10% '
                                                                      'annual compound interest after 2 '
                                                                      'years.',
                                                          'options': ['₹1,100', '₹1,200', '₹1,210', '₹210'],
                                                          'answer': '₹1,210',
                                                          'explanation': 'Amount = 1,000 × 1.1² = ₹1,210. '
                                                                         '₹210 is the interest, not the '
                                                                         'amount.'},
                                                         {'question': 'Find the area of a trapezium with '
                                                                      'parallel sides 6 cm and 10 cm and '
                                                                      'perpendicular height 4 cm.',
                                                          'options': ['24 cm²', '32 cm²', '40 cm²', '64 cm²'],
                                                          'answer': '32 cm²',
                                                          'explanation': 'Area = ½ × (6 + 10) × 4 = 32 cm².'},
                                                         {'question': 'Find the volume of a cube of side 3 '
                                                                      'cm.',
                                                          'options': ['9 cm³', '18 cm³', '27 cm³', '54 cm³'],
                                                          'answer': '27 cm³',
                                                          'explanation': 'Volume = side³ = 3³ = 27 cm³.'},
                                                         {'question': 'A fair six-sided die is rolled once. '
                                                                      'What is the probability of an even '
                                                                      'number?',
                                                          'options': ['1/6', '1/3', '1/2', '2/3'],
                                                          'answer': '1/2',
                                                          'explanation': 'The even outcomes are 2, 4 and 6: '
                                                                         'probability = 3/6 = 1/2.'}],
                                           'written_questions': [{'question': 'Expand (2x + 5)² and state '
                                                                              'the identity used.',
                                                                  'reference_answer': 'Use (a + b)² = a² + '
                                                                                      '2ab + b². Therefore '
                                                                                      '(2x + 5)² = 4x² + 20x '
                                                                                      '+ 25.'},
                                                                 {'question': 'A cuboid is 8 cm long, 5 cm '
                                                                              'wide and 3 cm high. Find its '
                                                                              'volume and total surface '
                                                                              'area.',
                                                                  'reference_answer': 'Volume = 8 × 5 × 3 = '
                                                                                      '120 cm³. Total '
                                                                                      'surface area = 2(lw + '
                                                                                      'wh + hl) = 2(40 + 15 '
                                                                                      '+ 24) = 158 cm².'},
                                                                 {'question': 'Find the compound interest on '
                                                                              '₹2,000 at 10% per year for 2 '
                                                                              'years, compounded annually.',
                                                                  'reference_answer': 'Amount = 2,000 × (1 + '
                                                                                      '10/100)² = ₹2,420. '
                                                                                      'Compound interest = '
                                                                                      '2,420 − 2,000 = '
                                                                                      '₹420.'}]},
 'Class 6 Mathematics — Foundation Practice 1': {'class': 'Class 6',
                                                 'subject': 'Mathematics',
                                                 'duration_minutes': 10,
                                                 'questions': [{'question': 'What is 25% of 80?',
                                                                'options': ['40', '60', '20', '25'],
                                                                'answer': '20',
                                                                'explanation': '25% is one quarter; 80/4 = '
                                                                               '20.'},
                                                               {'question': 'Convert 3 km to metres.',
                                                                'options': ['30,000 m',
                                                                            '3,000 m',
                                                                            '300 m',
                                                                            '30 m'],
                                                                'answer': '3,000 m',
                                                                'explanation': '1 km = 1,000 m, so 3 km = '
                                                                               '3,000 m.'},
                                                               {'question': 'Find the next number: 3, 6, 9, '
                                                                            '12, ...',
                                                                'options': ['15', '14', '16', '18'],
                                                                'answer': '15',
                                                                'explanation': 'The pattern adds 3 at each '
                                                                               'step.'}],
                                                 'written_questions': [{'question': 'Solve a question from '
                                                                                    'this test again, '
                                                                                    'showing each '
                                                                                    'calculation and '
                                                                                    'checking the result.',
                                                                        'reference_answer': 'Use the '
                                                                                            'corresponding '
                                                                                            'MCQ explanation '
                                                                                            'to check the '
                                                                                            'method. A '
                                                                                            'complete '
                                                                                            'response must '
                                                                                            'show '
                                                                                            'intermediate '
                                                                                            'steps and the '
                                                                                            'final answer '
                                                                                            'with units '
                                                                                            'where '
                                                                                            'relevant.'}]},
 'Class 6 Science — Foundation Practice 1': {'class': 'Class 6',
                                             'subject': 'Science',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Which part of a plant usually '
                                                                        'absorbs water from the soil?',
                                                            'options': ['Fruits',
                                                                        'Petals',
                                                                        'Roots',
                                                                        'Flowers'],
                                                            'answer': 'Roots',
                                                            'explanation': 'Roots take up water and '
                                                                           'dissolved minerals from the '
                                                                           'soil.'},
                                                           {'question': 'Which gas do humans need for '
                                                                        'aerobic respiration?',
                                                            'options': ['Neon',
                                                                        'Oxygen',
                                                                        'Helium',
                                                                        'Hydrogen'],
                                                            'answer': 'Oxygen',
                                                            'explanation': 'Oxygen is used in aerobic '
                                                                           'respiration to release energy '
                                                                           'from food.'},
                                                           {'question': 'What is the change from liquid '
                                                                        'water to water vapour called?',
                                                            'options': ['Evaporation',
                                                                        'Freezing',
                                                                        'Melting',
                                                                        'Condensation'],
                                                            'answer': 'Evaporation',
                                                            'explanation': 'Evaporation changes liquid water '
                                                                           'into water vapour.'}],
                                             'written_questions': [{'question': 'Explain evaporation and '
                                                                                'give an everyday example.',
                                                                    'reference_answer': 'Evaporation is the '
                                                                                        'change of a liquid '
                                                                                        'into vapour at its '
                                                                                        'surface. Wet '
                                                                                        'clothes drying are '
                                                                                        'an example.'}]},
 'Class 6 Science — Foundation Practice 2': {'class': 'Class 6',
                                             'subject': 'Science',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Which material is usually a good '
                                                                        'electrical conductor?',
                                                            'options': ['Plastic',
                                                                        'Copper',
                                                                        'Rubber',
                                                                        'Dry wood'],
                                                            'answer': 'Copper',
                                                            'explanation': 'Copper allows electric current '
                                                                           'to pass through it readily.'},
                                                           {'question': 'Which organ pumps blood around the '
                                                                        'human body?',
                                                            'options': ['Heart', 'Stomach', 'Kidney', 'Lung'],
                                                            'answer': 'Heart',
                                                            'explanation': 'The heart pumps blood through '
                                                                           'blood vessels.'},
                                                           {'question': 'Which process makes water vapour '
                                                                        'form liquid droplets?',
                                                            'options': ['Evaporation',
                                                                        'Melting',
                                                                        'Sublimation',
                                                                        'Condensation'],
                                                            'answer': 'Condensation',
                                                            'explanation': 'Cooling water vapour can cause '
                                                                           'it to condense into liquid '
                                                                           'water.'}],
                                             'written_questions': [{'question': 'Explain the difference '
                                                                                'between a conductor and an '
                                                                                'insulator. Give one example '
                                                                                'of each.',
                                                                    'reference_answer': 'A conductor permits '
                                                                                        'current to flow '
                                                                                        'readily, such as '
                                                                                        'copper. An '
                                                                                        'insulator strongly '
                                                                                        'resists current, '
                                                                                        'such as rubber.'}]},
 'Class 6 English — Foundation Practice 1': {'class': 'Class 6',
                                             'subject': 'English',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Choose the noun in: The kitten '
                                                                        'sleeps quietly.',
                                                            'options': ['quietly', 'The', 'kitten', 'sleeps'],
                                                            'answer': 'kitten',
                                                            'explanation': 'Kitten names an animal, so it is '
                                                                           'a noun.'},
                                                           {'question': 'Choose the correct sentence.',
                                                            'options': ['She gone to school.',
                                                                        'She goes to school.',
                                                                        'She go to school.',
                                                                        'She going to school.'],
                                                            'answer': 'She goes to school.',
                                                            'explanation': 'A singular third-person subject '
                                                                           'takes goes in the simple present '
                                                                           'tense.'},
                                                           {'question': 'Choose a synonym of happy.',
                                                            'options': ['joyful', 'angry', 'tired', 'afraid'],
                                                            'answer': 'joyful',
                                                            'explanation': 'Joyful and happy have similar '
                                                                           'meanings.'}],
                                             'written_questions': [{'question': 'Write four sentences about '
                                                                                'a helpful act. Use at least '
                                                                                'one adjective and one '
                                                                                'past-tense verb.',
                                                                    'reference_answer': 'Example: Yesterday '
                                                                                        'I helped an elderly '
                                                                                        'neighbour. Her '
                                                                                        'heavy bag had torn. '
                                                                                        'I carried the '
                                                                                        'groceries home. She '
                                                                                        'thanked me with a '
                                                                                        'warm smile. Accept '
                                                                                        'other clear, '
                                                                                        'grammatical '
                                                                                        'answers.'}]},
 'Class 6 English — Foundation Practice 2': {'class': 'Class 6',
                                             'subject': 'English',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Choose the past tense of write.',
                                                            'options': ['writes',
                                                                        'wrote',
                                                                        'written',
                                                                        'writing'],
                                                            'answer': 'wrote',
                                                            'explanation': 'The simple past form of write is '
                                                                           'wrote.'},
                                                           {'question': 'Which punctuation mark ends a '
                                                                        'direct question?',
                                                            'options': ['Question mark',
                                                                        'Comma',
                                                                        'Apostrophe',
                                                                        'Colon'],
                                                            'answer': 'Question mark',
                                                            'explanation': 'A direct question ends with a '
                                                                           'question mark.'},
                                                           {'question': 'Choose the adjective in: The bright '
                                                                        'moon shone.',
                                                            'options': ['moon', 'shone', 'The', 'bright'],
                                                            'answer': 'bright',
                                                            'explanation': 'Bright describes the noun '
                                                                           'moon.'}],
                                             'written_questions': [{'question': 'Change into the past tense: '
                                                                                'I walk to school and meet '
                                                                                'my friends.',
                                                                    'reference_answer': 'I walked to school '
                                                                                        'and met my '
                                                                                        'friends.'}]},
 'Class 6 Social Studies — Foundation Practice 1': {'class': 'Class 6',
                                                    'subject': 'Social Studies',
                                                    'duration_minutes': 10,
                                                    'questions': [{'question': 'Which direction is opposite '
                                                                               'to north?',
                                                                   'options': ['West',
                                                                               'Northeast',
                                                                               'South',
                                                                               'East'],
                                                                   'answer': 'South',
                                                                   'explanation': 'South is the direction '
                                                                                  'opposite to north.'},
                                                                  {'question': 'What does a map key explain?',
                                                                   'options': ['Only the weather',
                                                                               'The symbols used on a map',
                                                                               'Only the map price',
                                                                               'The age of every city'],
                                                                   'answer': 'The symbols used on a map',
                                                                   'explanation': 'A map key or legend '
                                                                                  'explains the meaning of '
                                                                                  'symbols.'},
                                                                  {'question': 'Which is an example of a '
                                                                               'historical source?',
                                                                   'options': ['An old inscription',
                                                                               'A prediction about tomorrow',
                                                                               'An imagined future city',
                                                                               'A weather forecast'],
                                                                   'answer': 'An old inscription',
                                                                   'explanation': 'An inscription is '
                                                                                  'evidence produced in the '
                                                                                  'past that historians can '
                                                                                  'study.'}],
                                                    'written_questions': [{'question': 'Explain why a map '
                                                                                       'needs a scale and a '
                                                                                       'key.',
                                                                           'reference_answer': 'A scale '
                                                                                               'relates map '
                                                                                               'distance to '
                                                                                               'real '
                                                                                               'distance. A '
                                                                                               'key explains '
                                                                                               'symbols, '
                                                                                               'helping '
                                                                                               'readers '
                                                                                               'understand '
                                                                                               'what the map '
                                                                                               'shows.'}]},
 'Class 6 Social Studies — Foundation Practice 2': {'class': 'Class 6',
                                                    'subject': 'Social Studies',
                                                    'duration_minutes': 10,
                                                    'questions': [{'question': 'Which line divides Earth '
                                                                               'into Northern and Southern '
                                                                               'Hemispheres?',
                                                                   'options': ['Arctic Circle',
                                                                               'Equator',
                                                                               'Prime Meridian',
                                                                               'Tropic of Cancer'],
                                                                   'answer': 'Equator',
                                                                   'explanation': 'The Equator is at 0° '
                                                                                  'latitude and separates '
                                                                                  'the two hemispheres.'},
                                                                  {'question': 'Which action helps conserve '
                                                                               'water?',
                                                                   'options': ['Repairing leaking taps',
                                                                               'Leaving taps running',
                                                                               'Ignoring pipe leaks',
                                                                               'Washing a driveway daily '
                                                                               'with a hose'],
                                                                   'answer': 'Repairing leaking taps',
                                                                   'explanation': 'Repairing leaks prevents '
                                                                                  'avoidable loss of water.'},
                                                                  {'question': 'Why do communities need '
                                                                               'rules?',
                                                                   'options': ['To stop all cooperation',
                                                                               'To remove all '
                                                                               'responsibilities',
                                                                               'To prevent all discussion',
                                                                               'To help people live together '
                                                                               'fairly and safely'],
                                                                   'answer': 'To help people live together '
                                                                             'fairly and safely',
                                                                   'explanation': 'Rules help protect '
                                                                                  'rights, set '
                                                                                  'responsibilities and '
                                                                                  'support cooperation.'}],
                                                    'written_questions': [{'question': 'Give two ways to '
                                                                                       'care for a shared '
                                                                                       'public space and '
                                                                                       'explain why they '
                                                                                       'help.',
                                                                           'reference_answer': 'Put litter '
                                                                                               'in bins and '
                                                                                               'protect '
                                                                                               'plants or '
                                                                                               'equipment. '
                                                                                               'These '
                                                                                               'actions keep '
                                                                                               'the space '
                                                                                               'clean, safe '
                                                                                               'and usable '
                                                                                               'for '
                                                                                               'everyone. '
                                                                                               'Accept other '
                                                                                               'sensible '
                                                                                               'examples.'}]},
 'Class 6 Computer Studies — Foundation Practice 1': {'class': 'Class 6',
                                                      'subject': 'Computer Studies',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Which is an input device?',
                                                                     'options': ['Speaker',
                                                                                 'Projector',
                                                                                 'Keyboard',
                                                                                 'Monitor'],
                                                                     'answer': 'Keyboard',
                                                                     'explanation': 'A keyboard sends typed '
                                                                                    'data and commands into '
                                                                                    'a computer.'},
                                                                    {'question': 'Which component carries '
                                                                                 'out program instructions?',
                                                                     'options': ['Monitor stand',
                                                                                 'CPU',
                                                                                 'Printer',
                                                                                 'Mouse mat'],
                                                                     'answer': 'CPU',
                                                                     'explanation': 'The central processing '
                                                                                    'unit executes '
                                                                                    'instructions.'},
                                                                    {'question': 'Which is an example of '
                                                                                 'software?',
                                                                     'options': ['A word processor',
                                                                                 'A keyboard',
                                                                                 'A screen',
                                                                                 'A cable'],
                                                                     'answer': 'A word processor',
                                                                     'explanation': 'Software consists of '
                                                                                    'programs; a word '
                                                                                    'processor is a '
                                                                                    'program.'}],
                                                      'written_questions': [{'question': 'Describe input, '
                                                                                         'processing and '
                                                                                         'output using a '
                                                                                         'calculator as an '
                                                                                         'example.',
                                                                             'reference_answer': 'Input: '
                                                                                                 'enter '
                                                                                                 'numbers '
                                                                                                 'and an '
                                                                                                 'operation. '
                                                                                                 'Processing: '
                                                                                                 'the '
                                                                                                 'calculator '
                                                                                                 'performs '
                                                                                                 'the '
                                                                                                 'calculation. '
                                                                                                 'Output: it '
                                                                                                 'displays '
                                                                                                 'the '
                                                                                                 'result.'}]},
 'Class 6 Computer Studies — Foundation Practice 2': {'class': 'Class 6',
                                                      'subject': 'Computer Studies',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Which is the safest action '
                                                                                 'when someone asks for your '
                                                                                 'password?',
                                                                     'options': ['Use it as your public '
                                                                                 'username',
                                                                                 'Keep it private and ask a '
                                                                                 'trusted adult for help',
                                                                                 'Post it in a group',
                                                                                 'Send it to a stranger'],
                                                                     'answer': 'Keep it private and ask a '
                                                                               'trusted adult for help',
                                                                     'explanation': 'Passwords should remain '
                                                                                    'private; seek help if '
                                                                                    'someone pressures you '
                                                                                    'to share them.'},
                                                                    {'question': 'What is an algorithm?',
                                                                     'options': ['A sequence of steps to '
                                                                                 'solve a problem',
                                                                                 'Only a computer screen',
                                                                                 'A broken cable',
                                                                                 'A type of desk'],
                                                                     'answer': 'A sequence of steps to solve '
                                                                               'a problem',
                                                                     'explanation': 'An algorithm describes '
                                                                                    'a sequence of steps for '
                                                                                    'completing a task.'},
                                                                    {'question': 'Why should important files '
                                                                                 'have backups?',
                                                                     'options': ['To guarantee files can '
                                                                                 'never be lost',
                                                                                 'To make passwords public',
                                                                                 'To replace all software '
                                                                                 'updates',
                                                                                 'To help recover them after '
                                                                                 'loss or damage'],
                                                                     'answer': 'To help recover them after '
                                                                               'loss or damage',
                                                                     'explanation': 'A separate backup can '
                                                                                    'help restore files if '
                                                                                    'the original is lost or '
                                                                                    'damaged.'}],
                                                      'written_questions': [{'question': 'Write an algorithm '
                                                                                         'for adding two '
                                                                                         'numbers and '
                                                                                         'explain one '
                                                                                         'safe-password '
                                                                                         'habit.',
                                                                             'reference_answer': 'Read two '
                                                                                                 'numbers, '
                                                                                                 'calculate '
                                                                                                 'their sum, '
                                                                                                 'and '
                                                                                                 'display '
                                                                                                 'it. Use a '
                                                                                                 'long, '
                                                                                                 'unique '
                                                                                                 'password '
                                                                                                 'and keep '
                                                                                                 'it '
                                                                                                 'private.'}]},
 'Class 7 Mathematics — Foundation Practice 1': {'class': 'Class 7',
                                                 'subject': 'Mathematics',
                                                 'duration_minutes': 10,
                                                 'questions': [{'question': 'Find 2⁵.',
                                                                'options': ['64', '32', '10', '25'],
                                                                'answer': '32',
                                                                'explanation': '2⁵ = 2 × 2 × 2 × 2 × 2 = '
                                                                               '32.'},
                                                               {'question': 'Find the complement of 35°.',
                                                                'options': ['55°', '65°', '145°', '35°'],
                                                                'answer': '55°',
                                                                'explanation': 'Complementary angles sum to '
                                                                               '90°: 90 − 35 = 55°.'},
                                                               {'question': 'A car travels 120 km in 3 '
                                                                            'hours. Find its average speed.',
                                                                'options': ['360 km/h',
                                                                            '117 km/h',
                                                                            '60 km/h',
                                                                            '40 km/h'],
                                                                'answer': '40 km/h',
                                                                'explanation': 'Average speed = '
                                                                               'distance/time = 120/3 = 40 '
                                                                               'km/h.'}],
                                                 'written_questions': [{'question': 'Solve a question from '
                                                                                    'this test again, '
                                                                                    'showing each '
                                                                                    'calculation and '
                                                                                    'checking the result.',
                                                                        'reference_answer': 'Use the '
                                                                                            'corresponding '
                                                                                            'MCQ explanation '
                                                                                            'to check the '
                                                                                            'method. A '
                                                                                            'complete '
                                                                                            'response must '
                                                                                            'show '
                                                                                            'intermediate '
                                                                                            'steps and the '
                                                                                            'final answer '
                                                                                            'with units '
                                                                                            'where '
                                                                                            'relevant.'}]},
 'Class 7 Science — Foundation Practice 1': {'class': 'Class 7',
                                             'subject': 'Science',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Which part of a plant usually '
                                                                        'absorbs water from the soil?',
                                                            'options': ['Petals',
                                                                        'Roots',
                                                                        'Flowers',
                                                                        'Fruits'],
                                                            'answer': 'Roots',
                                                            'explanation': 'Roots take up water and '
                                                                           'dissolved minerals from the '
                                                                           'soil.'},
                                                           {'question': 'Which gas do humans need for '
                                                                        'aerobic respiration?',
                                                            'options': ['Oxygen',
                                                                        'Helium',
                                                                        'Hydrogen',
                                                                        'Neon'],
                                                            'answer': 'Oxygen',
                                                            'explanation': 'Oxygen is used in aerobic '
                                                                           'respiration to release energy '
                                                                           'from food.'},
                                                           {'question': 'What is the change from liquid '
                                                                        'water to water vapour called?',
                                                            'options': ['Freezing',
                                                                        'Melting',
                                                                        'Condensation',
                                                                        'Evaporation'],
                                                            'answer': 'Evaporation',
                                                            'explanation': 'Evaporation changes liquid water '
                                                                           'into water vapour.'}],
                                             'written_questions': [{'question': 'Explain evaporation and '
                                                                                'give an everyday example.',
                                                                    'reference_answer': 'Evaporation is the '
                                                                                        'change of a liquid '
                                                                                        'into vapour at its '
                                                                                        'surface. Wet '
                                                                                        'clothes drying are '
                                                                                        'an example.'}]},
 'Class 7 Science — Foundation Practice 2': {'class': 'Class 7',
                                             'subject': 'Science',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Which material is usually a good '
                                                                        'electrical conductor?',
                                                            'options': ['Copper',
                                                                        'Rubber',
                                                                        'Dry wood',
                                                                        'Plastic'],
                                                            'answer': 'Copper',
                                                            'explanation': 'Copper allows electric current '
                                                                           'to pass through it readily.'},
                                                           {'question': 'Which organ pumps blood around the '
                                                                        'human body?',
                                                            'options': ['Stomach', 'Kidney', 'Lung', 'Heart'],
                                                            'answer': 'Heart',
                                                            'explanation': 'The heart pumps blood through '
                                                                           'blood vessels.'},
                                                           {'question': 'Which process makes water vapour '
                                                                        'form liquid droplets?',
                                                            'options': ['Melting',
                                                                        'Sublimation',
                                                                        'Condensation',
                                                                        'Evaporation'],
                                                            'answer': 'Condensation',
                                                            'explanation': 'Cooling water vapour can cause '
                                                                           'it to condense into liquid '
                                                                           'water.'}],
                                             'written_questions': [{'question': 'Explain the difference '
                                                                                'between a conductor and an '
                                                                                'insulator. Give one example '
                                                                                'of each.',
                                                                    'reference_answer': 'A conductor permits '
                                                                                        'current to flow '
                                                                                        'readily, such as '
                                                                                        'copper. An '
                                                                                        'insulator strongly '
                                                                                        'resists current, '
                                                                                        'such as rubber.'}]},
 'Class 7 English — Foundation Practice 1': {'class': 'Class 7',
                                             'subject': 'English',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Choose the noun in: The kitten '
                                                                        'sleeps quietly.',
                                                            'options': ['The', 'kitten', 'sleeps', 'quietly'],
                                                            'answer': 'kitten',
                                                            'explanation': 'Kitten names an animal, so it is '
                                                                           'a noun.'},
                                                           {'question': 'Choose the correct sentence.',
                                                            'options': ['She goes to school.',
                                                                        'She go to school.',
                                                                        'She going to school.',
                                                                        'She gone to school.'],
                                                            'answer': 'She goes to school.',
                                                            'explanation': 'A singular third-person subject '
                                                                           'takes goes in the simple present '
                                                                           'tense.'},
                                                           {'question': 'Choose a synonym of happy.',
                                                            'options': ['angry', 'tired', 'afraid', 'joyful'],
                                                            'answer': 'joyful',
                                                            'explanation': 'Joyful and happy have similar '
                                                                           'meanings.'}],
                                             'written_questions': [{'question': 'Write four sentences about '
                                                                                'a helpful act. Use at least '
                                                                                'one adjective and one '
                                                                                'past-tense verb.',
                                                                    'reference_answer': 'Example: Yesterday '
                                                                                        'I helped an elderly '
                                                                                        'neighbour. Her '
                                                                                        'heavy bag had torn. '
                                                                                        'I carried the '
                                                                                        'groceries home. She '
                                                                                        'thanked me with a '
                                                                                        'warm smile. Accept '
                                                                                        'other clear, '
                                                                                        'grammatical '
                                                                                        'answers.'}]},
 'Class 7 English — Foundation Practice 2': {'class': 'Class 7',
                                             'subject': 'English',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Choose the past tense of write.',
                                                            'options': ['wrote',
                                                                        'written',
                                                                        'writing',
                                                                        'writes'],
                                                            'answer': 'wrote',
                                                            'explanation': 'The simple past form of write is '
                                                                           'wrote.'},
                                                           {'question': 'Which punctuation mark ends a '
                                                                        'direct question?',
                                                            'options': ['Comma',
                                                                        'Apostrophe',
                                                                        'Colon',
                                                                        'Question mark'],
                                                            'answer': 'Question mark',
                                                            'explanation': 'A direct question ends with a '
                                                                           'question mark.'},
                                                           {'question': 'Choose the adjective in: The bright '
                                                                        'moon shone.',
                                                            'options': ['shone', 'The', 'bright', 'moon'],
                                                            'answer': 'bright',
                                                            'explanation': 'Bright describes the noun '
                                                                           'moon.'}],
                                             'written_questions': [{'question': 'Change into the past tense: '
                                                                                'I walk to school and meet '
                                                                                'my friends.',
                                                                    'reference_answer': 'I walked to school '
                                                                                        'and met my '
                                                                                        'friends.'}]},
 'Class 7 Social Studies — Foundation Practice 1': {'class': 'Class 7',
                                                    'subject': 'Social Studies',
                                                    'duration_minutes': 10,
                                                    'questions': [{'question': 'Which direction is opposite '
                                                                               'to north?',
                                                                   'options': ['Northeast',
                                                                               'South',
                                                                               'East',
                                                                               'West'],
                                                                   'answer': 'South',
                                                                   'explanation': 'South is the direction '
                                                                                  'opposite to north.'},
                                                                  {'question': 'What does a map key explain?',
                                                                   'options': ['The symbols used on a map',
                                                                               'Only the map price',
                                                                               'The age of every city',
                                                                               'Only the weather'],
                                                                   'answer': 'The symbols used on a map',
                                                                   'explanation': 'A map key or legend '
                                                                                  'explains the meaning of '
                                                                                  'symbols.'},
                                                                  {'question': 'Which is an example of a '
                                                                               'historical source?',
                                                                   'options': ['A prediction about tomorrow',
                                                                               'An imagined future city',
                                                                               'A weather forecast',
                                                                               'An old inscription'],
                                                                   'answer': 'An old inscription',
                                                                   'explanation': 'An inscription is '
                                                                                  'evidence produced in the '
                                                                                  'past that historians can '
                                                                                  'study.'}],
                                                    'written_questions': [{'question': 'Explain why a map '
                                                                                       'needs a scale and a '
                                                                                       'key.',
                                                                           'reference_answer': 'A scale '
                                                                                               'relates map '
                                                                                               'distance to '
                                                                                               'real '
                                                                                               'distance. A '
                                                                                               'key explains '
                                                                                               'symbols, '
                                                                                               'helping '
                                                                                               'readers '
                                                                                               'understand '
                                                                                               'what the map '
                                                                                               'shows.'}]},
 'Class 7 Social Studies — Foundation Practice 2': {'class': 'Class 7',
                                                    'subject': 'Social Studies',
                                                    'duration_minutes': 10,
                                                    'questions': [{'question': 'Which line divides Earth '
                                                                               'into Northern and Southern '
                                                                               'Hemispheres?',
                                                                   'options': ['Equator',
                                                                               'Prime Meridian',
                                                                               'Tropic of Cancer',
                                                                               'Arctic Circle'],
                                                                   'answer': 'Equator',
                                                                   'explanation': 'The Equator is at 0° '
                                                                                  'latitude and separates '
                                                                                  'the two hemispheres.'},
                                                                  {'question': 'Which action helps conserve '
                                                                               'water?',
                                                                   'options': ['Leaving taps running',
                                                                               'Ignoring pipe leaks',
                                                                               'Washing a driveway daily '
                                                                               'with a hose',
                                                                               'Repairing leaking taps'],
                                                                   'answer': 'Repairing leaking taps',
                                                                   'explanation': 'Repairing leaks prevents '
                                                                                  'avoidable loss of water.'},
                                                                  {'question': 'Why do communities need '
                                                                               'rules?',
                                                                   'options': ['To remove all '
                                                                               'responsibilities',
                                                                               'To prevent all discussion',
                                                                               'To help people live together '
                                                                               'fairly and safely',
                                                                               'To stop all cooperation'],
                                                                   'answer': 'To help people live together '
                                                                             'fairly and safely',
                                                                   'explanation': 'Rules help protect '
                                                                                  'rights, set '
                                                                                  'responsibilities and '
                                                                                  'support cooperation.'}],
                                                    'written_questions': [{'question': 'Give two ways to '
                                                                                       'care for a shared '
                                                                                       'public space and '
                                                                                       'explain why they '
                                                                                       'help.',
                                                                           'reference_answer': 'Put litter '
                                                                                               'in bins and '
                                                                                               'protect '
                                                                                               'plants or '
                                                                                               'equipment. '
                                                                                               'These '
                                                                                               'actions keep '
                                                                                               'the space '
                                                                                               'clean, safe '
                                                                                               'and usable '
                                                                                               'for '
                                                                                               'everyone. '
                                                                                               'Accept other '
                                                                                               'sensible '
                                                                                               'examples.'}]},
 'Class 7 Computer Studies — Foundation Practice 1': {'class': 'Class 7',
                                                      'subject': 'Computer Studies',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Which is an input device?',
                                                                     'options': ['Projector',
                                                                                 'Keyboard',
                                                                                 'Monitor',
                                                                                 'Speaker'],
                                                                     'answer': 'Keyboard',
                                                                     'explanation': 'A keyboard sends typed '
                                                                                    'data and commands into '
                                                                                    'a computer.'},
                                                                    {'question': 'Which component carries '
                                                                                 'out program instructions?',
                                                                     'options': ['CPU',
                                                                                 'Printer',
                                                                                 'Mouse mat',
                                                                                 'Monitor stand'],
                                                                     'answer': 'CPU',
                                                                     'explanation': 'The central processing '
                                                                                    'unit executes '
                                                                                    'instructions.'},
                                                                    {'question': 'Which is an example of '
                                                                                 'software?',
                                                                     'options': ['A keyboard',
                                                                                 'A screen',
                                                                                 'A cable',
                                                                                 'A word processor'],
                                                                     'answer': 'A word processor',
                                                                     'explanation': 'Software consists of '
                                                                                    'programs; a word '
                                                                                    'processor is a '
                                                                                    'program.'}],
                                                      'written_questions': [{'question': 'Describe input, '
                                                                                         'processing and '
                                                                                         'output using a '
                                                                                         'calculator as an '
                                                                                         'example.',
                                                                             'reference_answer': 'Input: '
                                                                                                 'enter '
                                                                                                 'numbers '
                                                                                                 'and an '
                                                                                                 'operation. '
                                                                                                 'Processing: '
                                                                                                 'the '
                                                                                                 'calculator '
                                                                                                 'performs '
                                                                                                 'the '
                                                                                                 'calculation. '
                                                                                                 'Output: it '
                                                                                                 'displays '
                                                                                                 'the '
                                                                                                 'result.'}]},
 'Class 7 Computer Studies — Foundation Practice 2': {'class': 'Class 7',
                                                      'subject': 'Computer Studies',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Which is the safest action '
                                                                                 'when someone asks for your '
                                                                                 'password?',
                                                                     'options': ['Keep it private and ask a '
                                                                                 'trusted adult for help',
                                                                                 'Post it in a group',
                                                                                 'Send it to a stranger',
                                                                                 'Use it as your public '
                                                                                 'username'],
                                                                     'answer': 'Keep it private and ask a '
                                                                               'trusted adult for help',
                                                                     'explanation': 'Passwords should remain '
                                                                                    'private; seek help if '
                                                                                    'someone pressures you '
                                                                                    'to share them.'},
                                                                    {'question': 'What is an algorithm?',
                                                                     'options': ['Only a computer screen',
                                                                                 'A broken cable',
                                                                                 'A type of desk',
                                                                                 'A sequence of steps to '
                                                                                 'solve a problem'],
                                                                     'answer': 'A sequence of steps to solve '
                                                                               'a problem',
                                                                     'explanation': 'An algorithm describes '
                                                                                    'a sequence of steps for '
                                                                                    'completing a task.'},
                                                                    {'question': 'Why should important files '
                                                                                 'have backups?',
                                                                     'options': ['To make passwords public',
                                                                                 'To replace all software '
                                                                                 'updates',
                                                                                 'To help recover them after '
                                                                                 'loss or damage',
                                                                                 'To guarantee files can '
                                                                                 'never be lost'],
                                                                     'answer': 'To help recover them after '
                                                                               'loss or damage',
                                                                     'explanation': 'A separate backup can '
                                                                                    'help restore files if '
                                                                                    'the original is lost or '
                                                                                    'damaged.'}],
                                                      'written_questions': [{'question': 'Write an algorithm '
                                                                                         'for adding two '
                                                                                         'numbers and '
                                                                                         'explain one '
                                                                                         'safe-password '
                                                                                         'habit.',
                                                                             'reference_answer': 'Read two '
                                                                                                 'numbers, '
                                                                                                 'calculate '
                                                                                                 'their sum, '
                                                                                                 'and '
                                                                                                 'display '
                                                                                                 'it. Use a '
                                                                                                 'long, '
                                                                                                 'unique '
                                                                                                 'password '
                                                                                                 'and keep '
                                                                                                 'it '
                                                                                                 'private.'}]},
 'Class 8 Mathematics — Foundation Practice 1': {'class': 'Class 8',
                                                 'subject': 'Mathematics',
                                                 'duration_minutes': 10,
                                                 'questions': [{'question': 'Solve 3x + 2 = 2x + 9.',
                                                                'options': ['7', '11', '5', '−7'],
                                                                'answer': '7',
                                                                'explanation': 'Subtract 2x and then 2: x = '
                                                                               '7.'},
                                                               {'question': 'What is the sum of the interior '
                                                                            'angles of a quadrilateral?',
                                                                'options': ['180°', '270°', '540°', '360°'],
                                                                'answer': '360°',
                                                                'explanation': 'A quadrilateral can be '
                                                                               'divided into two triangles: '
                                                                               '2 × 180° = 360°.'},
                                                               {'question': 'A price rises from ₹200 to '
                                                                            '₹250. Find the percentage '
                                                                            'increase.',
                                                                'options': ['50%', '125%', '25%', '20%'],
                                                                'answer': '25%',
                                                                'explanation': 'Increase = ₹50; percentage '
                                                                               'increase = 50/200 × 100 = '
                                                                               '25%.'}],
                                                 'written_questions': [{'question': 'Solve a question from '
                                                                                    'this test again, '
                                                                                    'showing each '
                                                                                    'calculation and '
                                                                                    'checking the result.',
                                                                        'reference_answer': 'Use the '
                                                                                            'corresponding '
                                                                                            'MCQ explanation '
                                                                                            'to check the '
                                                                                            'method. A '
                                                                                            'complete '
                                                                                            'response must '
                                                                                            'show '
                                                                                            'intermediate '
                                                                                            'steps and the '
                                                                                            'final answer '
                                                                                            'with units '
                                                                                            'where '
                                                                                            'relevant.'}]},
 'Class 8 Science — Foundation Practice 1': {'class': 'Class 8',
                                             'subject': 'Science',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Which part of a plant usually '
                                                                        'absorbs water from the soil?',
                                                            'options': ['Roots',
                                                                        'Flowers',
                                                                        'Fruits',
                                                                        'Petals'],
                                                            'answer': 'Roots',
                                                            'explanation': 'Roots take up water and '
                                                                           'dissolved minerals from the '
                                                                           'soil.'},
                                                           {'question': 'Which gas do humans need for '
                                                                        'aerobic respiration?',
                                                            'options': ['Helium',
                                                                        'Hydrogen',
                                                                        'Neon',
                                                                        'Oxygen'],
                                                            'answer': 'Oxygen',
                                                            'explanation': 'Oxygen is used in aerobic '
                                                                           'respiration to release energy '
                                                                           'from food.'},
                                                           {'question': 'What is the change from liquid '
                                                                        'water to water vapour called?',
                                                            'options': ['Melting',
                                                                        'Condensation',
                                                                        'Evaporation',
                                                                        'Freezing'],
                                                            'answer': 'Evaporation',
                                                            'explanation': 'Evaporation changes liquid water '
                                                                           'into water vapour.'}],
                                             'written_questions': [{'question': 'Explain evaporation and '
                                                                                'give an everyday example.',
                                                                    'reference_answer': 'Evaporation is the '
                                                                                        'change of a liquid '
                                                                                        'into vapour at its '
                                                                                        'surface. Wet '
                                                                                        'clothes drying are '
                                                                                        'an example.'}]},
 'Class 8 Science — Foundation Practice 2': {'class': 'Class 8',
                                             'subject': 'Science',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Which material is usually a good '
                                                                        'electrical conductor?',
                                                            'options': ['Rubber',
                                                                        'Dry wood',
                                                                        'Plastic',
                                                                        'Copper'],
                                                            'answer': 'Copper',
                                                            'explanation': 'Copper allows electric current '
                                                                           'to pass through it readily.'},
                                                           {'question': 'Which organ pumps blood around the '
                                                                        'human body?',
                                                            'options': ['Kidney', 'Lung', 'Heart', 'Stomach'],
                                                            'answer': 'Heart',
                                                            'explanation': 'The heart pumps blood through '
                                                                           'blood vessels.'},
                                                           {'question': 'Which process makes water vapour '
                                                                        'form liquid droplets?',
                                                            'options': ['Sublimation',
                                                                        'Condensation',
                                                                        'Evaporation',
                                                                        'Melting'],
                                                            'answer': 'Condensation',
                                                            'explanation': 'Cooling water vapour can cause '
                                                                           'it to condense into liquid '
                                                                           'water.'}],
                                             'written_questions': [{'question': 'Explain the difference '
                                                                                'between a conductor and an '
                                                                                'insulator. Give one example '
                                                                                'of each.',
                                                                    'reference_answer': 'A conductor permits '
                                                                                        'current to flow '
                                                                                        'readily, such as '
                                                                                        'copper. An '
                                                                                        'insulator strongly '
                                                                                        'resists current, '
                                                                                        'such as rubber.'}]},
 'Class 8 English — Foundation Practice 1': {'class': 'Class 8',
                                             'subject': 'English',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Choose the noun in: The kitten '
                                                                        'sleeps quietly.',
                                                            'options': ['kitten', 'sleeps', 'quietly', 'The'],
                                                            'answer': 'kitten',
                                                            'explanation': 'Kitten names an animal, so it is '
                                                                           'a noun.'},
                                                           {'question': 'Choose the correct sentence.',
                                                            'options': ['She go to school.',
                                                                        'She going to school.',
                                                                        'She gone to school.',
                                                                        'She goes to school.'],
                                                            'answer': 'She goes to school.',
                                                            'explanation': 'A singular third-person subject '
                                                                           'takes goes in the simple present '
                                                                           'tense.'},
                                                           {'question': 'Choose a synonym of happy.',
                                                            'options': ['tired', 'afraid', 'joyful', 'angry'],
                                                            'answer': 'joyful',
                                                            'explanation': 'Joyful and happy have similar '
                                                                           'meanings.'}],
                                             'written_questions': [{'question': 'Write four sentences about '
                                                                                'a helpful act. Use at least '
                                                                                'one adjective and one '
                                                                                'past-tense verb.',
                                                                    'reference_answer': 'Example: Yesterday '
                                                                                        'I helped an elderly '
                                                                                        'neighbour. Her '
                                                                                        'heavy bag had torn. '
                                                                                        'I carried the '
                                                                                        'groceries home. She '
                                                                                        'thanked me with a '
                                                                                        'warm smile. Accept '
                                                                                        'other clear, '
                                                                                        'grammatical '
                                                                                        'answers.'}]},
 'Class 8 English — Foundation Practice 2': {'class': 'Class 8',
                                             'subject': 'English',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Choose the past tense of write.',
                                                            'options': ['written',
                                                                        'writing',
                                                                        'writes',
                                                                        'wrote'],
                                                            'answer': 'wrote',
                                                            'explanation': 'The simple past form of write is '
                                                                           'wrote.'},
                                                           {'question': 'Which punctuation mark ends a '
                                                                        'direct question?',
                                                            'options': ['Apostrophe',
                                                                        'Colon',
                                                                        'Question mark',
                                                                        'Comma'],
                                                            'answer': 'Question mark',
                                                            'explanation': 'A direct question ends with a '
                                                                           'question mark.'},
                                                           {'question': 'Choose the adjective in: The bright '
                                                                        'moon shone.',
                                                            'options': ['The', 'bright', 'moon', 'shone'],
                                                            'answer': 'bright',
                                                            'explanation': 'Bright describes the noun '
                                                                           'moon.'}],
                                             'written_questions': [{'question': 'Change into the past tense: '
                                                                                'I walk to school and meet '
                                                                                'my friends.',
                                                                    'reference_answer': 'I walked to school '
                                                                                        'and met my '
                                                                                        'friends.'}]},
 'Class 8 Social Studies — Foundation Practice 1': {'class': 'Class 8',
                                                    'subject': 'Social Studies',
                                                    'duration_minutes': 10,
                                                    'questions': [{'question': 'Which direction is opposite '
                                                                               'to north?',
                                                                   'options': ['South',
                                                                               'East',
                                                                               'West',
                                                                               'Northeast'],
                                                                   'answer': 'South',
                                                                   'explanation': 'South is the direction '
                                                                                  'opposite to north.'},
                                                                  {'question': 'What does a map key explain?',
                                                                   'options': ['Only the map price',
                                                                               'The age of every city',
                                                                               'Only the weather',
                                                                               'The symbols used on a map'],
                                                                   'answer': 'The symbols used on a map',
                                                                   'explanation': 'A map key or legend '
                                                                                  'explains the meaning of '
                                                                                  'symbols.'},
                                                                  {'question': 'Which is an example of a '
                                                                               'historical source?',
                                                                   'options': ['An imagined future city',
                                                                               'A weather forecast',
                                                                               'An old inscription',
                                                                               'A prediction about tomorrow'],
                                                                   'answer': 'An old inscription',
                                                                   'explanation': 'An inscription is '
                                                                                  'evidence produced in the '
                                                                                  'past that historians can '
                                                                                  'study.'}],
                                                    'written_questions': [{'question': 'Explain why a map '
                                                                                       'needs a scale and a '
                                                                                       'key.',
                                                                           'reference_answer': 'A scale '
                                                                                               'relates map '
                                                                                               'distance to '
                                                                                               'real '
                                                                                               'distance. A '
                                                                                               'key explains '
                                                                                               'symbols, '
                                                                                               'helping '
                                                                                               'readers '
                                                                                               'understand '
                                                                                               'what the map '
                                                                                               'shows.'}]},
 'Class 8 Social Studies — Foundation Practice 2': {'class': 'Class 8',
                                                    'subject': 'Social Studies',
                                                    'duration_minutes': 10,
                                                    'questions': [{'question': 'Which line divides Earth '
                                                                               'into Northern and Southern '
                                                                               'Hemispheres?',
                                                                   'options': ['Prime Meridian',
                                                                               'Tropic of Cancer',
                                                                               'Arctic Circle',
                                                                               'Equator'],
                                                                   'answer': 'Equator',
                                                                   'explanation': 'The Equator is at 0° '
                                                                                  'latitude and separates '
                                                                                  'the two hemispheres.'},
                                                                  {'question': 'Which action helps conserve '
                                                                               'water?',
                                                                   'options': ['Ignoring pipe leaks',
                                                                               'Washing a driveway daily '
                                                                               'with a hose',
                                                                               'Repairing leaking taps',
                                                                               'Leaving taps running'],
                                                                   'answer': 'Repairing leaking taps',
                                                                   'explanation': 'Repairing leaks prevents '
                                                                                  'avoidable loss of water.'},
                                                                  {'question': 'Why do communities need '
                                                                               'rules?',
                                                                   'options': ['To prevent all discussion',
                                                                               'To help people live together '
                                                                               'fairly and safely',
                                                                               'To stop all cooperation',
                                                                               'To remove all '
                                                                               'responsibilities'],
                                                                   'answer': 'To help people live together '
                                                                             'fairly and safely',
                                                                   'explanation': 'Rules help protect '
                                                                                  'rights, set '
                                                                                  'responsibilities and '
                                                                                  'support cooperation.'}],
                                                    'written_questions': [{'question': 'Give two ways to '
                                                                                       'care for a shared '
                                                                                       'public space and '
                                                                                       'explain why they '
                                                                                       'help.',
                                                                           'reference_answer': 'Put litter '
                                                                                               'in bins and '
                                                                                               'protect '
                                                                                               'plants or '
                                                                                               'equipment. '
                                                                                               'These '
                                                                                               'actions keep '
                                                                                               'the space '
                                                                                               'clean, safe '
                                                                                               'and usable '
                                                                                               'for '
                                                                                               'everyone. '
                                                                                               'Accept other '
                                                                                               'sensible '
                                                                                               'examples.'}]},
 'Class 8 Computer Studies — Foundation Practice 1': {'class': 'Class 8',
                                                      'subject': 'Computer Studies',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Which is an input device?',
                                                                     'options': ['Keyboard',
                                                                                 'Monitor',
                                                                                 'Speaker',
                                                                                 'Projector'],
                                                                     'answer': 'Keyboard',
                                                                     'explanation': 'A keyboard sends typed '
                                                                                    'data and commands into '
                                                                                    'a computer.'},
                                                                    {'question': 'Which component carries '
                                                                                 'out program instructions?',
                                                                     'options': ['Printer',
                                                                                 'Mouse mat',
                                                                                 'Monitor stand',
                                                                                 'CPU'],
                                                                     'answer': 'CPU',
                                                                     'explanation': 'The central processing '
                                                                                    'unit executes '
                                                                                    'instructions.'},
                                                                    {'question': 'Which is an example of '
                                                                                 'software?',
                                                                     'options': ['A screen',
                                                                                 'A cable',
                                                                                 'A word processor',
                                                                                 'A keyboard'],
                                                                     'answer': 'A word processor',
                                                                     'explanation': 'Software consists of '
                                                                                    'programs; a word '
                                                                                    'processor is a '
                                                                                    'program.'}],
                                                      'written_questions': [{'question': 'Describe input, '
                                                                                         'processing and '
                                                                                         'output using a '
                                                                                         'calculator as an '
                                                                                         'example.',
                                                                             'reference_answer': 'Input: '
                                                                                                 'enter '
                                                                                                 'numbers '
                                                                                                 'and an '
                                                                                                 'operation. '
                                                                                                 'Processing: '
                                                                                                 'the '
                                                                                                 'calculator '
                                                                                                 'performs '
                                                                                                 'the '
                                                                                                 'calculation. '
                                                                                                 'Output: it '
                                                                                                 'displays '
                                                                                                 'the '
                                                                                                 'result.'}]},
 'Class 8 Computer Studies — Foundation Practice 2': {'class': 'Class 8',
                                                      'subject': 'Computer Studies',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Which is the safest action '
                                                                                 'when someone asks for your '
                                                                                 'password?',
                                                                     'options': ['Post it in a group',
                                                                                 'Send it to a stranger',
                                                                                 'Use it as your public '
                                                                                 'username',
                                                                                 'Keep it private and ask a '
                                                                                 'trusted adult for help'],
                                                                     'answer': 'Keep it private and ask a '
                                                                               'trusted adult for help',
                                                                     'explanation': 'Passwords should remain '
                                                                                    'private; seek help if '
                                                                                    'someone pressures you '
                                                                                    'to share them.'},
                                                                    {'question': 'What is an algorithm?',
                                                                     'options': ['A broken cable',
                                                                                 'A type of desk',
                                                                                 'A sequence of steps to '
                                                                                 'solve a problem',
                                                                                 'Only a computer screen'],
                                                                     'answer': 'A sequence of steps to solve '
                                                                               'a problem',
                                                                     'explanation': 'An algorithm describes '
                                                                                    'a sequence of steps for '
                                                                                    'completing a task.'},
                                                                    {'question': 'Why should important files '
                                                                                 'have backups?',
                                                                     'options': ['To replace all software '
                                                                                 'updates',
                                                                                 'To help recover them after '
                                                                                 'loss or damage',
                                                                                 'To guarantee files can '
                                                                                 'never be lost',
                                                                                 'To make passwords public'],
                                                                     'answer': 'To help recover them after '
                                                                               'loss or damage',
                                                                     'explanation': 'A separate backup can '
                                                                                    'help restore files if '
                                                                                    'the original is lost or '
                                                                                    'damaged.'}],
                                                      'written_questions': [{'question': 'Write an algorithm '
                                                                                         'for adding two '
                                                                                         'numbers and '
                                                                                         'explain one '
                                                                                         'safe-password '
                                                                                         'habit.',
                                                                             'reference_answer': 'Read two '
                                                                                                 'numbers, '
                                                                                                 'calculate '
                                                                                                 'their sum, '
                                                                                                 'and '
                                                                                                 'display '
                                                                                                 'it. Use a '
                                                                                                 'long, '
                                                                                                 'unique '
                                                                                                 'password '
                                                                                                 'and keep '
                                                                                                 'it '
                                                                                                 'private.'}]},
 'Class 9 Mathematics — Foundation Practice 1': {'class': 'Class 9',
                                                 'subject': 'Mathematics',
                                                 'duration_minutes': 10,
                                                 'questions': [{'question': 'Find the distance of point (−3, '
                                                                            '4) from the origin.',
                                                                'options': ['7 units',
                                                                            '1 unit',
                                                                            '25 units',
                                                                            '5 units'],
                                                                'answer': '5 units',
                                                                'explanation': 'Distance = √[(-3)² + 4²] = '
                                                                               '√25 = 5.'},
                                                               {'question': 'Expand (a − b)².',
                                                                'options': ['a² + 2ab + b²',
                                                                            'a² − 2b',
                                                                            'a² − 2ab + b²',
                                                                            'a² − b²'],
                                                                'answer': 'a² − 2ab + b²',
                                                                'explanation': 'The identity is (a − b)² = '
                                                                               'a² − 2ab + b².'},
                                                               {'question': 'Find the median of 3, 8, 4, 9, '
                                                                            '6.',
                                                                'options': ['5', '6', '4', '8'],
                                                                'answer': '6',
                                                                'explanation': 'Order the values: 3, 4, 6, '
                                                                               '8, 9. The middle value is '
                                                                               '6.'}],
                                                 'written_questions': [{'question': 'Solve a question from '
                                                                                    'this test again, '
                                                                                    'showing each '
                                                                                    'calculation and '
                                                                                    'checking the result.',
                                                                        'reference_answer': 'Use the '
                                                                                            'corresponding '
                                                                                            'MCQ explanation '
                                                                                            'to check the '
                                                                                            'method. A '
                                                                                            'complete '
                                                                                            'response must '
                                                                                            'show '
                                                                                            'intermediate '
                                                                                            'steps and the '
                                                                                            'final answer '
                                                                                            'with units '
                                                                                            'where '
                                                                                            'relevant.'}]},
 'Class 9 Physics — Foundation Practice 1': {'class': 'Class 9',
                                             'subject': 'Physics',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'A current of 2 A flows through a 3 '
                                                                        'Ω resistor. Find the potential '
                                                                        'difference.',
                                                            'options': ['1.5 V', '5 V', '0.67 V', '6 V'],
                                                            'answer': '6 V',
                                                            'explanation': 'Using V = IR gives 2 × 3 = 6 V.'},
                                                           {'question': 'Which instrument measures electric '
                                                                        'current?',
                                                            'options': ['Barometer',
                                                                        'Thermometer',
                                                                        'Ammeter',
                                                                        'Voltmeter'],
                                                            'answer': 'Ammeter',
                                                            'explanation': 'An ammeter measures current and '
                                                                           'is connected in series with the '
                                                                           'component.'},
                                                           {'question': 'A wave has frequency 5 Hz and '
                                                                        'wavelength 2 m. Find its speed.',
                                                            'options': ['3 m/s',
                                                                        '10 m/s',
                                                                        '2.5 m/s',
                                                                        '7 m/s'],
                                                            'answer': '10 m/s',
                                                            'explanation': 'Wave speed = frequency × '
                                                                           'wavelength = 5 × 2 = 10 m/s.'}],
                                             'written_questions': [{'question': 'Calculate the current '
                                                                                'through a 6 Ω resistor when '
                                                                                'the voltage across it is 12 '
                                                                                'V. Show your working.',
                                                                    'reference_answer': 'I = V/R = 12/6 = 2 '
                                                                                        'A.'}]},
 'Class 9 Physics — Foundation Practice 2': {'class': 'Class 9',
                                             'subject': 'Physics',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'An object travels 60 m in 12 s at '
                                                                        'constant speed. Find its speed.',
                                                            'options': ['48 m/s',
                                                                        '72 m/s',
                                                                        '5 m/s',
                                                                        '720 m/s'],
                                                            'answer': '5 m/s',
                                                            'explanation': 'Speed = distance/time = 60/12 = '
                                                                           '5 m/s.'},
                                                           {'question': 'What happens to pressure if the '
                                                                        'same perpendicular force acts over '
                                                                        'a smaller area?',
                                                            'options': ['It must stay unchanged',
                                                                        'It increases',
                                                                        'It decreases',
                                                                        'It becomes zero'],
                                                            'answer': 'It increases',
                                                            'explanation': 'Pressure = force/area, so '
                                                                           'reducing area at fixed force '
                                                                           'increases pressure.'},
                                                           {'question': 'In reflection, the angle of '
                                                                        'incidence equals which angle?',
                                                            'options': ['Angle of reflection',
                                                                        'Angle of refraction in every '
                                                                        'material',
                                                                        'Angle between mirror and incident '
                                                                        'ray',
                                                                        'Always 90°'],
                                                            'answer': 'Angle of reflection',
                                                            'explanation': 'The angles of incidence and '
                                                                           'reflection, both measured from '
                                                                           'the normal, are equal.'}],
                                             'written_questions': [{'question': 'Explain why a sharp knife '
                                                                                'can cut more easily than a '
                                                                                'blunt knife under the same '
                                                                                'applied force.',
                                                                    'reference_answer': 'The sharp edge has '
                                                                                        'a smaller contact '
                                                                                        'area. Pressure = '
                                                                                        'force/area, so the '
                                                                                        'same force produces '
                                                                                        'greater '
                                                                                        'pressure.'}]},
 'Class 9 Chemistry — Foundation Practice 1': {'class': 'Class 9',
                                               'subject': 'Chemistry',
                                               'duration_minutes': 10,
                                               'questions': [{'question': 'What is the atomic number of an '
                                                                          'element equal to?',
                                                              'options': ['Number of neutrons only',
                                                                          'Protons plus neutrons',
                                                                          'Number of electron shells',
                                                                          'Number of protons'],
                                                              'answer': 'Number of protons',
                                                              'explanation': 'Atomic number is the number of '
                                                                             'protons in the nucleus.'},
                                                             {'question': 'What is the chemical formula of '
                                                                          'water?',
                                                              'options': ['O₂', 'NaCl', 'H₂O', 'CO₂'],
                                                              'answer': 'H₂O',
                                                              'explanation': 'Each water molecule contains '
                                                                             'two hydrogen atoms and one '
                                                                             'oxygen atom.'},
                                                             {'question': 'Which process forms an ionic bond '
                                                                          'between sodium and chlorine?',
                                                              'options': ['Melting both atoms',
                                                                          'Transfer of an electron from '
                                                                          'sodium to chlorine',
                                                                          'Equal sharing of two protons',
                                                                          'Transfer of a neutron from '
                                                                          'chlorine'],
                                                              'answer': 'Transfer of an electron from sodium '
                                                                        'to chlorine',
                                                              'explanation': 'Electron transfer produces '
                                                                             'oppositely charged ions held '
                                                                             'by electrostatic attraction.'}],
                                               'written_questions': [{'question': 'Distinguish an element '
                                                                                  'from a compound and give '
                                                                                  'one example of each.',
                                                                      'reference_answer': 'An element '
                                                                                          'contains one type '
                                                                                          'of atom, such as '
                                                                                          'oxygen. A '
                                                                                          'compound contains '
                                                                                          'different '
                                                                                          'elements '
                                                                                          'chemically '
                                                                                          'combined in a '
                                                                                          'fixed proportion, '
                                                                                          'such as water.'}]},
 'Class 9 Chemistry — Foundation Practice 2': {'class': 'Class 9',
                                               'subject': 'Chemistry',
                                               'duration_minutes': 10,
                                               'questions': [{'question': 'An aqueous solution has pH 3. How '
                                                                          'is it classified?',
                                                              'options': ['Alkaline',
                                                                          'Necessarily pure water',
                                                                          'Acidic',
                                                                          'Neutral'],
                                                              'answer': 'Acidic',
                                                              'explanation': 'At ordinary school reference '
                                                                             'conditions, pH below 7 '
                                                                             'indicates an acidic solution.'},
                                                             {'question': 'Which equation is balanced?',
                                                              'options': ['2H₂ + O₂ → H₂O',
                                                                          '2H₂ + O₂ → 2H₂O',
                                                                          'H₂ + O₂ → H₂O',
                                                                          'H₂ + 2O₂ → H₂O'],
                                                              'answer': '2H₂ + O₂ → 2H₂O',
                                                              'explanation': 'The balanced equation has four '
                                                                             'hydrogen atoms and two oxygen '
                                                                             'atoms on each side.'},
                                                             {'question': 'Which method separates an '
                                                                          'insoluble solid from a liquid?',
                                                              'options': ['Filtration',
                                                                          'Magnetism in all cases',
                                                                          'Evaporation of the solid',
                                                                          'Adding more solid'],
                                                              'answer': 'Filtration',
                                                              'explanation': 'A filter can retain insoluble '
                                                                             'solid particles while the '
                                                                             'liquid passes through.'}],
                                               'written_questions': [{'question': 'Explain neutralisation '
                                                                                  'and give a balanced '
                                                                                  'equation using '
                                                                                  'hydrochloric acid and '
                                                                                  'sodium hydroxide.',
                                                                      'reference_answer': 'An acid reacts '
                                                                                          'with a base to '
                                                                                          'form salt and '
                                                                                          'water. HCl + NaOH '
                                                                                          '→ NaCl + H₂O.'}]},
 'Class 9 Biology — Foundation Practice 1': {'class': 'Class 9',
                                             'subject': 'Biology',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'Which cell structure contains most '
                                                                        'of a typical plant or animal cell’s '
                                                                        'genetic material?',
                                                            'options': ['Cell wall',
                                                                        'Vacuole only',
                                                                        'Cell membrane only',
                                                                        'Nucleus'],
                                                            'answer': 'Nucleus',
                                                            'explanation': 'In a typical nucleated plant or '
                                                                           'animal cell, most DNA is in the '
                                                                           'nucleus.'},
                                                           {'question': 'Which pigment absorbs light for '
                                                                        'photosynthesis?',
                                                            'options': ['Melanin',
                                                                        'Keratin',
                                                                        'Chlorophyll',
                                                                        'Haemoglobin'],
                                                            'answer': 'Chlorophyll',
                                                            'explanation': 'Chlorophyll in chloroplasts '
                                                                           'absorbs light energy for '
                                                                           'photosynthesis.'},
                                                           {'question': 'Which plant tissue mainly '
                                                                        'transports water from roots?',
                                                            'options': ['Petal tissue',
                                                                        'Xylem',
                                                                        'Phloem',
                                                                        'Epidermis only'],
                                                            'answer': 'Xylem',
                                                            'explanation': 'Xylem transports water and '
                                                                           'dissolved minerals from the '
                                                                           'roots.'}],
                                             'written_questions': [{'question': 'State two differences '
                                                                                'between typical plant and '
                                                                                'animal cells.',
                                                                    'reference_answer': 'Plant cells have a '
                                                                                        'cellulose cell wall '
                                                                                        'and usually a large '
                                                                                        'permanent vacuole. '
                                                                                        'Animal cells lack a '
                                                                                        'cell wall and '
                                                                                        'usually lack a '
                                                                                        'large permanent '
                                                                                        'vacuole. '
                                                                                        'Chloroplasts occur '
                                                                                        'in photosynthetic '
                                                                                        'plant cells.'}]},
 'Class 9 Biology — Foundation Practice 2': {'class': 'Class 9',
                                             'subject': 'Biology',
                                             'duration_minutes': 10,
                                             'questions': [{'question': 'What is transpiration?',
                                                            'options': ['Release of seeds only',
                                                                        'Breakdown of glucose only',
                                                                        'Loss of water vapour from aerial '
                                                                        'parts of plants',
                                                                        'Absorption of food by roots'],
                                                            'answer': 'Loss of water vapour from aerial '
                                                                      'parts of plants',
                                                            'explanation': 'Transpiration is water-vapour '
                                                                           'loss, mainly through stomata in '
                                                                           'leaves.'},
                                                           {'question': 'Which blood cells mainly transport '
                                                                        'oxygen?',
                                                            'options': ['Nerve cells',
                                                                        'Red blood cells',
                                                                        'Platelets',
                                                                        'White blood cells'],
                                                            'answer': 'Red blood cells',
                                                            'explanation': 'Red blood cells contain '
                                                                           'haemoglobin, which binds '
                                                                           'oxygen.'},
                                                           {'question': 'Which organs filter blood and '
                                                                        'produce urine?',
                                                            'options': ['Kidneys',
                                                                        'Lungs',
                                                                        'Stomach',
                                                                        'Pancreas'],
                                                            'answer': 'Kidneys',
                                                            'explanation': 'The kidneys filter blood and '
                                                                           'regulate water and dissolved '
                                                                           'substances while forming '
                                                                           'urine.'}],
                                             'written_questions': [{'question': 'Explain why photosynthesis '
                                                                                'and respiration are '
                                                                                'different processes.',
                                                                    'reference_answer': 'Photosynthesis uses '
                                                                                        'light energy to '
                                                                                        'make organic food '
                                                                                        'from carbon dioxide '
                                                                                        'and water, '
                                                                                        'releasing oxygen. '
                                                                                        'Aerobic respiration '
                                                                                        'releases usable '
                                                                                        'energy from organic '
                                                                                        'food using oxygen, '
                                                                                        'producing carbon '
                                                                                        'dioxide and '
                                                                                        'water.'}]},
 'Class 9 English Language — Foundation Practice 1': {'class': 'Class 9',
                                                      'subject': 'English Language',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Choose the correct '
                                                                                 'sentence.',
                                                                     'options': ['Each of the students have '
                                                                                 'a notebook.',
                                                                                 'Each of the students are a '
                                                                                 'notebook.',
                                                                                 'Each of the students were '
                                                                                 'a notebook.',
                                                                                 'Each of the students has a '
                                                                                 'notebook.'],
                                                                     'answer': 'Each of the students has a '
                                                                               'notebook.',
                                                                     'explanation': 'Each is singular and '
                                                                                    'takes has in this '
                                                                                    'sentence.'},
                                                                    {'question': 'Choose the passive form '
                                                                                 'of: The teacher praised '
                                                                                 'Riya.',
                                                                     'options': ['Riya is praising the '
                                                                                 'teacher.',
                                                                                 'Riya had praise the '
                                                                                 'teacher.',
                                                                                 'Riya was praised by the '
                                                                                 'teacher.',
                                                                                 'Riya praised the teacher.'],
                                                                     'answer': 'Riya was praised by the '
                                                                               'teacher.',
                                                                     'explanation': 'The simple-past passive '
                                                                                    'uses was/were + past '
                                                                                    'participle.'},
                                                                    {'question': 'Choose the correct '
                                                                                 'preposition: She has lived '
                                                                                 'here ___ 2020.',
                                                                     'options': ['from since',
                                                                                 'since',
                                                                                 'for',
                                                                                 'during to'],
                                                                     'answer': 'since',
                                                                     'explanation': 'Since introduces the '
                                                                                    'starting point of a '
                                                                                    'continuing period.'}],
                                                      'written_questions': [{'question': 'Write a short '
                                                                                         'formal request to '
                                                                                         'your principal for '
                                                                                         'permission to '
                                                                                         'start a reading '
                                                                                         'club. Include '
                                                                                         'purpose and a '
                                                                                         'proposed meeting '
                                                                                         'time.',
                                                                             'reference_answer': 'Example: '
                                                                                                 'Dear '
                                                                                                 'Principal, '
                                                                                                 'I request '
                                                                                                 'permission '
                                                                                                 'to start a '
                                                                                                 'reading '
                                                                                                 'club to '
                                                                                                 'encourage '
                                                                                                 'regular '
                                                                                                 'reading. '
                                                                                                 'We propose '
                                                                                                 'meeting on '
                                                                                                 'Fridays '
                                                                                                 'after '
                                                                                                 'school '
                                                                                                 'under a '
                                                                                                 'teacher’s '
                                                                                                 'supervision. '
                                                                                                 'Kindly '
                                                                                                 'consider '
                                                                                                 'our '
                                                                                                 'request. '
                                                                                                 'Yours '
                                                                                                 'faithfully, '
                                                                                                 '[Student '
                                                                                                 'name]. '
                                                                                                 'Accept '
                                                                                                 'other '
                                                                                                 'suitable '
                                                                                                 'formats '
                                                                                                 'and clear, '
                                                                                                 'polite '
                                                                                                 'wording.'}]},
 'Class 9 English Language — Foundation Practice 2': {'class': 'Class 9',
                                                      'subject': 'English Language',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Choose the correct '
                                                                                 'reported form: He said, “I '
                                                                                 'am tired.”',
                                                                     'options': ['He says that he tired.',
                                                                                 'He said that he is tire.',
                                                                                 'He said that he was tired.',
                                                                                 'He said that I am tired.'],
                                                                     'answer': 'He said that he was tired.',
                                                                     'explanation': 'In this ordinary '
                                                                                    'past-reporting context, '
                                                                                    'I changes to he and am '
                                                                                    'to was.'},
                                                                    {'question': 'Which sentence correctly '
                                                                                 'uses an apostrophe for one '
                                                                                 'girl’s bag?',
                                                                     'options': ['The girl bag’s is blue.',
                                                                                 'The girl’s bag is blue.',
                                                                                 'The girls bag is blue.',
                                                                                 'The girls’ bag is blue.'],
                                                                     'answer': 'The girl’s bag is blue.',
                                                                     'explanation': 'For a single girl, '
                                                                                    'possession is shown '
                                                                                    'with girl’s.'},
                                                                    {'question': 'Which is the best opening '
                                                                                 'for a formal request to a '
                                                                                 'principal?',
                                                                     'options': ['I am writing to request '
                                                                                 'permission to organise a '
                                                                                 'reading club.',
                                                                                 'Hey, give us a club!',
                                                                                 'Whatever, we need this.',
                                                                                 'You must say yes now.'],
                                                                     'answer': 'I am writing to request '
                                                                               'permission to organise a '
                                                                               'reading club.',
                                                                     'explanation': 'A formal request should '
                                                                                    'state its purpose '
                                                                                    'politely and clearly.'}],
                                                      'written_questions': [{'question': 'Combine without '
                                                                                         'changing meaning: '
                                                                                         'Although it was '
                                                                                         'raining, the '
                                                                                         'players continued '
                                                                                         'the match. Begin '
                                                                                         'with “Despite”.',
                                                                             'reference_answer': 'Despite '
                                                                                                 'the rain, '
                                                                                                 'the '
                                                                                                 'players '
                                                                                                 'continued '
                                                                                                 'the match. '
                                                                                                 'Also '
                                                                                                 'accept: '
                                                                                                 'Despite '
                                                                                                 'the fact '
                                                                                                 'that it '
                                                                                                 'was '
                                                                                                 'raining, '
                                                                                                 'the '
                                                                                                 'players '
                                                                                                 'continued '
                                                                                                 'the '
                                                                                                 'match.'}]},
 'Class 9 English Literature — Foundation Practice 1': {'class': 'Class 9',
                                                        'subject': 'English Literature',
                                                        'duration_minutes': 10,
                                                        'questions': [{'question': 'Original passage: “Mira '
                                                                                   'waited by the gate. When '
                                                                                   'her brother arrived, her '
                                                                                   'shoulders relaxed.” What '
                                                                                   'does her reaction '
                                                                                   'suggest?',
                                                                       'options': ['She had forgotten him',
                                                                                   'She wanted to run a race',
                                                                                   'She disliked the gate',
                                                                                   'She had been worried'],
                                                                       'answer': 'She had been worried',
                                                                       'explanation': 'Her relaxation after '
                                                                                      'his arrival suggests '
                                                                                      'earlier tension or '
                                                                                      'worry.'},
                                                                      {'question': 'Which phrase is a '
                                                                                   'simile?',
                                                                       'options': ['Time is a thief',
                                                                                   'The clock ticked',
                                                                                   'As quiet as a mouse',
                                                                                   'The wind whispered'],
                                                                       'answer': 'As quiet as a mouse',
                                                                       'explanation': 'A simile makes an '
                                                                                      'explicit comparison, '
                                                                                      'often using like or '
                                                                                      'as.'},
                                                                      {'question': 'What is the narrator of '
                                                                                   'a story?',
                                                                       'options': ['The person who prints '
                                                                                   'the book',
                                                                                   'The voice that tells the '
                                                                                   'story',
                                                                                   'Always the author in '
                                                                                   'real life',
                                                                                   'Only the main villain'],
                                                                       'answer': 'The voice that tells the '
                                                                                 'story',
                                                                       'explanation': 'The narrator is the '
                                                                                      'voice presenting the '
                                                                                      'story and need not be '
                                                                                      'identical to the '
                                                                                      'author.'}],
                                                        'written_questions': [{'question': 'Original '
                                                                                           'passage: “Mira '
                                                                                           'waited by the '
                                                                                           'gate. When her '
                                                                                           'brother arrived, '
                                                                                           'her shoulders '
                                                                                           'relaxed.” Infer '
                                                                                           'Mira’s feelings '
                                                                                           'before and after '
                                                                                           'his arrival. Use '
                                                                                           'evidence.',
                                                                               'reference_answer': 'Before '
                                                                                                   'his '
                                                                                                   'arrival, '
                                                                                                   'Mira '
                                                                                                   'appears '
                                                                                                   'worried '
                                                                                                   'or '
                                                                                                   'tense; '
                                                                                                   'waiting '
                                                                                                   'and the '
                                                                                                   'later '
                                                                                                   'relaxation '
                                                                                                   'support '
                                                                                                   'this '
                                                                                                   'inference. '
                                                                                                   'Afterwards '
                                                                                                   'she '
                                                                                                   'feels '
                                                                                                   'relieved, '
                                                                                                   'shown by '
                                                                                                   'her '
                                                                                                   'shoulders '
                                                                                                   'relaxing. '
                                                                                                   'Accept '
                                                                                                   'another '
                                                                                                   'reasonable '
                                                                                                   'interpretation '
                                                                                                   'supported '
                                                                                                   'by the '
                                                                                                   'text.'}]},
 'Class 9 English Literature — Foundation Practice 2': {'class': 'Class 9',
                                                        'subject': 'English Literature',
                                                        'duration_minutes': 10,
                                                        'questions': [{'question': 'Original line: “The '
                                                                                   'tired street slept under '
                                                                                   'the moon.” Which device '
                                                                                   'gives the street a human '
                                                                                   'action?',
                                                                       'options': ['A direct question',
                                                                                   'An instruction',
                                                                                   'Personification',
                                                                                   'A factual measurement'],
                                                                       'answer': 'Personification',
                                                                       'explanation': 'Describing the street '
                                                                                      'as sleeping gives a '
                                                                                      'non-human thing a '
                                                                                      'human action.'},
                                                                      {'question': 'What is a theme in a '
                                                                                   'literary work?',
                                                                       'options': ['The publisher’s address',
                                                                                   'An underlying idea '
                                                                                   'explored by the work',
                                                                                   'Only the page number',
                                                                                   'Always the title alone'],
                                                                       'answer': 'An underlying idea '
                                                                                 'explored by the work',
                                                                       'explanation': 'A theme is an idea or '
                                                                                      'concern developed '
                                                                                      'through characters, '
                                                                                      'events or language.'},
                                                                      {'question': 'Original passage: “Arun '
                                                                                   'returned the lost purse '
                                                                                   'though nobody was '
                                                                                   'watching.” Which trait '
                                                                                   'is most directly shown?',
                                                                       'options': ['Honesty',
                                                                                   'Jealousy',
                                                                                   'Impatience',
                                                                                   'Cruelty'],
                                                                       'answer': 'Honesty',
                                                                       'explanation': 'Returning the purse '
                                                                                      'without an audience '
                                                                                      'demonstrates '
                                                                                      'honesty.'}],
                                                        'written_questions': [{'question': 'Explain the '
                                                                                           'personification '
                                                                                           'in the original '
                                                                                           'line “The tired '
                                                                                           'street slept '
                                                                                           'under the moon.” '
                                                                                           'What mood might '
                                                                                           'it create?',
                                                                               'reference_answer': 'The '
                                                                                                   'street '
                                                                                                   'is '
                                                                                                   'described '
                                                                                                   'as tired '
                                                                                                   'and '
                                                                                                   'sleeping, '
                                                                                                   'which '
                                                                                                   'are '
                                                                                                   'human '
                                                                                                   'states/actions. '
                                                                                                   'This can '
                                                                                                   'suggest '
                                                                                                   'a quiet, '
                                                                                                   'still or '
                                                                                                   'peaceful '
                                                                                                   'night. '
                                                                                                   'Accept a '
                                                                                                   'supported '
                                                                                                   'alternative '
                                                                                                   'such as '
                                                                                                   'loneliness.'}]},
 'Class 9 History & Civics — Foundation Practice 1': {'class': 'Class 9',
                                                      'subject': 'History & Civics',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Which is a primary source '
                                                                                 'for studying an ancient '
                                                                                 'civilisation?',
                                                                     'options': ['A modern fictional film',
                                                                                 'A future prediction',
                                                                                 'An invented diary written '
                                                                                 'today',
                                                                                 'An inscription made during '
                                                                                 'that period'],
                                                                     'answer': 'An inscription made during '
                                                                               'that period',
                                                                     'explanation': 'An inscription created '
                                                                                    'in the period provides '
                                                                                    'contemporary evidence.'},
                                                                    {'question': 'Which feature is '
                                                                                 'associated with many '
                                                                                 'Harappan cities?',
                                                                     'options': ['Modern airports',
                                                                                 'Printed newspapers',
                                                                                 'Planned streets and '
                                                                                 'drainage',
                                                                                 'Electric railways'],
                                                                     'answer': 'Planned streets and drainage',
                                                                     'explanation': 'Archaeological remains '
                                                                                    'show planned streets '
                                                                                    'and drainage in major '
                                                                                    'Harappan settlements.'},
                                                                    {'question': 'What is a constitution?',
                                                                     'options': ['Only a school timetable',
                                                                                 'A framework of basic '
                                                                                 'principles and rules for '
                                                                                 'government',
                                                                                 'Only a weather report',
                                                                                 'A private shopping list'],
                                                                     'answer': 'A framework of basic '
                                                                               'principles and rules for '
                                                                               'government',
                                                                     'explanation': 'A constitution sets out '
                                                                                    'fundamental '
                                                                                    'institutions, powers '
                                                                                    'and governing '
                                                                                    'principles.'}],
                                                      'written_questions': [{'question': 'Explain why '
                                                                                         'historians compare '
                                                                                         'different sources '
                                                                                         'instead of relying '
                                                                                         'on one account.',
                                                                             'reference_answer': 'Sources '
                                                                                                 'may be '
                                                                                                 'incomplete, '
                                                                                                 'biased or '
                                                                                                 'mistaken. '
                                                                                                 'Comparing '
                                                                                                 'independent '
                                                                                                 'evidence '
                                                                                                 'helps '
                                                                                                 'identify '
                                                                                                 'agreement, '
                                                                                                 'contradictions '
                                                                                                 'and a '
                                                                                                 'better-supported '
                                                                                                 'account.'}]},
 'Class 9 History & Civics — Foundation Practice 2': {'class': 'Class 9',
                                                      'subject': 'History & Civics',
                                                      'duration_minutes': 10,
                                                      'questions': [{'question': 'Which institution makes '
                                                                                 'laws at the Union level in '
                                                                                 'India?',
                                                                     'options': ['A private company',
                                                                                 'A sports club',
                                                                                 'Parliament',
                                                                                 'A village school'],
                                                                     'answer': 'Parliament',
                                                                     'explanation': 'The Union legislature '
                                                                                    'is Parliament.'},
                                                                    {'question': 'Which movement was '
                                                                                 'launched in India in 1942?',
                                                                     'options': ['Civil Disobedience '
                                                                                 'Movement of 1930',
                                                                                 'Quit India Movement',
                                                                                 'Non-Cooperation Movement',
                                                                                 'Swadeshi Movement of 1905'],
                                                                     'answer': 'Quit India Movement',
                                                                     'explanation': 'The Quit India Movement '
                                                                                    'was launched in August '
                                                                                    '1942.'},
                                                                    {'question': 'Which is a central purpose '
                                                                                 'of the United Nations?',
                                                                     'options': ['Maintaining international '
                                                                                 'peace and security',
                                                                                 'Running every country’s '
                                                                                 'schools directly',
                                                                                 'Replacing all national '
                                                                                 'governments',
                                                                                 'Setting every shop’s '
                                                                                 'prices'],
                                                                     'answer': 'Maintaining international '
                                                                               'peace and security',
                                                                     'explanation': 'Maintaining '
                                                                                    'international peace and '
                                                                                    'security is a central '
                                                                                    'UN purpose.'}],
                                                      'written_questions': [{'question': 'Explain the roles '
                                                                                         'of the legislature '
                                                                                         'and judiciary in a '
                                                                                         'democracy.',
                                                                             'reference_answer': 'The '
                                                                                                 'legislature '
                                                                                                 'debates '
                                                                                                 'and makes '
                                                                                                 'laws. The '
                                                                                                 'judiciary '
                                                                                                 'interprets '
                                                                                                 'laws and '
                                                                                                 'resolves '
                                                                                                 'legal '
                                                                                                 'disputes; '
                                                                                                 'it also '
                                                                                                 'exercises '
                                                                                                 'its '
                                                                                                 'constitutional '
                                                                                                 'powers to '
                                                                                                 'protect '
                                                                                                 'rights and '
                                                                                                 'review '
                                                                                                 'government '
                                                                                                 'action.'}]},
 'Class 9 Geography — Foundation Practice 1': {'class': 'Class 9',
                                               'subject': 'Geography',
                                               'duration_minutes': 10,
                                               'questions': [{'question': 'What does latitude measure?',
                                                              'options': ['Height above sea level only',
                                                                          'Distance east of a town in metres',
                                                                          'Depth of the ocean',
                                                                          'Angular distance north or south '
                                                                          'of the Equator'],
                                                              'answer': 'Angular distance north or south of '
                                                                        'the Equator',
                                                              'explanation': 'Latitude is angular distance '
                                                                             'north or south of the Equator, '
                                                                             'measured in degrees.'},
                                                             {'question': 'Which layer lies directly below '
                                                                          'Earth’s crust?',
                                                              'options': ['Atmosphere',
                                                                          'Hydrosphere',
                                                                          'Mantle',
                                                                          'Inner core'],
                                                              'answer': 'Mantle',
                                                              'explanation': 'The mantle lies beneath the '
                                                                             'crust.'},
                                                             {'question': 'What is weathering?',
                                                              'options': ['Rotation of Earth',
                                                                          'Breakdown of rock at or near '
                                                                          'Earth’s surface',
                                                                          'Only transport of rock by rivers',
                                                                          'Formation of stars'],
                                                              'answer': 'Breakdown of rock at or near '
                                                                        'Earth’s surface',
                                                              'explanation': 'Weathering breaks down rock in '
                                                                             'place; transport is associated '
                                                                             'with erosion.'}],
                                               'written_questions': [{'question': 'Distinguish weather from '
                                                                                  'climate.',
                                                                      'reference_answer': 'Weather describes '
                                                                                          'short-term '
                                                                                          'atmospheric '
                                                                                          'conditions at a '
                                                                                          'place. Climate '
                                                                                          'describes '
                                                                                          'long-term '
                                                                                          'patterns and '
                                                                                          'averages of '
                                                                                          'weather over many '
                                                                                          'years.'}]},
 'Class 9 Geography — Foundation Practice 2': {'class': 'Class 9',
                                               'subject': 'Geography',
                                               'duration_minutes': 10,
                                               'questions': [{'question': 'On a 1:50,000 map, what ground '
                                                                          'distance does 1 cm represent?',
                                                              'options': ['5 km', '50 km', '500 m', '50 m'],
                                                              'answer': '500 m',
                                                              'explanation': '1 cm represents 50,000 cm = '
                                                                             '500 m.'},
                                                             {'question': 'Which soil type is widely '
                                                                          'associated with the northern '
                                                                          'river plains of India?',
                                                              'options': ['Only desert soil',
                                                                          'Alluvial soil',
                                                                          'Only laterite soil',
                                                                          'Only mountain soil'],
                                                              'answer': 'Alluvial soil',
                                                              'explanation': 'Rivers deposit alluvium across '
                                                                             'much of the northern plains.'},
                                                             {'question': 'Which is a renewable energy '
                                                                          'source?',
                                                              'options': ['Solar energy',
                                                                          'Coal',
                                                                          'Petroleum',
                                                                          'Natural gas'],
                                                              'answer': 'Solar energy',
                                                              'explanation': 'Sunlight is naturally '
                                                                             'replenished; fossil fuels form '
                                                                             'over much longer timescales.'}],
                                               'written_questions': [{'question': 'A map has a scale of '
                                                                                  '1:50,000. Two places are '
                                                                                  '6 cm apart on it. '
                                                                                  'Calculate their '
                                                                                  'straight-line ground '
                                                                                  'distance.',
                                                                      'reference_answer': 'Ground distance = '
                                                                                          '6 × 50,000 = '
                                                                                          '300,000 cm = '
                                                                                          '3,000 m = 3 '
                                                                                          'km.'}]},
 'Class 9 Computer Applications — Foundation Practice 1': {'class': 'Class 9',
                                                           'subject': 'Computer Applications',
                                                           'duration_minutes': 10,
                                                           'questions': [{'question': 'Which Java type '
                                                                                      'stores either true or '
                                                                                      'false?',
                                                                          'options': ['int',
                                                                                      'double',
                                                                                      'char',
                                                                                      'boolean'],
                                                                          'answer': 'boolean',
                                                                          'explanation': 'The boolean '
                                                                                         'primitive type has '
                                                                                         'the values true '
                                                                                         'and false.'},
                                                                         {'question': 'What is the value of '
                                                                                      '7 / 2 when both '
                                                                                      'operands are Java int '
                                                                                      'values?',
                                                                          'options': ['4', '2', '3', '3.5'],
                                                                          'answer': '3',
                                                                          'explanation': 'Integer division '
                                                                                         'truncates the '
                                                                                         'fractional part; 7 '
                                                                                         '/ 2 is 3.'},
                                                                         {'question': 'Which Java operator '
                                                                                      'tests equality of two '
                                                                                      'int values?',
                                                                          'options': ['+=', '==', '=', '!='],
                                                                          'answer': '==',
                                                                          'explanation': 'The == operator '
                                                                                         'compares primitive '
                                                                                         'values; = assigns '
                                                                                         'a value.'}],
                                                           'written_questions': [{'question': 'Evaluate this '
                                                                                              'Java code and '
                                                                                              'explain the '
                                                                                              'result: int x '
                                                                                              '= 5; x += 3; '
                                                                                              'System.out.println(x);',
                                                                                  'reference_answer': 'It '
                                                                                                      'prints '
                                                                                                      '8. '
                                                                                                      'The '
                                                                                                      'compound '
                                                                                                      'assignment '
                                                                                                      'adds '
                                                                                                      '3 to '
                                                                                                      'the '
                                                                                                      'existing '
                                                                                                      'value '
                                                                                                      '5 and '
                                                                                                      'stores '
                                                                                                      'the '
                                                                                                      'result '
                                                                                                      'in '
                                                                                                      'x.'}]},
 'Class 9 Computer Applications — Foundation Practice 2': {'class': 'Class 9',
                                                           'subject': 'Computer Applications',
                                                           'duration_minutes': 10,
                                                           'questions': [{'question': 'Which index accesses '
                                                                                      'the first element of '
                                                                                      'a non-empty Java '
                                                                                      'array?',
                                                                          'options': ['−1',
                                                                                      'The array length',
                                                                                      '0',
                                                                                      '1'],
                                                                          'answer': '0',
                                                                          'explanation': 'Java arrays use '
                                                                                         'zero-based '
                                                                                         'indexing.'},
                                                                         {'question': 'Which method should '
                                                                                      'usually compare the '
                                                                                      'contents of two '
                                                                                      'non-null Java String '
                                                                                      'objects?',
                                                                          'options': ['substring()',
                                                                                      'equals()',
                                                                                      'length()',
                                                                                      'charAt()'],
                                                                          'answer': 'equals()',
                                                                          'explanation': 'String.equals '
                                                                                         'compares character '
                                                                                         'content; == '
                                                                                         'compares '
                                                                                         'references.'},
                                                                         {'question': 'What is the main role '
                                                                                      'of a constructor in '
                                                                                      'Java?',
                                                                          'options': ['Initialising a newly '
                                                                                      'created object',
                                                                                      'Always returning an '
                                                                                      'int',
                                                                                      'Deleting the class '
                                                                                      'source file',
                                                                                      'Sorting every array '
                                                                                      'automatically'],
                                                                          'answer': 'Initialising a newly '
                                                                                    'created object',
                                                                          'explanation': 'A constructor runs '
                                                                                         'during object '
                                                                                         'creation and is '
                                                                                         'commonly used to '
                                                                                         'initialise '
                                                                                         'instance state.'}],
                                                           'written_questions': [{'question': 'Write Java '
                                                                                              'code to find '
                                                                                              'the sum of '
                                                                                              'the elements '
                                                                                              'of int[] a = '
                                                                                              '{2, 4, 6};.',
                                                                                  'reference_answer': 'int '
                                                                                                      'sum = '
                                                                                                      '0; '
                                                                                                      'for '
                                                                                                      '(int '
                                                                                                      'value '
                                                                                                      ': a) '
                                                                                                      '{ sum '
                                                                                                      '+= '
                                                                                                      'value; '
                                                                                                      '} '
                                                                                                      'System.out.println(sum); '
                                                                                                      'This '
                                                                                                      'prints '
                                                                                                      '12. '
                                                                                                      'Accept '
                                                                                                      'an '
                                                                                                      'equivalent '
                                                                                                      'indexed '
                                                                                                      'loop.'}]},
 'Class 10 Mathematics — Foundation Practice 1': {'class': 'Class 10',
                                                  'subject': 'Mathematics',
                                                  'duration_minutes': 10,
                                                  'questions': [{'question': 'For an acute angle θ, sin θ = '
                                                                             '3/5. Find cos θ.',
                                                                 'options': ['5/4', '2/5', '4/5', '3/4'],
                                                                 'answer': '4/5',
                                                                 'explanation': 'cos²θ = 1 − 9/25 = 16/25. '
                                                                                'Since θ is acute, cos θ = '
                                                                                '4/5.'},
                                                                {'question': 'Find the determinant of the '
                                                                             'matrix [[2, 1], [3, 4]].',
                                                                 'options': ['−5', '5', '11', '8'],
                                                                 'answer': '5',
                                                                 'explanation': 'For [[a,b],[c,d]], '
                                                                                'determinant = ad − bc = 8 − '
                                                                                '3 = 5.'},
                                                                {'question': 'A fair coin is tossed twice. '
                                                                             'Find the probability of two '
                                                                             'heads.',
                                                                 'options': ['1/4', '1/2', '3/4', '1'],
                                                                 'answer': '1/4',
                                                                 'explanation': 'The equally likely outcomes '
                                                                                'are HH, HT, TH and TT. Only '
                                                                                'HH has two heads.'}],
                                                  'written_questions': [{'question': 'Solve a question from '
                                                                                     'this test again, '
                                                                                     'showing each '
                                                                                     'calculation and '
                                                                                     'checking the result.',
                                                                         'reference_answer': 'Use the '
                                                                                             'corresponding '
                                                                                             'MCQ '
                                                                                             'explanation to '
                                                                                             'check the '
                                                                                             'method. A '
                                                                                             'complete '
                                                                                             'response must '
                                                                                             'show '
                                                                                             'intermediate '
                                                                                             'steps and the '
                                                                                             'final answer '
                                                                                             'with units '
                                                                                             'where '
                                                                                             'relevant.'}]},
 'Class 10 Physics — Foundation Practice 1': {'class': 'Class 10',
                                              'subject': 'Physics',
                                              'duration_minutes': 10,
                                              'questions': [{'question': 'A current of 2 A flows through a 3 '
                                                                         'Ω resistor. Find the potential '
                                                                         'difference.',
                                                             'options': ['5 V', '0.67 V', '6 V', '1.5 V'],
                                                             'answer': '6 V',
                                                             'explanation': 'Using V = IR gives 2 × 3 = 6 '
                                                                            'V.'},
                                                            {'question': 'Which instrument measures electric '
                                                                         'current?',
                                                             'options': ['Thermometer',
                                                                         'Ammeter',
                                                                         'Voltmeter',
                                                                         'Barometer'],
                                                             'answer': 'Ammeter',
                                                             'explanation': 'An ammeter measures current and '
                                                                            'is connected in series with the '
                                                                            'component.'},
                                                            {'question': 'A wave has frequency 5 Hz and '
                                                                         'wavelength 2 m. Find its speed.',
                                                             'options': ['10 m/s',
                                                                         '2.5 m/s',
                                                                         '7 m/s',
                                                                         '3 m/s'],
                                                             'answer': '10 m/s',
                                                             'explanation': 'Wave speed = frequency × '
                                                                            'wavelength = 5 × 2 = 10 m/s.'}],
                                              'written_questions': [{'question': 'Calculate the current '
                                                                                 'through a 6 Ω resistor '
                                                                                 'when the voltage across it '
                                                                                 'is 12 V. Show your '
                                                                                 'working.',
                                                                     'reference_answer': 'I = V/R = 12/6 = 2 '
                                                                                         'A.'}]},
 'Class 10 Chemistry — Foundation Practice 1': {'class': 'Class 10',
                                                'subject': 'Chemistry',
                                                'duration_minutes': 10,
                                                'questions': [{'question': 'What is the atomic number of an '
                                                                           'element equal to?',
                                                               'options': ['Protons plus neutrons',
                                                                           'Number of electron shells',
                                                                           'Number of protons',
                                                                           'Number of neutrons only'],
                                                               'answer': 'Number of protons',
                                                               'explanation': 'Atomic number is the number '
                                                                              'of protons in the nucleus.'},
                                                              {'question': 'What is the chemical formula of '
                                                                           'water?',
                                                               'options': ['NaCl', 'H₂O', 'CO₂', 'O₂'],
                                                               'answer': 'H₂O',
                                                               'explanation': 'Each water molecule contains '
                                                                              'two hydrogen atoms and one '
                                                                              'oxygen atom.'},
                                                              {'question': 'Which process forms an ionic '
                                                                           'bond between sodium and '
                                                                           'chlorine?',
                                                               'options': ['Transfer of an electron from '
                                                                           'sodium to chlorine',
                                                                           'Equal sharing of two protons',
                                                                           'Transfer of a neutron from '
                                                                           'chlorine',
                                                                           'Melting both atoms'],
                                                               'answer': 'Transfer of an electron from '
                                                                         'sodium to chlorine',
                                                               'explanation': 'Electron transfer produces '
                                                                              'oppositely charged ions held '
                                                                              'by electrostatic '
                                                                              'attraction.'}],
                                                'written_questions': [{'question': 'Distinguish an element '
                                                                                   'from a compound and give '
                                                                                   'one example of each.',
                                                                       'reference_answer': 'An element '
                                                                                           'contains one '
                                                                                           'type of atom, '
                                                                                           'such as oxygen. '
                                                                                           'A compound '
                                                                                           'contains '
                                                                                           'different '
                                                                                           'elements '
                                                                                           'chemically '
                                                                                           'combined in a '
                                                                                           'fixed '
                                                                                           'proportion, such '
                                                                                           'as water.'}]},
 'Class 10 Chemistry — Foundation Practice 2': {'class': 'Class 10',
                                                'subject': 'Chemistry',
                                                'duration_minutes': 10,
                                                'questions': [{'question': 'An aqueous solution has pH 3. '
                                                                           'How is it classified?',
                                                               'options': ['Necessarily pure water',
                                                                           'Acidic',
                                                                           'Neutral',
                                                                           'Alkaline'],
                                                               'answer': 'Acidic',
                                                               'explanation': 'At ordinary school reference '
                                                                              'conditions, pH below 7 '
                                                                              'indicates an acidic '
                                                                              'solution.'},
                                                              {'question': 'Which equation is balanced?',
                                                               'options': ['2H₂ + O₂ → 2H₂O',
                                                                           'H₂ + O₂ → H₂O',
                                                                           'H₂ + 2O₂ → H₂O',
                                                                           '2H₂ + O₂ → H₂O'],
                                                               'answer': '2H₂ + O₂ → 2H₂O',
                                                               'explanation': 'The balanced equation has '
                                                                              'four hydrogen atoms and two '
                                                                              'oxygen atoms on each side.'},
                                                              {'question': 'Which method separates an '
                                                                           'insoluble solid from a liquid?',
                                                               'options': ['Magnetism in all cases',
                                                                           'Evaporation of the solid',
                                                                           'Adding more solid',
                                                                           'Filtration'],
                                                               'answer': 'Filtration',
                                                               'explanation': 'A filter can retain insoluble '
                                                                              'solid particles while the '
                                                                              'liquid passes through.'}],
                                                'written_questions': [{'question': 'Explain neutralisation '
                                                                                   'and give a balanced '
                                                                                   'equation using '
                                                                                   'hydrochloric acid and '
                                                                                   'sodium hydroxide.',
                                                                       'reference_answer': 'An acid reacts '
                                                                                           'with a base to '
                                                                                           'form salt and '
                                                                                           'water. HCl + '
                                                                                           'NaOH → NaCl + '
                                                                                           'H₂O.'}]},
 'Class 10 Biology — Foundation Practice 1': {'class': 'Class 10',
                                              'subject': 'Biology',
                                              'duration_minutes': 10,
                                              'questions': [{'question': 'Which cell structure contains most '
                                                                         'of a typical plant or animal '
                                                                         'cell’s genetic material?',
                                                             'options': ['Vacuole only',
                                                                         'Cell membrane only',
                                                                         'Nucleus',
                                                                         'Cell wall'],
                                                             'answer': 'Nucleus',
                                                             'explanation': 'In a typical nucleated plant or '
                                                                            'animal cell, most DNA is in the '
                                                                            'nucleus.'},
                                                            {'question': 'Which pigment absorbs light for '
                                                                         'photosynthesis?',
                                                             'options': ['Keratin',
                                                                         'Chlorophyll',
                                                                         'Haemoglobin',
                                                                         'Melanin'],
                                                             'answer': 'Chlorophyll',
                                                             'explanation': 'Chlorophyll in chloroplasts '
                                                                            'absorbs light energy for '
                                                                            'photosynthesis.'},
                                                            {'question': 'Which plant tissue mainly '
                                                                         'transports water from roots?',
                                                             'options': ['Xylem',
                                                                         'Phloem',
                                                                         'Epidermis only',
                                                                         'Petal tissue'],
                                                             'answer': 'Xylem',
                                                             'explanation': 'Xylem transports water and '
                                                                            'dissolved minerals from the '
                                                                            'roots.'}],
                                              'written_questions': [{'question': 'State two differences '
                                                                                 'between typical plant and '
                                                                                 'animal cells.',
                                                                     'reference_answer': 'Plant cells have a '
                                                                                         'cellulose cell '
                                                                                         'wall and usually a '
                                                                                         'large permanent '
                                                                                         'vacuole. Animal '
                                                                                         'cells lack a cell '
                                                                                         'wall and usually '
                                                                                         'lack a large '
                                                                                         'permanent vacuole. '
                                                                                         'Chloroplasts occur '
                                                                                         'in photosynthetic '
                                                                                         'plant cells.'}]},
 'Class 10 Biology — Foundation Practice 2': {'class': 'Class 10',
                                              'subject': 'Biology',
                                              'duration_minutes': 10,
                                              'questions': [{'question': 'What is transpiration?',
                                                             'options': ['Breakdown of glucose only',
                                                                         'Loss of water vapour from aerial '
                                                                         'parts of plants',
                                                                         'Absorption of food by roots',
                                                                         'Release of seeds only'],
                                                             'answer': 'Loss of water vapour from aerial '
                                                                       'parts of plants',
                                                             'explanation': 'Transpiration is water-vapour '
                                                                            'loss, mainly through stomata in '
                                                                            'leaves.'},
                                                            {'question': 'Which blood cells mainly transport '
                                                                         'oxygen?',
                                                             'options': ['Red blood cells',
                                                                         'Platelets',
                                                                         'White blood cells',
                                                                         'Nerve cells'],
                                                             'answer': 'Red blood cells',
                                                             'explanation': 'Red blood cells contain '
                                                                            'haemoglobin, which binds '
                                                                            'oxygen.'},
                                                            {'question': 'Which organs filter blood and '
                                                                         'produce urine?',
                                                             'options': ['Lungs',
                                                                         'Stomach',
                                                                         'Pancreas',
                                                                         'Kidneys'],
                                                             'answer': 'Kidneys',
                                                             'explanation': 'The kidneys filter blood and '
                                                                            'regulate water and dissolved '
                                                                            'substances while forming '
                                                                            'urine.'}],
                                              'written_questions': [{'question': 'Explain why photosynthesis '
                                                                                 'and respiration are '
                                                                                 'different processes.',
                                                                     'reference_answer': 'Photosynthesis '
                                                                                         'uses light energy '
                                                                                         'to make organic '
                                                                                         'food from carbon '
                                                                                         'dioxide and water, '
                                                                                         'releasing oxygen. '
                                                                                         'Aerobic '
                                                                                         'respiration '
                                                                                         'releases usable '
                                                                                         'energy from '
                                                                                         'organic food using '
                                                                                         'oxygen, producing '
                                                                                         'carbon dioxide and '
                                                                                         'water.'}]},
 'Class 10 English Language — Foundation Practice 1': {'class': 'Class 10',
                                                       'subject': 'English Language',
                                                       'duration_minutes': 10,
                                                       'questions': [{'question': 'Choose the correct '
                                                                                  'sentence.',
                                                                      'options': ['Each of the students are '
                                                                                  'a notebook.',
                                                                                  'Each of the students were '
                                                                                  'a notebook.',
                                                                                  'Each of the students has '
                                                                                  'a notebook.',
                                                                                  'Each of the students have '
                                                                                  'a notebook.'],
                                                                      'answer': 'Each of the students has a '
                                                                                'notebook.',
                                                                      'explanation': 'Each is singular and '
                                                                                     'takes has in this '
                                                                                     'sentence.'},
                                                                     {'question': 'Choose the passive form '
                                                                                  'of: The teacher praised '
                                                                                  'Riya.',
                                                                      'options': ['Riya had praise the '
                                                                                  'teacher.',
                                                                                  'Riya was praised by the '
                                                                                  'teacher.',
                                                                                  'Riya praised the teacher.',
                                                                                  'Riya is praising the '
                                                                                  'teacher.'],
                                                                      'answer': 'Riya was praised by the '
                                                                                'teacher.',
                                                                      'explanation': 'The simple-past '
                                                                                     'passive uses was/were '
                                                                                     '+ past participle.'},
                                                                     {'question': 'Choose the correct '
                                                                                  'preposition: She has '
                                                                                  'lived here ___ 2020.',
                                                                      'options': ['since',
                                                                                  'for',
                                                                                  'during to',
                                                                                  'from since'],
                                                                      'answer': 'since',
                                                                      'explanation': 'Since introduces the '
                                                                                     'starting point of a '
                                                                                     'continuing period.'}],
                                                       'written_questions': [{'question': 'Write a short '
                                                                                          'formal request to '
                                                                                          'your principal '
                                                                                          'for permission to '
                                                                                          'start a reading '
                                                                                          'club. Include '
                                                                                          'purpose and a '
                                                                                          'proposed meeting '
                                                                                          'time.',
                                                                              'reference_answer': 'Example: '
                                                                                                  'Dear '
                                                                                                  'Principal, '
                                                                                                  'I request '
                                                                                                  'permission '
                                                                                                  'to start '
                                                                                                  'a reading '
                                                                                                  'club to '
                                                                                                  'encourage '
                                                                                                  'regular '
                                                                                                  'reading. '
                                                                                                  'We '
                                                                                                  'propose '
                                                                                                  'meeting '
                                                                                                  'on '
                                                                                                  'Fridays '
                                                                                                  'after '
                                                                                                  'school '
                                                                                                  'under a '
                                                                                                  'teacher’s '
                                                                                                  'supervision. '
                                                                                                  'Kindly '
                                                                                                  'consider '
                                                                                                  'our '
                                                                                                  'request. '
                                                                                                  'Yours '
                                                                                                  'faithfully, '
                                                                                                  '[Student '
                                                                                                  'name]. '
                                                                                                  'Accept '
                                                                                                  'other '
                                                                                                  'suitable '
                                                                                                  'formats '
                                                                                                  'and '
                                                                                                  'clear, '
                                                                                                  'polite '
                                                                                                  'wording.'}]},
 'Class 10 English Language — Foundation Practice 2': {'class': 'Class 10',
                                                       'subject': 'English Language',
                                                       'duration_minutes': 10,
                                                       'questions': [{'question': 'Choose the correct '
                                                                                  'reported form: He said, '
                                                                                  '“I am tired.”',
                                                                      'options': ['He said that he is tire.',
                                                                                  'He said that he was '
                                                                                  'tired.',
                                                                                  'He said that I am tired.',
                                                                                  'He says that he tired.'],
                                                                      'answer': 'He said that he was tired.',
                                                                      'explanation': 'In this ordinary '
                                                                                     'past-reporting '
                                                                                     'context, I changes to '
                                                                                     'he and am to was.'},
                                                                     {'question': 'Which sentence correctly '
                                                                                  'uses an apostrophe for '
                                                                                  'one girl’s bag?',
                                                                      'options': ['The girl’s bag is blue.',
                                                                                  'The girls bag is blue.',
                                                                                  'The girls’ bag is blue.',
                                                                                  'The girl bag’s is blue.'],
                                                                      'answer': 'The girl’s bag is blue.',
                                                                      'explanation': 'For a single girl, '
                                                                                     'possession is shown '
                                                                                     'with girl’s.'},
                                                                     {'question': 'Which is the best opening '
                                                                                  'for a formal request to a '
                                                                                  'principal?',
                                                                      'options': ['Hey, give us a club!',
                                                                                  'Whatever, we need this.',
                                                                                  'You must say yes now.',
                                                                                  'I am writing to request '
                                                                                  'permission to organise a '
                                                                                  'reading club.'],
                                                                      'answer': 'I am writing to request '
                                                                                'permission to organise a '
                                                                                'reading club.',
                                                                      'explanation': 'A formal request '
                                                                                     'should state its '
                                                                                     'purpose politely and '
                                                                                     'clearly.'}],
                                                       'written_questions': [{'question': 'Combine without '
                                                                                          'changing meaning: '
                                                                                          'Although it was '
                                                                                          'raining, the '
                                                                                          'players continued '
                                                                                          'the match. Begin '
                                                                                          'with “Despite”.',
                                                                              'reference_answer': 'Despite '
                                                                                                  'the rain, '
                                                                                                  'the '
                                                                                                  'players '
                                                                                                  'continued '
                                                                                                  'the '
                                                                                                  'match. '
                                                                                                  'Also '
                                                                                                  'accept: '
                                                                                                  'Despite '
                                                                                                  'the fact '
                                                                                                  'that it '
                                                                                                  'was '
                                                                                                  'raining, '
                                                                                                  'the '
                                                                                                  'players '
                                                                                                  'continued '
                                                                                                  'the '
                                                                                                  'match.'}]},
 'Class 10 English Literature — Foundation Practice 1': {'class': 'Class 10',
                                                         'subject': 'English Literature',
                                                         'duration_minutes': 10,
                                                         'questions': [{'question': 'Original passage: “Mira '
                                                                                    'waited by the gate. '
                                                                                    'When her brother '
                                                                                    'arrived, her shoulders '
                                                                                    'relaxed.” What does her '
                                                                                    'reaction suggest?',
                                                                        'options': ['She wanted to run a '
                                                                                    'race',
                                                                                    'She disliked the gate',
                                                                                    'She had been worried',
                                                                                    'She had forgotten him'],
                                                                        'answer': 'She had been worried',
                                                                        'explanation': 'Her relaxation after '
                                                                                       'his arrival suggests '
                                                                                       'earlier tension or '
                                                                                       'worry.'},
                                                                       {'question': 'Which phrase is a '
                                                                                    'simile?',
                                                                        'options': ['The clock ticked',
                                                                                    'As quiet as a mouse',
                                                                                    'The wind whispered',
                                                                                    'Time is a thief'],
                                                                        'answer': 'As quiet as a mouse',
                                                                        'explanation': 'A simile makes an '
                                                                                       'explicit comparison, '
                                                                                       'often using like or '
                                                                                       'as.'},
                                                                       {'question': 'What is the narrator of '
                                                                                    'a story?',
                                                                        'options': ['The voice that tells '
                                                                                    'the story',
                                                                                    'Always the author in '
                                                                                    'real life',
                                                                                    'Only the main villain',
                                                                                    'The person who prints '
                                                                                    'the book'],
                                                                        'answer': 'The voice that tells the '
                                                                                  'story',
                                                                        'explanation': 'The narrator is the '
                                                                                       'voice presenting the '
                                                                                       'story and need not '
                                                                                       'be identical to the '
                                                                                       'author.'}],
                                                         'written_questions': [{'question': 'Original '
                                                                                            'passage: “Mira '
                                                                                            'waited by the '
                                                                                            'gate. When her '
                                                                                            'brother '
                                                                                            'arrived, her '
                                                                                            'shoulders '
                                                                                            'relaxed.” Infer '
                                                                                            'Mira’s feelings '
                                                                                            'before and '
                                                                                            'after his '
                                                                                            'arrival. Use '
                                                                                            'evidence.',
                                                                                'reference_answer': 'Before '
                                                                                                    'his '
                                                                                                    'arrival, '
                                                                                                    'Mira '
                                                                                                    'appears '
                                                                                                    'worried '
                                                                                                    'or '
                                                                                                    'tense; '
                                                                                                    'waiting '
                                                                                                    'and the '
                                                                                                    'later '
                                                                                                    'relaxation '
                                                                                                    'support '
                                                                                                    'this '
                                                                                                    'inference. '
                                                                                                    'Afterwards '
                                                                                                    'she '
                                                                                                    'feels '
                                                                                                    'relieved, '
                                                                                                    'shown '
                                                                                                    'by her '
                                                                                                    'shoulders '
                                                                                                    'relaxing. '
                                                                                                    'Accept '
                                                                                                    'another '
                                                                                                    'reasonable '
                                                                                                    'interpretation '
                                                                                                    'supported '
                                                                                                    'by the '
                                                                                                    'text.'}]},
 'Class 10 English Literature — Foundation Practice 2': {'class': 'Class 10',
                                                         'subject': 'English Literature',
                                                         'duration_minutes': 10,
                                                         'questions': [{'question': 'Original line: “The '
                                                                                    'tired street slept '
                                                                                    'under the moon.” Which '
                                                                                    'device gives the street '
                                                                                    'a human action?',
                                                                        'options': ['An instruction',
                                                                                    'Personification',
                                                                                    'A factual measurement',
                                                                                    'A direct question'],
                                                                        'answer': 'Personification',
                                                                        'explanation': 'Describing the '
                                                                                       'street as sleeping '
                                                                                       'gives a non-human '
                                                                                       'thing a human '
                                                                                       'action.'},
                                                                       {'question': 'What is a theme in a '
                                                                                    'literary work?',
                                                                        'options': ['An underlying idea '
                                                                                    'explored by the work',
                                                                                    'Only the page number',
                                                                                    'Always the title alone',
                                                                                    'The publisher’s '
                                                                                    'address'],
                                                                        'answer': 'An underlying idea '
                                                                                  'explored by the work',
                                                                        'explanation': 'A theme is an idea '
                                                                                       'or concern developed '
                                                                                       'through characters, '
                                                                                       'events or language.'},
                                                                       {'question': 'Original passage: “Arun '
                                                                                    'returned the lost purse '
                                                                                    'though nobody was '
                                                                                    'watching.” Which trait '
                                                                                    'is most directly shown?',
                                                                        'options': ['Jealousy',
                                                                                    'Impatience',
                                                                                    'Cruelty',
                                                                                    'Honesty'],
                                                                        'answer': 'Honesty',
                                                                        'explanation': 'Returning the purse '
                                                                                       'without an audience '
                                                                                       'demonstrates '
                                                                                       'honesty.'}],
                                                         'written_questions': [{'question': 'Explain the '
                                                                                            'personification '
                                                                                            'in the original '
                                                                                            'line “The tired '
                                                                                            'street slept '
                                                                                            'under the '
                                                                                            'moon.” What '
                                                                                            'mood might it '
                                                                                            'create?',
                                                                                'reference_answer': 'The '
                                                                                                    'street '
                                                                                                    'is '
                                                                                                    'described '
                                                                                                    'as '
                                                                                                    'tired '
                                                                                                    'and '
                                                                                                    'sleeping, '
                                                                                                    'which '
                                                                                                    'are '
                                                                                                    'human '
                                                                                                    'states/actions. '
                                                                                                    'This '
                                                                                                    'can '
                                                                                                    'suggest '
                                                                                                    'a '
                                                                                                    'quiet, '
                                                                                                    'still '
                                                                                                    'or '
                                                                                                    'peaceful '
                                                                                                    'night. '
                                                                                                    'Accept '
                                                                                                    'a '
                                                                                                    'supported '
                                                                                                    'alternative '
                                                                                                    'such as '
                                                                                                    'loneliness.'}]},
 'Class 10 History & Civics — Foundation Practice 1': {'class': 'Class 10',
                                                       'subject': 'History & Civics',
                                                       'duration_minutes': 10,
                                                       'questions': [{'question': 'Which is a primary source '
                                                                                  'for studying an ancient '
                                                                                  'civilisation?',
                                                                      'options': ['A future prediction',
                                                                                  'An invented diary written '
                                                                                  'today',
                                                                                  'An inscription made '
                                                                                  'during that period',
                                                                                  'A modern fictional film'],
                                                                      'answer': 'An inscription made during '
                                                                                'that period',
                                                                      'explanation': 'An inscription created '
                                                                                     'in the period provides '
                                                                                     'contemporary '
                                                                                     'evidence.'},
                                                                     {'question': 'Which feature is '
                                                                                  'associated with many '
                                                                                  'Harappan cities?',
                                                                      'options': ['Printed newspapers',
                                                                                  'Planned streets and '
                                                                                  'drainage',
                                                                                  'Electric railways',
                                                                                  'Modern airports'],
                                                                      'answer': 'Planned streets and '
                                                                                'drainage',
                                                                      'explanation': 'Archaeological remains '
                                                                                     'show planned streets '
                                                                                     'and drainage in major '
                                                                                     'Harappan settlements.'},
                                                                     {'question': 'What is a constitution?',
                                                                      'options': ['A framework of basic '
                                                                                  'principles and rules for '
                                                                                  'government',
                                                                                  'Only a weather report',
                                                                                  'A private shopping list',
                                                                                  'Only a school timetable'],
                                                                      'answer': 'A framework of basic '
                                                                                'principles and rules for '
                                                                                'government',
                                                                      'explanation': 'A constitution sets '
                                                                                     'out fundamental '
                                                                                     'institutions, powers '
                                                                                     'and governing '
                                                                                     'principles.'}],
                                                       'written_questions': [{'question': 'Explain why '
                                                                                          'historians '
                                                                                          'compare different '
                                                                                          'sources instead '
                                                                                          'of relying on one '
                                                                                          'account.',
                                                                              'reference_answer': 'Sources '
                                                                                                  'may be '
                                                                                                  'incomplete, '
                                                                                                  'biased or '
                                                                                                  'mistaken. '
                                                                                                  'Comparing '
                                                                                                  'independent '
                                                                                                  'evidence '
                                                                                                  'helps '
                                                                                                  'identify '
                                                                                                  'agreement, '
                                                                                                  'contradictions '
                                                                                                  'and a '
                                                                                                  'better-supported '
                                                                                                  'account.'}]},
 'Class 10 History & Civics — Foundation Practice 2': {'class': 'Class 10',
                                                       'subject': 'History & Civics',
                                                       'duration_minutes': 10,
                                                       'questions': [{'question': 'Which institution makes '
                                                                                  'laws at the Union level '
                                                                                  'in India?',
                                                                      'options': ['A sports club',
                                                                                  'Parliament',
                                                                                  'A village school',
                                                                                  'A private company'],
                                                                      'answer': 'Parliament',
                                                                      'explanation': 'The Union legislature '
                                                                                     'is Parliament.'},
                                                                     {'question': 'Which movement was '
                                                                                  'launched in India in '
                                                                                  '1942?',
                                                                      'options': ['Quit India Movement',
                                                                                  'Non-Cooperation Movement',
                                                                                  'Swadeshi Movement of 1905',
                                                                                  'Civil Disobedience '
                                                                                  'Movement of 1930'],
                                                                      'answer': 'Quit India Movement',
                                                                      'explanation': 'The Quit India '
                                                                                     'Movement was launched '
                                                                                     'in August 1942.'},
                                                                     {'question': 'Which is a central '
                                                                                  'purpose of the United '
                                                                                  'Nations?',
                                                                      'options': ['Running every country’s '
                                                                                  'schools directly',
                                                                                  'Replacing all national '
                                                                                  'governments',
                                                                                  'Setting every shop’s '
                                                                                  'prices',
                                                                                  'Maintaining international '
                                                                                  'peace and security'],
                                                                      'answer': 'Maintaining international '
                                                                                'peace and security',
                                                                      'explanation': 'Maintaining '
                                                                                     'international peace '
                                                                                     'and security is a '
                                                                                     'central UN purpose.'}],
                                                       'written_questions': [{'question': 'Explain the roles '
                                                                                          'of the '
                                                                                          'legislature and '
                                                                                          'judiciary in a '
                                                                                          'democracy.',
                                                                              'reference_answer': 'The '
                                                                                                  'legislature '
                                                                                                  'debates '
                                                                                                  'and makes '
                                                                                                  'laws. The '
                                                                                                  'judiciary '
                                                                                                  'interprets '
                                                                                                  'laws and '
                                                                                                  'resolves '
                                                                                                  'legal '
                                                                                                  'disputes; '
                                                                                                  'it also '
                                                                                                  'exercises '
                                                                                                  'its '
                                                                                                  'constitutional '
                                                                                                  'powers to '
                                                                                                  'protect '
                                                                                                  'rights '
                                                                                                  'and '
                                                                                                  'review '
                                                                                                  'government '
                                                                                                  'action.'}]},
 'Class 10 Geography — Foundation Practice 1': {'class': 'Class 10',
                                                'subject': 'Geography',
                                                'duration_minutes': 10,
                                                'questions': [{'question': 'What does latitude measure?',
                                                               'options': ['Distance east of a town in '
                                                                           'metres',
                                                                           'Depth of the ocean',
                                                                           'Angular distance north or south '
                                                                           'of the Equator',
                                                                           'Height above sea level only'],
                                                               'answer': 'Angular distance north or south of '
                                                                         'the Equator',
                                                               'explanation': 'Latitude is angular distance '
                                                                              'north or south of the '
                                                                              'Equator, measured in '
                                                                              'degrees.'},
                                                              {'question': 'Which layer lies directly below '
                                                                           'Earth’s crust?',
                                                               'options': ['Hydrosphere',
                                                                           'Mantle',
                                                                           'Inner core',
                                                                           'Atmosphere'],
                                                               'answer': 'Mantle',
                                                               'explanation': 'The mantle lies beneath the '
                                                                              'crust.'},
                                                              {'question': 'What is weathering?',
                                                               'options': ['Breakdown of rock at or near '
                                                                           'Earth’s surface',
                                                                           'Only transport of rock by rivers',
                                                                           'Formation of stars',
                                                                           'Rotation of Earth'],
                                                               'answer': 'Breakdown of rock at or near '
                                                                         'Earth’s surface',
                                                               'explanation': 'Weathering breaks down rock '
                                                                              'in place; transport is '
                                                                              'associated with erosion.'}],
                                                'written_questions': [{'question': 'Distinguish weather from '
                                                                                   'climate.',
                                                                       'reference_answer': 'Weather '
                                                                                           'describes '
                                                                                           'short-term '
                                                                                           'atmospheric '
                                                                                           'conditions at a '
                                                                                           'place. Climate '
                                                                                           'describes '
                                                                                           'long-term '
                                                                                           'patterns and '
                                                                                           'averages of '
                                                                                           'weather over '
                                                                                           'many years.'}]},
 'Class 10 Geography — Foundation Practice 2': {'class': 'Class 10',
                                                'subject': 'Geography',
                                                'duration_minutes': 10,
                                                'questions': [{'question': 'On a 1:50,000 map, what ground '
                                                                           'distance does 1 cm represent?',
                                                               'options': ['50 km', '500 m', '50 m', '5 km'],
                                                               'answer': '500 m',
                                                               'explanation': '1 cm represents 50,000 cm = '
                                                                              '500 m.'},
                                                              {'question': 'Which soil type is widely '
                                                                           'associated with the northern '
                                                                           'river plains of India?',
                                                               'options': ['Alluvial soil',
                                                                           'Only laterite soil',
                                                                           'Only mountain soil',
                                                                           'Only desert soil'],
                                                               'answer': 'Alluvial soil',
                                                               'explanation': 'Rivers deposit alluvium '
                                                                              'across much of the northern '
                                                                              'plains.'},
                                                              {'question': 'Which is a renewable energy '
                                                                           'source?',
                                                               'options': ['Coal',
                                                                           'Petroleum',
                                                                           'Natural gas',
                                                                           'Solar energy'],
                                                               'answer': 'Solar energy',
                                                               'explanation': 'Sunlight is naturally '
                                                                              'replenished; fossil fuels '
                                                                              'form over much longer '
                                                                              'timescales.'}],
                                                'written_questions': [{'question': 'A map has a scale of '
                                                                                   '1:50,000. Two places are '
                                                                                   '6 cm apart on it. '
                                                                                   'Calculate their '
                                                                                   'straight-line ground '
                                                                                   'distance.',
                                                                       'reference_answer': 'Ground distance '
                                                                                           '= 6 × 50,000 = '
                                                                                           '300,000 cm = '
                                                                                           '3,000 m = 3 '
                                                                                           'km.'}]},
 'Class 10 Computer Applications — Foundation Practice 1': {'class': 'Class 10',
                                                            'subject': 'Computer Applications',
                                                            'duration_minutes': 10,
                                                            'questions': [{'question': 'Which Java type '
                                                                                       'stores either true '
                                                                                       'or false?',
                                                                           'options': ['double',
                                                                                       'char',
                                                                                       'boolean',
                                                                                       'int'],
                                                                           'answer': 'boolean',
                                                                           'explanation': 'The boolean '
                                                                                          'primitive type '
                                                                                          'has the values '
                                                                                          'true and false.'},
                                                                          {'question': 'What is the value of '
                                                                                       '7 / 2 when both '
                                                                                       'operands are Java '
                                                                                       'int values?',
                                                                           'options': ['2', '3', '3.5', '4'],
                                                                           'answer': '3',
                                                                           'explanation': 'Integer division '
                                                                                          'truncates the '
                                                                                          'fractional part; '
                                                                                          '7 / 2 is 3.'},
                                                                          {'question': 'Which Java operator '
                                                                                       'tests equality of '
                                                                                       'two int values?',
                                                                           'options': ['==', '=', '!=', '+='],
                                                                           'answer': '==',
                                                                           'explanation': 'The == operator '
                                                                                          'compares '
                                                                                          'primitive values; '
                                                                                          '= assigns a '
                                                                                          'value.'}],
                                                            'written_questions': [{'question': 'Evaluate '
                                                                                               'this Java '
                                                                                               'code and '
                                                                                               'explain the '
                                                                                               'result: int '
                                                                                               'x = 5; x += '
                                                                                               '3; '
                                                                                               'System.out.println(x);',
                                                                                   'reference_answer': 'It '
                                                                                                       'prints '
                                                                                                       '8. '
                                                                                                       'The '
                                                                                                       'compound '
                                                                                                       'assignment '
                                                                                                       'adds '
                                                                                                       '3 to '
                                                                                                       'the '
                                                                                                       'existing '
                                                                                                       'value '
                                                                                                       '5 '
                                                                                                       'and '
                                                                                                       'stores '
                                                                                                       'the '
                                                                                                       'result '
                                                                                                       'in '
                                                                                                       'x.'}]},
 'Class 10 Computer Applications — Foundation Practice 2': {'class': 'Class 10',
                                                            'subject': 'Computer Applications',
                                                            'duration_minutes': 10,
                                                            'questions': [{'question': 'Which index accesses '
                                                                                       'the first element of '
                                                                                       'a non-empty Java '
                                                                                       'array?',
                                                                           'options': ['The array length',
                                                                                       '0',
                                                                                       '1',
                                                                                       '−1'],
                                                                           'answer': '0',
                                                                           'explanation': 'Java arrays use '
                                                                                          'zero-based '
                                                                                          'indexing.'},
                                                                          {'question': 'Which method should '
                                                                                       'usually compare the '
                                                                                       'contents of two '
                                                                                       'non-null Java String '
                                                                                       'objects?',
                                                                           'options': ['equals()',
                                                                                       'length()',
                                                                                       'charAt()',
                                                                                       'substring()'],
                                                                           'answer': 'equals()',
                                                                           'explanation': 'String.equals '
                                                                                          'compares '
                                                                                          'character '
                                                                                          'content; == '
                                                                                          'compares '
                                                                                          'references.'},
                                                                          {'question': 'What is the main '
                                                                                       'role of a '
                                                                                       'constructor in Java?',
                                                                           'options': ['Always returning an '
                                                                                       'int',
                                                                                       'Deleting the class '
                                                                                       'source file',
                                                                                       'Sorting every array '
                                                                                       'automatically',
                                                                                       'Initialising a newly '
                                                                                       'created object'],
                                                                           'answer': 'Initialising a newly '
                                                                                     'created object',
                                                                           'explanation': 'A constructor '
                                                                                          'runs during '
                                                                                          'object creation '
                                                                                          'and is commonly '
                                                                                          'used to '
                                                                                          'initialise '
                                                                                          'instance state.'}],
                                                            'written_questions': [{'question': 'Write Java '
                                                                                               'code to find '
                                                                                               'the sum of '
                                                                                               'the elements '
                                                                                               'of int[] a = '
                                                                                               '{2, 4, 6};.',
                                                                                   'reference_answer': 'int '
                                                                                                       'sum '
                                                                                                       '= 0; '
                                                                                                       'for '
                                                                                                       '(int '
                                                                                                       'value '
                                                                                                       ': a) '
                                                                                                       '{ '
                                                                                                       'sum '
                                                                                                       '+= '
                                                                                                       'value; '
                                                                                                       '} '
                                                                                                       'System.out.println(sum); '
                                                                                                       'This '
                                                                                                       'prints '
                                                                                                       '12. '
                                                                                                       'Accept '
                                                                                                       'an '
                                                                                                       'equivalent '
                                                                                                       'indexed '
                                                                                                       'loop.'}]}}
