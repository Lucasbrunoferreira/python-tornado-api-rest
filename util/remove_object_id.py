def remove_objectid(complete_list):
    for i, x in enumerate(complete_list):
        complete_list[i]['id'] = complete_list[i]['_id']['$oid']

        del complete_list[i]['_id']

        print(complete_list)

    return complete_list
