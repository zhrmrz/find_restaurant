from collections import Counter
class Sol:
    def find_restaurant(self,list1,list2):
        cnt1=Counter(list1+list2)
        return list(cnt1.keys())[0]



if __name__ == '__main__':
    p1=Sol()
    print(p1.find_restaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))
