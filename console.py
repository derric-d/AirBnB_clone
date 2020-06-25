#!/usr/bin/env python3
'''this is the entry point for the interpreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    cli class
    '''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''quit interpreter with str(quit)'''
        return True

    def do_EOF(self, arg):
        '''quit interpreter with ctr+d signal'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
