from aiogram.utils import executor

import logging
from bot import dp
import handlers
from log import setup_logging


def main():
    setup_logging()
    logging.info("init bot")
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
