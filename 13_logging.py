>>> # Logging allows you to write status messages to a file or other output streams. These messages contain information on which parts of your code have executed, and what problems may have arisen. Each log message has a level: debug, info, warning, wrror, critical. 
# Study again!!!!
>>> import logging
>>> dir(logging)
['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 'Filter', 'Filterer', 'Formatter', 'Handler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 'Manager', 'NOTSET', 'NullHandler', 'PercentStyle', 'PlaceHolder', 'RootLogger', 'StrFormatStyle', 'StreamHandler', 'StringTemplateStyle', 'Template', 'WARN', 'WARNING', '_STYLES', '_StderrHandler', '__all__', '__author__', '__builtins__', '__cached__', '__date__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__status__', '__version__', '_acquireLock', '_addHandlerRef', '_after_at_fork_child_reinit_locks', '_at_fork_reinit_lock_weakset', '_checkLevel', '_defaultFormatter', '_defaultLastResort', '_handlerList', '_handlers', '_levelToName', '_lock', '_logRecordFactory', '_loggerClass', '_nameToLevel', '_register_at_fork_reinit_lock', '_releaseLock', '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime', '_str_formatter', '_warnings_showwarning', 'addLevelName', 'atexit', 'basicConfig', 'captureWarnings', 'collections', 'critical', 'currentframe', 'debug', 'disable', 'error', 'exception', 'fatal', 'getLevelName', 'getLogRecordFactory', 'getLogger', 'getLoggerClass', 'info', 'io', 'lastResort', 'log', 'logMultiprocessing', 'logProcesses', 'logThreads', 'makeLogRecord', 'os', 'raiseExceptions', 're', 'root', 'setLogRecordFactory', 'setLoggerClass', 'shutdown', 'sys', 'threading', 'time', 'traceback', 'warn', 'warning', 'warnings', 'weakref']
>>> # Create and configure logger
>>> logging.basicConfig(filename = "E:\\python\\Lumberjack.Log")
>>> logger = logging.getLogger()
>>> # Test the logger
>>> logger.info("Our first message.")
>>> print(logger.level)
30
>>> #there are 6 main levels:
>>> #notset - 0
>>> #debug - 10
>>> #info - 20
>>> #warning - 30
>>> #error - 40
>>> #critical - 50
>>> # our test log was an info message which has a value of 20, but basicConfig sets the level of root logger to warning by default
>>> # to fix this update the basic config call and set the level to debug
>>> logging.basicConfig(filename = "E:\\python\\Lumberjack.Log", level=logging.DEBUG)
>>> # This will guarantee that we will see all log messages
>>> logger = logging.getLogger()
>>> logger.info("Our first message.")
>>> print(logger.level)
30


>>> # Create and configure logger
>>> LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
>>> logging.basicConfig(filename = "E:\\python\\Lumberjack.Log", level=logging.DEBUG, format=LOG_FORMAT)
>>> logger = logging.getLogger()
>>> # Test the logger
>>> logger.info("Our first message.")
>>> print(logger.level)

