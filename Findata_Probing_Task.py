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

#input name of company

company_name = input("Enter name of your company (Company A or Company B): ")

if company_name == "Company A":
    quarter1 = companyA_quarter1
    quarter2 = companyA_quarter2
#open quarters
    print(f"{company_name} Quarter1:")
    print(quarter1)
    print(f"\n{company_name} Quarter2:")
    print(quarter2)
# prints difference
    print("\nDifference between CompanyA Quarter2 and Quarter1")
    for key in ['Revenue', 'Expenses', 'Net Income', 'EPS', 'Assets', 'Liabilities', 'Equity']:
        difference = companyA_quarter2[key] - companyA_quarter1[key]
        print(f"{key}: ${difference}")    
elif company_name == "Company B":
    quarter1 = companyB_quarter1
    quarter2 = companyB_quarter2
#open quarters    
    print(f"{company_name} Quarter1:")
    print(quarter1)
    print(f"\n{company_name} Quarter2:")
    print(quarter2)
#prints difference
    print("\nDifference between CompanyB Quarter2 and Quarter1")
    for key in ['Revenue', 'Expenses', 'Net Income', 'EPS', 'Assets', 'Liabilities', 'Equity']:
        difference = companyB_quarter2[key] - companyB_quarter1[key]
        print(f"{key}: ${difference}")
else:
    print("your Company name is invalid.Please enter 'Company A' or 'Company B':")






