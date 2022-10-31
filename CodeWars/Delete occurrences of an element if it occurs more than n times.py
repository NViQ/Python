def delete_nth(order,max_e):
    new_order = []
    for i in order:
        if max_e == 1 and new_order.count(i) == 0:
            new_order.append(i)
        elif new_order.count(i) < max_e:
            new_order.append(i)
    print(new_order)


# delete_nth([20, 37, 20, 21], 1) #[20, 37, 21])
delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) #[1, 1, 3, 3, 7, 2, 2, 2])