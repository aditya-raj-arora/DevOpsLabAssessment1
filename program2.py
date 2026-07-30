class Order():
    def __init__(self, name, item, quan, price):
        self.name=name
        self.item=item
        self.quan=quan
        self.price=price
        self.cost=quan*price
    def printBill(self):
        print("Order for", self.name)
        print("="*50)
        print(f"{self.item:<20} | {self.quan:<10} | {self.price:<10} | {self.cost:<10}")
def main():
    inputs=[
        ["John Doe", "Breaad", 15, 30],
        ["Jane Doe", "Maggi", 5, 80]
    ]
    m=0
    d={}
    t=0
    l=[]
    for inp in inputs:
        o=Order(inp[0],inp[1], inp[2], inp[3])
        o.printBill()
        if m<o.cost:
            m=o.scost
            M=o
        if o.item not in d:
            d[o.item]=1
        else:
            d[o.item]+=1
        t+=o.cost
        l.append((o.cost,o))
    l.sort()
    for i in l:
        i.printBill()

if __name__=="__main__":
    main()
