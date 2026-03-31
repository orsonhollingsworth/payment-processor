import logging
import os

from payment_processor.config import Config
from payment_processor.payment import Payment
from payment_processor.processor import Processor
from payment_processor.registry import Registry

def main():
    # Configure the logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    # Load configuration
    config = Config(os.path.join(os.getcwd(), 'config.yaml'))

    # Initialize the payment processor
    registry = Registry()
    processor = Processor(registry)

    # Process payments
    for payment in config.payments:
        processor.process_payment(Payment(payment))

if __name__ == '__main__':
    main()