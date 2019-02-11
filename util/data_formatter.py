import datetime as date


def object_id(data):
    if type(data) is list:
        for i, x in enumerate(data):
            data[i]['id'] = data[i]['_id']['$oid']
            del data[i]['_id']
        return data
    elif type(data) is dict:
        if '$oid' in data['_id']:
            data['id'] = data['_id']['$oid']
            del data['_id']
            return data
        else:
            raise ValueError
    else:
        raise TypeError


def timestamp(key, data):
    if type(data) is list:
        for i, x in enumerate(data):
            data[i].update(
                {
                    key: date.datetime.utcfromtimestamp(int(data[i][key]['$date']) / 1000).strftime('%Y-%m-%d %H:%M:%S')
                }
            )
        return data
    elif type(data) is dict:
            try:
                data.update(
                    {
                        key: date.datetime.utcfromtimestamp(int(data[key]['$date'])/1000).strftime('%Y-%m-%d %H:%M:%S')
                     }
                )
            except KeyError:
                pass
            finally:
                return data
    else:
        raise TypeError


def object_id_and_timestamp(timestamp_key, data):
    result_formatted_object_id = object_id(data=data)
    formatted_data = timestamp(key=timestamp_key,
                               data=result_formatted_object_id)
    return formatted_data

