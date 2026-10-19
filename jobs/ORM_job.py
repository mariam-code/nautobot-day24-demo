from nautobot.apps import jobs
from nautobot.dcim.models import Device

name = "Examples" 

class DeviceORMJob(jobs.Job):
     class Meta:
        name = "Device ORM Job"

     def run(self):
          
     device = Device.objects.filter(
         role__name="Access Switch",
     )
 
     for device in Devices:
         self.logger.info(
             f"Device: {device.name} | Status: {device.status}"
         )
        
jobs.register_jobs(DeviceORMJob)
