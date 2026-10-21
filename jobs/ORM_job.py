from nautobot.apps import jobs
from nautobot.dcim.models import Device
from nautobot.extras.models.groups import DynamicGroup

name = "Examples"


class DeviceORMJob(jobs.Job):

    class Meta:
        name = "Device ORM Job"
        has_sensitive_variables = False
        approval_required =  True

    def run(self):

        devices = Device.objects.filter(
            role__name="Access Switch"
        )

        self.logger.info("ORM results:")

        for device in devices:
            self.logger.info(
                f"Device: {device.name} | Status: {device.status}"
            )

        group = DynamicGroup.objects.get(
            name="Pilot-site group"
        )

        self.logger.info("Dynamic Group results:")

        for device in group.members:
            self.logger.info(
                f"Device: {device.name} | Status: {device.status}"
            )


jobs.register_jobs(DeviceORMJob)
