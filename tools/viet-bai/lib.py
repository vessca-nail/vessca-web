"""Công cụ ghi bài blog VESSCA (4 ngôn ngữ). Xem content/HUONG-DAN-VIET-BAI.md."""
import json
import os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','content','posts')+os.sep
def luu(slug,title,cat,at,excerpt,mt,md,kw,anh,content,faq,i18n=None):
    d={'slug':slug,'title':title,'category':cat,'author':'VESSCA','status':'published',
       'publishedAt':at,'updatedAt':at,'excerpt':excerpt,'metaTitle':mt,'metaDescription':md,
       'keywords':kw,'coverAlt':anh['bia']['alt'],'faq':faq,'anh':anh,'content':content}
    if i18n: d['i18n']=i18n
    json.dump(d,open(B+slug+'.json','w'),ensure_ascii=False,indent=2)
    print('ok',slug,len(content.split()))
DIA_VI='VESSCA ở 251/30 Lê Quang Định, phường Gia Định (Bình Thạnh cũ), mở cửa 9:00–20:30 mỗi ngày, điện thoại 0933.528.501'
def them(slug,i18n):
    p=B+slug+'.json'; d=json.load(open(p)); d['i18n']=i18n
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=2); print('i18n ok',slug,list(i18n))
EN_END='VESSCA is at 251/30 Le Quang Dinh, Gia Dinh ward (Binh Thanh), Ho Chi Minh City, open 9:00–20:30 daily.'
KO_END='VESSCA: 호치민 빈탄 251/30 Lê Quang Định(Gia Định 동), 매일 9:00–20:30.'
ZH_END='VESSCA:胡志明市平盛郡 251/30 Lê Quang Định(Gia Định 坊),每天 9:00–20:30。'
import re
CHU={'en':'Photo','ko':'사진','zh':'图片'}
def them2(slug,i18n,alts=None):
    """Như them(), nhưng thay <!--anh:N--> bằng ảnh đã có trong bản tiếng Việt."""
    p=B+slug+'.json'; d=json.load(open(p))
    figs={}
    for m in re.finditer(r'<figure><img src="(/media/blog/'+re.escape(slug)+r'-(\d)\.jpg)"[^>]*>.*?<a href="([^"]+)">([^<]+)</a></figcaption></figure>',d['content']):
        figs[m.group(2)]=(m.group(1),m.group(3),m.group(4))
    for lang,t in i18n.items():
        def rep(m):
            n=m.group(1)
            if n not in figs: return ''
            src,link,au=figs[n]
            alt=((alts or {}).get(lang) or {}).get(n) or t['coverAlt']
            return f'<figure><img src="{src}" alt="{alt}" width="1000" loading="lazy" /><figcaption>{alt} · {CHU[lang]}: <a href="{link}">{au}</a></figcaption></figure>'
        t['content']=re.sub(r'<!--anh:(\d)-->',rep,t['content'])
    d['i18n']=i18n
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=2); print('i18n ok',slug,list(i18n),'figs',list(figs))


def A(bia,trong):
    """bia/trong = (tim, vi, en, ko, zh)"""
    def one(t):
        return {'tim':t[0],'alt':t[1],'altI18n':{'en':t[2],'ko':t[3],'zh':t[4]}}
    return {'bia':one(bia),'trong_bai':[one(x) for x in trong]}
def F(pairs): return [{'q':q,'a':a} for q,a in pairs]
def bai(slug,at,cat,anh,V,E,K,Z):
    """V/E/K/Z = (title, excerpt, metaTitle, metaDesc, keywords, content, faq_pairs)"""
    ends={'en':EN_END,'ko':KO_END,'zh':ZH_END}
    i18n={}
    for lang,X in (('en',E),('ko',K),('zh',Z)):
        c=X[5].strip()+f'\n<p>{ends[lang]}</p>'
        i18n[lang]={'title':X[0],'excerpt':X[1],'metaTitle':X[2],'metaDescription':X[3],
            'keywords':X[4],'coverAlt':anh['bia']['altI18n'][lang],'content':c,'faq':F(X[6])}
    luu(slug,V[0],cat,at,V[1],V[2],V[3],V[4],anh,V[5].strip(),F(V[6]),i18n)
