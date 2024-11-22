import sys

def solve(items):
    itemlist = items.split(';')

    freq = {}

    for item in itemlist:
        if freq.get(item) == None:
            freq[item] = 1
        else:
            freq[item] +=1
    maxfreq = 0
    res = 0
    for item in itemlist:
        if freq[item] > maxfreq:
            maxfreq=freq[item]
            res = item
    print(res)

def main():
    solve('apple;laptop;apple;laptop;laptop')
if __name__=='__main__':
    main()

