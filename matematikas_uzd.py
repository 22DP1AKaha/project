questions = ['1+1=','3-10=','12*7=','12:4=','15:3=']
answers = [2,-7,84,3,5]
pareizas_atbildes = 0
for indekss in range(5):
    question = questions[indekss]
    pareiza_atbilde = answers[indekss]
    user_answer = input(f'{indekss}) {question}')
    if float(user_answer) == pareiza_atbilde:
        pareizas_atbildes = pareizas_atbildes+1
print(pareizas_atbildes)