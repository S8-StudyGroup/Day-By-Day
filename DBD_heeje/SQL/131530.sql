/* [Programmers] 131530. 가격대 별 상품 개수 구하기 */

SELECT PriceGroup * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM (
    SELECT FLOOR(PRICE / 10000) AS PriceGroup
    FROM PRODUCT
) AS PriceGroupTable
GROUP BY PriceGroup
ORDER BY PriceGroup;