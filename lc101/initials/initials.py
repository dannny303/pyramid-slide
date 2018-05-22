def get_initials(fullname):
    myname = fullname
    namelist = myname.split()
    init = ""
 
    for eachname in namelist:
        init = init.upper() + eachname.upper()[0]
    print('My initials are', (init))

def main():
    get_initials(input('Whats your fullname?\n'))
    
    
    
if __name__ == '__main__':
    main()

