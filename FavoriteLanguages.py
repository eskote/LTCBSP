# FavoriteLanguages

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

poll_users = [
    'bryan',
    'sam',
    'rachel',
    'thomas',
    'phil',
    'ken',
    'dallas',
    'sarah'
]

for poll_user in poll_users:
    for language_user in favorite_languages:
        if poll_user in language_user:
            print(f"User {poll_user} has already taken the poll!")

language = favorite_languages['sarah'].title()

print(f"Sarah's favorite language is {language}!")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print(f"Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

bryan = {
    'car': 'Porsche',
    'OS': 'Debian',
    'food': 'ramen',
    'city': 'Oklahoma City'
}

print(f"Bryan's favorite car is {bryan['car']}")
print(f"Bryan's favorite OS is {bryan['OS']}")
print(f"Bryan's favorite food is {bryan['food']}")
print(f"Bryan's favorite city is {bryan['city']}")

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': 'c',
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
