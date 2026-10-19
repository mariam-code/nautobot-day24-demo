from nautobot.apps import jobs
from nautobot.dcim.models import Device

name = "Examples" 

class DeviceNoteJob(jobs.Job):

    device = jobs.ObjectVar(
        model=Device,
        description="Select a device",
        required=True,
    )

    note = jobs.StringVar(
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
