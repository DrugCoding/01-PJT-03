import sys

sys.stdin = open("_신용카드만들기1.txt")

a = int(input())
card = []
for i in range(a):
    num_ = input()
    card_ = []
    if num_[0] == '3' or num_[0] == '4' or num_[0] == '5' or num_[0] == '6' or num_[0] == '9':
        card_.append(num_)
        print(card_)
        sum_ = 0
        for i in range(a):
            sum_ += card_.count(i)
            if sum_ > 16:
                card.append(card_)

print(card)