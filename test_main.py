import pytest
from main import BankAccount

#testing for the balances in the accounts
@pytest.mark.parametrize("initial_amount, output", [(100, 100), (200, 200), (300, 300)])
def test_balance(initial_amount, output):
    object = BankAccount(initial_amount, "USD")
    user_balance = object.my_balance()
    expected_balance = f"Your account balance is {output}"
    assert expected_balance == user_balance


# parametrize allows us have a fill of testing multiple users with diffrent test senerios.
# it takes in this valriables initial_amount, deposit, expected_balance_amount (100(this is the initial_amount), 50 (This is the deposite), 150(this is the expected amount))
@pytest.mark.parametrize(
    "initial_amount, deposit, expected_balance_amount",
    [(100, 50, 150), (200, 200, 400), (300, 300, 600)],
)
def test_deposit(initial_amount, deposit, expected_balance_amount):
    currency = "USD"

    object = BankAccount(initial_amount, "USD")
    user_deposit = object.deposit(deposit)
    expected_message = f"Deposit of {currency} {deposit} successful. Your new balance is {currency} {expected_balance_amount}"
    assert expected_message == user_deposit

# checking for a negative deposit
def test_faliure_on_negative_deposit():
    initial_amount = 100
    currency = "USD"
    deposit = -200

    Rodger = BankAccount(initial_amount, "USD")
    user_deposit = Rodger.deposit(deposit)
    expected_message = f"Sorry negative value ({deposit}) not allowed"
    assert user_deposit == expected_message

    # check that balance was not updated
    user_balance = Rodger.my_balance()
    expected_balance = f"Your account balance is {initial_amount}"
    assert user_balance == user_balance

# checking for withdrawals from the account
def test_withdraw():
    initial_amount = 100
    currency = "USD"
    withdraw_amount = 50

    Rodger = BankAccount(initial_amount, "USD")
    user_withdraw = Rodger.withdraw(withdraw_amount)
    expected_message = f"Withdrawal successful. Your new balance is {currency} {initial_amount - withdraw_amount}"
    assert expected_message == user_withdraw

#checking for excess withdrawals that are more the actual balance
def test_withdraw_more_than_balance():
    initial_amount = 100
    currency = "USD"
    withdraw_amount = 200

    Rodger = BankAccount(initial_amount, "USD")
    user_withdraw = Rodger.withdraw(withdraw_amount)
    expected_message = "Insufficient balance"
    assert expected_message == user_withdraw

#checking for withdrawal of the actual balance
def test_withdraw_of_same_amount():
    initial_amount = 100
    currency = "USD"
    withdraw_amount = 100

    Rodger = BankAccount(initial_amount, "USD")
    user_withdraw = Rodger.withdraw(withdraw_amount)
    expected_message = f"Withdrawal successful. Your new balance is {currency} {initial_amount - withdraw_amount}"
    assert expected_message == user_withdraw

# checking for negative withdrawals
def test_faliure_on_negative_withdraw():
    initial_amount = 100
    currency = "USD"
    withdraw_amount = -50

    Rodger = BankAccount(initial_amount, "USD")
    user_withdraw = Rodger.withdraw(withdraw_amount)
    expected_error = f"Sorry negative value ({withdraw_amount}) not allowed"
    expected_balance = initial_amount

    assert user_withdraw == expected_error
    user_balance = Rodger.my_balance()
    expected_balance = f"Your account balance is {initial_amount}"
    assert user_balance == user_balance
