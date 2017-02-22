# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-13 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0057_auto_20170209_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeringadult',
            name='beneficiary_changed_birthday_day',
            field=models.CharField(blank=True, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5), (b'6', 6), (b'7', 7), (b'8', 8), (b'9', 9), (b'10', 10), (b'11', 11), (b'12', 12), (b'13', 13), (b'14', 14), (b'15', 15), (b'16', 16), (b'17', 17), (b'18', 18), (b'19', 19), (b'20', 20), (b'21', 21), (b'22', 22), (b'23', 23), (b'24', 24), (b'25', 25), (b'26', 26), (b'27', 27), (b'28', 28), (b'29', 29), (b'30', 30), (b'31', 31), (b'32', 32)], default=0, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='registeringadult',
            name='beneficiary_changed_birthday_month',
            field=models.CharField(blank=True, choices=[('1', '\u0643\u0627\u0646\u0648\u0646 \u0627\u0644\u062b\u0627\u0646\u064a'), ('2', '\u0634\u0628\u0627\u0637'), ('3', '\u0622\u0630\u0627\u0631'), ('4', '\u0646\u064a\u0633\u0627\u0646'), ('5', '\u0623\u064a\u0627\u0631'), ('6', '\u062d\u0632\u064a\u0631\u0627\u0646'), ('7', '\u062a\u0645\u0648\u0632'), ('8', '\u0622\u0628'), ('9', '\u0623\u064a\u0644\u0648\u0644'), ('10', '\u062a\u0634\u0631\u064a\u0646 \u0627\u0644\u0623\u0648\u0644'), ('11', '\u062a\u0634\u0631\u064a\u0646 \u0627\u0644\u062b\u0627\u0646\u064a'), ('12', '\u0643\u0627\u0646\u0648\u0646 \u0627\u0644\u0623\u0648\u0644')], default=0, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='registeringadult',
            name='beneficiary_changed_birthday_year',
            field=models.CharField(blank=True, choices=[(b'1930', 1930), (b'1931', 1931), (b'1932', 1932), (b'1933', 1933), (b'1934', 1934), (b'1935', 1935), (b'1936', 1936), (b'1937', 1937), (b'1938', 1938), (b'1939', 1939), (b'1940', 1940), (b'1941', 1941), (b'1942', 1942), (b'1943', 1943), (b'1944', 1944), (b'1945', 1945), (b'1946', 1946), (b'1947', 1947), (b'1948', 1948), (b'1949', 1949), (b'1950', 1950), (b'1951', 1951), (b'1952', 1952), (b'1953', 1953), (b'1954', 1954), (b'1955', 1955), (b'1956', 1956), (b'1957', 1957), (b'1958', 1958), (b'1959', 1959), (b'1960', 1960), (b'1961', 1961), (b'1962', 1962), (b'1963', 1963), (b'1964', 1964), (b'1965', 1965), (b'1966', 1966), (b'1967', 1967), (b'1968', 1968), (b'1969', 1969), (b'1970', 1970), (b'1971', 1971), (b'1972', 1972), (b'1973', 1973), (b'1974', 1974), (b'1975', 1975), (b'1976', 1976), (b'1977', 1977), (b'1978', 1978), (b'1979', 1979), (b'1980', 1980), (b'1981', 1981), (b'1982', 1982), (b'1983', 1983), (b'1984', 1984), (b'1985', 1985), (b'1986', 1986), (b'1987', 1987), (b'1988', 1988), (b'1989', 1989), (b'1990', 1990), (b'1991', 1991), (b'1992', 1992), (b'1993', 1993), (b'1994', 1994), (b'1995', 1995), (b'1996', 1996), (b'1997', 1997), (b'1998', 1998), (b'1999', 1999), (b'2000', 2000), (b'2001', 2001), (b'2002', 2002), (b'2003', 2003), (b'2004', 2004), (b'2005', 2005), (b'2006', 2006), (b'2007', 2007), (b'2008', 2008), (b'2009', 2009), (b'2010', 2010), (b'2011', 2011), (b'2012', 2012), (b'2013', 2013), (b'2014', 2014), (b'2015', 2015), (b'2016', 2016), (b'2017', 2017), (b'2018', 2018), (b'2019', 2019), (b'2020', 2020), (b'2021', 2021), (b'2022', 2022), (b'2023', 2023), (b'2024', 2024), (b'2025', 2025), (b'2026', 2026), (b'2027', 2027), (b'2028', 2028), (b'2029', 2029), (b'2030', 2030), (b'2031', 2031), (b'2032', 2032), (b'2033', 2033), (b'2034', 2034), (b'2035', 2035), (b'2036', 2036), (b'2037', 2037), (b'2038', 2038), (b'2039', 2039), (b'2040', 2040), (b'2041', 2041), (b'2042', 2042), (b'2043', 2043), (b'2044', 2044), (b'2045', 2045), (b'2046', 2046), (b'2047', 2047), (b'2048', 2048), (b'2049', 2049), (b'2050', 2050)], default=0, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='registeringadult',
            name='beneficiary_changed_mother_full_name',
            field=models.CharField(blank=True, max_length=64L, null=True),
        ),
        migrations.AlterField(
            model_name='complaintcategory',
            name='complaint_type',
            field=models.CharField(blank=True, choices=[('distribution', 'CARD DISTRIBUTION'), ('card', 'CARD'), ('payment', 'PAYMENT'), ('school', 'SCHOOL-RELATED'), ('remove', 'REMOVE FROM THE PROGRAM'), ('other', 'OTHER')], max_length=50, null=True),
        ),
    ]
