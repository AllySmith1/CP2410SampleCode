
from array_stack import ArrayStack


def transfer(S, T):

    while not S.is_empty():
        T.push(S.pop())


stack_one = ArrayStack()
stack_one.push(1)
stack_one.push(2)
stack_one.push(3)
stack_one.push(4)
stack_one.push(5)

stack_two = ArrayStack()

transfer(stack_one, stack_two)




