/* 151139. 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기 */

SELECT MONTH(START_DATE) as MONTH, CAR_ID, COUNT(CAR_ID) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE YEAR(START_DATE) = 2022 AND MONTH(START_DATE) BETWEEN 8 AND 10
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
    ) AND YEAR(START_DATE) = 2022 AND MONTH(START_DATE) BETWEEN 8 AND 10
GROUP BY MONTH, CAR_ID
ORDER BY MONTH asc, CAR_ID desc;