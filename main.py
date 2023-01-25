
questions = ("Qual a cor do céu? ",
             "Qual a cor da grama? ",
             "Qual o formato da bola? ",
             "Como é o nome do bom velhinho do natal? ",
             "Qual a cor do oceano? ",
             "Quantos litros de sangue um ser humano normalmente possui? ",
             "Quanto tempo a luz do Sol demora para chegar à Terra?",
             "Quais os planetas do sistema solar?",
             "Que substância é absorvida pelas plantas e expirada por todos os seres vivos?",
             "Quem foi eleito o primeiro presidente do Brasil?")

options = (("A. amarelo", "B. preto", "C. azul", "D. magenta", "E. rosa"),
           ("A. amarela", "B. verde", "C. azul", "D. magenta", "E. rosa"),
           ("A. quadrada", "B. retangular", "C. hexagonal", "D. redonda", "E. triangular"),
           ("A. papai noel", "B. fada madrinnha", "C. coelho da páscoa", "D. duende", "E. São João"),
           ("A. amarelo", "B. preto", "C. azul", "D. magenta", "E. rosa"),
           ("A. 7 litros", "B. Entre 7 e 10 litros", "C. Entre 4 a 6 litros", "D. 3 litros", "E. Entre 1 e 3 litros"),
           ("A. 8 minutos", "B. 30 segundos", "C. 4 minutos", "D. 2 minutos", "E. 40 segundos"),
           ("A. Terra, Vênus, Saturno, Júpiter, Marte, Netuno, Mercúrio", "B. Terra, Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio", "C. Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Terra, Urano, Vênus", "D. Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio", "E. Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Sol, Terra, Urano, Vênus"),
           ("A. Oxigênio", "B. Amônia", "C. Nitrogênio", "D. Dióxido de Carbono", "E. Hidrogênio"),
           ("A. Lula", "B. Floriano Peixoto", "C. Deodoro da Fonseca", "D. Getúlio Vargas", "E. Henrique Cardoso"))

answers = ("C", "B", "D", "A", "C", "C", "A", "B", "D", "C")
guesses = []
score = 0
question_num = 0


for question in questions:
    while True:
        print("---------------------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A,B,C,D,E): ").upper()
        guesses.append(guess)
        if guess == "A" or guess == "B" or guess == "C" or guess == "D" or guess == "E":
            if guess == answers[question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[question_num]} is the correct answer")
            question_num += 1
            break
        else:
            print("Você precisa escolher alguma das alternativas!")

print("--------------------------")
print("          RESULTS         ")
print("--------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/ len(questions) *100)
print(f"Your score is {score}%")