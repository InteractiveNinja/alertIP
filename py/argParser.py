from typing import List



def passArgs(args: List[str]):
    noLog = False
    if len(args) >= 2:
        if "--no-log" in args: noLog = True
    return noLog