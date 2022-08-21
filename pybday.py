#!/usr/bin/python3.8
import sys
import main

args = sys.argv[1:] + ["", ""]

def is_integer(n):
    if n == '0':
        n = n[1:]
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

if not args[0]:
    main.check()
elif args[0] == 'add' and args[1] and args[2]:
    main.add_new(name=args[1], birthdate=args[2])
elif args[0] == 'remove' and is_integer(args[1]):
    main.remove(id=args[1])
else:
    help = """
    pybday      get table
    pybday add [name] [birth date: dd.mm.yyyy]        add new person
    pybday remove [id: int]        remove person
    """
    print(help)
