# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("lottery", Path(__file__).resolve().parents[1] / "euroMillions.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

class LotteryTests(unittest.TestCase):
    def test_ticket_ranges_and_uniqueness(self):
        for _ in range(30):
            numbers, stars = app.draw()
            self.assertEqual(len(numbers), 5)
            self.assertEqual(len(set(numbers)), 5)
            self.assertTrue(all(1 <= n <= 50 for n in numbers))
            self.assertEqual(len(stars), 2)
            self.assertEqual(len(set(stars)), 2)
            self.assertTrue(all(1 <= n <= 12 for n in stars))
    def test_ticket_format(self):
        self.assertIn("Stars: 1, 2", app.format_ticket([1, 2, 3, 4, 5], [1, 2]))

if __name__ == "__main__":
    unittest.main()
