#!/usr/bin/env python3
'''this is the entry point for the interpreter'''
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    '''
    cli class
    '''
    prompt = '(hbnb) '

    '''
    ERRORS:
    "** class name missing **",
    "** class doesn't exist **",
    "** instance id missing **",
    "** no instance found **",
    "** attribute name missing **",
    "** value missing **"
    '''

    def do_quit(self, arg):
        '''quit interpreter with str(quit)'''
        return True

    def do_EOF(self, arg):
        '''quit interpreter with ctr+d signal'''
        return True

    def do_create(self, arg):
        '''
        create new cls instance w/:
        create <cls_name>
        musyt print instance.id
        '''
        a = arg.split(" ")
        # get a valid input from cmd: cls name
        inst = a[0]

        inst.save() # save is base model method
        print(inst.id)

    def do_show(self, args):
        '''
        show str of an instance,
        lookup with cls name & id
        'show User 123'
        '''
        a = args.split(" ")

    def do_destroy(self, args):
        '''
        destroy instances
        'destroy User 123'
        '''
        a = args.split(" ")

    def do_all(self, args):
        '''
        show all instances , can specify  class
        'all' or 'all User'
        '''
        # retrive all from db

    def do_update(self, args):
        '''
        update the instance given,
        lookup with name & id and pass attr to update and value to give
        'update User 123 name 'Betty'
        '''
        a = args.split(" ")
        # parse class and attributes and set them


if __name__ == '__main__':
    HBNBCommand().cmdloop()
