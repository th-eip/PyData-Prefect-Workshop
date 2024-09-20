# Example of processing some data
from prefect import task, flow, get_run_logger


@task
def add(a, b):
    logger = get_run_logger()
    logger.info(f"Adding up {a}+ {b} = {a+b}")
    return a + b 

@task
def square_num(num):
    logger = get_run_logger()
    logger.info(f"Squaring {num} which results in {num**2}")
    return num ** 2

@flow
def add_and_square(a:int = 2, b:int = 3):
    add_result = add(a, b)
    square_result = square_num(add_result)
    print(f"({a} + {b}) squared = {square_result}")

if __name__ == "__main__":
    add_and_square(4, 8)
