def dataframeToDictlist(org_data):
    fields = org_data.keys()
    data_list = []
    num = len(org_data[fields[0]])
    print("total number:"+str(num))
    for n in range(num):
        tmp_record = dict()
        for field in fields:
            tmp_record[field] = org_data[field][n]
        data_list.append(tmp_record)
    print("total number after change:"+str(len(data_list)))
    return data_list
