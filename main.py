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
def add_new_contact(new_contact):
    contacts[new_contact[0]] = new_contact[1]


@input_error
def change_contact(contact):
    examination = contacts[contact[0]]
    contacts[contact[0]] = contact[1]


@input_error
def get_contact_phone(name_contact):
    return f'Number:{contacts[name_contact[0]]}'


def main():
    commands = {
        'add': add_new_contact,
        'change': change_contact,
        'phone': get_contact_phone,
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
        elif result:
            print(result)


if __name__ == '__main__':
    contacts = {
    }
    main()
