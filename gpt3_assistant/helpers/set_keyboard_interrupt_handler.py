import sys
import signal
import logging


def set_keyboard_interrupt_handler():
    def signal_handler(_sig, _frame):
        logging.info("Shutting down...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
