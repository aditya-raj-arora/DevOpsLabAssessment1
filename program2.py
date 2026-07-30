class Record():
    def __init__(self, region, hours, affect):
        self.region=region
        self.hours=hours
        self.affect=affect
    def printBill(self):
        print("="*43)
        print(f"{'Outage Records for '+self.region:^43}")
        print("-"*43)
        print(f"{'Hours':<20} | {'Affected People':<20}")
        print("-"*43)
        print(f"{self.hours:<20} | {self.affect:<20}")
        print("="*43)
def main():
    inputs=[
        ["Region A", 5, 6000],
        ["Region B", 3, 4000],
    ]
    t=0
    d=0
    l=[]
    L=[]
    records = [Record(inp[0], inp[1], inp[2]) for inp in inputs]
    for record in records:
        if t<record.hours:
            t=record.hours
            T=record
            d+=record.hours
        if record.affect>5000:
            l.append(record)
        L.append((record.hours,record))
        # record.printBill()
    print("\nRegion with Longest Outage:")
    T.printBill()
    print(f"\nTotal Hours of Outage: {d}")
    print("\nRegions with More than 5000 Affected People:")
    for record in l:
        record.printBill()
    print("\nAverage Hours of Outage:", d/len(records) if records else 0)
    print("\nSorted Records by Hours of Outage:")
    L.sort()
    for i in L:
        i[1].printBill()

if __name__=="__main__":
    main()
