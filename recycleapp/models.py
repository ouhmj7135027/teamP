from django.db import models

# Create your models here.


class Category(models.Model):
    TAG_CHOICES = (
        ('페트병 플라스틱류', '페트병 플라스틱류'),
        ('기타 플라스틱류', '기타 플라스틱류'),
        ('일반', '일반쓰레기'),
        ('음식물', '음식물쓰레기'),
        ('유리', '유리'),
        ('병', '병'),
        ('대형', '대형폐기물'),
        ('종이류', '종이류'),
        ('종이팩류', '종이팩류'),
        ('종이팩', '종이팩'),
        ('금속캔', '금속캔'),
        ('유리병류', '유리병류'),
        ('고철류', '고철류'),
        ('비닐류', '비닐류'),
        ('스티로폼 완충재', '스틔로폼 완충제'),
        ('의류','의류'),
        ('폐형광등','폐형광등'),
        ('폐건전지', '폐건전지'),
        ('폐가전제품','폐가전제품'),
        ('대형폐기물', '대형폐기물'),
        ('소형가전제품','소형가전제품'),
        
    )

    waste_name=models.CharField(max_length=50, verbose_name='카테고리')
    image = models.FileField(upload_to='images/')
    description = models.CharField(max_length = 500, verbose_name='처리방법')
    tag = models.CharField(max_length=20, choices=TAG_CHOICES)

    def __str__(self):
        return self.waste_name
