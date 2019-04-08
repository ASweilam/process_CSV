import csv

# this code just process csv that has two args column (numbers) and a third opr as operator string (add, sub, div). No exceptions handling
# were added as it was not required. 

def ReadOperate(CSVFile):
    for row in csv.DictReader(open(CSVFile)):
        if row["opr"] == "add":
            result = int(row["arg1"]) + int(row["arg2"])
            dic = {"arg1": int(row["arg1"]), "arg2": int(row["arg2"]), "opr": row["opr"], "result": result}
            with open('output_file.csv', 'a', newline='') as f:
                w = csv.DictWriter(f, dic.keys())
                w.writerow(dic)
        elif row["opr"] == "sub":
            result = int(row["arg1"]) - int(row["arg2"])
            dic = {"arg1": int(row["arg1"]), "arg2": int(row["arg2"]), "opr": row["opr"], "result": result}
            with open('output_file.csv', 'a', newline='') as f:
                 w = csv.DictWriter(f, dic.keys())
                 w.writerow(dic)
        elif row["opr"] == "div":
            result = int(row["arg1"]) / int(row["arg2"])
            dic = {"arg1": int(row["arg1"]), "arg2": int(row["arg2"]), "opr": row["opr"], "result": result}
            with open('output_file.csv', 'a', newline='') as f:
                 w = csv.DictWriter(f, dic.keys())
                 w.writerow(dic)

if __name__ == '__main__':

    ReadOperate('intr1.csv')  #add csv input file with arg1,arg2, opr as headers. then 1, 2, add as a data row.