'''match_case:= 👉 match-case is like switch statement (in other languages)

👉 It is used to check one value with many conditions 

✔ match → value to check
✔ case → different conditions
✔ _ → default case (like else)'''


def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal server error"
        case _:
            return "unknown status"
        
print(http_status(404))