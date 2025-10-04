import unittest
import pandas as pd
import json
import os
from io import StringIO
from uav-safety.streamlit_app import read_jsonl

class TestDashboardCritical(unittest.TestCase):
    def setUp(self):
        # Create sample collision log file
        self.collision_log = 'uav-safety/logs/collision.jsonl'
        with open(self.collision_log, 'w') as f:
            f.write('{"time": "2025-03-10T10:00:00Z", "min_distance": 5.2, "risk": "OK", "distance": 5.2}\n')
            f.write('{"time": "2025-03-10T10:01:00Z", "min_distance": 3.1, "risk": "ALERT", "distance": 3.1}\n')

        # Create sample intrusion log file
        self.intrusion_log = 'uav-safety/logs/intrusion.jsonl'
        with open(self.intrusion_log, 'w') as f:
            f.write('{"time": "2025-03-10T10:00:00Z", "status": "CLEAR"}\n')
            f.write('{"time": "2025-03-10T10:01:00Z", "status": "INTRUSION"}\n')

    def test_read_jsonl_collision(self):
        df = read_jsonl(self.collision_log)
        self.assertFalse(df.empty)
        self.assertIn('risk', df.columns)
        self.assertEqual(df.iloc[1]['risk'], 'ALERT')

    def test_read_jsonl_intrusion(self):
        df = read_jsonl(self.intrusion_log)
        self.assertFalse(df.empty)
        self.assertIn('status', df.columns)
        self.assertEqual(df.iloc[1]['status'], 'INTRUSION')

    def tearDown(self):
        # Clean up log files
        if os.path.exists(self.collision_log):
            os.remove(self.collision_log)
        if os.path.exists(self.intrusion_log):
            os.remove(self.intrusion_log)

if __name__ == '__main__':
    unittest.main()
