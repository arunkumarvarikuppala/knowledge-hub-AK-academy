# syllabus_data.py
# Knowledge Hub - Additional ICSE syllabus content
#
# IMPORTANT:
# These are starter chapter lists, not a complete official syllabus.
# Verify each chapter against the applicable CISCE syllabus before
# marking it as officially confirmed.


def make_chapter(chapter_name, subject, class_name):
    """Create a starter lesson for a chapter."""

    return {
        "notes": f"""
### {chapter_name}

**Class:** {class_name}

**Subject:** {subject}

**Learning guide**

This chapter has been added to the Knowledge Hub learning catalogue.

1. Read the chapter from your school-prescribed textbook.
2. Write down the important definitions and concepts.
3. Prepare short notes in your own words.
4. Ask the Knowledge Hub AI Tutor to explain difficult concepts.
5. Practise questions given by your teacher.

**Important:** These are starter learning instructions, not verified
chapter-specific notes. The teacher should add and verify the actual
lesson content against the applicable CISCE syllabus.
""",
        "questions": [
            f"Write the important definitions from {chapter_name}.",
            f"Explain the main concepts of {chapter_name}.",
            f"Write a short note on {chapter_name}.",
            f"Give an example related to {chapter_name}.",
            f"Prepare one question about {chapter_name} and answer it.",
        ],
    }


# Additional subject and chapter catalogue.
# Existing detailed lessons in app.py will be preserved when merged.

CHAPTER_CATALOGUE = {
    "Class 9": {
        "Mathematics": [
            "Rational and Irrational Numbers",
            "Compound Interest",
            "Expansions",
            "Factorisation",
            "Coordinate Geometry",
            "Geometry",
            "Triangles",
            "Quadrilaterals",
            "Circles",
            "Statistics",
            "Probability",
        ],
        "Physics": [
            "Measurements and Experimentation",
            "Motion in One Dimension",
            "Laws of Motion",
            "Pressure in Fluids",
            "Upthrust in Fluids",
            "Heat",
            "Reflection of Light",
            "Sound",
            "Electricity and Magnetism",
        ],
        "Chemistry": [
            "The Language of Chemistry",
            "Chemical Changes and Reactions",
            "Water",
            "Atomic Structure and Chemical Bonding",
            "The Periodic Table",
            "Study of Gas Laws",
            "Atmospheric Pollution",
        ],
        "Biology": [
            "The Cell",
            "Tissues",
            "The Flower",
            "Pollination and Fertilisation",
            "Seeds: Structure and Germination",
            "Respiration in Plants",
            "Digestive System",
            "Skeleton: Movement and Locomotion",
            "Skin",
            "The Respiratory System",
            "Health and Hygiene",
        ],
        "English Language": [
            "Composition Writing",
            "Letter Writing",
            "Notice and Email Writing",
            "Comprehension",
            "Grammar",
            "Summary Writing",
        ],
        "English Literature": [
            "Julius Caesar: Acts I and II",
            "Bonku Babu's Friend",
            "Oliver Asks for More",
            "The Model Millionaire",
            "The Home-coming",
            "The Boy Who Broke the Bank",
            "The Night Mail",
            "Skimbleshanks: The Railway Cat",
            "I Remember, I Remember",
            "A Doctor's Journal Entry for August 6, 1945",
            "A Work of Artifice",
        ],
        "History & Civics": [
            "The Harappan Civilisation",
            "The Vedic Period",
            "Jainism and Buddhism",
            "The Mauryan Empire",
            "The Sangam Age",
            "The Gupta Empire",
            "The Constitution",
            "Elections",
            "Local Self-Government",
        ],
        "Geography": [
            "Our World",
            "Structure of the Earth",
            "Landforms of the Earth",
            "Hydrosphere",
            "Atmosphere",
            "Weathering",
            "Natural Regions of the World",
            "Map Work",
        ],
        "Computer Applications": [
            "Introduction to Computers",
            "Introduction to Java",
            "Objects and Classes",
            "Values and Data Types",
            "Operators in Java",
            "Input in Java",
            "Mathematical Library Methods",
            "Conditional Constructs",
            "Iterative Constructs",
            "Nested Loops",
        ],
    },
    "Class 10": {
        "Mathematics": [
            "Goods and Services Tax",
            "Banking",
            "Shares and Dividends",
            "Linear Inequations",
            "Quadratic Equations",
            "Ratio and Proportion",
            "Remainder and Factor Theorems",
            "Matrices",
            "Arithmetic Progressions",
            "Coordinate Geometry",
            "Similarity",
            "Loci",
            "Circles",
            "Tangents and Intersecting Chords",
            "Constructions",
            "Trigonometry",
            "Heights and Distances",
            "Mensuration",
            "Statistics",
            "Probability",
        ],
        "Physics": [
            "Force",
            "Work, Energy and Power",
            "Machines",
            "Refraction of Light at Plane Surfaces",
            "Refraction Through a Lens",
            "Spectrum",
            "Sound",
            "Current Electricity",
            "Household Circuits",
            "Electromagnetism",
            "Calorimetry",
            "Radioactivity",
        ],
        "Chemistry": [
            "Periodic Properties",
            "Chemical Bonding",
            "Acids, Bases and Salts",
            "Analytical Chemistry",
            "Mole Concept and Stoichiometry",
            "Electrolysis",
            "Metallurgy",
            "Study of Compounds",
            "Organic Chemistry",
        ],
        "Biology": [
            "Cell Cycle and Cell Division",
            "Genetics",
            "Absorption by Roots",
            "Transpiration",
            "Photosynthesis",
            "Chemical Coordination in Plants",
            "The Circulatory System",
            "The Excretory System",
            "The Nervous System",
            "Sense Organs",
            "The Endocrine System",
            "The Reproductive System",
            "Population",
            "Pollution",
        ],
        "English Language": [
            "Composition Writing",
            "Formal and Informal Letter Writing",
            "Notice and Email Writing",
            "Comprehension",
            "Grammar",
            "Summary Writing",
        ],
        "English Literature": [
            "Julius Caesar: Acts III, IV and V",
            "With the Photographer",
            "The Elevator",
            "The Girl Who Can",
            "The Pedestrian",
            "The Last Lesson",
            "Haunted Houses",
            "The Glove and the Lions",
            "When Great Trees Fall",
            "A Considerable Speck",
            "The Power of Music",
        ],
        "History & Civics": [
            "The Union Legislature",
            "The Union Executive",
            "The Judiciary",
            "The First War of Independence",
            "Growth of Nationalism",
            "The Muslim League",
            "The Quit India Movement",
            "The INA",
            "The United Nations",
            "Major Agencies of the United Nations",
            "Non-Aligned Movement",
        ],
        "Geography": [
            "Interpretation of Topographical Maps",
            "Map of India",
            "Climate",
            "Soils in India",
            "Natural Vegetation",
            "Water Resources",
            "Mineral and Energy Resources",
            "Agriculture",
            "Industries",
            "Transport",
            "Waste Management",
        ],
        "Computer Applications": [
            "Revision of Java Fundamentals",
            "Class as the Basis of All Computation",
            "User-Defined Methods",
            "Constructors",
            "Library Classes",
            "Encapsulation",
            "Arrays",
            "String Handling",
            "Algorithm Development",
            "Searching and Sorting",
        ],
    },
}


EXTRA_SYLLABUS = {
    class_name: {
        subject: {
            chapter_name: make_chapter(
                chapter_name,
                subject,
                class_name,
            )
            for chapter_name in chapters
        }
        for subject, chapters in subjects.items()
    }
    for class_name, subjects in CHAPTER_CATALOGUE.items()
}