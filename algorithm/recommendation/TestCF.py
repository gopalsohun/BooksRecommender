from algorithm.recommendation.CF import CF


reviews = {
    'Aisha': {'Harry Potter': 2.5, 'Charmed': 3.5, 'Twilight': 3.0, 'Spartan': 3.5, 'Data Mining': 2.5, 'Database Design': 3.0},
    'Gopal': {'Harry Potter': 3.0, 'Charmed': 3.5, 'Spartan': 5.0, 'Database Design': 3.0, 'Data Mining': 3.5},
    'Nilesh': {'Harry Potter': 2.5, 'Charmed': 3.0, 'Spartan': 3.5, 'Database Design': 4.0},
    'Taahir': {'Charmed': 3.5, 'Twilight': 3.0, 'Database Design': 4.5, 'Spartan': 4.0, 'Data Mining': 2.5},
    'Shweta': {'Harry Potter': 3.0, 'Charmed': 4.0, 'Twilight': 2.0, 'Spartan': 3.0, 'Database Design': 3.0, 'Data Mining': 2.0},
    'Kevish': {'Harry Potter': 3.0, 'Charmed': 4.0, 'Database Design': 3.0, 'Spartan': 5.0, 'Data Mining': 3.5},
    'Anubhav': {'Charmed': 4.5, 'Spartan': 4.0}
}

bx_recommender = CF(reviews)
bx_recommender.openDataset('/Users/Gopal/Downloads/Dataset/')
print(bx_recommender.getRecommendation('171118'))