import requests
import csv
from datetime import datetime

# URL API Shopee
url = "https://shopee.vn/api/v4/seller_operation/get_shop_ratings_new"

# Danh sách shopid và userid
shop_list = [{'shopid': '24710134', 'userid': '24711470'}, {'shopid': '225909574', 'userid': '225913958'}, {'shopid': '201774917', 'userid': '201778079'}, {'shopid': '35080757', 'userid': '35082141'}, {'shopid': '308542026', 'userid': '308561611'}, {'shopid': '173392916', 'userid': '173395365'}, {'shopid': '106933589', 'userid': '106935068'}, {'shopid': '93936823', 'userid': '93938301'}, {'shopid': '70681764', 'userid': '70683225'}, {'shopid': '58542133', 'userid': '58543563'}, {'shopid': '65589552', 'userid': '65591005'}, {'shopid': '88201679', 'userid': '88203157'}, {'shopid': '442733715', 'userid': '442753292'}, {'shopid': '308461157', 'userid': '308480742'}, {'shopid': '130641691', 'userid': '130643515'}, {'shopid': '63521925', 'userid': '63523369'}, {'shopid': '27495839', 'userid': '27497198'}, {'shopid': '35284879', 'userid': '35286263'}, {'shopid': '61963112', 'userid': '61964554'}, {'shopid': '269296276', 'userid': '269299979'}, {'shopid': '182445910', 'userid': '182448571'}, {'shopid': '91686190', 'userid': '91687668'}, {'shopid': '26274679', 'userid': '26276015'}, {'shopid': '292786634', 'userid': '292805915'}, {'shopid': '73224788', 'userid': '73226251'}, {'shopid': '518715302', 'userid': '518734881'}, {'shopid': '58411241', 'userid': '58412671'}, {'shopid': '155343961', 'userid': '155345891'}, {'shopid': '37251700', 'userid': '37253085'}, {'shopid': '37251933', 'userid': '37253318'}, {'shopid': '556642251', 'userid': '556661834'}, {'shopid': '44806875', 'userid': '44808261'}, {'shopid': '253598734', 'userid': '253599409'}, {'shopid': '63481848', 'userid': '63483291'}, {'shopid': '413403797', 'userid': '413423374'}, {'shopid': '774973980', 'userid': '774957734'}, {'shopid': '254657873', 'userid': '254658684'}, {'shopid': '189431669', 'userid': '189434445'}, {'shopid': '95303264', 'userid': '95304742'}, {'shopid': '1150105706', 'userid': '1150425730'}, {'shopid': '81155644', 'userid': '81157119'}, {'shopid': '93177350', 'userid': '93178828'}, {'shopid': '2577648', 'userid': '2578927'}, {'shopid': '90494790', 'userid': '90496268'}, {'shopid': '82611496', 'userid': '82612973'}, {'shopid': '215110322', 'userid': '215114106'}, {'shopid': '272356020', 'userid': '272360300'}, {'shopid': '41299884', 'userid': '41301270'}, {'shopid': '11442764', 'userid': '11444064'}, {'shopid': '157594197', 'userid': '157596181'}, {'shopid': '115491915', 'userid': '115493739'}, {'shopid': '16237192', 'userid': '16238527'}, {'shopid': '90428978', 'userid': '90430456'}, {'shopid': '45194730', 'userid': '45196115'}, {'shopid': '15374634', 'userid': '15375970'}, {'shopid': '41482786', 'userid': '41484172'}, {'shopid': '127805122', 'userid': '127806946'}, {'shopid': '46725128', 'userid': '46726514'}, {'shopid': '272432350', 'userid': '272436646'}, {'shopid': '392838844', 'userid': '392858421'}, {'shopid': '42973303', 'userid': '42974690'}, {'shopid': '14390734', 'userid': '14392038'}, {'shopid': '154779484', 'userid': '154781401'}, {'shopid': '90740928', 'userid': '90742406'}, {'shopid': '19202634', 'userid': '19203970'}, {'shopid': '91680258', 'userid': '91681736'}, {'shopid': '242644740', 'userid': '242650364'}, {'shopid': '89607375', 'userid': '89608853'}, {'shopid': '22043257', 'userid': '22044593'}, {'shopid': '729014007', 'userid': '729033592'}, {'shopid': '969562773', 'userid': '969697669'}, {'shopid': '26177032', 'userid': '26178368'}, {'shopid': '1362679168', 'userid': '1363386527'}, {'shopid': '325696535', 'userid': '325716134'}, {'shopid': '201171779', 'userid': '201174933'}, {'shopid': '958778013', 'userid': '958900117'}, {'shopid': '893659686', 'userid': '893708770'}, {'shopid': '212205841', 'userid': '212209475'}, {'shopid': '327863047', 'userid': '327882622'}, {'shopid': '860214008', 'userid': '860229183'}, {'shopid': '1293364953', 'userid': '1293894696'}, {'shopid': '824123908', 'userid': '824110988'}, {'shopid': '7669738', 'userid': '7671030'}, {'shopid': '252386387', 'userid': '252386930'}, {'shopid': '1270647859', 'userid': '1271140378'}, {'shopid': '851157471', 'userid': '851167098'}, {'shopid': '120420833', 'userid': '120422655'}, {'shopid': '552040620', 'userid': '552060201'}, {'shopid': '82364307', 'userid': '82365783'}, {'shopid': '1103428920', 'userid': '1103697424'}, {'shopid': '313752154', 'userid': '313771753'}, {'shopid': '949754848', 'userid': '949866427'}, {'shopid': '460047409', 'userid': '460066986'}, {'shopid': '73409588', 'userid': '73411052'}, {'shopid': '833640645', 'userid': '833629200'}, {'shopid': '451212855', 'userid': '451232432'}, {'shopid': '423746879', 'userid': '423766456'}, {'shopid': '984689722', 'userid': '984843293'}, {'shopid': '344800939', 'userid': '344820514'}, {'shopid': '978947723', 'userid': '979094449'}, {'shopid': '8516029', 'userid': '8517325'}, {'shopid': '975865932', 'userid': '976008765'}, {'shopid': '1078205440', 'userid': '1078448693'}, {'shopid': '76823929', 'userid': '76825401'}, {'shopid': '987285709', 'userid': '987442451'}, {'shopid': '549924811', 'userid': '549944392'}, {'shopid': '100256821', 'userid': '100258300'}, {'shopid': '641413885', 'userid': '641433470'}, {'shopid': '658242548', 'userid': '658262133'}, {'shopid': '382964977', 'userid': '382984554'}, {'shopid': '192616045', 'userid': '192618889'}, {'shopid': '829357864', 'userid': '829341473'}, {'shopid': '1299184044', 'userid': '1299730922'}, {'shopid': '1159922989', 'userid': '1160253562'}, {'shopid': '1089361687', 'userid': '1089616746'}, {'shopid': '213800943', 'userid': '213804664'}, {'shopid': '563541817', 'userid': '563561402'}, {'shopid': '834756665', 'userid': '834746706'}, {'shopid': '844389545', 'userid': '844391101'}, {'shopid': '772696738', 'userid': '772680492'}, {'shopid': '900723602', 'userid': '900779495'}, {'shopid': '196261835', 'userid': '196264785'}, {'shopid': '378820744', 'userid': '378840321'}, {'shopid': '203796246', 'userid': '203799454'}, {'shopid': '279658061', 'userid': '279663640'}, {'shopid': '211133030', 'userid': '211136590'}, {'shopid': '899683686', 'userid': '899738500'}, {'shopid': '534730986', 'userid': '534750565'}, {'shopid': '365181681', 'userid': '365201258'}, {'shopid': '1134285263', 'userid': '1134588174'}, {'shopid': '328273016', 'userid': '328292591'}, {'shopid': '903805788', 'userid': '903864967'}, {'shopid': '489501653', 'userid': '489521231'}, {'shopid': '1007255438', 'userid': '1007437951'}, {'shopid': '932578580', 'userid': '932670027'}, {'shopid': '414003158', 'userid': '414022735'}, {'shopid': '86427647', 'userid': '86429124'}, {'shopid': '293689082', 'userid': '293708391'}, {'shopid': '754426389', 'userid': '754445974'}, {'shopid': '1202044690', 'userid': '1202420379'}, {'shopid': '88361186', 'userid': '88362664'}, {'shopid': '28506070', 'userid': '28507454'}, {'shopid': '436777764', 'userid': '436797341'}, {'shopid': '144664840', 'userid': '144666664'}, {'shopid': '1053077389', 'userid': '1053320218'}, {'shopid': '1207030092', 'userid': '1207415716'}, {'shopid': '393477900', 'userid': '393497477'}, {'shopid': '993446455', 'userid': '993610081'}, {'shopid': '735989388', 'userid': '736008973'}, {'shopid': '801176484', 'userid': '801162693'}, {'shopid': '235346769', 'userid': '235351801'}, {'shopid': '82095709', 'userid': '82097186'}, {'shopid': '1279365103', 'userid': '1279869837'}, {'shopid': '238930514', 'userid': '238935858'}, {'shopid': '145988635', 'userid': '145990459'}, {'shopid': '703090265', 'userid': '703109850'}, {'shopid': '585448275', 'userid': '585467860'}, {'shopid': '939665862', 'userid': '939765734'}, {'shopid': '254610901', 'userid': '254611707'}, {'shopid': '882130256', 'userid': '882167662'}, {'shopid': '1069148821', 'userid': '1069412032'}, {'shopid': '134952940', 'userid': '134954764'}, {'shopid': '257372007', 'userid': '257373240'}, {'shopid': '172168844', 'userid': '172171260'}, {'shopid': '54406901', 'userid': '54408325'}, {'shopid': '885498482', 'userid': '885539270'}, {'shopid': '645219934', 'userid': '645239519'}, {'shopid': '1348586749', 'userid': '1349268271'}, {'shopid': '189865177', 'userid': '189867960'}, {'shopid': '78513158', 'userid': '78514632'}, {'shopid': '67293298', 'userid': '67294755'}, {'shopid': '120950544', 'userid': '120952368'}, {'shopid': '949804684', 'userid': '949916312'}, {'shopid': '284793106', 'userid': '284800547'}, {'shopid': '1057158747', 'userid': '1057406580'}, {'shopid': '35162351', 'userid': '35163735'}, {'shopid': '358672644', 'userid': '358692221'}]

# Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

# Tạo file CSV để lưu dữ liệu
with open('ratings_all66k.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Shop ID', 'Rating Star', 'Comment', 'Username', 'Product Name', 'Review Time'])

    total_reviews_collected = 0
    max_total_reviews = 100000  # Số lượng đánh giá tối đa cần lấy tổng cộng

    for shop in shop_list:
        if total_reviews_collected >= max_total_reviews:
            break

        shopid = shop["shopid"]
        userid = shop["userid"]
        offset = 0
        shop_reviews = 0
        max_reviews_per_shop = 1000  # Giới hạn số đánh giá mỗi shop

        while shop_reviews < max_reviews_per_shop:
            if total_reviews_collected >= max_total_reviews:
                break

            params = {
                'limit': 100,  # Lấy 100 đánh giá mỗi lần
                'offset': offset,
                'replied': 'false',
                'shopid': shopid,
                'userid': userid
            }

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                try:
                    data = response.json()
                    if not isinstance(data, dict) or 'data' not in data or not isinstance(data['data'], dict):
                        print(f"Phản hồi không hợp lệ từ shop {shopid}: {data}")
                        break

                    items = data['data'].get('items', [])

                    if not items:
                        print(f"Shop {shopid} không có thêm đánh giá.")
                        break

                    for item in items:
                        if shop_reviews >= max_reviews_per_shop or total_reviews_collected >= max_total_reviews:
                            break

                        rating_star = item.get('rating_star', '')
                        comment = item.get('comment', '').strip()
                        username = item.get('author_username', '')
                        timestamp = item.get('ctime', 0)
                        review_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else ''
                        product_name = item['product_items'][0]['name'] if item.get('product_items') else ''

                        if not comment:
                            continue

                        writer.writerow([shopid, rating_star, comment, username, product_name, review_time])
                        shop_reviews += 1
                        total_reviews_collected += 1

                    offset += params['limit']
                except Exception as e:
                    print(f"Lỗi khi xử lý dữ liệu từ shop {shopid}: {e}")
                    break
            else:
                print(f"Không thể lấy dữ liệu từ shop {shopid}, mã trạng thái: {response.status_code}")
                print("Nội dung phản hồi:", response.text)
                break

print("Dữ liệu đã được lưu vào file ratings_all66k.csv")
