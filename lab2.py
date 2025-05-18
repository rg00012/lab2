def display_main_menu():
    print("Enter some numbers separated by commas")

def get_user_input():
    userinput=input()
    numlistbutinstring=[]
    numlistbutinstring=userinput.split(",")

    numlist=[]
    for x in numlistbutinstring:
        numlist.append(int (x))
    return numlist

def calc_average(numlist):
    average=sum(numlist)/len(numlist)
    print("average=" + str(average))
    return average


def find_min_max(numlist):
    minlist=min(numlist)
    maxlist=max(numlist)
    minmaxlist=[minlist,maxlist]
    print("sorted list is: ",minmaxlist)
    return minmaxlist

def sort_temperature(numlist):
    descendinglist=sorted(numlist,reverse=True)
    print("in descending order: ",descendinglist)
    return descendinglist

def calc_median_temperature(numlist):
    import statistics
    medianlist=statistics.median(numlist)
    print("median list=" + str(medianlist))
    return medianlist

def main():
    display_main_menu()
    numlist=get_user_input()
    calc_average(numlist)
    find_min_max(numlist)
    sort_temperature(numlist)
    calc_median_temperature(numlist)

if __name__ == "__main__":
    main()