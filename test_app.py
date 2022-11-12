import app
from flask import Flask, request, jsonify
import pandas as pd
import unittest

class TestApp(unittest.TestCase):

    def test_upload_file_base(self):
        """
        Quick test. Production code would 
        have more robust tests. 
        """
        tester = app.create_app().test_client()
        flag = False
        try:
            response = tester.post('/upload')
        except:
            flag = True
        finally:
            self.assertFalse(flag)    
        
    def test_retrieve_data_base(self):
        """
        Quick test. Production code would 
        have more robust tests. 
        """
        tester = app.create_app().test_client()
        flag = False
        try:
            response = tester.get("/retrieve")
        except:
            flag = True
        finally:
            self.assertFalse(flag)   

if __name__ == '__main__':
    unittest.main()