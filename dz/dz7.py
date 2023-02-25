import ast


def safe_calculate(func):
    def wrapper(expression):
        try:
            # Перевіряємо вхідний вираз на безпечність виконання
            parsed = ast.parse(expression, mode='eval')
            if isinstance(parsed, ast.Expression):
                # Виконуємо обчислення
                return func(expression)
            else:
                raise ValueError('Invalid expression')
        except Exception as e:
            # Повертаємо повідомлення про помилку
            return f'Error: {str(e)}'
    return wrapper


@safe_calculate
def calculate(expression):
    return eval(expression)


calculate('64 / 8')