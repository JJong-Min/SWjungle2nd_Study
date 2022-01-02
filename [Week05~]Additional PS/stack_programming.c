#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

typedef struct ArrayStack
{
    int top;
    int capacity;
    int *array;
} Stack;

Stack *createStack(int capacity) {
    /* stack크기는 고정적인지 사용자에게 받는지 물어보기 */
    /* 구현 시 array를 사용하는지, linked list를 사용하는지, stack이 꽉차면 realloc을 하는지*/
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    if(!stack) {
        return NULL;
    }
    stack->capacity = capacity;
    stack->top = -1;
    /* stack에 저장되는 데이터는 어떠한 타입인지 */
    stack->array = (int*)malloc(stack->capacity *sizeof(int));
    return stack;
}

int isEmpty (Stack *stack) {
    return (stack->top <= -1);
}

int isFull (Stack *stack) {
    return (stack->top >= stack->capacity - 1);
}

int peek (Stack *stack) {
    if (isEmpty(stack)) {
        /* return 뭐해야하는지 물어보기 */
        return INT_MIN;
    }
    return stack->array[stack->top];
}

void push (Stack *stack, int data) {
    if (isFull(stack)) {
        /* return 뭐해야하는지 물어보기 */
        printf("stack is full\n");
    } else {
        stack->array[++stack->top] = data;
        printf("%d pushed to stack\n", data);
    }
}

int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("stack is empty");
    } else {
        return stack->array[stack->top--];
    }
}

int main() {
    Stack *stack = createStack(3);
    push(stack, 1);
    push(stack, 2);
    push(stack, 3);
    push(stack, 4);
    pop(stack);
}