secret_code, meeting_point, time = input().split()
time = int(time)

class String:
    def __init__(self, secret_code, meeting_point, time):
        self.sc = secret_code
        self.mp = meeting_point
        self.t = time

str = String(secret_code, meeting_point, time)
print("secret code :", str.sc)
print("meeting point :", str.mp)
print("time :", str.t)