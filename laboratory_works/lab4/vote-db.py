from random import randint
import math
import functools

class Congressman:
    def __init__(self, name='Ivan', price=None):
        if price == None:
            dice = randint(1, 100)
            if dice <= 20:
                price = math.inf
            elif dice <= 30:
                price = 0
            else:
                price = randint(1, 1000)
        self.name = name
        self.price = price

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return '{0}: {1}'.format(self.name, self.price)

    def give(self, payment):
        return self.price <= payment


def generate_congressmans(count):
    return [Congressman() for n in range(count)]


def vote(price, data, print_data=False):
    money_amount = data['money_amount']
    congressmans = data['congressmans']
    friends = data['friends']
    neutrals = data['neutrals']
    enemies = data['enemies']

    if money_amount < price * len(list(filter((lambda x: 0 < x.price < math.inf), congressmans))):
        raise ValueError('Not enough money')
    votes = 0
    for c in congressmans:
        if c.price == 0:
            votes += 1
            if c not in friends:
                friends.add(c)
        else:
            voted = False
            if c not in enemies:
                voted = c.give(price)
                money_amount -= price
            if voted:
                votes += 1
            if c.price == math.inf:
                if c not in enemies:
                    enemies.add(c)
            else:
                if c not in neutrals:
                    neutrals.add(c)
    votes_percents = votes / len(congressmans) * 100
    if print_data:
        print('friends:', len(friends))
        print('neutrals:', len(neutrals))
        print('enemies:', len(enemies))
        print('votes:', votes)
        print('percent:', votes_percents)
    return votes_percents


def main(money_amount, price, print_data=True):
    data = {
        'money_amount': money_amount,
        'congressmans': generate_congressmans(450),
        'friends': ListSet(),
        'neutrals': ListSet(), 'enemies': ListSet()
    }
    vote(price, data, print_data)


main(10000000, 300)