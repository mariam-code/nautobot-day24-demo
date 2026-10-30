from nautobot.apps import jobs

name = "Examples"


class StatusChangeJob(jobs.JobHookReceiver):

    class Meta:
        name = "Status Change Job"

    def receive_job_hook(self, change, action, changed_object):
        self.logger.info(
            f"Device {changed_object} was {action}"
        )


jobs.register_jobs(StatusChangeJob)
