def reading():
    f = open('input.txt', 'r')
    numbers = f.readline().split()
    f.close()
    return numbers


answer = []


def main_function(numbers, element=0):
    global answer
    if int(numbers[element]) > 0:
        answer.append(numbers[element])
        main_function(numbers, element + 1)
    elif int(numbers[element]) < 0:
        answer.insert(0, numbers[element])
        main_function(numbers, element + 1)
    return answer


def writing(ans):
    f = open('output.txt', 'w')
    for an in ans:
        f.write(an + ' ')
    f.close()
