create table "poc_remocon1_2_end_9" as
select 
    time as time,
    regexp_replace( substr( message , 17 ), '\r|\n|\r\n', '') as traceid
from 
    "IoTCoreCWL"."/aws/lambda/postvnext-asia-poc-remoteCommandReceiveAck-lmd"."all_log_streams" 
where
    /* https://tool.konisimple.net/date/unixtime で算出したUNIXTIME に、000 を付加してください。 （ミリ秒なので3桁追加が必要） */
    /*
        end_1 2022-09-08 (14:27)	2022-09-08 (14:42)
        2022-09-08 14:27:00 ⇒  1662614820000
        2022-09-08 14:42:59 ⇒　1662615779999
        end_2 2022-09-08 (14:53)	2022-09-08 (15:08)
        2022-09-08 14:53:00 ⇒　1662616380000
        2022-09-08 15:08:59 ⇒　1662617339999
        end_3 2022-09-08 (15:21)	2022-09-08 (15:36)
        2022-09-08 15:21:00 ⇒　1662618060000
        2022-09-08 15:36:59 ⇒　1662619019999
        end_4 2022-09-08 (15:49)	2022-09-08 (16:04)
        2022-09-08 15:49:00 ⇒　1662619740000
        2022-09-08 16:04:59 ⇒　1662620699999
        end_5 2022-09-08 (16:20)	2022-09-08 (16:35)
        2022-09-08 16:20:00 ⇒　1662621600000
        2022-09-08 16:35:59 ⇒　1662622559999
        end_6 2022-09-08 (16:43)	2022-09-08 (16:58)
        2022-09-08 16:43:00 ⇒　1662622980000
        2022-09-08 16:58:59 ⇒　1662623939999
        end_7 2022-09-08 (17:09)	2022-09-08 (17:19)
        2022-09-08 17:09:00 ⇒　1662624540000
        2022-09-08 17:19:59 ⇒　1662625199999
        end_8 2022-09-08 (17:47)	2022-09-08 (18:02)
        2022-09-08 17:47:00 ⇒　1662626820000
        2022-09-08 18:02:59 ⇒　1662627779999
        end_9 2022-09-08 (18:12)	2022-09-08 (18:27) 
        2022-09-08 18:12:00 ⇒　1662628320000
        2022-09-08 18:27:59 ⇒　1662629279999
    */
    time between 1662628320000 and 1662629279999
    and message like '%Success traceId:%'
    order by time asc
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★Athena Query from proxy
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

create table "proxy_result_02" as
select 
    time as time,
    regexp_replace(substr(message ,-32, 5) ,\, '') as starttime
from
    FROM "/ecs/postvnext-asia-poc-proxy-dev-ecs-log-group"."all_log_streams"
    WHERE message like '%"GET /devproxy/ HTTP/1.1" 200%'
	AND message NOT like '%RetryAttempts%'


regexp_replace( substr( message , 17 ), '\r|\n|\r\n', '')
regexp_replace(substr(message ,-32, 5) , , '')


★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★引き算
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

create table "proxy_02_poc_result_test" as
Select 
 (cast(startTime as double) - cast(endTime as double)) as result,
  time as time,
  cast(startTime as double) as startTime,
  cast(endTime as double) as endTime
From "AwsDataCatalog"."performance_test_poc"."proxy_result_02"

order by result asc


★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
★★★★計算    
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

select
    approx_percentile(duration, 0.90)  as "90% tile",
    approx_percentile(duration, 0.95)  as "95% tile",
    approx_percentile(duration, 0.99)  as "99% tile",
    floor ( avg(duration) ) as avg
from poc_call_result_1