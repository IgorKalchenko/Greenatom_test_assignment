# Проблема кода в вопросе заключается в том, что в первоначальной версси lambda-функция воспринимала step как
# внешнюю изменяемую переменную, соответственно lambda использовало не каждое значение step во время цикла (так как
# оное нигде не сохранялось и просто поглощалось сборщиком мусора), а то значение step, которое эта переменная имела на
# момент вызова функции (в коде это 4). Чтобы исправить проблему достаточно передать lambda-функции
# локальную переменную (например bound_step), которая привяжет к анонимной функции значения step из цикла.
# Таким образом, функция каждый раз будет вызываться с корректным значением переменной bound_step
from typing import List, Callable


def create_handlers(callback: Callable) -> List[Callable[[int], Callable]]:
    handlers: list = []
    for step in range(5):
        handlers.append(lambda bound_step=step: callback(bound_step))
    return handlers


def execute_handlers(handlers: List[Callable[[int], Callable]]) -> None:
    for handler in handlers:
        handler()
