def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    
print("Hello! Welcome to THE Quiz" "\n" "10 pts for easch question")
ans = input("Are you ready to play (yes/no): ")
a ="Note: write answers! do not write option."
score = 0
total_questions = 4

correct_ans =["python", "steve jobs", "artificial intelligence", "bitcoin"]

if ans.lower() == "yes":
    print(a)
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java" )
    ans=input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- Who is the Founder of Facebook? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is more better among these? ")
    give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is the best Investment? ")
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
Code language: PHP (php)

i = score*10
if i &lt; 30:
    print("Ouch, your score is ",i,"/ 40 .")
elif i ==30:
    print("Nice! you scored ",i,"/ 40 .")
else:
    print("Congratulations! it's a perfect ",i,"/ 40 .")
