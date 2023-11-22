# [Programmers] 42577. 전화번호 목록

def solution(phone_book):
    phone_set = set()
    for phone in phone_book:
        for i in range(1, len(phone)):
            phone_set.add(phone[:i])
    
    for phone in phone_book:
        if phone in phone_set:
            return False
    return True