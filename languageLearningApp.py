import random
words = [
    {"Deutsch": "Ich", "English": "I"},
    {"Deutsch": "Du", "English": "You"},
    {"Deutsch": "Er", "English": "He"},
    {"Deutsch": "Sie", "English": "She"},
    {"Deutsch": "Es", "English": "It"},
    {"Deutsch": "Wir", "English": "We"},
    {"Deutsch": "Ihr", "English": "You"},
    {"Deutsch": "Mussen", "English": "Must"},
    {"Deutsch": "Hallo", "English": "Hello"},
    {"Deutsch": "Guten Morgen", "English": "Good morning"},
    {"Deutsch": "Danke", "English": "Thank you"},
    {"Deutsch": "Bitte", "English": "Please / You're welcome"},
    {"Deutsch": "Ja", "English": "Yes"},
    {"Deutsch": "Nein", "English": "No"},
    {"Deutsch": "Vielleicht", "English": "Maybe"},
    {"Deutsch": "Entschuldigung", "English": "Excuse me"},
    {"Deutsch": "Wo", "English": "Where"},
    {"Deutsch": "Wann", "English": "When"},
    {"Deutsch": "Warum", "English": "Why"},
    {"Deutsch": "Wie", "English": "How"},
    {"Deutsch": "Was", "English": "What"},
    {"Deutsch": "Essen", "English": "Food"},
    {"Deutsch": "Trinken", "English": "Drink"},
    {"Deutsch": "Lernen", "English": "Learn"},
    {"Deutsch": "Arbeiten", "English": "Work"},
    {"Deutsch": "Schlafen", "English": "Sleep"},
    {"Deutsch": "Lesen", "English": "Read"},
    {"Deutsch": "Schreiben", "English": "Write"},
    {"Deutsch": "Sprechen", "English": "Speak"},
    {"Deutsch": "Sehen", "English": "See"}
]




def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['Deutsch']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['English'].lower()

        if user_answer == correct_answer:
            print("Correct!!\n!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is '{word['English']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")       




def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)


if __name__=="__main__":
    main()

