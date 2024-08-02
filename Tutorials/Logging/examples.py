'''
Python logging examples
'''
import logging
from splunklib.client import connect


class Solution:
    def __init__(self, debug=False) -> None:
        self.debug = debug

    def default_logging(self) -> None:
        '''
        Example of how to configure logging library to write logs to a file on disk
        '''
        # Create a logger object
        logger = logging.getLogger('splunk_logger')
        logger.setLevel(logging.INFO)

        # Create a handler for the Splunk instance
        splunk_handler = connect(
            token="YOUR_TOKEN"
        )  # Replace with your token value

        # Create a formatter and add it to the handler
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        splunk_handler.setFormatter(formatter)

        # Add the handler to the logger object
        logger.addHandler(splunk_handler)

        # Log messages
        logger.info("This is an info message")
        logger.warning("This is a warning message")

    def logging_to_AWS(self) -> None:
        '''
        How to get python logging to show in AWS logs?
        '''
        '''
        1. Install the AWS Logs Agent on your EC2 instance.
        2. Configure the agent to send logs to CloudWatch Logs.
        3. Create a log group in CloudWatch Logs for your Python application logs.
        4. Configure the Python logging library to write logs to a file on disk.
        5. Configure the AWS Logs Agent to monitor the log file and send its contents to CloudWatch Logs.
        '''

    def splunk_logging(self) -> None:
        '''
        Example of writing logs to splunk
        '''
        # Create a logger object
        logger = logging.getLogger('my_logger')
        logger.setLevel(logging.INFO)

        # Create a Splunk handler object and set the level to INFO
        splunk_handler = SplunkHandler(
            host='localhost', port=8088, token='your-token-here'
        )
        splunk_handler.setLevel(logging.INFO)

        # Add the handler to the logger
        logger.addHandler(splunk_handler)

        # Log some messages
        logger.info('This is an info message')
        logger.warning('This is a warning message')

    def new_relic_setup(self):
        '''
        Example of new relic setup
        '''
        '''     
        1. Install the New Relic Python Agent:
        pip install newrelic

        2. Configure the agent:
        Create a newrelic.ini file in your project root directory and add the following configuration settings:
        [newrelic]
        license_key = YOUR_LICENSE_KEY
        app_name = YOUR_APP_NAME
        log_level = info
        log_file = newrelic_agent.log
        monitor_mode = true

        3. Initialize the agent in your application code:
        import newrelic.agent
        newrelic.agent.initialize('newrelic.ini')

        4. Add instrumentation to your code:
        # Instrument a function call with a custom name and attributes
        @newrelic.agent.function_trace()
        def myfunc():
            # Do something here
            pass

        # Instrument an entire module with a custom name and attributes
        @newrelic.agent.background_task()
        def mymodule():
            # Do something here
            pass
        '''


if __name__ == '__main__':
    test = Solution(debug=True)
