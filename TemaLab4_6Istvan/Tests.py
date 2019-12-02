'''
Created on Oct 24, 2019

@author: Tonirel
'''
from Adaugare import create_tz,get_suma,get_tip,get_zi,valid_tz,add_tz, create_state
from Cautari import sum_gr8_than,b4_day_gr8_than,tz_anumit_tip
from Service import sv_el_tz_tip,sv_sum_tip,sv_sold,sv_tz_tip_ord,sv_del_tz_zi,sv_del_tz_per,sv_del_tz_tip,sv_el_tz_small_and_type,sv_undo
def run_all_tests():
    test_create_tz()
    test_valid_tz()
    test_sum_gr8_than()
    test_b4_day_gr8_than()
    test_tz_anumit_tip()
    test_sv_el_tz_tip()
    test_add_tz()
    test_sv_sum_tip()
    test_sv_sold()
    test_sv_tz_tip_ord()
    test_sv_del_tz_zi()
    test_sv_del_tz_per()
    test_sv_del_tz_tip()
    test_sv_el_tz_small_and_type()
    test_undo()
def test_create_tz():
    tz=create_tz(1,100.50,'intrare')
    assert(get_zi(tz)==1)
    assert(get_suma(tz)==100.50)
    assert(get_tip(tz)=='intrare')
    
def test_add_tz():
    s=create_state()
    s2=create_state()
    zi=1
    suma=100
    tip='intrare'
    tz=create_tz(zi,suma,tip)
    add_tz(s, tz)
    add_tz(s2,tz)
    assert(s==s2)
    
def test_valid_tz():
    tz=create_tz(1,100.50,'intrare')
    valid_tz(tz)
        
    tz1=create_tz(-3,100.50,'intrare')
    try:
        valid_tz(tz1)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="zi incorecta!")
        
    tz2=create_tz(3,-34.6,'intrare')
    try:
        valid_tz(tz2)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="suma incorecta!")
        
    tz3=create_tz(3,100.50,'random')
    try:
        valid_tz(tz3)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="tip incorect!")
def test_sum_gr8_than():
    tz1=create_tz(1, 10, 'intrare')
    tz2=create_tz(2, 50, 'iesire')
    assert(sum_gr8_than(30,tz1)==False)
    assert(sum_gr8_than(30,tz2)==True)
def test_b4_day_gr8_than():
    tz1=create_tz(10,50,'intrare')
    assert(b4_day_gr8_than(30,15,tz1)==True)
    tz2=create_tz(10,50,'intrare')
    assert(b4_day_gr8_than(30,5,tz2)==False)
    tz3=create_tz(10,50,'intrare')
    assert(b4_day_gr8_than(100,15,tz3)==False)
    tz4=create_tz(10,50,'intrare')
    assert(b4_day_gr8_than(100,5,tz4)==False)
def test_tz_anumit_tip():
    tz1=create_tz(10,50,'intrare')
    assert(tz_anumit_tip(tz1,'intrare')==True)
    tz2=create_tz(10,50,'iesire')
    assert(tz_anumit_tip(tz2,'iesire')==True)
    tz3=create_tz(10,50,'intrare')
    assert(tz_anumit_tip(tz3,'iesire')==False)
    tz4=create_tz(10,50,'iesire')
    assert(tz_anumit_tip(tz4,'intrare')==False)
    
def test_sv_el_tz_tip():
    s=create_state()
    s2=create_state()
    tz1=create_tz(10,100,'intrare')
    add_tz(s,tz1)
    tz2=create_tz(15,150,'iesire')
    add_tz(s,tz2)
    tz3=create_tz(50,200,'intrare')
    add_tz(s,tz3)
    
    add_tz(s2,tz1)
    add_tz(s2,tz3)
    T='iesire'
    assert (sv_el_tz_tip(T,s)==s2)
    
    s2=create_state()
    add_tz(s2,tz2)
    T='intrare'
    assert(sv_el_tz_tip(T, s)==s2)
def test_sv_el_tz_small_and_type():
    s=create_state()
    s2=create_state()
    tz1=create_tz(10,100,'intrare')
    add_tz(s,tz1)
    tz2=create_tz(15,150,'iesire')
    add_tz(s,tz2)
    tz3=create_tz(50,200,'intrare')
    add_tz(s,tz3)
    T='intrare'
    S=120
    add_tz(s2,tz2)
    add_tz(s2,tz3)
    assert(sv_el_tz_small_and_type(S,T,s)==s2)
def test_sv_sum_tip():
    s=create_state()
    T='intrare'
    assert(sv_sum_tip(T,s)=='Lista este goala!')
    tz1=create_tz(10,100,'intrare')
    add_tz(s,tz1)
    T='iesire'
    assert(sv_sum_tip(T,s)==0)
    tz2=create_tz(15,150,'iesire')
    add_tz(s,tz2)
    tz3=create_tz(50,200,'intrare')
    add_tz(s,tz3)
    T='intrare'
    assert(sv_sum_tip(T,s)==300)
    T='iesire'
    assert(sv_sum_tip(T,s)==150)
def test_sv_sold():
    s=create_state()
    Z=5
    assert(sv_sold(Z,s)=='Lista este goala!')
    tz1=create_tz(1,100,'intrare')
    add_tz(s,tz1)
    tz2=create_tz(3,200,'intrare')
    add_tz(s,tz2)
    tz3=create_tz(2,50,'iesire')
    add_tz(s,tz3)
    tz4=create_tz(4,20,'iesire')
    add_tz(s,tz4)
    assert(sv_sold(Z,s)==230)
    Z=2
    assert(sv_sold(Z,s)==50)
def test_sv_tz_tip_ord():
    s=create_state()
    T='intrare'
    assert(sv_tz_tip_ord(T,s)=='Lista este goala!')
    tz1=create_tz(1,100,'intrare')
    add_tz(s,tz1)
    tz2=create_tz(3,200,'intrare')
    add_tz(s,tz2)
    tz3=create_tz(2,50,'iesire')
    add_tz(s,tz3)
    tz4=create_tz(4,20,'iesire')
    add_tz(s,tz4)
    s2=create_state()
    add_tz(s2,tz1)
    add_tz(s2,tz2)
    assert(sv_tz_tip_ord(T,s)==s2)
    
def test_sv_del_tz_zi():
    s=create_state()
    Z=2
    assert(sv_del_tz_zi(s,Z)=='Lista este goala!')
    tz1=create_tz(1,100,'intrare')
    add_tz(s,tz1)
    tz2=create_tz(1,200,'intrare')
    add_tz(s,tz2)
    tz3=create_tz(2,50,'iesire')
    add_tz(s,tz3)
    tz4=create_tz(2,20,'iesire')
    add_tz(s,tz4)
    s2=create_state()
    add_tz(s2,tz1)
    add_tz(s2,tz2)
    assert(sv_del_tz_zi(s,Z)==s2)
def test_sv_del_tz_per():
    s=create_state()
    Z1=2
    Z2=5
    assert(sv_del_tz_per(s,Z1,Z2)=='Lista este goala!')
    tz1=create_tz(1,100,'intrare')
    add_tz(s,tz1)
    tz2=create_tz(1,200,'intrare')
    add_tz(s,tz2)
    tz3=create_tz(2,50,'iesire')
    add_tz(s,tz3)
    tz4=create_tz(3,20,'iesire')
    add_tz(s,tz4)
    Z1=1
    Z2=2
    s2=create_state()
    add_tz(s2,tz4)
    assert(sv_del_tz_per(s,Z1,Z2)==s2)
    Z1=2
    Z2=1
    assert(sv_del_tz_per(s,Z1,Z2)==s2)
def test_sv_del_tz_tip():
    s=create_state()
    T='intrare'
    assert(sv_del_tz_tip(s,T)=='Lista este goala!')
    tz1=create_tz(1,100,'intrare')
    add_tz(s,tz1)
    tz2=create_tz(1,200,'intrare')
    add_tz(s,tz2)
    tz3=create_tz(2,50,'iesire')
    add_tz(s,tz3)
    tz4=create_tz(3,20,'iesire')
    add_tz(s,tz4)
    s2=create_state()
    add_tz(s2,tz3)
    add_tz(s2,tz4)
    assert(sv_del_tz_tip(s,T)==s2)
    s3=create_state()
    T='iesire'
    assert(sv_del_tz_tip(s,T)==s3)
def test_undo():
    s=create_state()
    us=create_state()
    tz1=create_tz(1,100,'intrare')
    add_tz(s,tz1)
    us.append(tz1)
    tz2=create_tz(2,200,'iesire')
    add_tz(s,tz2)
    us2=create_state()
    us2.append(tz1)
    us2.append(tz1)
    us.append(us2.copy())
    s2=create_state()
    add_tz(s2,tz1)
    del s[:]
    s+=sv_undo(s,us).copy()
    assert(us==s2)