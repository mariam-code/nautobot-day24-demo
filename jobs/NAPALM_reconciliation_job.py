from nautobot.apps import jobs
from nautobot.dcim.models import Device

name = "Examples"


class ReconciliationJob(jobs.Job):

    class Meta:
        name = "NAPALM Reconciliation Job"

    def run(self):

        devices = Device.objects.filter(
            name="router1"
        )

        self.logger.info(
            "Starting reconciliation check"
        )

        for device in devices:

            live_hostname = "router1-live"

            if device.name != live_hostname:

                self.logger.warning(
                    f"Mismatch detected - Nautobot: {device.name} | Live: {live_hostname}"
                )

            else:

                self.logger.info(
                    f"Match detected - {device.name}"
                )


jobs.register_jobs(ReconciliationJob)
