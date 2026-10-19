from nautobot.apps.jobs import jobs
from nautobot.dcim.models import Device

name = "Examples" 

class DeviceNoteJob(jobs.Job):

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
        
jobs.register_jobs(DeviceNoteJob)  # <- required in Nautobot 2.x
