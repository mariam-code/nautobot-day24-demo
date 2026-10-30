from nautobot.apps import jobs

name = "Examples"


class StatusChangeJob(jobs.Job):

    class Meta:
        name = "Status Change Job"

    def run(self):
        self.logger.info(
            "Device status changed and Job Hook triggered successfully."
        )


jobs.register_jobs(StatusChangeJob)
