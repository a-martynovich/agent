import pytest


NMAP_FIXTURE = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE nmaprun>
<?xml-stylesheet href="file:///usr/bin/../share/nmap/nmap.xsl" type="text/xsl"?>
<!-- Nmap 7.60 scan initiated Tue Mar  5 23:21:33 2019 as: nmap -sS -sU -oX - 127.0.0.1 -->
<nmaprun scanner="nmap" args="nmap -sS -sU -oX - 127.0.0.1" start="1551806493" startstr="Tue Mar  5 23:21:33 2019" version="7.60" xmloutputversion="1.04">
<scaninfo type="syn" protocol="tcp" numservices="1000" services="1,3-4,6-7,9,13,17,19-26,30,32-33,37,42-43,49,53,70,79-85,88-90,99-100,106,109-111,113,119,125,135,139,143-144,146,161,163,179,199,211-212,222,254-256,259,264,280,301,306,311,340,366,389,406-407,416-417,425,427,443-445,458,464-465,481,497,500,512-515,524,541,543-545,548,554-555,563,587,593,616-617,625,631,636,646,648,666-668,683,687,691,700,705,711,714,720,722,726,749,765,777,783,787,800-801,808,843,873,880,888,898,900-903,911-912,981,987,990,992-993,995,999-1002,1007,1009-1011,1021-1100,1102,1104-1108,1110-1114,1117,1119,1121-1124,1126,1130-1132,1137-1138,1141,1145,1147-1149,1151-1152,1154,1163-1166,1169,1174-1175,1183,1185-1187,1192,1198-1199,1201,1213,1216-1218,1233-1234,1236,1244,1247-1248,1259,1271-1272,1277,1287,1296,1300-1301,1309-1311,1322,1328,1334,1352,1417,1433-1434,1443,1455,1461,1494,1500-1501,1503,1521,1524,1533,1556,1580,1583,1594,1600,1641,1658,1666,1687-1688,1700,1717-1721,1723,1755,1761,1782-1783,1801,1805,1812,1839-1840,1862-1864,1875,1900,1914,1935,1947,1971-1972,1974,1984,1998-2010,2013,2020-2022,2030,2033-2035,2038,2040-2043,2045-2049,2065,2068,2099-2100,2103,2105-2107,2111,2119,2121,2126,2135,2144,2160-2161,2170,2179,2190-2191,2196,2200,2222,2251,2260,2288,2301,2323,2366,2381-2383,2393-2394,2399,2401,2492,2500,2522,2525,2557,2601-2602,2604-2605,2607-2608,2638,2701-2702,2710,2717-2718,2725,2800,2809,2811,2869,2875,2909-2910,2920,2967-2968,2998,3000-3001,3003,3005-3007,3011,3013,3017,3030-3031,3052,3071,3077,3128,3168,3211,3221,3260-3261,3268-3269,3283,3300-3301,3306,3322-3325,3333,3351,3367,3369-3372,3389-3390,3404,3476,3493,3517,3527,3546,3551,3580,3659,3689-3690,3703,3737,3766,3784,3800-3801,3809,3814,3826-3828,3851,3869,3871,3878,3880,3889,3905,3914,3918,3920,3945,3971,3986,3995,3998,4000-4006,4045,4111,4125-4126,4129,4224,4242,4279,4321,4343,4443-4446,4449,4550,4567,4662,4848,4899-4900,4998,5000-5004,5009,5030,5033,5050-5051,5054,5060-5061,5080,5087,5100-5102,5120,5190,5200,5214,5221-5222,5225-5226,5269,5280,5298,5357,5405,5414,5431-5432,5440,5500,5510,5544,5550,5555,5560,5566,5631,5633,5666,5678-5679,5718,5730,5800-5802,5810-5811,5815,5822,5825,5850,5859,5862,5877,5900-5904,5906-5907,5910-5911,5915,5922,5925,5950,5952,5959-5963,5987-5989,5998-6007,6009,6025,6059,6100-6101,6106,6112,6123,6129,6156,6346,6389,6502,6510,6543,6547,6565-6567,6580,6646,6666-6669,6689,6692,6699,6779,6788-6789,6792,6839,6881,6901,6969,7000-7002,7004,7007,7019,7025,7070,7100,7103,7106,7200-7201,7402,7435,7443,7496,7512,7625,7627,7676,7741,7777-7778,7800,7911,7920-7921,7937-7938,7999-8002,8007-8011,8021-8022,8031,8042,8045,8080-8090,8093,8099-8100,8180-8181,8192-8194,8200,8222,8254,8290-8292,8300,8333,8383,8400,8402,8443,8500,8600,8649,8651-8652,8654,8701,8800,8873,8888,8899,8994,9000-9003,9009-9011,9040,9050,9071,9080-9081,9090-9091,9099-9103,9110-9111,9200,9207,9220,9290,9415,9418,9485,9500,9502-9503,9535,9575,9593-9595,9618,9666,9876-9878,9898,9900,9917,9929,9943-9944,9968,9998-10004,10009-10010,10012,10024-10025,10082,10180,10215,10243,10566,10616-10617,10621,10626,10628-10629,10778,11110-11111,11967,12000,12174,12265,12345,13456,13722,13782-13783,14000,14238,14441-14442,15000,15002-15004,15660,15742,16000-16001,16012,16016,16018,16080,16113,16992-16993,17877,17988,18040,18101,18988,19101,19283,19315,19350,19780,19801,19842,20000,20005,20031,20221-20222,20828,21571,22939,23502,24444,24800,25734-25735,26214,27000,27352-27353,27355-27356,27715,28201,30000,30718,30951,31038,31337,32768-32785,33354,33899,34571-34573,35500,38292,40193,40911,41511,42510,44176,44442-44443,44501,45100,48080,49152-49161,49163,49165,49167,49175-49176,49400,49999-50003,50006,50300,50389,50500,50636,50800,51103,51493,52673,52822,52848,52869,54045,54328,55055-55056,55555,55600,56737-56738,57294,57797,58080,60020,60443,61532,61900,62078,63331,64623,64680,65000,65129,65389"/>
<scaninfo type="udp" protocol="udp" numservices="1000" services="2-3,7,9,13,17,19-23,37-38,42,49,53,67-69,80,88,111-113,120,123,135-139,158,161-162,177,192,199,207,217,363,389,402,407,427,434,443,445,464,497,500,502,512-515,517-518,520,539,559,593,623,626,631,639,643,657,664,682-689,764,767,772-776,780-782,786,789,800,814,826,829,838,902-903,944,959,965,983,989-990,996-1001,1007-1008,1012-1014,1019-1051,1053-1060,1064-1070,1072,1080-1081,1087-1088,1090,1100-1101,1105,1124,1200,1214,1234,1346,1419,1433-1434,1455,1457,1484-1485,1524,1645-1646,1701,1718-1719,1761,1782,1804,1812-1813,1885-1886,1900-1901,1993,2000,2002,2048-2049,2051,2148,2160-2161,2222-2223,2343,2345,2362,2967,3052,3130,3283,3296,3343,3389,3401,3456-3457,3659,3664,3702-3703,4000,4008,4045,4444,4500,4666,4672,5000-5003,5010,5050,5060,5093,5351,5353,5355,5500,5555,5632,6000-6002,6004,6050,6346-6347,6970-6971,7000,7938,8000-8001,8010,8181,8193,8900,9000-9001,9020,9103,9199-9200,9370,9876-9877,9950,10000,10080,11487,16086,16402,16420,16430,16433,16449,16498,16503,16545,16548,16573,16674,16680,16697,16700,16708,16711,16739,16766,16779,16786,16816,16829,16832,16838-16839,16862,16896,16912,16918-16919,16938-16939,16947-16948,16970,16972,16974,17006,17018,17077,17091,17101,17146,17184-17185,17205,17207,17219,17236-17237,17282,17302,17321,17331-17332,17338,17359,17417,17423-17424,17455,17459,17468,17487,17490,17494,17505,17533,17549,17573,17580,17585,17592,17605,17615-17616,17629,17638,17663,17673-17674,17683,17726,17754,17762,17787,17814,17823-17824,17836,17845,17888,17939,17946,17989,18004,18081,18113,18134,18156,18228,18234,18250,18255,18258,18319,18331,18360,18373,18449,18485,18543,18582,18605,18617,18666,18669,18676,18683,18807,18818,18821,18830,18832,18835,18869,18883,18888,18958,18980,18985,18987,18991,18994,18996,19017,19022,19039,19047,19075,19096,19120,19130,19140-19141,19154,19161,19165,19181,19193,19197,19222,19227,19273,19283,19294,19315,19322,19332,19374,19415,19482,19489,19500,19503-19504,19541,19600,19605,19616,19624-19625,19632,19639,19647,19650,19660,19662-19663,19682-19683,19687,19695,19707,19717-19719,19722,19728,19789,19792,19933,19935-19936,19956,19995,19998,20003-20004,20019,20031,20082,20117,20120,20126,20129,20146,20154,20164,20206,20217,20249,20262,20279,20288,20309,20313,20326,20359-20360,20366,20380,20389,20409,20411,20423-20425,20445,20449,20464-20465,20518,20522,20525,20540,20560,20665,20678-20679,20710,20717,20742,20752,20762,20791,20817,20842,20848,20851,20865,20872,20876,20884,20919,21000,21016,21060,21083,21104,21111,21131,21167,21186,21206-21207,21212,21247,21261,21282,21298,21303,21318,21320,21333,21344,21354,21358,21360,21364,21366,21383,21405,21454,21468,21476,21514,21524-21525,21556,21566,21568,21576,21609,21621,21625,21644,21649,21655,21663,21674,21698,21702,21710,21742,21780,21784,21800,21803,21834,21842,21847,21868,21898,21902,21923,21948,21967,22029,22043,22045,22053,22055,22105,22109,22123-22124,22341,22692,22695,22739,22799,22846,22914,22986,22996,23040,23176,23354,23531,23557,23608,23679,23781,23965,23980,24007,24279,24511,24594,24606,24644,24854,24910,25003,25157,25240,25280,25337,25375,25462,25541,25546,25709,25931,26407,26415,26720,26872,26966,27015,27195,27444,27473,27482,27707,27892,27899,28122,28369,28465,28493,28543,28547,28641,28840,28973,29078,29243,29256,29810,29823,29977,30263,30303,30365,30544,30656,30697,30704,30718,30975,31059,31073,31109,31189,31195,31335,31337,31365,31625,31681,31731,31891,32345,32385,32528,32768-32780,32798,32815,32818,32931,33030,33249,33281,33354-33355,33459,33717,33744,33866,33872,34038,34079,34125,34358,34422,34433,34555,34570,34577-34580,34758,34796,34855,34861-34862,34892,35438,35702,35777,35794,36108,36206,36384,36458,36489,36669,36778,36893,36945,37144,37212,37393,37444,37602,37761,37783,37813,37843,38037,38063,38293,38412,38498,38615,39213,39217,39632,39683,39714,39723,39888,40019,40116,40441,40539,40622,40708,40711,40724,40732,40805,40847,40866,40915,41058,41081,41308,41370,41446,41524,41638,41702,41774,41896,41967,41971,42056,42172,42313,42431,42434,42508,42557,42577,42627,42639,43094,43195,43370,43514,43686,43824,43967,44101,44160,44179,44185,44190,44253,44334,44508,44923,44946,44968,45247,45380,45441,45685,45722,45818,45928,46093,46532,46836,47624,47765,47772,47808,47915,47981,48078,48189,48255,48455,48489,48761,49152-49163,49165-49182,49184-49202,49204-49205,49207-49216,49220,49222,49226,49259,49262,49306,49350,49360,49393,49396,49503,49640,49968,50099,50164,50497,50612,50708,50919,51255,51456,51554,51586,51690,51717,51905,51972,52144,52225,52503,53006,53037,53571,53589,53838,54094,54114,54281,54321,54711,54807,54925,55043,55544,55587,56141,57172,57409-57410,57813,57843,57958,57977,58002,58075,58178,58419,58631,58640,58797,59193,59207,59765,59846,60172,60381,60423,61024,61142,61319,61322,61370,61412,61481,61550,61685,61961,62154,62287,62575,62677,62699,62958,63420,63555,64080,64481,64513,64590,64727,65024"/>
<verbose level="0"/>
<debugging level="0"/>
<taskprogress task="UDP Scan" time="1551806497" percent="99.99" remaining="1" etc="1551806497"/>
<host starttime="1551806493" endtime="1551806497"><status state="up" reason="localhost-response" reason_ttl="0"/>
<address addr="127.0.0.1" addrtype="ipv4"/>
<hostnames>
<hostname name="localhost" type="PTR"/>
</hostnames>
<ports><extraports state="closed" count="1996">
<extrareasons reason="resets" count="999"/>
<extrareasons reason="port-unreaches" count="997"/>
</extraports>
<port protocol="tcp" portid="631"><state state="open" reason="syn-ack" reason_ttl="64"/><service name="ipp" method="table" conf="3"/></port>
<port protocol="udp" portid="68"><state state="open|filtered" reason="no-response" reason_ttl="0"/><service name="dhcpc" method="table" conf="3"/></port>
<port protocol="udp" portid="631"><state state="open|filtered" reason="no-response" reason_ttl="0"/><service name="ipp" method="table" conf="3"/></port>
<port protocol="udp" portid="5353"><state state="open|filtered" reason="no-response" reason_ttl="0"/><service name="zeroconf" method="table" conf="3"/></port>
</ports>
<times srtt="32" rttvar="0" to="100000"/>
</host>
<runstats><finished time="1551806497" timestr="Tue Mar  5 23:21:37 2019" elapsed="4.41" summary="Nmap done at Tue Mar  5 23:21:37 2019; 1 IP address (1 host up) scanned in 4.41 seconds" exit="success"/><hosts up="1" down="0" total="1"/>
</runstats>
</nmaprun>
"""

RASPBERRY_FIXTURE = """
Hardware        : BCM2708
Revision        : 900092
Serial          : 00000000ebd5f1e8
"""

INVALID_CERT = """
-----BEGIN CERTIFICATE-----
MIIC5TCCAc2gAwIBAgIJAPMjGMrzQcI/MA0GCSqGSIb3DQEBCwUAMBQxEjAQBgNV
BAMMCWxvY2FsaG9zdDAeFw0xOTAzMDUyMDE5MjRaFw0xOTA0MDQyMDE5MjRaMBQx
EjAQBgNVBAMMCWxvY2FsaG9zdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
ggEBAOgfhzltW1Bx/PLve7sk228G9FeBQmTVkEwiU1tgagvIzM8fhoeDnXoMVRf5
GPWZr4h0E4BtDRQUO7NqgW+r3RQMq4nJljTV9f8Om3Owx41BM5M5w5YH75JZzcZ1
OVBmJRPOG06I3Hk/uQjCGo1YN7ZggAdUmFQqQ03GdstqQhd6UzbV2dPphq+R2npV
oAjByawBwuxi+NJXxz20dUVkXrrxGgDUKcUn4NPsIUGf9hSHZcDMZ3XQcQQ/ykD9
i/zeVU6jGnsMOO+YZUguBlq/GKI2fzezfG7fv394oAJP9mV0T8k9ArciTigUehuv
a8sHA+vrvRXCNbpV8vEQbRh/+0sCAwEAAaM6MDgwFAYDVR0RBA0wC4IJbG9jYWxo
b3N0MAsGA1UdDwQEAwIHgDATBgNVHSUEDDAKBggrBgEFBQcDATANBgkqhkiG9w0B
AQsFAAOCAQEAL+KRDdqbbAFiMROy7eNkbMUj3Dp4S24y5QnGjFl4eSFLWu9UhBT+
FcElSbo1vKaW5DJi+XG9snyZfqEuknQlBEDTuBlOEqguGpmzYE/+T0wt9zLTByN8
N44fGr4f9ORj6Y6HJkzdlp+XCDdzHb2+3ienNle6bWlmBpbQaMVrayDxJ5yxldgJ
czUUClEc0OJDMw8PsHyYvrl+jk0JFXgDqBgAutPzSiC+pWL3H/5DO8t/NcccNNlR
2UZyh8r3qmVWo1jROR98z/J59ytNgMfYTmVI+ClUWKF5OWEOneKTf7dvic0Bqiyb
1lti7kgwF5QeRU2eEn3VC2F5JreBMpTkeA==
-----END CERTIFICATE-----
"""


INVALID_KEY = """
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDoH4c5bVtQcfzy
73u7JNtvBvRXgUJk1ZBMIlNbYGoLyMzPH4aHg516DFUX+Rj1ma+IdBOAbQ0UFDuz
aoFvq90UDKuJyZY01fX/DptzsMeNQTOTOcOWB++SWc3GdTlQZiUTzhtOiNx5P7kI
whqNWDe2YIAHVJhUKkNNxnbLakIXelM21dnT6Yavkdp6VaAIwcmsAcLsYvjSV8c9
tHVFZF668RoA1CnFJ+DT7CFBn/YUh2XAzGd10HEEP8pA/Yv83lVOoxp7DDjvmGVI
LgZavxiiNn83s3xu379/eKACT/ZldE/JPQK3Ik4oFHobr2vLBwPr670VwjW6VfLx
EG0Yf/tLAgMBAAECggEBALPEbxJfid+UV+TA6Z823SZwSV1XgtbauqTr1Iio85fq
zAsAjEx49sWltWUaimTywAm6c7v7OKy7Or0pl9KnVFEJuvO8BjMnHRuJ8YQ4fWL9
AvdbPgj8XmKGYCH5eQi2ArMC5Qz+W1kfq6qHwM6Eaqk4tQ54SnysOnGKaUgCI+tP
XBIuWTs6OrWmJDuW6J0zNPRBZAbVEsaFaTdLtJ4kDPlmDmHHMzrLkQhvQ7oSFoEW
FtLNlWAV0uZ2PpHQbrcx1ALabH1Yz3yRcgjDYtu5oCRN6+4wJEylg1NxiQk9BP/m
amRFIuyBVpnh69ErYeLrP320nHew3NML6Xxr3dI9yVECgYEA/3oAR6rCVtjrozHG
hWq/SdRY5Cq4nvt+ocTlgZo2/qULDR8xo4HE4ABliE9/TMEysgA2erAfEvSV15mt
m/BWOHZZ1mbpAm1jbRmBMjVPGytH997LOAnBCwLLjtIjbJMrRxKws6fSO+gwRY9v
MMeiJdW2LpVgBd+AunZEBjyMYCMCgYEA6JlHM5SyCfwuZSdIue0iI3t8n8nBV7zu
mqwItZHX/h8xu/V5cT7eVLsC3yti2+EHir8V6AXJ919LlSFjZObEBwL+xtyK+HZj
uQmXN78QtnFRUO3EBlTmYCYzPGE0cNwg9t1RQS0KMs5ypQ9vYUoXwqNvp97XxsB0
d4+wMLz+lrkCgYEA1ibWhTzGmzZKkAnxd3T71E+EE/8bs2jtxXzfRbyXzO1cTiuP
2Je3CG5Mre61rwlkDYHQKRfpdGJCGPBhbw4PuFS9CdRKDhbT+WgfvI6jOQsW0NiZ
UOgcQbaeG6Jav3C+Hl20cWSD/mOr0yNg+WreqQh0JqhgTYwExEjOzMuEgDECgYBD
niugxx1q4bDrHxx5UIKYJhH4scJPK1GCDXkKr7dG3PKsXZRMY6Zmo2cWUZqPqT90
ClDn/qbUDxP96pLmhl9+WlSOoxaTXHdpF2yqfBTztMWa7UQLQysl0HUcnHWOSbAb
lANHGzzXwER7z5zlf5CguLqA5rt7v/8bst3ZjVfFoQKBgQCFepRalYYqKUYbl6Lx
y0UxgC/XRPUlsL5IANipOt8Yu2M/+RJKW1jdUJx3sUCRYBV5IpX8jqnHax+MIki5
wU3JBrpGqAAoGa/78B572+9Dmr6Bj0yAoWQ67tht87M1mQxpKv6IE4CEt8+o+5sR
I9bBs17EE1GV43TaxFaOc/oUYw==
-----END PRIVATE KEY-----
"""


CERT = """
-----BEGIN CERTIFICATE-----
MIIClzCCAj2gAwIBAgIUFXu9cEa7n79yDQWNHG9nfHHiw+kwCgYIKoZIzj0EAwIw
XzELMAkGA1UEBhMCVUsxDzANBgNVBAcTBkxvbmRvbjEjMCEGA1UEChMaV2ViIG9m
IFRydXN0ZWQgVGhpbmdzLCBMdGQxGjAYBgNVBAMTEWNhMC1jYS53b3R0LmxvY2Fs
MB4XDTE5MDMxMjEwMjQwMFoXDTE5MDMxOTEwMjQwMFowezELMAkGA1UEBhMCVUsx
DzANBgNVBAgTBkxvbmRvbjEjMCEGA1UEChMaV2ViIG9mIFRydXN0ZWQgVGhpbmdz
LCBMdGQxNjA0BgNVBAMTLTQ4NTNiNjMwODIyOTQ2MDE5MzkzYjE2YzViNzEwYjll
LmQud290dC5sb2NhbDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABEzKyyQJ2VSw
5F90xOkHLaJmTHjJwu3C/G2fgYDMw02NbuTzjIhTCyqhHbeY8GO/ZXIZ5ASE1ACB
4OJVYrpRUVajgbowgbcwDgYDVR0PAQH/BAQDAgeAMB0GA1UdJQQWMBQGCCsGAQUF
BwMCBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBSshZgvlzrA9p6p
EJXTRi4wgYOyITAfBgNVHSMEGDAWgBSpts1xq4g96OM2x5RvKrEUAIU3ATA4BgNV
HREEMTAvgi00ODUzYjYzMDgyMjk0NjAxOTM5M2IxNmM1YjcxMGI5ZS5kLndvdHQu
bG9jYWwwCgYIKoZIzj0EAwIDSAAwRQIgGSUuYz+Osx1FFZnIntWlb2g3dkpT1O/C
5zSuz7b/JcECIQDTa1z7edWWjwBLmFwaCR/2XXU6pt/52Fh+YUq/vwGq5A==
-----END CERTIFICATE-----
"""


KEY = """
-----BEGIN PRIVATE KEY-----
MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgGJEzRpQVxxo0jRKh
0zV00O5iyOkUajHp9ULu0vE6J3KhRANCAARMysskCdlUsORfdMTpBy2iZkx4ycLt
wvxtn4GAzMNNjW7k84yIUwsqoR23mPBjv2VyGeQEhNQAgeDiVWK6UVFW
-----END PRIVATE KEY-----
"""


@pytest.fixture
def nmap_fixture():
    return NMAP_FIXTURE


@pytest.fixture
def raspberry_cpuinfo():
    return RASPBERRY_FIXTURE


@pytest.fixture
def netif_gateways():
    return {
        'default': {
            2: ('192.168.1.1', 'wlo1')
        },
        2: [('192.168.1.1', 'wlo1', True)]
    }


@pytest.fixture
def netif_ifaddresses():
    return {
        17: [
            {
                'addr': 'aa:aa:aa:aa:aa:aa',
                'broadcast': 'ff:ff:ff:ff:ff:ff'
            }
        ],
        2: [
            {
                'addr': '192.168.1.3',
                'netmask': '255.255.255.0',
                'broadcast': '192.168.1.255'
            }
        ],
        10: [
            {
                'addr': 'fe80::1e93:cce9:0000:0000%wlo1',
                'netmask': 'ffff:ffff:ffff:ffff::/64'
            }
        ]
    }


@pytest.fixture
def netif_gateways_invalid():
    return {}


@pytest.fixture
def cert():
    return CERT


@pytest.fixture
def key():
    return KEY


@pytest.fixture
def invalid_cert():
    return INVALID_CERT


@pytest.fixture
def invalid_key():
    return INVALID_KEY


@pytest.fixture
def gen_id():
    return {"device_id": "60f4e66c1e7746c3ba8f3301d8a4d1c4.d.wott.local"}


@pytest.fixture
def uptime():
    return "60 60"
