import logging

logging.basicConfig(filename='./W2D2/app.log' ,level=logging.DEBUG)
logging.info("----------Started the error checking process--------------")

nums = [10,5,0,3,0]
res = []
for num in nums:
    if num == 0:
        logging.error("Division by zero encountered for number 0")
        continue
    result = 10/num
    res.append(result)
logging.info(f"Result is {res}")
logging.info("------------Finished the error checking process-----------")

    
