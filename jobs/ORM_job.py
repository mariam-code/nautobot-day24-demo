from nautobot.apps import jobs
from nautobot.dcim.models import Device
from nautobot.extras.models.groups import DynamicGroup

name = "Examples"


class DeviceORMJob(jobs.Job):

    device = jobs.ObjectVar(
        model=Device,
        required=True,
        description="Device selected from the Device page",
    )

    class Meta:
        name = "Device ORM Job"
        has_sensitive_variables = False
        approval_required = True

    def run(self, device):

        self.logger.info(
            f"Device selected from Job Button: {device.name}"
        )

        devices = Device.objects.filter(
            role__name="Access Switch"
        )

        self.logger.info("ORM results:")

        for dev in devices:
            self.logger.info(
                f"Device: {dev.name} | Status: {dev.status}"
            )

        group = DynamicGroup.objects.get(
            name="Pilot-site group"
        )

        self.logger.info("Dynamic Group results:")

        for dev in group.members:
            self.logger.info(
                f"Device: {dev.name} | Status: {dev.status}"
            )


jobs.register_jobs(DeviceORMJob)
