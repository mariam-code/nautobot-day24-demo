from nautobot.extras.models.groups import DynamicGroup

group = DynamicGroup.objects.get(
    name="pilot-site"
)

for device in group.members:
    self.logger.info(
        f"Device: {device.name} | Status: {device.status}"
    )
