from Gem import Gem


def selection_sort_by_price(price_list):
    for i in range(len(price_list)):
        for j in range(i + 1, len(price_list)):
            if price_list[i].price < price_list[j].price:
                price_list[i], price_list[j] = price_list[j], price_list[i]
                Gem.compare_count()
                Gem.change_count()
    return price_list