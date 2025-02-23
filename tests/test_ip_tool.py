import unittest
import tempfile
from io import StringIO
import sys

# Import the check_collision function from ip_tool.py
from ip_tool import check_collision

class TestIPTool(unittest.TestCase):

    def run_check_collision(self, content):
        # Write the provided content to a temporary file
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            tmp.write(content)
            tmp_name = tmp.name
        
        # Capture the output of check_collision
        captured_output = StringIO()
        sys_stdout_backup = sys.stdout
        sys.stdout = captured_output
        try:
            check_collision(tmp_name)
        finally:
            sys.stdout = sys_stdout_backup
        
        return captured_output.getvalue()

    def test_no_collision(self):
        content = "192.168.1.0/24\n10.0.0.0/24\n"
        output = self.run_check_collision(content)
        self.assertIn("No collisions found", output)

    def test_collision(self):
        # In this example 192.168.1.0/24 and 192.168.1.128/25 overlap
        content = "192.168.1.0/24\n192.168.1.128/25\n"
        output = self.run_check_collision(content)
        self.assertIn("Colliding IP networks found", output)
        self.assertIn("192.168.1.0/24 collides with 192.168.1.128/25", output)

if __name__ == '__main__':
    unittest.main()
