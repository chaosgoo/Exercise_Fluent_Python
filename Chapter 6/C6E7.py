from C6E4 import *
promos = [globals()[name] for name in globals()
            if name.endswith('_promo')
                and name != 'best_promo']

def best_promo(order):
    '''选择可用的最佳折扣'''
    return max(promo(order) for promo in promos)

print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))