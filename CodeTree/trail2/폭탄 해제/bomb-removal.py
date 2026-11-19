unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class unlock:
    def __init__(self, unlock_code, wire_color, seconds):
        self.uc = unlock_code
        self.wc = wire_color
        self.sec = seconds

ul = unlock(unlock_code, wire_color, seconds)
print("code :", ul.uc)
print("color :", ul.wc)
print("second :", ul.sec)