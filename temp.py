def SaveClasses(classes):
    with open('classes.txt', 'a') as file:
        for key, value in classes.items():
            file.write(key + ' ' + ";".join(str(value)) + '\n')


a = {'1a': [1,2,3], '1b':[4,5,6]}

SaveClasses(a)