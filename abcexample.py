import abc

#class PluginBase(metaclass=abc.ABCMeta):
class PluginBase(abc.ABC): 

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""



#class RegisteredImplementation:
class RegisteredImplementation(PluginBase):

    def load(self, input):
        super().load(input)
        return input.read()

    def save(self, output, data):
        super().save(data)
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(RegisteredImplementation,
                                  PluginBase))
    print('Instance:', isinstance(RegisteredImplementation(),
                                  PluginBase))
