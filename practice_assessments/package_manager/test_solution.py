import unittest
from solution import PackageManager


class TestPackageManager(unittest.TestCase):
    def test_level_1_packages(self):
        pm = PackageManager()
        self.assertTrue(pm.add_package("app"))
        self.assertFalse(pm.add_package("app"))
        self.assertFalse(pm.is_installed("app"))
        self.assertTrue(pm.install("app"))
        self.assertTrue(pm.is_installed("app"))
        self.assertFalse(pm.install("missing"))

    def test_level_2_install_order(self):
        pm = PackageManager()
        for package in ["app", "lib-a", "lib-b"]:
            pm.add_package(package)
        self.assertTrue(pm.add_dependency("app", "lib-b"))
        self.assertTrue(pm.add_dependency("app", "lib-a"))
        self.assertEqual(pm.install_order("app"), ["lib-a", "lib-b", "app"])

    def test_level_3_checked_install(self):
        pm = PackageManager()
        for package in ["app", "lib"]:
            pm.add_package(package)
        self.assertTrue(pm.add_dependency_checked("app", "lib"))
        self.assertFalse(pm.add_dependency_checked("lib", "app"))
        self.assertEqual(pm.install_with_dependencies("app"), ["lib", "app"])
        self.assertTrue(pm.is_installed("lib"))
        self.assertTrue(pm.is_installed("app"))

    def test_level_4_dependents(self):
        pm = PackageManager()
        for package in ["app", "tool", "lib"]:
            pm.add_package(package)
        pm.add_dependency_checked("app", "lib")
        pm.add_dependency_checked("tool", "lib")
        pm.install_with_dependencies("app")
        pm.install_with_dependencies("tool")
        self.assertEqual(pm.dependents("lib"), ["app", "tool"])
        self.assertFalse(pm.remove_package("lib"))
        self.assertTrue(pm.remove_package("app"))


if __name__ == "__main__":
    unittest.main()

