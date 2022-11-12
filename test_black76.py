import black76
import pandas as pd
import unittest

class TestOption(unittest.TestCase):
    '''
    Values from https://www.lme.com/en/trading/contract-types/options/black-scholes-76-formula
    '''
    def test_constructor(self):
        '''
        Checks that Option object is instantiated
        '''
        flag = False
        inputs_dict_base = {'price': 2006.0, 
                      'strike': 2100.0, 
                    'interest': 0.051342, 
                    'maturity': 0.084931507, 
              'time_to_prompt': 0.123287671, 
                 'option_type': 'call', 
                  'volatility': 0.35}
        options = black76.Option(inputs_dict_base)
        self.assertIsInstance(options, black76.Option)


    def test_validate_data_base(self):
        '''
        Base case, all inputs correct type
        '''
        flag = False
        inputs_dict_base = {'price': 2006.0, 
                      'strike': 2100.0, 
                    'interest': 0.051342, 
                    'maturity': 0.084931507, 
              'time_to_prompt': 0.123287671, 
                 'option_type': 'call', 
                  'volatility': 0.35}
        try:
            options = black76.Option(inputs_dict_base)
            options.validate_data()
        except:
            flag = True
        self.assertFalse(flag)

    def test_validate_data_bad(self):
        '''
        Missing strike price.
        '''
        flag = False
        inputs_dict_base = {'price': 2006.0, 
                      #missing strike
                    'interest': 0.051342, 
                    'maturity': 0.084931507, 
              'time_to_prompt': 0.123287671, 
                 'option_type': 'call', 
                  'volatility': 0.35}
        try:
            options = black76.Option(inputs_dict_base)
            options.validate_data()
        except Exception:
            flag = True
        self.assertTrue(flag)

    def test_calc_discount_factor_base(self):
        '''
        Base case, all inputs present and correct
        '''
        inputs_dict_base = {'price': 2006.0, 
                      'strike': 2100.0, 
                    'interest': 0.051342, 
                    'maturity': 0.084931507, 
              'time_to_prompt': 0.123287671, 
                 'option_type': 'call', 
                  'volatility': 0.35}
        options = black76.Option(inputs_dict_base)
        d = options.calc_discount_factor()
        self.assertAlmostEqual(d, 0.993846, places=6)
    
    def test_calc_price_base(self):
        '''
        Base case, all inputs present and correct
        '''
        inputs_dict_base = {'price': 2006.0, 
                      'strike': 2100.0, 
                    'interest': 0.051342, 
                    'maturity': 0.084931507, 
              'time_to_prompt': 0.123287671, 
                 'option_type': 'call', 
                  'volatility': 0.35}
        options = black76.Option(inputs_dict_base)
        prices = options.calc_price()
        self.assertEqual(prices, 44.49088684770973)
    
    def test_get_data(self):
        '''
        Base case, all inputs present and correct
        '''
        DATA_PATH = 'data.csv'
        data = black76.get_data(DATA_PATH)
        self.assertIsInstance(data, pd.DataFrame)

    def test_run_all(self):
        '''
        Base case, all inputs present and correct
        '''
        DATA_PATH = 'data.csv'
        actual = black76.run(DATA_PATH)
        expected = {"{'price': 2006, 'strike': 2100, 'interest': 0.051342, 'maturity': 0.084931507, 'time_to_prompt': 0.123287671, 'option_type': 'call', 'volatility': 0.35}"\
                    : {'call': 44.49088684770973, 'put': 137.8972561318364}}
        self.assertTrue(all([lambda key: actual[key] == expected[key] for key in actual]))

if __name__ == '__main__':
    unittest.main()