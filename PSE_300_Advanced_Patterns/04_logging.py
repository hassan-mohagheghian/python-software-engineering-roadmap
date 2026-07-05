# Advanced - Logging
# -----------------------------------------------------------------------------
# The logging module provides a flexible framework for emitting log
# messages. Unlike print(), logging supports severity levels, output
# destinations, and formatting.
#
# Key concepts:
# 1. Levels — DEBUG, INFO, WARNING, ERROR, CRITICAL.
# 2. Basic config — level, format, handlers.
# 3. Handlers — FileHandler, StreamHandler, RotatingFileHandler.
# 4. Getters — getLogger(__name__) for per-module loggers.
# -----------------------------------------------------------------------------


import logging
from logging.handlers import RotatingFileHandler


# =============================================================================
# Basic Logging
# =============================================================================


def basic_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s: %(message)s",
    )

    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning")
    logging.error("This is an error")
    logging.critical("This is critical")


# =============================================================================
# Named Logger (Per-Module)
# =============================================================================


logger = logging.getLogger(__name__)


def named_logger_demo():
    logging.basicConfig(level=logging.INFO, format="%(name)s — %(message)s")
    logger.info("Processing started")
    logger.warning("Low memory")
    logger.error("Connection failed")


# =============================================================================
# File Handler
# =============================================================================


def file_handler_demo():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(
                "app.log",
                maxBytes=1_000_000,
                backupCount=3,
            ),
        ],
    )

    for i in range(5):
        logging.info(f"Log entry {i}")

    print("  Logs written to app.log and stdout")


# =============================================================================
# Custom Logger with Levels
# =============================================================================


def custom_logger_demo():
    logging.basicConfig(level=logging.WARNING, format="%(message)s")

    # This logger respects the root level
    log = logging.getLogger("myapp")
    log.setLevel(logging.DEBUG)

    # These go through root which filters at WARNING
    log.debug("This won't show (root filters at WARNING)")
    log.warning("This will show")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Logging ===")
    basic_logging()

    print("\n=== File Handler ===")
    file_handler_demo()

    print("\n=== Custom Logger ===")
    custom_logger_demo()

    # Cleanup
    import os
    if os.path.exists("app.log"):
        os.remove("app.log")


if __name__ == "__main__":
    main()
