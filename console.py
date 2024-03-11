#!/usr/bin/python 3
""" Console cmd interpreter running on cmd module """
class HBNBCommand(cmd.Cmd):
    """ HBNBcommand class defined, inherits builtin in cmd module"""

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

if__name__ == '__main__':
    HBNBCommand.cmdloop()
