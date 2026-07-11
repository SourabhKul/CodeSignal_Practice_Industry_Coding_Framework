import unittest
from solution import BuildSystem


class TestBuildSystem(unittest.TestCase):
    def test_level_1_targets(self):
        system = BuildSystem()
        self.assertTrue(system.add_target("app"))
        self.assertFalse(system.add_target("app"))
        self.assertFalse(system.is_built("app"))
        self.assertTrue(system.build("app"))
        self.assertTrue(system.is_built("app"))
        self.assertEqual(system.touch("app"), 2)
        self.assertFalse(system.is_built("app"))

    def test_level_2_order(self):
        system = BuildSystem()
        for target in ["app", "lib", "core"]:
            system.add_target(target)
        self.assertTrue(system.add_dependency("app", "lib"))
        self.assertTrue(system.add_dependency("lib", "core"))
        self.assertEqual(system.build_order("app"), ["core", "lib", "app"])

    def test_level_3_recursive_build(self):
        system = BuildSystem()
        for target in ["app", "lib", "core"]:
            system.add_target(target)
        self.assertTrue(system.add_dependency_checked("app", "lib"))
        self.assertTrue(system.add_dependency_checked("lib", "core"))
        self.assertFalse(system.add_dependency_checked("core", "app"))
        self.assertEqual(system.build_with_dependencies("app"), ["core", "lib", "app"])
        self.assertEqual(system.build_with_dependencies("app"), [])

    def test_level_4_stale_cascade(self):
        system = BuildSystem()
        for target in ["app", "lib", "core"]:
            system.add_target(target)
        system.add_dependency_checked("app", "lib")
        system.add_dependency_checked("lib", "core")
        system.build_with_dependencies("app")
        self.assertEqual(system.touch_cascade("core"), ["app", "core", "lib"])
        self.assertEqual(system.stale_targets(), ["app", "core", "lib"])


if __name__ == "__main__":
    unittest.main()

