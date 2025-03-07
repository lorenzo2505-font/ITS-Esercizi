#http status (match statement version)

http_status = 200

match http_status:
    case 200 |  201: # | = or
        print("succes!")
    case 400:
        print("bad request")
    case 401:
        print("not found")
    case 500 | 501:
        print("server error")
    case _ :
        print("unknown")
