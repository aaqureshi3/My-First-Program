#!/usr/bin/env python3

def interact():
    """
    The top-level function that defines the text-based user interface
    as described in the introduction.
    """
    begin = int(input('How many supporters from each team? '))
    states_list = [make_initial_state(begin)]
    show_current_state(states_list)
    length = len(make_initial_state(begin))
    while True:
        pos = input('? ')
        if pos == 'b':
            states_list.pop(-1)
            show_current_state(states_list)
        elif pos == 'q':
            break
        elif int(pos) < length - 1:
            post_move = make_move(states_list[-1], int(pos))
            states_list.append(post_move)
            show_current_state(states_list)
        else:
            show_current_state(states_list)

def make_initial_state(supporters):
    """
    Creates a string of alternating Tottenham(T) and Arsenal(A) supporters
    of length 'supporters' with two blank seats represented by two underscores
    at the end of the string.

    make_initial_state(int) -> str
    """
    return "TA"*supporters + "__"

def make_position_string(length):
    """
    Takes the length of the state and returns a string 01234... to be
    displayed in the interaction to make it easier for the user to pick
    the position of the pair to be moved.
    
    make_position_string(int) -> string
    """
    string = ""
    for i in range(0,length):
       if i < 10:
           string = string + str(i)
       else:
           string = string + str(i)[-1]
    return string

def num_diffs(state):
    """
    Takes a state and returns the number of differences between
    adjacent entries.

    num_diffs(str) -> int
    """
    differences = 0
    for i in range(0, len(state) - 1):
        if state[i] != state[i+1]:
            differences += 1
    return differences

def position_of_blanks(state):
    """
    Takes a state and returns the position of the first blank entry.

    position_of_blanks(str) -> int
    """
    for i in range(0,len(state)):
        if state[i] == "_":
            return i
            break
        else:
            None


def make_move(state, position):
    """
    Takes a state and a position and returns a new state where the pair
    at the given position have been swapped with the blank entries.

    make_move(str, int) -> str
    """
    lst = list(state)
    blank1 = position_of_blanks(state)
    lst[position], lst[blank1] = lst[blank1], lst[position]
    lst[position + 1], lst[blank1 + 1] = lst[blank1 + 1], lst[position + 1]
    return ''.join(lst)
        

def show_current_state(states):
    """
    Displays (prints) the state information for the
    current state as required for the user interaction, where states
    is the list of states representing the history of moves, and the
    current state is the last state in states.

    show_current_state(list) -> str
    """
    cur_state = states[-1]
    print(make_position_string(len(cur_state)))
    print(cur_state + ' ' + str(num_diffs(cur_state))
          + ' ' + str(len(states) - 1))        
        


if __name__ == '__main__':
    interact()
