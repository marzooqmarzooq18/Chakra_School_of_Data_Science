class Singleton:
    _instance = None  # Class variable to store the single instance

    def __new__(cls, value):
        if cls._instance is None:
            # Create a new instance only once
            cls._instance = super().__new__(cls)
            cls._instance.value = value
            print(f"[Singleton] Instance created with value = '{value}'")
        else:
            # Reuse the existing instance
            print(f"[Singleton] Returning existing instance (value = '{cls._instance.value}')")
        return cls._instance

    def __repr__(self):
        return f"<Singleton value={self.value} id={id(self)}>"


# Demonstration of Singleton behavior
if __name__ == "__main__":
    obj1 = Singleton("DatabaseConnection")
    obj2 = Singleton("CacheConnection")

    print(obj1 is obj2)  # True - both point to the same instance
    print(obj1)
    print(obj2)
