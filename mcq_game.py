from question import question

question_prompts = [
"What is the color of a banana?\n(a) Red\n(b) Yellow\n(c) Purple\n(d) Pink\n\n",
"What is the color is an apple?\n(a) Red\n(b) Yellow\n(c) Magenta\n(d) Black\n\n",
"What is the color is a strawberry?\n(a) Green\n(b) Blue\n(c) Purple\n(d) Red\n\n"
]

questions = [
 question(question_prompts[0], "b"),
 question(question_prompts[1], "a"),
 question(question_prompts[2], "d")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You scored " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
