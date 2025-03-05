import logging
from utils import calculator
from utils import validator

logging.basicConfig(filename='./logs/app.log',level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s",datefmt='%d-%b-%y %H:%M:%S')

def main():
    while True:
        logging.info("----MATH CALCULATOR STARTED----")
        expression = input("Enter the expression: ")
        if(expression.lower()=="exit"):
            print("Exited the calculator")
            break
        logging.debug(f"Received expression: {expression}")
        if validator.is_valid_expression(expression):
            logging.info("the given Expression is valid")
            result = calculator.calculate(expression)
            logging.info(f"Result of the expression: {result}")
            print(f"Result: {result}")
        else:
            logging.error(f"Invalid expression: {expression}")
            print("Invalid expression please enter valid expression")
        logging.info("----MATH CALCULATOR ENDED----")

if __name__ == "__main__":
    main()