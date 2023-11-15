/* [Programmers] 131120. 3월에 태어난 여성 회원 목록 출력하기 */

SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER = 'W' and TLNO is not NULL and MONTH(DATE_OF_BIRTH) = '03'
ORDER BY MEMBER_ID asc;
