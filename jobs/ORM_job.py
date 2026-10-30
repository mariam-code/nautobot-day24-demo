from nautobot.apps import jobs
from nautobot.dcim.models import Device

name = "Examples"


class DeviceORMJob(jobs.Job):

    class Meta:
        name = "Device ORM Job"

    def run(self):

        self.logger.info("Starting Device ORM Job")

        devices = Device.objects.filter(
            role__name="Access Switch"
        )

        if not devices.exists():
            self.logger.warning(
                "No devices found with role Access Switch"
            )
            return

        for device in devices:

            self.logger.debug(
                f"Processing device {device.name}"
            )

            self.logger.info(
                f"Device: {device.name} | Status: {device.status}"
            )

            if not device.serial:
                self.logger.warning(
                    f"{device.name} has no serial number"
                )

            try:
                device.cf["Support Tier"] = "Day32"
                device.validated_save()

            except Exception as exc:
                self.logger.error(
                    f"Failed to update {device.name}: {exc}"
                )
                raise

        self.logger.info(
            "Device processing complete"
        )


jobs.register_jobs(DeviceORMJob)
