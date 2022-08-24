def input_error(func):
    def inner(string):
        try:
            result = func(string)
            return result
        except IndexError:
            print('Give me name and phone please')
        except KeyError:
            print('Enter correctly user name')
        except ValueError:
            print('Enter correct type')

    return inner


@input_error
def add(string):
    contacts[string[0]] = string[1]


@input_error
def change(string):
    s = contacts[string[0]]
    contacts[string[0]] = string[1]


@input_error
def phone(string):
    return f'Number:{contacts[string[0]]}'


def main():
    commands = {
        'add': add,
        'change': change,
        'phone': phone,
    }

    while True:
        result = ''
        a = input().lower()
        if a == '.':
            break
        elif a in ("good bye", "close", "exit"):
            print("Good Bye!")
            break
        elif a == 'hello':
            print('How can I help you?')
        elif a == 'show all':
            print(contacts)
        elif a.split()[0] in commands:
            result = commands[a.split()[0]](a.split()[1:])
        if result:
            print(result)


if __name__ == '__main__':
    contacts = {
    }
    main()
