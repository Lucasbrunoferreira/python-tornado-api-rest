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
            data[i].update({key: parse_to_datetime(data[i][key]['$date'])})
        return data
    elif type(data) is dict:
            try:
                data.update({key: parse_to_datetime(data[key]['$date'])})
            except KeyError:
                pass
            finally:
                return data
    else:
        raise TypeError


def parse_to_datetime(timestamp_to_format):
    normalize_timestamp = int(timestamp_to_format) / 1000
    utc_date = date.datetime.utcfromtimestamp(normalize_timestamp)
    return utc_date.strftime('%Y-%m-%d %H:%M:%S')


def object_id_and_timestamp(timestamp_key, data):
    result_formatted_object_id = object_id(data=data)
    formatted_data = timestamp(key=timestamp_key,
                               data=result_formatted_object_id)
    return formatted_data

