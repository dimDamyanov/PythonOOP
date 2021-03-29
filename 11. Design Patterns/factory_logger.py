from abc import ABC, abstractmethod
import os


class Logger(ABC):
    @abstractmethod
    def log(self, obj):
        pass


class FileLogger(Logger):
    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, obj):
        with open(self.file_path, 'a') as file:
            file.write(obj)
            file.write('\n')


class StdoutLogger(Logger):
    def log(self, obj):
        print(obj)


class LoggersFactory:
    def __init__(self):
        self.environment = os.environ.get('ENVIRONMENT', 'dev')
        self.logs_file_path = os.environ.get('LOG_FILE_PATH', None)
        self.__init_logger()

    def get(self):
        return self.logger

    def __init_logger(self):
        if self.environment == 'dev':
            self.logger = StdoutLogger()
        else:
            self.logger = FileLogger(self.logs_file_path)


loggers_factory = LoggersFactory()

logger = loggers_factory.get()

logger.log('It works')
