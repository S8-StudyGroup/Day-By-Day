/* [Programmers] 131115. 가격이 제일 비싼 식품의 정보 출력하기 */

SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE desc limit 1;
