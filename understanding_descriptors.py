# cSpell:ignore

# https://www.pythontutorial.net/python-oop/python-descriptors/

# Saturday, December 14, 2024
# trying to understand descriptors

class RequiredString:
    def __set_name__(self, owner, name):
        print(f"__set_name__ was called with owner={owner} and name={name}")
        self.property_name = name

    def __get__(self, instance, owner):
        print(f"__get__ was called with instance={instance} and owner={owner}")
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self, instance, value):
        print(f"__set__ was called with instance={instance} and value={value}")

        if not isinstance(value, str):
            raise ValueError(f"The {self.property_name} must a string")

        if len(value) == 0:
            raise ValueError(f"The {self.property_name} cannot be empty")

        instance.__dict__[self.property_name] = value


class Person:
    first_name = RequiredString()
    last_name = RequiredString()


print(first_name)

# if I create class RequiredString, I can put validation logic to it...

# I tend to use DataClasses... which may save me from spending much time creating my own data class...
