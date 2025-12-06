class Device:
    def __init__(self):
        print("Device initialized")

    def features(self):
        print("Basic device features")

# -------------------------
class Phone(Device):
    def __init__(self):
        super().__init__()      # Calls Device __init__
        print("Phone initialized")

    def features(self):
        super().features()      # Calls Device.features()
        print("Phone features: calling, texting")

# -------------------------
class Camera(Device):
    def __init__(self):
        super().__init__()      # Calls Device __init__
        print("Camera initialized")

    def features(self):
        super().features()      # Calls Device.features()
        print("Camera features: photo, video")

# -------------------------
class SmartPhone(Phone, Camera):
    def __init__(self):
        super().__init__()      # Calls next class in MRO
        print("SmartPhone initialized")

    def features(self):
        super().features()      # Calls next class in MRO
        print("SmartPhone features: internet, apps")

# -------------------------
obj = SmartPhone()
print("\n--- Features ---")
obj.features()

print("\nMRO order:")
print(SmartPhone.mro())