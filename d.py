from abc import ABC, abstractmethod
import logging

# abstract interface so that Operation is not tightly coupled to any logger and is instead flexible
class Logger(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def log(self, msg, level):
        pass
    
    @abstractmethod
    def setLevel(self, level):
        pass

class LoggingHandler(Logger):
    def __init__(self):
        pass
    
    def log(self, msg, level):
        if level == "INFO":
            logging.info(msg)
        elif level == "WARNING":
            logging.warning(msg)
        elif level == "ERROR":
            logging.error(msg)
        elif level == "CRITICAL":
            logging.critical(msg)
    
    def setLevel(self, level):
        logging.setLevel(level)

class LoguruHandler(Logger):
    # still uses logging, !import loguru!, just showing an example of how this is divided
    def __init__(self):
        pass
    
    def log(self, msg, level):
        if level == "INFO":
            logging.info(msg)
        elif level == "WARNING":
            logging.warning(msg)
        elif level == "ERROR":
            logging.error(msg)
        elif level == "CRITICAL":
            logging.critical(msg)
    
    def setLevel(self, level):
        logging.setLevel(level)


class Operation:
    def __init__(self, log_method: Logger):
        self.log_method = log_method

    def calculate(self):
        try:
            #something
            self.log_method.log('all goood!', "INFO")
        except:
            self.log_method.log('error occured', "ERROR")

def main():
    testing1 = Operation(LoggingHandler())
    testing1.calculate()
    testing2 = Operation(LoguruHandler())
    testing2.calculate()

if __name__ == "__main__":
    main()

