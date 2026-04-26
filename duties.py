class Duty:
    pass

class Coin:
    pass

class DutyRepository:
    def get_duty_by_number(self, number):
        pass
    def save_duty(self, duty: Duty):
        pass
    def delete_duty_by_number(self, number):
        pass
    def list_all_duties(self):
        pass
    
class CoinRepository:
    def get_coin_by_name(self, name):
        pass
    def save_coin(salf, coin: Coin):
        pass
    def delete_coin_by_name(self, name):
        pass
    def list_all_coins(self):
        pass

class DatabaseDutyRepository(DutyRepository):
    # placeholder for real db interaction logic
    pass

class DatabaseCoinRepository(CoinRepository):
    # placeholder for real db interaction logic
    pass

class InMemoryDutyRepository(DutyRepository):
    pass

class InMemoryCoinRepository(CoinRepository):
    pass