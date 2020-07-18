import matplotlib.pyplot as plt
import DB


def drawGraphs():

    database = DB.DBClass()

    database.getDB()
    DB.fillData()

    vals_in_installment = DB.output_products_count_in_installments
    vals_no_in_installment = DB.output_products_count_no_in_installments
    allVals = vals_in_installment + vals_no_in_installment
    allNames = DB.output_products_name
    labels = ["В рассрочку", "Разовая оплата"]
    
    percent1 = (sum(vals_in_installment) / sum(allVals)) * 100
    percent2 = (sum(vals_no_in_installment) / sum(allVals)) * 100

    result = [percent1, percent2] 

    plt.figure(figsize=(12.8,5), dpi=80)
    plt.subplot(1, 2, 1)
    plt.pie(result, autopct='%1.1f%%')
    plt.legend(labels)
    plt.subplot(1, 2, 2)
    plt.bar(allNames, allVals)
    plt.tight_layout()

    plt.savefig('outputGraph.png')
    plt.close()

