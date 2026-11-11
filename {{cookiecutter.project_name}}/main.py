import structlog
from src.logging_conf import setup_logging

logger = structlog.getLogger("src")


def main() -> None:
    logger.info("Application started", extra={"custom_field": "custom_value"})


if __name__ == "__main__":
    setup_logging()
    main()
