def split_messages(a):
    b = []
    for x in a:
        if x.decode().startswith('+CMGL:'):
            r = a.index(x)
            t = r+1
            q = str.encode(a[r].decode(), 'utf-8')
            q = q.decode().strip().replace('\"','')
            q = q.split(',')
            z = str.encode(a[t].decode('utf-8'), 'utf-8') 
            z = z.decode('utf-8').rstrip().replace('\"','')
            b.append(
                        {
                        'from':q[2],
                        'date':q[4],
                        'time':q[5],
                        'mesg':z,
                        }
                    )
    return b

