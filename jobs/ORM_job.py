from nautobot.apps import jobs
from nautobot.dcim.models import Device
from nautobot.extras.models.groups import DynamicGroup

name = "Examples" 

class DeviceORMJob(jobs.Job):
     class Meta:
        name = "Device ORM Job"

     def run(self):
          
         devices = Device.objects.filter(
              role__name="Access Switch",
         )
 
         for device in devices:
             self.logger.info(
                 f"Device: {device.name} | Status: {device.status}"
             )
              
             device.cf["support_tier"] = "Bronze"
             device.validated_save()

         group = DynamicGroup.objects.get(
          name="pilot-site"
         )

     for device in group.members:
         self.logger.info(
             f"Device: {device.name} | Status: {device.status}"
         )

jobs.register_jobs(DeviceORMJob)
