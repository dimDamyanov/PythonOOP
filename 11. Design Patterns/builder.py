from abc import ABC, abstractmethod


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


class LoggersBuilder:
    def __init__(self):
        self.file_path = None
        self.environment = 'dev'

    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_environment(self, environment):
        self.environment = environment

    def build(self) -> Logger:
        if self.environment == 'prod':
            return FileLogger(self.file_path)
        else:
            return StdoutLogger()


loggers_builder = LoggersBuilder()
loggers_builder.set_file_path('./logs3.txt')
loggers_builder.set_environment('prod')
loggers_builder.build().log('It works with builders')
