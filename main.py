def main():
    
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('You must enter a number')
            continue
        else:
            print (number)
            break

    return number


if __name__ == '__main__':
    
    main()
