result = []


def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('You can`t divide by 0')
        return 0
    except TypeError:
        print('You get a TypeError')
        return 0
    except ValueError:
        print('You get a ValueError')
        return 0


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}


for key in data:
    res = divider(key, data[key])
    result.append(res)


print(f'You result: {result}')
