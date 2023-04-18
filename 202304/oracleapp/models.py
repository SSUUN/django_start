from django.db import models
### 데이터 타입 라이브러리 정의

#-- db 에서 varcjar2 또는 char 등 문자열 타입
from django.db.models.fields import CharField

#-- db 에서 number 또는 integrr 등 숫자형 타입
from django.db.models.fields import IntegerField,DateField

# 앱이름
import os
file_app_name=os.path.dirname(__file__).split("\\")[-1]

# Create your models here.


### models.py 에 클래스 추가되는 경우 무조건 아래 명령 실행
### 클래스 수정만 하면 안해도 된다 근데 가끔 안됨 그때 ㄴ해야함
# > python manage.py makemigrations oracleapp(앱이름)
                    # makemigrations
# > python manage.py migrate

#  실제 db 에있는 테이블의 형상과 동잉하게 생성하기
#- 테이블명,컬럼명은 실제 이름과 동일하게 작성해야함
# - 테이블은 class 로 생성 컬럼명은 변수

# 회원정보테이블
class Member(models.Model):
    mem_id=CharField(primary_key=True,
                     max_length=15,
                     null=False,
                     )
    mem_pass=CharField(max_length=15,null=False,)
    mem_name=CharField(max_length=20,null=False,)
    mem_add1=CharField(max_length=100,null=False,)

    # 해당 클래스가 사용할 실제 테이블 
    class Meta:
        # 실제 사용할 이름 정의
        db_table="member"

        # 사용할 앱이름 정의
        app_label=file_app_name

        #외부 데이터 베이스에 테이블존재여부 확인
        # 존재하면 : False
        #존재하지 않으면 : True
        # 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed=False
class Lprod(models.Model):
    
    lprod_id=IntegerField(max_length=5,null=False,)
    lprod_gu=CharField(primary_key=True,max_length=4,null=False,)
    lprod_nm=CharField(max_length=40,null=False,)
    
    # 해당 클래스가 사용할 실제 테이블 
    class Meta:
        # 실제 사용할 이름 정의
        db_table="lprod"

        # 사용할 앱이름 정의
        app_label=file_app_name

        #외부 데이터 베이스에 테이블존재여부 확인
        # 존재하면 : False
        #존재하지 않으면 : True
        # 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed=False
class Buyer(models.Model):
    
    buyer_id=CharField(primary_key=True,max_length=6,null=False,)
    buyer_name=CharField(max_length=40,null=False,)
    buyer_lgu=models.ForeignKey(Lprod,
                                to_field="lprod_gu",
                                db_column="buyer_lgu",
                                on_delete=models.PROTECT)
    
    buyer_bank=CharField(max_length=60,null=False,)
    buyer_bankno=CharField(max_length=60,null=False,)
    buyer_bankname=CharField(max_length=15,null=False,)
    
    # 해당 클래스가 사용할 실제 테이블 
    class Meta:
        # 실제 사용할 이름 정의
        db_table="buyer"

        # 사용할 앱이름 정의
        app_label=file_app_name

        #외부 데이터 베이스에 테이블존재여부 확인
        # 존재하면 : False
        #존재하지 않으면 : True
        # 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed=False

class Prod(models.Model):
    
    prod_id=CharField(primary_key=True,max_length=10,null=False,)
    prod_name=CharField(max_length=40,null=False,)

    prod_lgu=models.ForeignKey(Lprod,
                               to_field="lprod_gu",
                               db_column="prod_lgu",
                              on_delete=models.PROTECT)
    
    #CharField(max_length=4,null=False,)
    prod_buyer=models.ForeignKey(Buyer,
                               to_field="buyer_id",
                               db_column="prod_buyer",
                              on_delete=models.PROTECT)
    #CharField(max_length=6,null=False,)

    prod_cost=IntegerField(max_length=10,null=False,)
    prod_price=IntegerField(max_length=10,null=False,)
    prod_sale=IntegerField(max_length=10,null=False,)

    # 해당 클래스가 사용할 실제 테이블 
    class Meta:
        # 실제 사용할 이름 정의
        db_table="prod"

        # 사용할 앱이름 정의
        app_label=file_app_name

        #외부 데이터 베이스에 테이블존재여부 확인
        # 존재하면 : False
        #존재하지 않으면 : True
        # 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed=False

class Buyprod(models.Model):
    
    buy_date=DateField(primary_key=True,null=False,)
    buy_prod=models.ForeignKey(Prod,
                               to_field="prod_id",
                               db_column="buy_prod",
                              on_delete=models.PROTECT)

    buy_qty=IntegerField(max_length=10,null=False,)
    buy_cost=IntegerField(max_length=10,null=False,)
    #CharField(max_length=4,null=False,)
    

    # 해당 클래스가 사용할 실제 테이블 
    class Meta:
        # 실제 사용할 이름 정의
        db_table="buyprod"

        # 사용할 앱이름 정의
        app_label=file_app_name

        #외부 데이터 베이스에 테이블존재여부 확인
        # 존재하면 : False
        #존재하지 않으면 : True
        # 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed=False




class Cart(models.Model):
    
    # 부모자식 관계는 자식 쪽에서 연결 
    
    # to_field 침조힐부머클래스의 변서명
    # db_colum 자식클래스엣 부모ㅡ를 참조할 컬럼명
     # on _delee 데이터 삭제시 부모데이터 처리방법
     #      protect 부모들 참조하는 자식이 있다면 삭제하지 않기
            #c ascare 붑모와 관렩된자식삭제
    cart_member=models.ForeignKey(Member,
                                  to_field="mem_id",
                                  db_column="cart_member",
                                on_delete=models.PROTECT)
    
    cart_no=CharField(primary_key=True,max_length=13,null=False,)

    #cart_prod=CharField(max_length=10,null=False,)
    cart_prod=models.ForeignKey(Prod,
                                  to_field="prod_id",
                                  db_column="cart_prod",
                                on_delete=models.PROTECT)
    
    cart_qty=IntegerField(max_length=8,null=False,)

    # 해당 클래스가 사용할 실제 테이블 
    class Meta:
        # 실제 사용할 이름 정의
        db_table="cart"

        # 사용할 앱이름 정의
        app_label=file_app_name

        #외부 데이터 베이스에 테이블존재여부 확인
        # 존재하면 : False
        #존재하지 않으면 : True
        # 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed=False
