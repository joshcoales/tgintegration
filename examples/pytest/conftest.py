import os
import pytest

from tgintegration import IntegrationTestClient


# Create a session-scoped fixture that all tests use to receive their IntegrationTestClient instance
@pytest.fixture(scope="session")
def client():
    # Setup
    print('Initializing IntegrationTestClient')

    examples_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    c = IntegrationTestClient(
        session_name='my_account',
        bot_under_test='@BotListBot',  # We're going to test the @BotListBot
        max_wait_response=8,  # Wait max 8 seconds for responses, ...
        raise_no_response=True,  # ... then raise NoResponseReceived errors
        min_wait_consecutive=1.5,  # Wait at least 1.5 seconds to collect more than one message
        global_delay=1.5,  # Space out all messages by 1.5 seconds
        workdir=examples_dir  # Load configuration from parent folder
    )

    print("Starting client...")
    c.start()

    yield c  # py.test sugar to separate setup from teardown

    # Teardown
    c.stop()
