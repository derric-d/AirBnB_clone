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
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    cli class
    '''
    prompt = '(hbnb) '

    '''
    need to do error handling:
    '''
    def error_handler(self, args, n_args):
        '''show errors'''
        cls_lst = ["BaseModel", "User",
                   "Place", "State",
                   "City", "Amenity", "Review"]
        err_lst = ["** class name missing **",
                   "** class doesn't exist **",
                   "** instance id missing **",
                   "** no instance found **",
                   "** attribute name missing **",
                   "** value missing **"]

        if not args:  # have class name
            print(err_lst[0])
            return 1
        a = args.split(" ")
        if n_args >= 1 and a[0] not in cls_lst:  # name in list
            print(err_lst[1])
            return 1
        elif n_args == 1:
            return 0
        if n_args >= 2 and len(a) < 2:  # need to give id for instance
            print(err_lst[2])
            return 1
        for i in range(len(a)):
            if a[i][0] == '"':
                a[i] = a[i].replace('"', '')
        key = "{}.{}".format(a[i])
        if n_args >= 2 and key not in storage.all():  # need to give valid id
            print(err_lst[3])
            return 1
        elif n_args == 2:
            return 0
        if n_args >= 4 and len(a) < 3:
            print(err_lst[4])
            return 1
        if n_args >= 4 and len(a) < 4:
            print(err_lst[5])
            return 1
        return 0

    def emptyline(self):
        '''enables emmptyline'''
        pass

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
        if (self.error_handler(arg, 1) == 1):
            return
        a = arg.split(" ")
        # get a valid input from cmd: cls name
        inst = eval(a[0])()

        inst.save()   # save is base model method
        print(inst.id)

    def do_show(self, args):
        '''
        show str of an instance,
        lookup with cls name & id
        'show User 123'
        '''
        if (self.error_handler(args, 2) == 1):
            return
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
        if (self.error_handler(args, 2) == 1):
            return
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
        if not args:
            print([str(x) for x in all_lst.values()])
            return
        if (self.error_handler(args, 1) == 1):
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
        if (self.error_handler(args, 4) == 1):
            return
        a = args.split(" ")
        # parse class and attributes and set them
        ret_l = storage.all()
        key = "{}.{}".format(a[0], a[1])
        for i in range(len(a[1:]) + 1):
            if a[i][0] == '"':
                a[i] = a[i].replace('"', '')
        u_k = a[2]  # update key
        u_v = a[3]  # update value
        try:
            if u_v.isdigit():
                u_v = int(u_v)
            elif float(u_v):
                u_v = float(u_v)
        except ValueError:
            pass
        c_att = type(ret_l[key]).__dict__
        if u_k in c_att.keys():
            try:
                u_v = type(c_att[u_k])(u_v)
            except Exception:
                print("Invalid type for value")
                return
        setattr(storage.all()[key], u_k, u_v)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
