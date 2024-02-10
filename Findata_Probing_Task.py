#financials function reads and analyses files

def financials(filename):
    with open(filename, 'r') as file:
        data = {}
        for line in file:
            if ':' in line:
                key, value = line.strip().split(': ')
                if key in ['Revenue', 'Expenses', 'Net Income', 'EPS', 'Assets', 'Liabilities', 'Equity']:
                    data[key] = float(value.strip('$').replace(',', ''))
                else:
                    data[key] = value
        return data
#calls financials function to print the results(difference Quarter2 and Quarter1)

companyA_quarter1 = financials('CompanyA_Quarter1.txt')
companyA_quarter2 = financials('CompanyA_Quarter2.txt')
companyB_quarter1 = financials('CompanyB_Quarter1.txt')
companyB_quarter2 = financials('CompanyB_Quarter2.txt')

print("Difference between CompanyA Quarter2 and Quarter1")
for key in ['Revenue', 'Expenses', 'Net Income', 'EPS', 'Assets', 'Liabilities', 'Equity']:
    difference = companyA_quarter2[key] - companyA_quarter1[key]
    print(f"{key}: ${difference}")

print("\nDifference between CompanyB Quarter2 and Quarter1")
for key in ['Revenue', 'Expenses', 'Net Income', 'EPS', 'Assets', 'Liabilities', 'Equity']:
    difference = companyB_quarter2[key] - companyB_quarter1[key]
    print(f"{key}: ${difference}")




