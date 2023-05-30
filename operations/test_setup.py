class TestClass:
    def setup_class(self):
        print("setup class gets called")

    def setup_method(self):
        print("setup method gets called")

    def test_method_1(self):
        print("method1 gets called")

    def test_method_2(self):
        print("method2 gets called")
