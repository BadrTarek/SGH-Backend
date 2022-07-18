def project_server():
    return "http://127.0.0.1:8000/"


def print_error_in_console(request_name , error):
    print("\n" + "*" * 70 + request_name + "*" * 70 + "\n")
    print(error)
    print("\n" + "*" * 100 + "\n")
    
