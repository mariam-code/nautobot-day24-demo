from nautobot.apps import jobs
from nautobot.dcim.models import Device

name = "Examples"


class ReconciliationJob(jobs.Job):

    class Meta:
        name = "NAPALM Reconciliation Job"

    def run(self):

        devices = Device.objects.filter(
            location__name="containerlab:frr01"
        )

        self.logger.info(
            "Starting reconciliation check"
        )

        for device in devices:

            # Simulated live hostname
            live_hostname = device.name

            if device.name != live_hostname:

                self.logger.warning(
                    f"Mismatch detected - Nautobot: {device.name} | Live: {live_hostname}"
                )

            else:

                self.logger.info(
                    f"Match detected - {device.name}"
                )


jobs.register_jobs(ReconciliationJob)
