from nautobot.apps import jobs

name = "Examples"


class DeviceButtonJob(jobs.JobButtonReceiver):

    class Meta:
        name = "Device Button Job"

    def receive_job_button(self, obj):
        self.logger.info(
            f"Button pressed for {obj.name}"
        )


jobs.register_jobs(DeviceButtonJob)
