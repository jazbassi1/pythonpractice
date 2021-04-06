print("Hello, welcome to Jaz's Quiz")

ans = input("Are you ready to play ? (yes / no): ")
score = 0
total_questions = 10


if ans.lower() == 'yes':
    ans = input('1. What is the capital of the United Kingdom ? ')
    if ans.lower() == 'london':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = input('2. Who is the longest-reigning monarch in British history ? ')
    if ans.lower() == 'the queen' or 'queen':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = int(input('3. What is 5 multiplied by 5 ? '))
    if ans == 25:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = input('4. What is the most common colour of toilet paper in France ? ')
    if ans.lower() == 'pink':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

#     ans = int(input('5. How many days are there is February ? '))

    if ans == 28:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        ans = int(input('5. How many days are there in February ? '))

    ans = input('6. What color do you create when you mix green and red ? ')
    if ans.lower() == 'brown':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = int(input('7. How many days are there in a leap year ? '))
    if ans == 366:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = input('8. Which country was the fortune cookie invented ? ')
    if ans.lower() == 'united states' or 'us' or 'america':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = input('9. I am an odd number. Take away one letter and I become even. What number am I? ? ')
    if ans == 'seven' or 7:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    ans = int(input('The Final Question :) 10. What is 800 + 200 + 200 - 200 ? '))
    if ans == 1000:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    print(f"Thanks for playing ! You got {score} questions correct. ")
    mark = (score/total_questions) * 100

    print("Score: ",mark, '%')
else:
    print('Ok Goodbye :)')
    
