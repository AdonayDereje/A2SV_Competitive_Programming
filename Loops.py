if __name__ == '__main__':
    n = int(input())

    if n < 1 or n > 20:
        print ("out of range") 
#

    else:
        for values in range(n):
            print(values * values)
        
