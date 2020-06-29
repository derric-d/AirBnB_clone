#!/usr/bin/env python3
'''this is the entry point for the interpreter'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.city import City
'''
likely still need:
from models import storage
'''


class HBNBCommand(cmd.Cmd):
    '''
    cli class
    '''
    prompt = '(hbnb) '

    '''
    need to do error handling:

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

        inst.save()   # save is base model method
        print(inst.id)

    def do_show(self, args):
        '''
        show str of an instance,
        lookup with cls name & id
        'show User 123'
        '''
        a = args.split(" ")
        ret_inst = storage.all()
        key = "{}.{}".format(a[0], a[1])
        print(ret_inst[key])

    def do_destroy(self, args):
        '''
        ERROR & storage check
        destroy instances
        'destroy User 123'
        '''
        a = args.split(" ")
        ret_i = storage.all()
        key = "{}.{}".format(a[0], a[1])
        del ret_i[key]
        storage.save()

    def do_all(self, args):
        '''
        ERROR & storage check
        show all instances , can specify  class
        'all' or 'all User'
        '''
        # retrive all from db
        all_lst = storage.all()
        if not arg:
            print([str(x) for x in all_lst.values()])
            return
        a = args.split(" ")
        print([str(y) for y in all_lst.values()
              if y.__class__.__name__ == a[0]])

    def do_update(self, args):
        '''
        ERROR & storage check
        update the instance given,
        lookup with name & id and pass attr to update and value to give
        'update User 123 name 'Betty'
        '''
        a = args.split(" ")
        # parse class and attributes and set them
        ret_l = storage.all()
        key = "{}.{}".format(a[0], a[1])
        '''
        for i in range(len(a[1:]) + 1):
            print(args[i][0])
        '''
        # parse and set attr.

if __name__ == '__main__':
    HBNBCommand().cmdloop()
