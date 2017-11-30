from C6E4 import *
promos = [fidelity_promo, bulk_item_promo, large_order_promo]
def best_promo(order):
    '''选择折扣最大的方法'''
    # for promo in promos:
        # print('Discount:',promo(order))
    return max(promo(order) for promo in promos)
print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))