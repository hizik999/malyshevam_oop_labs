class LimitedInstances:
    _instances = []
    limit = 5

    def __new__(cls):
        if len(cls._instances) >= cls.limit:
            raise RuntimeError("Превышен лимит созданных объектов")
        instance = super(LimitedInstances, cls).__new__(cls)
        cls._instances.append(instance)
        return instance

    def __del__(self):
        type(self)._instances.remove(self)

creation_results = []
errors = []

for _ in range(7):
    try:
        creation_results.append(LimitedInstances())
    except RuntimeError as e:
        errors.append(str(e))

print(len(creation_results), errors)
