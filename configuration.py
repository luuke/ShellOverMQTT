from configparser import ConfigParser, NoSectionError, NoOptionError

class BrokerConfiguration:
    def __init__(self, address=None, port=1883, login=None, password=None):
        self.Address = address
        self.Port = port
        self.Login = login
        self.Password = password

class Configuration:
    required = dict(
            MQTTBroker=["Address", "Port", "Login", "Password"],
            MQTTClient=["Name"]
        )

    def __init__(self, configFile=None):
        self.filename = configFile
        self.parser = ConfigParser()
        self.parser.read(self.filename)
        self._checkConfigurationFile()

    def _checkConfigurationFile(self):
        for section in self.required.keys():
            if not self.parser.has_section(section):
                raise NoSectionError(section)

            for option in self.required.get(section):
                if not self.parser.has_option(section, option):
                    raise NoOptionError(option, section)

    def GetBrokerConfiguration(self):
        self.parser.read(self.filename)
        address = self.parser.get("MQTTBroker", "Address")
        port = self.parser.get("MQTTBroker", "Port")
        login = self.parser.get("MQTTBroker", "Login")
        password = self.parser.get("MQTTBroker", "Password")
        return BrokerConfiguration(address=address, port=port, login=login, password=password)