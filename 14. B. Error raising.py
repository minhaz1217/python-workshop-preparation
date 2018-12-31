try:
    raise NameError("Hello there was a name error")
except NameError as err:
    print(err)