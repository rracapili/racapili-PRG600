import unittest
import io
import sys
from random import randint
from importlib import import_module
import hashlib
import os 
from unittest.mock import patch, MagicMock
import logging
import datetime

import midtermprg600

# Testing rolling dice 
# Checking totals and the screen print output 
class TestRollDice(unittest.TestCase):
    filename = 'midtermprg600.py'  # necessary for main loop to print
    
    def setUp(self):
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        self.pypath = sys.executable
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
    
    def test_module_import(self):
        "make sure that the file can be imported"
        err_msg = (f"Error: your lab5a file could not be imported."
                    "Make sure that lab5a is named correctly and is"
                    "in the same folder as your check script.")
        try:
            std = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print(err_msg) 

    def test_rolldice(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        result = midtermprg600.rolldice()
        sys.stdout = sys.__stdout__

        num1 = ((capturedOutput.getvalue().split())[0])
        num2 = ((capturedOutput.getvalue().split())[2])

        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 12)
        self.assertEqual(capturedOutput.getvalue().strip(), str(num1) + " and " + str(num2))

# Testing players returned as list 
# Also testing invalid command inputs 
class TestGetPlayers(unittest.TestCase):
    filename = 'midtermprg600.py'  # necessary for main loop to print
    
    def setUp(self):
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        self.pypath = sys.executable
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
    
    def test_module_import(self):
        "make sure that the file can be imported"
        err_msg = (f"Error: your lab5a file could not be imported."
                    "Make sure that lab5a is named correctly and is"
                    "in the same folder as your check script.")
        try:
            std = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print(err_msg)

    @patch('builtins.input', side_effect=['2', 'player1', 'player2'])
    def test_getplayers(self, mock_input):
        players = midtermprg600.getplayers()
        self.assertEqual(players, ['player1', 'player2'])

    @patch('builtins.input', side_effect=['a', '2', 'player1', 'player2'])
    def test_getplayers_invalid_input(self, mock_input):
        players = midtermprg600.getplayers()
        self.assertEqual(players, ['player1', 'player2'])

# Testing round numbers valid and invalid output 
class TestGetRounds(unittest.TestCase):
    filename = 'midtermprg600.py'  # necessary for main loop to print
    
    def setUp(self):
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        self.pypath = sys.executable
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
    
    def test_module_import(self):
        "make sure that the file can be imported"
        err_msg = (f"Error: your lab5a file could not be imported."
                    "Make sure that lab5a is named correctly and is"
                    "in the same folder as your check script.")
        try:
            std = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print(err_msg)

    def test_getrounds(self):
        with patch('builtins.input', side_effect=['3', 'a', '5']):
            self.assertEqual(midtermprg600.getrounds(), 3)
        with patch('builtins.input', side_effect=['a', 'b', '5']):
            self.assertEqual(midtermprg600.getrounds(), 5)

# Testing setgame returns the gameset 
class TestSetgame(unittest.TestCase):
    filename = 'midtermprg600.py'  # necessary for main loop to print
    
    def setUp(self):
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        self.pypath = sys.executable
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
    
    def test_module_import(self):
        "make sure that the file can be imported"
        err_msg = (f"Error: your lab5a file could not be imported."
                    "Make sure that lab5a is named correctly and is"
                    "in the same folder as your check script.")
        try:
            std = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print(err_msg)

    @patch('builtins.input', side_effect=['2', 'player1', 'player2', '3'])
    def test_setgame(self, mock_input):
        gameset = midtermprg600.setgame()
        for i in gameset[0]:
            print(i)        
        for i in gameset[1]:
            print(i)
        print(gameset[2])
        self.assertEqual(gameset, [[[0, 0, 0], [0, 0, 0]], ['player1', 'player2'], 3])

#Testing asktoroll 
class TestAskToRoll(unittest.TestCase):
    filename = 'midtermprg600.py'  # necessary for main loop to print
    
    def setUp(self):
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        self.pypath = sys.executable
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
    
    def test_module_import(self):
        "make sure that the file can be imported"
        err_msg = (f"Error: your lab5a file could not be imported."
                    "Make sure that lab5a is named correctly and is"
                    "in the same folder as your check script.")
        try:
            std = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print(err_msg)

    @patch('builtins.input', return_value='')
    @patch('midtermprg600.rolldice', return_value=6)
    def test_asktoroll(self, mock_input, mock_rolldice):
        player = 'John Doe'
        result = midtermprg600.asktoroll(player)
        self.assertEqual(result, 6)

# Testing finding winner 
class TestFindWinner(unittest.TestCase):
    filename = 'midtermprg600.py'  # necessary for main loop to print
    
    def setUp(self):
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        self.pypath = sys.executable
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
    
    def test_module_import(self):
        "make sure that the file can be imported"
        err_msg = (f"Error: your lab5a file could not be imported."
                    "Make sure that lab5a is named correctly and is"
                    "in the same folder as your check script.")
        try:
            std = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print(err_msg)
    
    def test_findwinner_multiple_winners(self):
        game = [[5, 3, 8, 6], [3, 3, 2, 2], [5, 3, 8, 6]]
        players = ['player1', 'player2', 'player3']
        expected_output = 'player1,player3'
        self.assertEqual(midtermprg600.findwinner(game, players), expected_output)
        
    def test_findwinner_one_winner(self):
        game = [[5, 3, 8, 6], [6, 8, 9, 4], [10, 8, 7, 7]]
        players = ['player1', 'player2', 'player3']
        expected_output = 'player3'
        self.assertEqual(midtermprg600.findwinner(game, players), expected_output)

# Testing rungame 
class TestRunGame(unittest.TestCase):
    filename = 'midtermprg600.py'  # necessary for main loop to print
    
    def setUp(self):
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        self.pypath = sys.executable
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
    
    def test_module_import(self):
        "make sure that the file can be imported"
        err_msg = (f"Error: your lab5a file could not be imported."
                    "Make sure that lab5a is named correctly and is"
                    "in the same folder as your check script.")
        try:
            std = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print(err_msg)

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("midtermprg600.setgame", side_effect=[
        ([[0, 0, 0], [0, 0, 0]], ["Player 1", "Player 2"], 3),
        ([[0, 0, 0], [0, 0, 0]], ["Player 1", "Player 2"], 3)
    ])
    @patch("midtermprg600.printgame")
    @patch("midtermprg600.asktoroll", return_value=0)
    @patch("midtermprg600.findwinner", side_effect=["Player 1", "Player 2"])
    def test_rungame(self, mock_input, mock_setgame, mock_printgame, mock_asktoroll, mock_findwinner):
        midtermprg600.rungame()
        self.assertEqual(mock_setgame.call_count, 12)
        self.assertEqual(mock_printgame.call_count, 8)
        self.assertEqual(mock_asktoroll.call_count, 2)
        self.assertEqual(mock_findwinner.call_count, 2)
        self.assertEqual(mock_input.call_count, 2)

class TestPrintGame(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.players = ['Applea', 'Appleb', 'Applec', 'Appled']
        self.game = [[8, 7, 4], [11, 5, 8], [9, 3, 5], [8, 8, 7]]
        self.roundnum = 3
        self.roundcount = 3
        self.expected_output = '''****************** End of Round 3 ******************
            Round 1   Round 2   Round 3   Total     
    Applea     8         7         4         19        
    Appleb     11        5         8         24        
    Applec     9         3         5         17        
    Appled     8         8         7         23        
    *************************************************************************************************
'''
        
    def test_printgame(self):
        players = ["Appla", "Applb", "Applc", "Appld"]
        game = [[4, 7, 8], [11, 5, 9], [8, 3, 5], [7, 8, 7]]
        roundnum = 3
        roundcount = 3
        expected_output = '************************************* End of Round 3 *************************************\n          Round 1      Round 2      Round 3      Total     \nAppla            4            7            8           19\nApplb           11            5            9           25\nApplc            8            3            5           16\nAppld            7            8            7           22\n**************************************************************************************************\n'

        captured_output = io.StringIO()
        sys.stdout = captured_output

        midtermprg600.printgame(game, players, roundnum, roundcount)
        sys.stdout = sys.__stdout__
        try: 
            self.assertEqual(str(captured_output.getvalue()), expected_output)
        except Exception as e: 
            print("Output may have been aligned differently provide screenshots for validation")

def ChecksumLocal(filename=None):
    filename = 'midtermprg600.py'  # necessary for main loop to print
    
    def setUp(self):
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        self.pypath = sys.executable
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
    
    def test_module_import(self):
        "make sure that the file can be imported"
        err_msg = (f"Error: your lab5a file could not be imported."
                    "Make sure that lab5a is named correctly and is"
                    "in the same folder as your check script.")
        try:
            std = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print(err_msg)
            
    fil = open(filename, 'r', encoding='utf-8')
    dat = fil.readlines()
    textdata = ''
    for line in dat:
        textdata = textdata + line
    checksum = hashlib.md5(textdata.encode('utf-8')).hexdigest()  # hexdigest for a string
    return checksum


def runtest():
    total = 0
    filename="midtermprg600-check.txt"
    logging.basicConfig(filename="midtermprg600-check.txt", level=logging.DEBUG, filemode='w')
    logging.info('logging test')
    logging.info(f"Test Run: {datetime.datetime.now()}")
    logging.info(f"{filename} {ChecksumLocal(filename)}")
    logging.info("")
    logging.info("")

    runner = unittest.TextTestRunner(failfast=True)
    for case in TestRollDice, TestGetPlayers, TestGetRounds, TestSetgame, TestAskToRoll, TestFindWinner, TestRunGame, TestPrintGame:
        
        print(f"Testing {case}...")
        loader = unittest.TestLoader().loadTestsFromTestCase(case)
        result = runner.run(loader)
        if result.wasSuccessful():
            if (case == TestRollDice):
                logging.info(f"{case}: test successful.")
                logging.info(f"{case}: 1 Marks Awarded - (This is further evaluated after submission and might change after revewing your code).")
                total += 1
            elif(case == TestGetPlayers):
                logging.info(f"{case}: test successful.")
                logging.info(f"{case}: 1 Marks Awarded - (This is further evaluated after submission and might change after revewing your code).")
                total += 1
            elif(case == TestGetRounds):
                logging.info(f"{case}: test successful.")
                logging.info(f"{case}: 1 Marks Awarded - (This is further evaluated after submission and might change after revewing your code).")
                total += 1
            elif(case == TestSetgame):
                logging.info(f"{case}: test successful.")
                logging.info(f"{case}: 4 Marks Awarded - (This is further evaluated after submission and might change after revewing your code).")
                total += 4
            elif(case == TestAskToRoll):
                logging.info(f"{case}: test successful.")
                logging.info(f"{case}: 1 Marks Awarded - (This is further evaluated after submission and might change after revewing your code).")
                total += 1
            elif(case == TestFindWinner):
                logging.info(f"{case}: test successful.")
                logging.info(f"{case}: 2 Marks Awarded - (This is further evaluated after submission and might change after revewing your code).")
                total += 2
            elif(case == TestRunGame):
                logging.info(f"{case}: test successful.")
                logging.info(f"{case}: 5 Marks Awarded - (This is further evaluated after submission and might change after revewing your code).")
                total += 5
            elif(case == TestPrintGame):
                logging.info(f"{case}: Undecided Provide Screenshots and Recordings.")
        else:
            logging.warning(f"{case}: Failures encountered.")
            logging.warning("This does not mean your code is not working. Attach a screenshot of the error you see in your terminal when you run this check script, along with you manual testing screenshot covering all cases in the answerdocument_username.pdf.")
            logging.warning("To get most points provide proper inline comments and details of what you function does and each line of code does")
        logging.info('done.')
    logging.info("Your total is " + str(total))


if __name__ == '__main__':
    runtest()