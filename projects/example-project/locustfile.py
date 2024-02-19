import random
from loguru import logger
from locust import task, User, HttpUser
import time
from faker import Faker


class RegisterTest(HttpUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set any class level requirement variables here. For example account list
        # hostname, portname etc.

        self.host = "https://hacken.io/"
    
    fake = Faker()

    def on_start(self):
        # This function is the first function it has been called and it is never being called again.
        # So if we have a database to login users to web api for example
        # We can pop our current user here from database and use that user credentials like
        # self.account = all_accounts.pop()    And use this account on next tasks.
        logger.debug("on_Start called. ")    

    def on_stop(self):
        # This function is the last function to call. So again here something like thread killing - account deleting
        # can be done here.
        logger.warning("on_stop called.")

    

    @task
    def register(self):
        name = self.fake.first_name() + '_' + self.fake.last_name() + str(random.randint(0, 9999))

        user = {
            "username": name,
            "email": name + '@test.hacken.net',
            "password": self.fake.password(32),
        }

        # We don't have anything to register, however if we had, it could be done like this.
        logger.debug("Created user: "+ str(user))

        # And again we don't have any database however if we had, we could save it like this.
        # mongodb.put_account(user["email"], user["username"], password=user["password"])
        with self.client.get(f"{self.host}", name="normal_request", catch_response=True) as response:
            if response.status_code >= 400:
                response.failure(f"Status code = {response.status_code}, message = {response.content}")


    @task
    def hacken_audits(self):
        startTime = int(round(time.monotonic() * 1000))

        with self.client.get(f"{self.host}/audits", headers = {
                                                                  #any header here, cookies - authorizations etc.  
                                                                },
                                                                name="get_audits", catch_response=True) as response:
            if response.status_code == 200:
                response.failure(f"Status code = {response.status_code}, message = {response.content}")
