from openpyxl import load_workbook

wb = load_workbook(filename='兑换码 沈阳 实体卡，聂超 20161128 -.xlsx', read_only=True)
ws = wb['Sheet1']
rows = list(ws.rows)
for row in rows:
    row = list(row)
    var = '\'' + str(row[3].value) + '\''
    print(var + ',', end='')

print('')
print("MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBANB8/mt/j4WzukHi" +
            "E/JtqgmhQ9eni016GkXiN5QrgCvgb7R7PuccYDGoiYDDMJctKC68VDJ1vRolGVnC" +
            "vur0vas2+ALvB5UvxNoeiXNcaaBVL2aekUC1ypF8SF3GvmMNxcfusZmW0OWEg6K8" +
            "vFPwJLAjJEMKK1+DNiqWqWGOH1mrAgMBAAECgYEAruAZG5wMi45cbcSvDIq1tIwi" +
            "9rGfI+aGQRXlno/6W1NO/yjdc0cW3LBMXcfbawLCkKkBSq39Zv+1StgSAcw1hfLl" +
            "Vx/g8AKmyr1rqXhuSoz2aSqoTFc7yvxaaaVfDtnNuFyd7KM2oFNKO7MAmIyFN4Jv" +
            "GV/X+G758ugChEQmhTECQQDqFLKZ3A8BX7NX5v/8iO3tqiLAWlD6atitrCTvggNF" +
            "mbgtuHEmG9CPUl8qwXYBDxblWB5K4/tYl1rsk85Dqu4JAkEA5ALMuF0lHzbXJkc3" +
            "RCRItmo9bCOiGOUq0H6VuvW8WFmnHmVir0qjkcujkFuh1uWhoCjnD5GREv5dNG63" +
            "5933EwJBAM29N2VoN4Abn0QJcsGBkK4ttbGfMEGJm7y56xTgDwQjoe/9huXZ2Ku/" +
            "2Il51MAFhTg7BRUJ4KbzESWSm9555BECQAHOP97J5gxcO9HyyG5Ct0yyhLABjDwU" +
            "PIWQKxFi9s3gT+F+vgxTU/5IlZAEGcEA6onBKStHZNW4q/ZJVi2A5X8CQAEmhqGO" +
            "Clvk6DGdC8uxQMeJxVXWH83KaDEVf1imRCAoQKsZbysEXjSk0GkBzDFnmI0kBHwZ" +
            "NHj0uIfgGipMMuo=")

print('MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDI6d306Q8fIfCOaTXyiUeJHkrIvYI'
    		+ "SRcc73s3vF1ZT7XN8RNPwJxo8pWaJMmvyTn9N4HQ632qJBVHf8sxHi/fEsraprwCtzvzQETrNRwVxLO5jVmRGi60j8Ue1efIlzPXV9je9"
    		+ "mkjzOmdssymZkh2QhUrCmZYI/FCEa3/cNMW0QIDAQAB")

str="123"
str=""
