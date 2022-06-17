import yaml


class Test_PythonHomePage:
    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        with open("config.yaml", 'r') as stream:
            try:
                cls.conf = yaml.load(stream)
                print(cls.conf['Browser'])
            except yaml.YAMLError as exc:
                print(exc)

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        print("Hello from teardown")

    def test_search(self):
        assert self.conf['Browser'] == "firefox"
