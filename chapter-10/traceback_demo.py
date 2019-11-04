import traceback

try:
    raise Exception("This is the error message :)")
except Exception as e:
    errorfile = open('errorfile.txt', 'w')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print('The traceback info was printed to errorfile.txt')
