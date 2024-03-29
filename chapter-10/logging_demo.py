import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - \
%(levelname)s - %(message)s')
logging.debug('Start of program')


# There is a mistake in the code below, easily found with logging
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}.')
    logging.debug('End of factorial(%s)' % (n))
    return total


# Mistake is fixed
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}.')
    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')
