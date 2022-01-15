import turtle
import pandas
FONT = ("Courier", 24, "normal")

screen = turtle.Screen()
correct_answers = []
screen.title('Us States Games')
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)


class Writing_states_name(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('Red')

    def Drawing_names(self,x,y,name):

        self.penup()
        self.goto(x,y)
        self.pendown()
        self.write(f'{name}', align='center', font= ("arial", 10, "normal"))

pen = Writing_states_name()
data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()
states_not_found = states

while len(correct_answers)<50:

    correct = len(correct_answers)
    answer_state = screen.textinput(title=f'Correct {correct}/50', prompt='Whats a another state name?')
    answer_state = answer_state.title()



    if answer_state == 'Exit':
        new_data = pandas.DataFrame(states_not_found)
        new_data.to_csv('states_to_learn.csv')
        break
    elif answer_state in states:
        print('good')
        answer_state_row = data[data.state == answer_state]
        x = int(answer_state_row.x)
        y = int(answer_state_row.y)

        pen.Drawing_names(x,y,answer_state)

        correct_answers.append(answer_state)
        states_not_found.remove(answer_state)


    else:
        print('not good')
print(states_not_found)


screen.exitonclick()