from nautobot.dcim.models import Device


def test_access_switch_devices_exist():

    devices = Device.objects.filter(
        role__name="Access Switch"
    )

    assert devices.count() > 0
