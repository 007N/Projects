#!/usr/bin/python
# -*- coding: utf-8 -*-

# This programme does not work. It needs to be fixed.

def get_pipe_number():
    nbr_pipes = \
        int(input('Please enter the number of pipes you want to stack. >> '
            ))
    while nbr_pipes <= 1:
        nbr_pipes = \
            input('Please enter the number of pipes you want to stack. ( Please choose a number greater than 1. ) >> '
                  )
    return nbr_pipes


def find_base(pipes):
    current_pipe_number = 1
    while pipes != current_pipe_number * (current_pipe_number + 1) / 2:
        current_pipe_number += 1
        print current_pipe_number
    print '\nPour faire tenir ' + str(pipes) \
        + ' tuyaux ensembles, vous devrez mettre ' \
        + str(current_pipe_number) \
        + ' tuyaux à la base de votre pyramide.\n'


def main():
    i = get_pipe_number()
    find_base(i)

if __name__ == '__main__':
    main()
