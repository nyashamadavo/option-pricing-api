
from math import exp, log, sqrt
import pandas as pd
from statistics import NormalDist

DATA_PATH = 'data.csv'

class Option:

    def __init__(self, inputs: dict) -> None:
        '''Option constructor for both put and call

        Parameters
        ----------
        inputs : dict
            dictionary containing: 
                price (futures price),
                strike, 
                interest (interest rate),
                time_to_prompt (time to prompt), 
                maturity, 
                option type (call or put)
        Uses expressive names for easier validation.  
        '''
        self.price = inputs.get('price')
        self.strike = inputs.get('strike')
        self.interest = inputs.get('interest')
        self.maturity = inputs.get('maturity')
        self.time_to_prompt = inputs.get('time_to_prompt')
        self.option_type = inputs.get('option_type')
        self.volatility = inputs.get('volatility')
        self.option_price = float

    def validate_data(self) -> None:
        """Checks  for valid numerical and string data and raises
        error in case of missing data or wrong data types
        """
        numerical_data = [self.price, self.strike, self.interest, self.time_to_prompt, self.maturity] 
        string_data = [self.option_type]
        if not numerical_data or not string_data:
             raise ValueError('Inputs have missing data')            
        if not all(numerical_data + string_data):
            raise ValueError('Inputs have missing data')
        if not(all([isinstance(float(item), float) for item in numerical_data])) or \
                not(isinstance(string_data[0], str)):
           raise ValueError('Input(s) with incorrect type(s)') 
        if self.option_type not in ('call', 'put'):
            raise ValueError('Missing or incorrect option type') 

    def calc_discount_factor(self) -> float:
        """Calculates the discount factor for the option price 
        """
        ln = log
        self.continuous_interest = ln(1 + self.interest)
        self.discount_factor = exp(-self.continuous_interest * self.time_to_prompt)
        return self.discount_factor

    def calc_price(self) -> float:
        """
        Calculates the option price on a future as per Black76 formula. 
        https://www.lme.com/en/trading/contract-types/options/black-scholes-76-formula
        Uses the variable names from the above referenced documentation to make validation easier 
        since test is time constrained.

        Formula for call:            
        c = exp(-r(T+2/52)) * [F*N(d1) - X*N(d2)]
        Formula for put:
        p = exp(-r(T+2/52)) * [X*N(- d2) - F*N(- d1)]
        where
        d1 = (ln(F/X) + volatility**2 * T/2) / (volatility * sqrt(T)) 
        d2 = d1 - volatility * sqrt(T)
        """
        N = NormalDist(mu=0, sigma=1).cdf
        ln = log
        r = self.interest
        T = self.maturity
        F = self.price
        X = self.strike
        volatility = self.volatility

        d1 = (ln(F/X) + volatility**2 * T/2) / (volatility * sqrt(T))
        d2 = d1 - volatility * sqrt(T)
        c = exp(-r * (T+2/52)) * (F*N(d1) - X*N(d2))
        p = exp(-r * (T+2/52)) * (X*N(-d2) - F*N(-d1))
        self.result_dict = {'call':c, 'put':p}
        return self.result_dict[self.option_type]

    def __repr__(self) -> str:
        return str(self.result_dict)
        
def get_data(DATA_PATH: str) -> pd.DataFrame:
    '''
    Obtains the input parameters from an Excel file

    Parameters
    ----------
    DATA_PATH : str
        Path to file containing data

    Returns:
    --------
    data : pd.DataFrame
        Pricing data for all options 
    '''
    data = pd.read_csv(DATA_PATH)
    data = data.dropna()
    return data

def run(DATA_PATH: str) -> dict:
    data = get_data(DATA_PATH)
    options_dict = {}
    for idx in range(len(data)):        
        inputs = data.iloc[idx,:].to_dict()
        option = Option(inputs)
        option.validate_data()
        option.option_price = option.calc_price() \
             * option.calc_discount_factor()
        options_dict[str(inputs)] = option        
    return options_dict
#print(data.to_dict())
#import pdb; pdb.set_trace();
#o = Option(data.to_dict())
#o.run(DATA_PATH)

if __name__ == '__main__':
    run(DATA_PATH)