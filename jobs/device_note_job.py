from nautobot.apps.jobs import Job, ObjectVar, StringVar
from nautobot.dcim.models import Device


class DeviceNoteJob(Job):

    device = ObjectVar(
        model=Device,
        description="Select a device",
        required=True,
    )

    note = StringVar(
        description="Enter a note",
        required=False,
    )

    class Meta:
        name = "Device Note Job"

    def run(self, device, note=""):
        self.logger.info(
            f"Selected device: {device.name} | Note: {note}"
        )
