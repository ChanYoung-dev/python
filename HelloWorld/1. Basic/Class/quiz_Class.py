# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
#
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self. house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3}억 {4}년"\
              .format(self.location, self.house_type, self.deal_type,\
                      self.price, self.completion_year))
house1 = House("강남", "아파트", "매매", 10, 2010)
house2 = House("마포", "오피스텔", "전세", 5, 2007)
house3 = House("송파", "빌라", "월세", 500, 2000)

houses = []
houses.append(house1)
houses.append(house2)
houses.append(house3)
for house in houses:
    house.show_detail()
