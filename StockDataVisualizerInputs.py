from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from Constants import Constants

class StockDataVisualizerInputs:
    def __init__(self):
        #TODO: Add input objects for remaining required inputs.
        self.userInputs = {
            Constants.SYMBOL: SymbolInput(),
            Constants.CHARTTYPE: ChartTypeInput()
        }

    def gatherUserInput(self):
        """ 
        Using the required self.userInputs, prompts user for required inputs and validates provided values. 
        Valid inputs are stored in the respective self.userInputs[i].value 
        """
        # For each user input object 
        for field in self.userInputs:
            ui = self.userInputs[field]
            while True:
                #display the optional options txt to display valid options to the user
                print(ui.optionsTxt)
                
                # Prompt the user for valid input
                userInput = input(ui.promptMsg + ":")
                
                # try to set the value which will validate the input
                if(ui.trySetValue(userInput)):
                    # if input is valid move on
                    break
                else:
                    # If input is invalid notify user and continue looping asking for valid input.
                    print("Value '" + userInput + "' is not valid.")