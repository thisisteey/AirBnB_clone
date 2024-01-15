#!/usr/bin/python3
"""A console class which is the entry point of the project is defined"""
import cmd
import models
from re import search
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The console of the HBnB project is represented"""
    prompt = "(hbnb) "
    classes = \
        {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_EOF(self, args):
        """signal to exit the program in non-interactive mode"""
        return True

    def do_quit(self, args):
        """the command quit to exit the program"""
        return True

    def emptyline(self):
        """the prompt would not execute anything"""
        pass

    def do_create(self, args):
        """creates a new instance of a class, save it and print the id"""
        clsargs = parse(args)
        if len(clsargs) == 0:
            print("** class name missing **")
        elif clsargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(clsargs[0])().id)
            models.storage.save()

    def do_show(self, args):
        """prints the string representation of a class instance and id"""
        clsargs = parse(args)
        objdict = models.storage.all()
        if len(clsargs) == 0:
            print("** class name missing **")
        elif clsargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(clsargs) == 1:
            print("** instance id missing **")
        elif f"{clsargs[0]}.{clsargs[1]}" not in objdict:
            print("** no instance found **")
        else:
            print(objdict[f"{clsargs[0]}.{clsargs[1]}"])

    def do_destroy(self, args):
        """deletes an instance based on the class name and its id"""
        clsargs = parse(args)
        objdict = models.storage.all()
        if len(clsargs) == 0:
            print("** class name missing **")
        elif clsargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(clsargs) == 1:
            print("** instance id missing **")
        elif f"{clsargs[0]}.{clsargs[1]}" not in objdict:
            print("** no instance found **")
        else:
            del objdict[f"{clsargs[0]}.{clsargs[1]}"]
            models.storage.save()

    def do_all(self, args):
        """prints all string representation of all class based instances"""
        clsargs = parse(args)
        if len(clsargs) > 0 and clsargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objlst = []
            for obj in models.storage.all().values():
                objclsname = obj.__class__.__name__
                if len(clsargs) > 0 and clsargs[0] == objclsname:
                    objlst.append(obj.__str__())
                elif len(clsargs) == 0:
                    objlst.append(obj.__str__())
            print(objlst)

    def do_count(self, args):
        """gets and returns the number of instances in a class"""
        clsargs = parse(args)
        count = 0
        for obj in models.storage.all().values():
            if clsargs[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, args):
        """updates an instance based on the class name and id"""
        clsargs = parse(args)
        objdict = models.storage.all()
        if len(clsargs) == 0:
            print("** class name missing **")
            return False
        if clsargs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(clsargs) == 1:
            print("** instance id missing **")
            return False
        if f"{clsargs[0]}.{clsargs[1]}" not in objdict.keys():
            print("** no instance found **")
            return False
        if len(clsargs) == 2:
            print("** attribute name missing **")
            return False
        if len(clsargs) == 3:
            try:
                type(eval(clsargs[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(clsargs) == 4:
            obj = objdict[f"{clsargs[0]}.{clsargs[1]}"]
            if clsargs[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[clsargs[2]])
                obj.__dict__[clsargs[2]] = valtype(clsargs[3])
            else:
                obj.__dict__[clsargs[2]] = clsargs[3]
        elif type(eval(clsargs[2])) == dict:
            obj = objdict[f"{clsargs[0]}.{clsargs[1]}"]
            for ky, val in eval(clsargs[2]).items():
                if (ky in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[ky]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[ky])
                    obj.__dict__[ky] = valtype(val)
                else:
                    obj.__dict__[ky] = val
        models.storage.save()

    def default(self, args):
        """default message for invalid module input of the HBNBCommand"""
        argsdict = {
            "show": self.do_show,
            "update": self.do_update,
            "all": self.do_all,
            "count": self.do_count,
            "destroy": self.do_destroy
        }
        dtmt = search(r"\.", args)
        if dtmt is not None:
            clsargs = [args[:dtmt.span()[0]], args[dtmt.span()[1]:]]
            dtmt = search(r"\((.*?)\)", clsargs[1])
            if dtmt is not None:
                pscmd = [clsargs[1][:dtmt.span()[0]], dtmt.group()[1:-1]]
                if pscmd[0] in argsdict.keys():
                    fulcal = f"{clsargs[0]} {pscmd[1]}"
                    return argsdict[pscmd[0]](fulcal)
        print(f"** Invalid syntax: {args}")
        return False


def parse(args):
    """splits the str and gets items in curly braces or square brackets"""
    cbmtch = search(r"\{(.*?)\}", args)
    sqrb = search(r"\[(.*?)\]", args)
    if cbmtch is None:
        if sqrb is None:
            return [x.strip(",") for x in split(args)]
        else:
            toks = split(args[:sqrb.span()[0]])
            reslst = [x.strip(",") for x in toks]
            reslst.append(sqrb.group())
            return reslst
    else:
        toks = split(args[:cbmtch.span()[0]])
        reslst = [x.strip(",") for x in toks]
        reslst.append(cbmtch.group())
        return reslst


if __name__ == "__main__":
    HBNBCommand().cmdloop()
