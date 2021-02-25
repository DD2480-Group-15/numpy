import os

def write_it(method_name, record):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, method_name + "_coverage.txt")
    f = open(filename, "a+")
    f.writelines(record)
    f.close()

def check_coverage(number_of_branches, method_name):
    f = open(method_name + "_coverage.txt", "r+")
    thelist = list(set(f.read().split(" ")))
    f.close()
    print(thelist)
    nmbr = number_of_branches
    missing = []
    for i in range(number_of_branches):
        if str(i+1) not in thelist:
            nmbr -= 1
            missing.append(str(i+1))

    coverage = (nmbr/number_of_branches)*100
    f = open("coverage_total.txt", "a+")
    f.writelines("----------------------------------------------------------------\n")
    f.writelines("Coverage for " + method_name + "\n")
    f.writelines("Coverage is: " + str(coverage) + " percent\n")
    if missing:
        branches = ""
        for i in range(len(missing)):
            branches += "ID" + str(missing[i])
            if not i+1 == len(missing):
                branches += ", "
        f.writelines("Missing branches are: " + branches)
    f.writelines("\n----------------------------------------------------------------\n")


if __name__ == '__main__':
    #write_it("einsum", ["1 ","2 ","3 "])
    check_coverage(16, "einsum")
    check_coverage(24, "einsum_path")