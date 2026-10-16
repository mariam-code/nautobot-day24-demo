from nautobot.apps import jobs

name = "Examples"  # Grouping shown in the UI


class HelloWorldJob(jobs.Job):
    class Meta:
        name = "Hello World"  # Job name


    def run(self):
        self.logger.info("Welcome to Nautobot")  # This is the logic that runs when the Job is executed
        self.logger.info("This is the warning")
        self.logger.info("Job ran successfully")


jobs.register_jobs(HelloWorldJob)  # <- required in Nautobot 2.x
