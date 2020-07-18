"""
------------------------------------------------------------------------
Functions
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-30"
------------------------------------------------------------------------
"""

from Stack_array import Stack


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    
    while not source.is_empty():
        target1.push(source.pop())
        if not source.is_empty():
            target2.push(source.pop())
            
    return target1, target2

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack. 
    When finished, the contents of source1 and source2 are interlaced 
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())
        
    if not source1.is_empty():
        while not source1.is_empty():
            target.push(source1.pop())
    if not source2.is_empty():
        while not source2.is_empty():
            target.push(source2.pop())
            
    return target
    
    
    return target

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    string = string.upper()
    i = 0
    
    palindrome = True
    
    str = string.strip("!").split(" ")
    string = ""
    for str in str:
        string += str
        
    n = len(string)
    
    while i < (n//2):
        stack.push(string[i])
        i += 1
    i += 1
    
    while i < n:
        if stack.is_empty():
            palindrome = False
            return palindrome
        else:
            top = stack.pop()
            
            if top == string[i]:
                palindrome = True
                i += 1
            else:
                palindrome = False
     
                
    return palindrome
    
def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    OPERATORS = "+-*/"
    stack = Stack()
    item = string.split(" ")
    for i in item:
        if i not in OPERATORS:
            stack.push(i)
        if i in OPERATORS:
            top = int(stack.pop())
            top_next = int(stack.pop())
            if i == OPERATORS[0]:
                top = top_next + top
                stack.push(top)
            elif i == OPERATORS[1]:
                top = top_next - top
                stack.push(top)
            elif i == OPERATORS[2]:
                top = top_next * top
                stack.push(top)
            elif i == OPERATORS[3]:
                top = top_next / top
                stack.push(top)
    answer = stack.peek()
    
    return answer

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    
    stack = Stack()

    path = []
    stack.push("Start")
    exit = False
    
    
    while exit == False and not stack.is_empty():
        stop = stack.pop()
        if stop!="Start":
            path.append(stop)
            
        value = maze[stop]
        
        if "X" in value:
            exit = True
            path.append("X")
        else:
            for val in value:
                stack.push(val)
    return path