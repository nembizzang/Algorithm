SELECT mcdp_cd '진료과 코드', COUNT(mcdp_cd) '5월예약건수'
	FROM appointment
	WHERE LEFT(apnt_ymd,7)='2022-05'
	GROUP BY mcdp_cd
	ORDER BY COUNT(mcdp_cd), mcdp_cd