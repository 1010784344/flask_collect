
import logging
import logging.handlers
import datetime


if __name__ == '__main__':
    # 日志器
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    # 处理器1
    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    # 格式器1
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # 处理器2
    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    # 格式器2
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    # logger对象添加一个处理器对象
    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

# 一个logging 模块总共有日志器，处理器，格式器，这几个对象
# 日志器，处理器是各自独立的，都是由 logging 模块引出来，然后再进行关联
# 格式器是有隶属于处理器的，因为处理器的作用是将数据吐向不同的地方，
# 而格式器决定了吐出的时候以什么样的格式，所以两者应该是关联的






