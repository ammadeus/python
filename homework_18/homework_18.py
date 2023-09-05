# 1.Write a test for the Bank class that we wrote in 14 lesson. You should write a test for the open_account method.
# Ensure that the account is opened and has balance.

import unittest

class Bank:
    @staticmethod
    def open_account(name, initial_balance):
        pass

class TestBankOpenAccount(unittest.TestCase):

    def test_open_account(self):
        # Chiamata al metodo open_account
        account_number = Bank.open_account("Nome Cognome", 1000)  
        self.assertIsInstance(account_number, int)
        self.assertTrue(Bank.is_account_open(account_number))  
        self.assertEqual(Bank.get_balance(account_number), 1000)  

if __name__ == '__main__':
    unittest.main()

    
# 2. Test update method. It should check that code added interest and sent a message (print function was called).


import unittest

class Bank:
    @staticmethod
    def open_account(name, initial_balance):
        pass
    
    @staticmethod
    def update(account_number):
        pass
    
    @staticmethod
    def get_balance(account_number):
        pass
    
    @staticmethod
    def is_message_sent(account_number):
        pass

class TestBankUpdateMethod(unittest.TestCase):

    def test_update_method(self):
        account_number = 123  

        Bank.update(account_number)
        initial_balance = 1000  
        interest_rate = 0.10    
        expected_balance = initial_balance * (1 + interest_rate)
        actual_balance = Bank.get_balance(account_number)
        self.assertAlmostEqual(actual_balance, expected_balance, places=2)
        print(f"Saldo atteso: {expected_balance:.2f}")
        print(f"Saldo effettivo: {actual_balance:.2f}")
        self.assertTrue(Bank.is_message_sent(account_number))
        print("Messaggio inviato: True")

if __name__ == '__main__':
    unittest.main()