from nautobot.apps import jobs
from nautobot.dcim.models import Device

name = "Examples" 

class DeviceORMJob(jobs.Job):
     class Meta:
        name = "Device ORM Job"

     device = Device.objects.filter(
         role__name="Access_Switch",
     )
 
      def run(self):
          self.logger.info(
              f"Device: {device.name} | Status: {device.status}"
          )
        
jobs.register_jobs(DeviceORMJob)
