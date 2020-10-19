

#creating Round class here
class Round_Handler:
    def __init__(self,round_id, owner, brewer ,active_status):
        self.round_id = round_id
        self.brewer = brewer
        self.owner = owner
        self.active_status = active_status
        self.round_history = []

    def add_to_round(self,order_id,name,drink):
        self.round_history.append({"RoundID": self.round_id,"OrderID":order_id,"Name": name, "Drink": drink})
