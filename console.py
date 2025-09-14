#!/usr/bin/python3
"""Console for AirBnB_clone project."""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
            "BaseModel": BaseModel,
                "User": User,
                    "State": State,
                        "City": City,
                            "Amenity": Amenity,
                                "Place": Place,
                                    "Review": Review
                                    }

class HBNBCommand(cmd.Cmd):
        """Command interpreter for AirBnB clone."""
            prompt = "(hbnb) "

                def do_create(self, arg):
                            """Create a new instance, save it, and print its id."""
                                    args = shlex.split(arg)
                                            if not args:
                                                            print("** class name missing **")
                                                                        return
                                                                            cls = classes.get(args[0])
                                                                                    if not cls:
                                                                                                    print("** class doesn't exist **")
                                                                                                                return
                                                                                                                    instance = cls()
                                                                                                                            storage.new(instance)
                                                                                                                                    storage.save()
                                                                                                                                            print(instance.id)

                                                                                                                                                def emptyline(self):
                                                                                                                                                            """Do nothing on empty input line or spaces."""
                                                                                                                                                                    return

                                                                                                                                                                    def do_quit(self, arg):
                                                                                                                                                                                """Quit command to exit the console."""
                                                                                                                                                                                        return True

                                                                                                                                                                                        def do_EOF(self, arg):
                                                                                                                                                                                                    """Exit the console on EOF."""
                                                                                                                                                                                                            print()
                                                                                                                                                                                                                    return True

                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                        storage.reload()
                                                                                                                                                                                                                            HBNBCommand().cmdloop()
