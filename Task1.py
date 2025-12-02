"""
Chatbot Workflow

1. Costumor input() something
2. Analyze the input question
3. Search for answer, using fastf1 pakage
4. print() answer
5. loop 1.-4. until costomer exit

"""

# create dic f1_faq
f1_faq = {
    "who is oscar piastri?":"He is a autralian driver, also won the 2025 driver championship.",
    "what is mclaren?":"McLaren is a British F1 team founded in 1963.",
    "who will win the 2025 abu dabi grid?":"Oscar piastri is P1, also lando norris is P6."
}

# write function name get_answer(), set all in lowercase
def get_answer(question):
    question = question.lower()

    # iterate, search the dic
    for key in f1_faq:
        if key in question:
            return f1_faq[key]
 #       else:
 #           print(f"sorry i don't have an answer." ) 
    return f"sorry i don't have an answer." 
# 只要 return 被執行，整個 function 就立刻停止，後面的程式碼一行都不會跑
    


# create function name chatbot(), loop till user said end
def chatbot():
    print("Wellcome, user! Type exit to quit.")
    while True:
        user_input = input("You:")
        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        answer = get_answer(user_input)
        print("Bot:",answer)


chatbot()