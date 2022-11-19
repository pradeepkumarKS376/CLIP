import re

import PyPDF2

result_list = []
result_list2 = []
result=""

pdf_path = r"D:\Check\SALT Tax Bill\485686-PropertyTaxBill-2022.pdf"
#pdf_path = "D:\Check\990702118000000000.PDF"
#pdf_path= "D:\Check\Property.pdf"
search_keywords= ['Account Number','Total Amount Due For July 2022','Appraised Value']
#search_keywords= ['Account Number:','Deadline for filing a protest:','Appraised  Value:']
#search_keywords=['Property ID:','DATE OF NOTICE:','Situs:','Deadline for filing a protest:','2022 Exemption Amount']
Inputtext=""

def SearchTextExist(pdf_path,search_keywords,result):
    pdfFileObj = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for page_number in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(page_number)
        page_content = pageObj.extractText()
        for search_terms in search_keywords:
            #Search = re.compile("[a-zA-z\ ]+:+[\ ]+[0-9]+|[a-zA-Z0-9\: ]+[\$0-9 ,-]+|[a-z\t0-9\%]+")
            Search = re.compile("[a-zA-Z0-9\ \,]+")
            AccNo = Search.findall(page_content)
            for i in AccNo:
                i = str(i).lower()
                print(i)
                search_terms = str(search_terms).lower()
                if search_terms in i:
                    #print(i)
                    result = {"page": page_number, "": i}.__str__().lower().replace("'","")
                    result_list.append(result)
                    #print("Keyword found")
                else:
                    #result = {"page": page_number, "": i}.__str__().lower().replace("'", "")
                    result_list2.append(result)
                    #print(i+" :Keyword Not found")
                    #Search = re.compile(" [a-zA-Z0-9\ \:]+[\$0-9\,]+")
    print(result_list)
    #print(result_list2)
    return result_list

SearchTextExist(pdf_path,search_keywords,result)