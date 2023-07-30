# SELECT mcdp_cd AS "진료과 코드", COUNT(*) AS "5월예약건수"
#     FROM appointment
#     WHERE DATE_FORMAT(apnt_ymd,"%Y%m") = "202205"
#     GROUP BY mcdp_cd
#     ORDER BY "5월예약건수", "진료과 코드";
    
SELECT mcdp_cd '진료과 코드', COUNT(mcdp_cd) '5월예약건수'
	FROM appointment
	WHERE LEFT(apnt_ymd,7)='2022-05'
	GROUP BY mcdp_cd
	ORDER BY COUNT(mcdp_cd), mcdp_cd