import tkinter as tk
import math
from tkinter import ttk, messagebox

_m = math

# ============================================================
# MẠNG NGỮ NGHĨA TAM GIÁC - 60 CÔNG THỨC (ĐÃ SỬA TRÙNG)
# ============================================================
MANG_NGU_NGHIA_TAM_GIAC = {
    "ten_hinh": "Tam giác",
    "cac_node": [
        "canh_a","canh_b","canh_c",
        "goc_A","goc_B","goc_C",
        "chu_vi","ban_kinh_p","dien_tich",
        "duong_cao_hA","duong_cao_hB","duong_cao_hC",
        "ban_kinh_ngoai_tiep_R","ban_kinh_noi_tiep_r",
        "trung_tuyen_mA","trung_tuyen_mB","trung_tuyen_mC",
        "phan_giac_lA","phan_giac_lB","phan_giac_lC",
    ],
    "rang_buoc": [
        # === I. CƠ BẢN ===
        "1.  P = a + b + c",
        "2.  p = (a + b + c) / 2",
        "3.  a < b + c  (Bất đẳng thức 1)",
        "4.  b < a + c  (Bất đẳng thức 2)",
        "5.  c < a + b  (Bất đẳng thức 3)",
        "6.  A + B + C = 180°",
        "7.  A = 180° − (B + C)",
        # === II. DIỆN TÍCH ===
        "8.  S = (1/2)·a·h_a",
        "9.  S = (1/2)·b·h_b",
        "10. S = (1/2)·c·h_c",
        "11. S = √[p(p−a)(p−b)(p−c)]  (Heron)",
        "12. S = (1/2)·a·b·sin(C)",
        "13. S = (1/2)·b·c·sin(A)",
        "14. S = (1/2)·a·c·sin(B)",
        "15. S = p·r",
        "16. S = (abc)/(4R)",
        # === III. ĐỊNH LÝ SIN ===
        "17. a / sin(A) = 2R",
        "18. b / sin(B) = 2R",
        "19. c / sin(C) = 2R",
        # === IV. ĐỊNH LÝ COS ===
        "20. a² = b² + c² − 2bc·cos(A)",
        "21. b² = a² + c² − 2ac·cos(B)",
        "22. c² = a² + b² − 2ab·cos(C)",
        "23. cos(A) = (b²+c²−a²) / (2bc)",
        "24. cos(B) = (a²+c²−b²) / (2ac)",
        "25. cos(C) = (a²+b²−c²) / (2ab)",
        # === V. SUY RA TỪ ĐỊNH LÝ SIN ===
        "26. a = 2R·sin(A)",
        "27. b = 2R·sin(B)",
        "28. c = 2R·sin(C)",
        "29. sin(A) = a/(2R)",
        # === VI. ĐƯỜNG CAO ===
        "30. h_a = 2S / a",
        "31. h_b = 2S / b",
        "32. h_c = 2S / c",
        "33. h_a = b·sin(C)",
        "34. h_a = c·sin(B)",
        "35. h_b = a·sin(C)",
        "36. h_b = c·sin(A)",
        "37. h_c = a·sin(B)",
        "38. h_c = b·sin(A)",
        # === VII. BÁN KÍNH ===
        "39. r = S / p",
        "40. R = (abc)/(4S)",
        "41. tan(A) = 4S/(b²+c²−a²)  [Góc từ S và 3 cạnh]",   # ← MỚI (CT41 cũ ≡ CT17)
        "42. r = (p−a)·tan(A/2)",
        "43. r = (p−b)·tan(B/2)",
        "44. r = (p−c)·tan(C/2)",
        # === VIII. DIỆN TÍCH NÂNG CAO ===
        "45. S = 2R²·sin(A)·sin(B)·sin(C)",
        # === IX. TRUNG TUYẾN (ĐÃ GỘP) ===
        "46. m_a = (1/2)·√(2b²+2c²−a²)",
        "47. m_b = (1/2)·√(2a²+2c²−b²)",
        "48. m_c = (1/2)·√(2a²+2b²−c²)",
        # === X. PHÂN GIÁC ===
        "49. l_a = 2bc·cos(A/2) / (b+c)",
        "50. l_b = 2ac·cos(B/2) / (a+c)",
        "51. l_c = 2ab·cos(C/2) / (a+b)",
        # === XI. GÓC TỪ BK NỘI TIẾP (CT52-54 MỚI) ===
        "52. A = 2·arctan[r/(p−a)]",                            
        "53. B = 2·arctan[r/(p−b)]",                            
        "54. C = 2·arctan[r/(p−c)]",                            
        # === XII. HỆ THỨC HÌNH CHIẾU ===
        "55. a = b·cos(C) + c·cos(B)",
        "56. b = a·cos(C) + c·cos(A)",
        "57. c = a·cos(B) + b·cos(A)",
        # === XIII. CÔNG THỨC ĐẶC BIỆT ===
        "58. r = 4R·sin(A/2)·sin(B/2)·sin(C/2)",
        "59. S = p²·tan(A/2)·tan(B/2)·tan(C/2)",
        "60. p = r·(cot(A/2)+cot(B/2)+cot(C/2))",
    ],
    "ma_tran": {
        "1":  ["chu_vi","canh_a","canh_b","canh_c"],
        "2":  ["ban_kinh_p","canh_a","canh_b","canh_c"],
        "3":  ["canh_a","canh_b","canh_c"],
        "4":  ["canh_b","canh_a","canh_c"],
        "5":  ["canh_c","canh_a","canh_b"],
        "6":  ["goc_C","goc_A","goc_B"],
        "7":  ["goc_A","goc_B","goc_C"],
        "8":  ["dien_tich","canh_a","duong_cao_hA"],
        "9":  ["dien_tich","canh_b","duong_cao_hB"],
        "10": ["dien_tich","canh_c","duong_cao_hC"],
        "11": ["dien_tich","ban_kinh_p","canh_a","canh_b","canh_c"],
        "12": ["dien_tich","canh_a","canh_b","goc_C"],
        "13": ["dien_tich","canh_b","canh_c","goc_A"],
        "14": ["dien_tich","canh_a","canh_c","goc_B"],
        "15": ["dien_tich","ban_kinh_p","ban_kinh_noi_tiep_r"],
        "16": ["dien_tich","canh_a","canh_b","canh_c","ban_kinh_ngoai_tiep_R"],
        "17": ["ban_kinh_ngoai_tiep_R","canh_a","goc_A"],
        "18": ["ban_kinh_ngoai_tiep_R","canh_b","goc_B"],
        "19": ["ban_kinh_ngoai_tiep_R","canh_c","goc_C"],
        "20": ["canh_a","canh_b","canh_c","goc_A"],
        "21": ["canh_b","canh_a","canh_c","goc_B"],
        "22": ["canh_c","canh_a","canh_b","goc_C"],
        "23": ["goc_A","canh_a","canh_b","canh_c"],
        "24": ["goc_B","canh_a","canh_b","canh_c"],
        "25": ["goc_C","canh_a","canh_b","canh_c"],
        "26": ["canh_a","ban_kinh_ngoai_tiep_R","goc_A"],
        "27": ["canh_b","ban_kinh_ngoai_tiep_R","goc_B"],
        "28": ["canh_c","ban_kinh_ngoai_tiep_R","goc_C"],
        "29": ["goc_A","canh_a","ban_kinh_ngoai_tiep_R"],
        "30": ["duong_cao_hA","dien_tich","canh_a"],
        "31": ["duong_cao_hB","dien_tich","canh_b"],
        "32": ["duong_cao_hC","dien_tich","canh_c"],
        "33": ["duong_cao_hA","canh_b","goc_C"],
        "34": ["duong_cao_hA","canh_c","goc_B"],
        "35": ["duong_cao_hB","canh_a","goc_C"],
        "36": ["duong_cao_hB","canh_c","goc_A"],
        "37": ["duong_cao_hC","canh_a","goc_B"],
        "38": ["duong_cao_hC","canh_b","goc_A"],
        "39": ["ban_kinh_noi_tiep_r","dien_tich","ban_kinh_p"],
        "40": ["ban_kinh_ngoai_tiep_R","canh_a","canh_b","canh_c","dien_tich"],
        "41": ["goc_A","dien_tich","canh_a","canh_b","canh_c"],          # MỚI
        "42": ["ban_kinh_noi_tiep_r","ban_kinh_p","canh_a","goc_A"],
        "43": ["ban_kinh_noi_tiep_r","ban_kinh_p","canh_b","goc_B"],
        "44": ["ban_kinh_noi_tiep_r","ban_kinh_p","canh_c","goc_C"],
        "45": ["dien_tich","ban_kinh_ngoai_tiep_R","goc_A","goc_B","goc_C"],
        "46": ["trung_tuyen_mA","canh_a","canh_b","canh_c"],
        "47": ["trung_tuyen_mB","canh_a","canh_b","canh_c"],
        "48": ["trung_tuyen_mC","canh_a","canh_b","canh_c"],
        "49": ["phan_giac_lA","canh_b","canh_c","goc_A"],
        "50": ["phan_giac_lB","canh_a","canh_c","goc_B"],
        "51": ["phan_giac_lC","canh_a","canh_b","goc_C"],
        "52": ["goc_A","ban_kinh_noi_tiep_r","ban_kinh_p","canh_a"],     
        "53": ["goc_B","ban_kinh_noi_tiep_r","ban_kinh_p","canh_b"],      
        "54": ["goc_C","ban_kinh_noi_tiep_r","ban_kinh_p","canh_c"],     
        "55": ["canh_a","canh_b","canh_c","goc_B","goc_C"],
        "56": ["canh_b","canh_a","canh_c","goc_A","goc_C"],
        "57": ["canh_c","canh_a","canh_b","goc_A","goc_B"],
        "58": ["ban_kinh_noi_tiep_r","ban_kinh_ngoai_tiep_R","goc_A","goc_B","goc_C"],
        "59": ["dien_tich","ban_kinh_p","goc_A","goc_B","goc_C"],
        "60": ["ban_kinh_p","ban_kinh_noi_tiep_r","goc_A","goc_B","goc_C"],
    },
}

# ============================================================
# TINH TOAN
# ============================================================
def kiem_tra_ton_tai(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a+b > c) and (b+c > a) and (a+c > b)

def phan_loai_tam_giac(a, b, c):
    if abs(a-b) < 1e-9 and abs(b-c) < 1e-9:
        return "Tam giác đều"
    canh = sorted([a,b,c])
    vuong = abs(canh[0]**2+canh[1]**2-canh[2]**2) < 1e-9*canh[2]**2
    can = abs(a-b)<1e-9*max(a,b) or abs(b-c)<1e-9*max(b,c) or abs(a-c)<1e-9*max(a,c)
    if can: return "Tam giác vuông cân" if vuong else "Tam giác cân"
    return "Tam giác vuông" if vuong else "Tam giác thường"

def tinh_day_du(a, b, c):
    kq = {}
    if not kiem_tra_ton_tai(a, b, c):
        kq["loi"] = "Ba cạnh không tạo thành tam giác!\n(Điều kiện: tổng 2 cạnh > cạnh còn lại)"
        return kq
    p = (a+b+c)/2
    S = _m.sqrt(max(0, p*(p-a)*(p-b)*(p-c)))
    if S < 1e-12:
        kq["loi"] = "Tam giác suy biến (diện tích = 0)!"
        return kq
    cosA = max(-1, min(1, (b**2+c**2-a**2)/(2*b*c)))
    cosB = max(-1, min(1, (a**2+c**2-b**2)/(2*a*c)))
    cosC = max(-1, min(1, (a**2+b**2-c**2)/(2*a*b)))
    A = _m.degrees(_m.acos(cosA))
    B = _m.degrees(_m.acos(cosB))
    C = _m.degrees(_m.acos(cosC))
    R = (a*b*c)/(4*S)
    r = S/p
    kq["phan_loai"]          = phan_loai_tam_giac(a,b,c)
    kq["canh_a"]             = round(a,6); kq["canh_b"]=round(b,6); kq["canh_c"]=round(c,6)
    kq["goc_A"]              = round(A,4); kq["goc_B"]=round(B,4); kq["goc_C"]=round(C,4)
    kq["chu_vi"]             = round(a+b+c,6)
    kq["ban_kinh_p"]         = round(p,6)
    kq["dien_tich"]          = round(S,6)
    kq["duong_cao_hA"]       = round(2*S/a,6)
    kq["duong_cao_hB"]       = round(2*S/b,6)
    kq["duong_cao_hC"]       = round(2*S/c,6)
    kq["ban_kinh_ngoai_tiep_R"] = round(R,6)
    kq["ban_kinh_noi_tiep_r"]   = round(r,6)
    kq["trung_tuyen_mA"]    = round(0.5*_m.sqrt(2*b**2+2*c**2-a**2),6)
    kq["trung_tuyen_mB"]    = round(0.5*_m.sqrt(2*a**2+2*c**2-b**2),6)
    kq["trung_tuyen_mC"]    = round(0.5*_m.sqrt(2*a**2+2*b**2-c**2),6)
    Ar=_m.radians(A); Br=_m.radians(B); Cr=_m.radians(C)
    kq["phan_giac_lA"] = round((2*b*c*_m.cos(Ar/2))/(b+c),6)
    kq["phan_giac_lB"] = round((2*a*c*_m.cos(Br/2))/(a+c),6)
    kq["phan_giac_lC"] = round((2*a*b*_m.cos(Cr/2))/(a+b),6)
    return kq

# ============================================================
# GIẢI TAM GIÁC (hỗ trợ SSA 2 nghiệm)
# Trả về: (kq1, chuoi1, kq2_hoac_None, chuoi2_hoac_None)
# ============================================================
def _giai_SSA(canh_doi, canh_ke, goc_doi_deg, ten_a, ten_b, ten_A):
    """Giải bài toán SSA: biết canh_doi, canh_ke, goc_doi.
       Trả về list các (a,b,c) nghiệm hợp lệ cùng mô tả."""
    A = _m.radians(goc_doi_deg)
    sinB = canh_ke * _m.sin(A) / canh_doi
    if sinB > 1+1e-9:
        return [], f"sin({ten_b}) = {sinB:.4f} > 1 → Vô nghiệm!"
    results = []
    msg = ""
    if abs(sinB - 1) < 1e-9:
        # 1 nghiệm: góc B = 90°
        B = _m.pi/2; C = _m.pi - A - B
        if C > 1e-9:
            c = canh_doi * _m.sin(C) / _m.sin(A)
            results.append((canh_doi, canh_ke, c))
        msg = f"sin({ten_b})=1 → {ten_b}=90° (1 nghiệm)"
    else:
        B1 = _m.asin(sinB); B2 = _m.pi - B1
        for Bi in [B1, B2]:
            C = _m.pi - A - Bi
            if C > 1e-9:
                c = canh_doi * _m.sin(C) / _m.sin(A)
                if c > 0:
                    results.append((canh_doi, canh_ke, c))
        if len(results) == 2: msg = "SSA → 2 nghiệm"
        elif len(results) == 1: msg = "SSA → 1 nghiệm duy nhất"
        else: msg = "SSA → Vô nghiệm"
    return results, msg

def giai_tam_giac_tu_du_lieu(gv_raw, unit_goc="do"):
    """unit_goc: 'do' hoặc 'rad' """
    chuoi = []
    nghiem2 = None; chuoi2 = []
    try:
        # Chuyển góc về độ nếu nhập radian
        gv = dict(gv_raw)
        if unit_goc == "rad":
            for k in ["goc_A","goc_B","goc_C"]:
                if k in gv: gv[k] = _m.degrees(gv[k])

        def _r(key): return _m.radians(gv[key])

        a = b = c = None
        # --- 3 CẠNH ---
        if all(k in gv for k in ["canh_a","canh_b","canh_c"]):
            a,b,c = gv["canh_a"],gv["canh_b"],gv["canh_c"]
            chuoi.append(("3,4,5","Kiểm tra bất đẳng thức tam giác (a<b+c, b<a+c, c<a+b)"))
        # --- 2 CẠNH + GÓC KẸP ---
        elif "canh_a" in gv and "canh_b" in gv and "goc_C" in gv:
            a,b = gv["canh_a"],gv["canh_b"]; C=_r("goc_C")
            c = _m.sqrt(a**2+b**2-2*a*b*_m.cos(C))
            chuoi.append(("22","c² = a²+b²−2ab·cos(C)  → tìm c"))
        elif "canh_a" in gv and "canh_c" in gv and "goc_B" in gv:
            a,c = gv["canh_a"],gv["canh_c"]; B=_r("goc_B")
            b = _m.sqrt(a**2+c**2-2*a*c*_m.cos(B))
            chuoi.append(("21","b² = a²+c²−2ac·cos(B)  → tìm b"))
        elif "canh_b" in gv and "canh_c" in gv and "goc_A" in gv:
            b,c = gv["canh_b"],gv["canh_c"]; A=_r("goc_A")
            a = _m.sqrt(b**2+c**2-2*b*c*_m.cos(A))
            chuoi.append(("20","a² = b²+c²−2bc·cos(A)  → tìm a"))
        # --- 1 CẠNH + 2 GÓC (AAS / ASA) ---
        elif "canh_a" in gv and "goc_A" in gv and "goc_B" in gv:
            a=gv["canh_a"]; A=_r("goc_A"); B=_r("goc_B"); C=_m.pi-A-B
            if C<=1e-9: return {"loi":"Tổng A+B ≥ 180°!"},[],None,[]
            b=a*_m.sin(B)/_m.sin(A); c=a*_m.sin(C)/_m.sin(A)
            chuoi.append(("7","C = 180°−(A+B)  → tìm góc C"))
            chuoi.append(("17,18,19","a/sin(A)=2R → b,c"))
        elif "canh_b" in gv and "goc_A" in gv and "goc_B" in gv:
            b=gv["canh_b"]; A=_r("goc_A"); B=_r("goc_B"); C=_m.pi-A-B
            if C<=1e-9: return {"loi":"Tổng A+B ≥ 180°!"},[],None,[]
            a=b*_m.sin(A)/_m.sin(B); c=b*_m.sin(C)/_m.sin(B)
            chuoi.append(("7","C = 180°−(A+B)  → tìm C")); chuoi.append(("17,18,19","a,c từ định lý sin"))
        elif "canh_b" in gv and "goc_B" in gv and "goc_C" in gv:
            b=gv["canh_b"]; B=_r("goc_B"); C=_r("goc_C"); A=_m.pi-B-C
            if A<=1e-9: return {"loi":"Tổng B+C ≥ 180°!"},[],None,[]
            a=b*_m.sin(A)/_m.sin(B); c=b*_m.sin(C)/_m.sin(B)
            chuoi.append(("7","A = 180°−(B+C)")); chuoi.append(("17,18,19","a,c từ định lý sin"))
        elif "canh_c" in gv and "goc_A" in gv and "goc_C" in gv:
            c=gv["canh_c"]; A=_r("goc_A"); C=_r("goc_C"); B=_m.pi-A-C
            if B<=1e-9: return {"loi":"Tổng A+C ≥ 180°!"},[],None,[]
            a=c*_m.sin(A)/_m.sin(C); b=c*_m.sin(B)/_m.sin(C)
            chuoi.append(("7","B = 180°−(A+C)")); chuoi.append(("17,18,19","a,b từ định lý sin"))
        elif "canh_c" in gv and "goc_B" in gv and "goc_C" in gv:
            c=gv["canh_c"]; B=_r("goc_B"); C=_r("goc_C"); A=_m.pi-B-C
            if A<=1e-9: return {"loi":"Tổng B+C ≥ 180°!"},[],None,[]
            a=c*_m.sin(A)/_m.sin(C); b=c*_m.sin(B)/_m.sin(C)
            chuoi.append(("7","A = 180°−(B+C)")); chuoi.append(("17,18,19","a,b từ định lý sin"))
        elif "canh_a" in gv and "goc_A" in gv and "goc_C" in gv:
            a=gv["canh_a"]; A=_r("goc_A"); C=_r("goc_C"); B=_m.pi-A-C
            if B<=1e-9: return {"loi":"Tổng A+C ≥ 180°!"},[],None,[]
            b=a*_m.sin(B)/_m.sin(A); c=a*_m.sin(C)/_m.sin(A)
            chuoi.append(("7","B = 180°−(A+C)")); chuoi.append(("17,18,19","b,c từ định lý sin"))
        # --- SSA (2 CẠNH + GÓC ĐỐI — CÓ THỂ 2 NGHIỆM) ---
        elif "canh_a" in gv and "canh_b" in gv and "goc_A" in gv:
            nghiems, msg = _giai_SSA(gv["canh_a"],gv["canh_b"],gv["goc_A"],"a","b","B")
            if not nghiems: return {"loi": f"SSA(a,b,A): {msg}"},[],None,[]
            a,b,c = nghiems[0]
            chuoi.append(("17,18,19",f"SSA: sin(B)=b·sin(A)/a → {msg}"))
            if len(nghiems)==2:
                a2,b2,c2 = nghiems[1]
                nghiem2 = tinh_day_du(a2,b2,c2); chuoi2=list(chuoi)
                chuoi2.append(("20","Nghiệm 2: cạnh c₂ từ định lý cos"))
        elif "canh_a" in gv and "canh_c" in gv and "goc_A" in gv:
            nghiems, msg = _giai_SSA(gv["canh_a"],gv["canh_c"],gv["goc_A"],"a","c","C")
            if not nghiems: return {"loi": f"SSA(a,c,A): {msg}"},[],None,[]
            a,c,b = nghiems[0]
            chuoi.append(("17,18,19",f"SSA: sin(C)=c·sin(A)/a → {msg}"))
            if len(nghiems)==2:
                a2,c2,b2 = nghiems[1]
                nghiem2 = tinh_day_du(a2,b2,c2); chuoi2=list(chuoi)
        elif "canh_b" in gv and "canh_a" in gv and "goc_B" in gv:
            nghiems, msg = _giai_SSA(gv["canh_b"],gv["canh_a"],gv["goc_B"],"b","a","A")
            if not nghiems: return {"loi": f"SSA(b,a,B): {msg}"},[],None,[]
            b,a,c = nghiems[0]
            chuoi.append(("17,18,19",f"SSA: sin(A)=a·sin(B)/b → {msg}"))
            if len(nghiems)==2:
                b2,a2,c2 = nghiems[1]; nghiem2=tinh_day_du(a2,b2,c2); chuoi2=list(chuoi)
        elif "canh_b" in gv and "canh_c" in gv and "goc_B" in gv:
            nghiems, msg = _giai_SSA(gv["canh_b"],gv["canh_c"],gv["goc_B"],"b","c","C")
            if not nghiems: return {"loi": f"SSA(b,c,B): {msg}"},[],None,[]
            b,c,a = nghiems[0]
            chuoi.append(("17,18,19",f"SSA: sin(C)=c·sin(B)/b → {msg}"))
            if len(nghiems)==2:
                b2,c2,a2 = nghiems[1]; nghiem2=tinh_day_du(a2,b2,c2); chuoi2=list(chuoi)
        elif "canh_c" in gv and "canh_a" in gv and "goc_C" in gv:
            nghiems, msg = _giai_SSA(gv["canh_c"],gv["canh_a"],gv["goc_C"],"c","a","A")
            if not nghiems: return {"loi": f"SSA(c,a,C): {msg}"},[],None,[]
            c,a,b = nghiems[0]
            chuoi.append(("17,18,19",f"SSA: sin(A)=a·sin(C)/c → {msg}"))
            if len(nghiems)==2:
                c2,a2,b2 = nghiems[1]; nghiem2=tinh_day_du(a2,b2,c2); chuoi2=list(chuoi)
        elif "canh_c" in gv and "canh_b" in gv and "goc_C" in gv:
            nghiems, msg = _giai_SSA(gv["canh_c"],gv["canh_b"],gv["goc_C"],"c","b","B")
            if not nghiems: return {"loi": f"SSA(c,b,C): {msg}"},[],None,[]
            c,b,a = nghiems[0]
            chuoi.append(("17,18,19",f"SSA: sin(B)=b·sin(C)/c → {msg}"))
            if len(nghiems)==2:
                c2,b2,a2 = nghiems[1]; nghiem2=tinh_day_du(a2,b2,c2); chuoi2=list(chuoi)
        # --- DIỆN TÍCH + 2 CẠNH ---
        elif "dien_tich" in gv and "canh_a" in gv and "canh_b" in gv:
            S=gv["dien_tich"]; a=gv["canh_a"]; b=gv["canh_b"]
            sinC=2*S/(a*b)
            if sinC>1+1e-9 or sinC<=0: return {"loi":"Diện tích không hợp lệ với 2 cạnh a,b!"},[],None,[]
            sinC=min(1,sinC)
            C=_m.asin(sinC); c=_m.sqrt(a**2+b**2-2*a*b*_m.cos(C))
            chuoi.append(("12","sin(C)=2S/(ab)  → tìm C")); chuoi.append(("22","c² = a²+b²−2ab·cos(C)"))
            # SSA dạng ngược: sin(C) có thể có 2 nghiệm
            if sinC < 1-1e-9:
                C2=_m.pi-C; c2_sq=a**2+b**2-2*a*b*_m.cos(C2)
                if c2_sq > 0:
                    c2=_m.sqrt(c2_sq)
                    nghiem2=tinh_day_du(a,b,c2)
                    if "loi" not in nghiem2:
                        chuoi2=list(chuoi)
                        chuoi2.append(("22","Nghiệm 2: C₂=π−C → c₂"))
        elif "dien_tich" in gv and "canh_b" in gv and "canh_c" in gv:
            S=gv["dien_tich"]; b=gv["canh_b"]; c=gv["canh_c"]
            sinA=2*S/(b*c)
            if sinA>1+1e-9 or sinA<=0: return {"loi":"Diện tích không hợp lệ với 2 cạnh b,c!"},[],None,[]
            sinA=min(1,sinA); A=_m.asin(sinA); a=_m.sqrt(b**2+c**2-2*b*c*_m.cos(A))
            chuoi.append(("13","sin(A)=2S/(bc)  → tìm A")); chuoi.append(("20","a² = b²+c²−2bc·cos(A)"))
        elif "dien_tich" in gv and "canh_a" in gv and "canh_c" in gv:
            S=gv["dien_tich"]; a=gv["canh_a"]; c=gv["canh_c"]
            sinB=2*S/(a*c)
            if sinB>1+1e-9 or sinB<=0: return {"loi":"Diện tích không hợp lệ với 2 cạnh a,c!"},[],None,[]
            sinB=min(1,sinB); B=_m.asin(sinB); b=_m.sqrt(a**2+c**2-2*a*c*_m.cos(B))
            chuoi.append(("14","sin(B)=2S/(ac)  → tìm B")); chuoi.append(("21","b² = a²+c²−2ac·cos(B)"))
        # --- CHU VI + 2 CẠNH ---
        elif "chu_vi" in gv and "canh_a" in gv and "canh_b" in gv:
            P=gv["chu_vi"]; a=gv["canh_a"]; b=gv["canh_b"]; c=P-a-b
            if c<=0: return {"loi":"Chu vi không hợp lệ!"},[],None,[]
            chuoi.append(("1","c = P − a − b"))
        elif "chu_vi" in gv and "canh_a" in gv and "canh_c" in gv:
            P=gv["chu_vi"]; a=gv["canh_a"]; c=gv["canh_c"]; b=P-a-c
            if b<=0: return {"loi":"Chu vi không hợp lệ!"},[],None,[]
            chuoi.append(("1","b = P − a − c"))
        elif "chu_vi" in gv and "canh_b" in gv and "canh_c" in gv:
            P=gv["chu_vi"]; b=gv["canh_b"]; c=gv["canh_c"]; a=P-b-c
            if a<=0: return {"loi":"Chu vi không hợp lệ!"},[],None,[]
            chuoi.append(("1","a = P − b − c"))
        # --- R + 2 GÓC ---
        elif "ban_kinh_ngoai_tiep_R" in gv and "goc_A" in gv and "goc_B" in gv:
            R=gv["ban_kinh_ngoai_tiep_R"]; A=_r("goc_A"); B=_r("goc_B"); C=_m.pi-A-B
            if C<=1e-9: return {"loi":"Tổng A+B ≥ 180°!"},[],None,[]
            a=2*R*_m.sin(A); b=2*R*_m.sin(B); c=2*R*_m.sin(C)
            chuoi.append(("7","C = 180°−(A+B)")); chuoi.append(("26,27,28","a,b,c = 2R·sinA/B/C"))
        # --- BÀI TOÁN NGƯỢC: ĐƯỜNG CAO ---
        elif "duong_cao_hA" in gv and "canh_a" in gv and "canh_b" in gv:
            hA=gv["duong_cao_hA"]; a=gv["canh_a"]; b=gv["canh_b"]
            S=hA*a/2
            sinC=2*S/(a*b); 
            if sinC>1+1e-9 or sinC<=0: return {"loi":"h_a và cạnh a,b không hợp lệ!"},[],None,[]
            sinC=min(1,sinC); C=_m.asin(sinC); c=_m.sqrt(a**2+b**2-2*a*b*_m.cos(C))
            chuoi.append(("8","S = h_a·a/2  → diện tích")); chuoi.append(("12","sin(C)=2S/(ab)  → tìm C,c"))
        elif "duong_cao_hA" in gv and "canh_b" in gv and "goc_C" in gv:
            hA=gv["duong_cao_hA"]; b=gv["canh_b"]; C=_r("goc_C")
            sinC=_m.sin(C); 
            if abs(sinC)<1e-12: return {"loi":"Góc C không hợp lệ!"},[],None,[]
            return {"loi":"Cần thêm thông số (h_a + b + C không đủ để xác định tam giác)!"},[],None,[]
        # --- BÀI TOÁN NGƯỢC: BÁN KÍNH NỘI TIẾP + 2 CẠNH ---
        elif "ban_kinh_noi_tiep_r" in gv and "canh_a" in gv and "canh_b" in gv:
            r=gv["ban_kinh_noi_tiep_r"]; a=gv["canh_a"]; b=gv["canh_b"]
            def f(x):
                if x<=0 or x>=a+b: return float('inf')
                pp=(a+b+x)/2
                if pp<=a or pp<=b or pp<=x: return float('inf')
                return r**2*pp - (pp-a)*(pp-b)*(pp-x)
            # Binary search
            lo,hi = abs(a-b)+1e-9, a+b-1e-9
            found=False
            for _ in range(200):
                mid=(lo+hi)/2
                if abs(hi-lo)<1e-10: found=True; break
                if f(lo)*f(mid)<=0: hi=mid
                else: lo=mid
            if not found or abs(f(mid))>1e-6:
                return {"loi":"Không tìm được cạnh c từ r,a,b (kiểm tra lại giá trị)!"},[],None,[]
            c=mid
            chuoi.append(("39,11","r=S/p, Heron → tìm c từ r,a,b (phương trình số)"))
        else:
            return {
                "loi": "Không đủ dữ liệu để tính tam giác!\nCần ít nhất:\n"
                       "• 3 cạnh  • 2 cạnh + góc kẹp\n"
                       "• 1 cạnh + 2 góc  • S + 2 cạnh\n"
                       "• P + 2 cạnh  • R + 2 góc\n"
                       "• h_a + 2 cạnh  • r + 2 cạnh\n"
                       "• SSA (2 cạnh + góc đối — có thể 2 nghiệm)"
            }, [], None, []

        kq = tinh_day_du(a, b, c)
        if "loi" not in kq:
            chuoi += [
                ("2","p = (a+b+c)/2  → nửa chu vi"),
                ("11","S = √[p(p-a)(p-b)(p-c)]  (Heron)"),
                ("23,24,25","cos(A),cos(B),cos(C) → suy ra góc"),
                ("30,31,32","h_a=2S/a, h_b=2S/b, h_c=2S/c  → đường cao"),
                ("40","R = abc/(4S)  → bán kính ngoại tiếp"),
                ("39","r = S/p  → bán kính nội tiếp"),
                ("46,47,48","m_a,m_b,m_c  → trung tuyến"),
                ("49,50,51","l_a,l_b,l_c  → phân giác"),
            ]
            if nghiem2 and "loi" not in nghiem2:
                chuoi2 += [
                    ("2","[Nghiệm 2] p = (a+b+c)/2"),
                    ("11","[Nghiệm 2] S = √[p(p-a)(p-b)(p-c)]"),
                    ("23,24,25","[Nghiệm 2] Tính các góc"),
                ]
        return kq, chuoi, nghiem2, chuoi2
    except Exception as e:
        return {"loi": f"Dữ liệu không hợp lệ: {e}"}, [], None, []

# ============================================================
# ĐƠN VỊ
# ============================================================
DON_VI_CANH_OPTS = ["đơn vị","cm","m","mm","inch"]
DON_VI_GOC_OPTS  = ["độ (°)","radian"]

# ============================================================
# MÀU SẮC & FONT
# ============================================================
MAU_NEN          = "#f0f4f8"
MAU_PANEL        = "#0000ff"
MAU_PANEL_NHAT   = "#e8edf2"
MAU_VIEN         = "#c8d0da"
MAU_TIEU_DE      = "#1557b0"
MAU_CHU          = "#1a1a2e"
MAU_CHU_MO       = "#6b7280"
MAU_NUT_TINH     = "#1a73e8"
MAU_NUT_XOA      = "#e53935"
MAU_NUT_MANG     = "#2e7d32"
MAU_NUT_VE       = "#7c3aed"
MAU_NUT_NGHIEM2  = "#d97706"
MAU_ENTRY_BG     = "#ffffff"
MAU_ENTRY_FG     = "#1a1a2e"
MAU_ENTRY_DIS    = "#f3f7fb"
MAU_ENTRY_DIS_FG = "#374151"
MAU_BORDER       = "#dde3ea"
MAU_HIGHLIGHT    = "#e3f0ff"
MAU_THANH_TRANG  = "#eef3fa"
MAU_NGHIEM2      = "#fff7ed"
MAU_NGHIEM2_VIEN = "#f59e0b"

FONT_TIEU_DE = ("Segoe UI",16,"bold")
FONT_MUC     = ("Segoe UI",11,"bold")
FONT_THUONG  = ("Segoe UI",10)

TEN_HIEN_THI = {
    "canh_a":"Cạnh a","canh_b":"Cạnh b","canh_c":"Cạnh c",
    "goc_A":"Góc A","goc_B":"Góc B","goc_C":"Góc C",
    "dien_tich":"Diện tích S","chu_vi":"Chu vi P",
    "ban_kinh_p":"Nửa chu vi p",
    "duong_cao_hA":"Đường cao h_a","duong_cao_hB":"Đường cao h_b","duong_cao_hC":"Đường cao h_c",
    "ban_kinh_ngoai_tiep_R":"Bán kính ngoại tiếp R","ban_kinh_noi_tiep_r":"Bán kính nội tiếp r",
    "trung_tuyen_mA":"Trung tuyến m_a","trung_tuyen_mB":"Trung tuyến m_b","trung_tuyen_mC":"Trung tuyến m_c",
    "phan_giac_lA":"Phân giác l_a","phan_giac_lB":"Phân giác l_b","phan_giac_lC":"Phân giác l_c",
    "phan_loai":"Phân loại",
}
DON_VI_NODE = {
    "goc_A":"","goc_B":"","goc_C":"",  # unit suffix added dynamically
    "dien_tich":" đvdt","chu_vi":" đv","ban_kinh_p":" đv",
    "canh_a":" đv","canh_b":" đv","canh_c":" đv",
    "duong_cao_hA":" đv","duong_cao_hB":" đv","duong_cao_hC":" đv",
    "ban_kinh_ngoai_tiep_R":" đv","ban_kinh_noi_tiep_r":" đv",
    "trung_tuyen_mA":" đv","trung_tuyen_mB":" đv","trung_tuyen_mC":" đv",
    "phan_giac_lA":" đv","phan_giac_lB":" đv","phan_giac_lC":" đv",
}


# ============================================================
# CỬA SỔ VẼ TAM GIÁC
# ============================================================
class CuaSoVeTamGiac:
    def __init__(self, parent, kq):
        self.kq = kq
        self.win = tk.Toplevel(parent)
        self.win.title("Vẽ tam giác tỉ lệ thực")
        self.win.configure(bg=MAU_NEN)
        self.win.geometry("820x650")
        self._show_options = {"cao":tk.BooleanVar(value=True),
                              "trung":tk.BooleanVar(value=True),
                              "ngoai":tk.BooleanVar(value=True),
                              "noi":tk.BooleanVar(value=True)}
        self._build()

    def _build(self):
        # Toolbar
        tb = tk.Frame(self.win, bg=MAU_PANEL, pady=6)
        tb.pack(fill="x")
        tk.Label(tb,text="VẼ TAM GIÁC TỈ LỆ THỰC",font=FONT_MUC,bg=MAU_PANEL,fg=MAU_TIEU_DE).pack(side="left",padx=14)
        opts = [("Đường cao","cao"),("Trung tuyến","trung"),("Vòng ngoại","ngoai"),("Vòng nội","noi")]
        for lbl,key in opts:
            tk.Checkbutton(tb,text=lbl,variable=self._show_options[key],
                           command=self._draw,bg=MAU_PANEL,fg=MAU_CHU,
                           activebackground=MAU_PANEL,font=FONT_THUONG).pack(side="left",padx=6)
        # Canvas
        self.canvas = tk.Canvas(self.win, bg="#f8fafc", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=8, pady=8)
        self.canvas.bind("<Configure>", lambda e: self._draw())

    def _draw(self):
        kq = self.kq
        if not kq or "loi" in kq: return
        c = self.canvas; c.delete("all")
        W = c.winfo_width(); H = c.winfo_height()
        if W < 10 or H < 10: return

        a = kq["canh_a"]; b = kq["canh_b"]; cc = kq["canh_c"]
        A = _m.radians(kq["goc_A"]); B = _m.radians(kq["goc_B"]); C = _m.radians(kq["goc_C"])
        # Đặt B tại gốc, C tại (a, 0)
        Bx,By = 0,0; Cx,Cy = a,0
        Ax = cc*_m.cos(B); Ay = cc*_m.sin(B)

        # Scale & center
        all_x=[Bx,Cx,Ax]; all_y=[By,Cy,Ay]
        minx,maxx = min(all_x),max(all_x)
        miny,maxy = min(all_y),max(all_y)
        pad=60
        sx = (W-2*pad)/(maxx-minx) if maxx>minx else 1
        sy = (H-2*pad)/(maxy-miny) if maxy>miny else 1
        sc = min(sx,sy)
        ox = pad - minx*sc + (W-2*pad - (maxx-minx)*sc)/2
        oy = H - pad + miny*sc - (H-2*pad - (maxy-miny)*sc)/2

        def tx(x): return ox + x*sc
        def ty(y): return oy - y*sc

        # Draw circles
        S = kq["dien_tich"]; p = kq["ban_kinh_p"]
        R = kq.get("ban_kinh_ngoai_tiep_R",0); r = kq.get("ban_kinh_noi_tiep_r",0)

        # Circumcenter (ngoại tâm)
        if self._show_options["ngoai"].get() and R>0:
            # circumcenter coordinates
            D = 2*(Ax*(By-Cy)+Bx*(Cy-Ay)+Cx*(Ay-By))
            if abs(D)>1e-12:
                Ox = ((Ax**2+Ay**2)*(By-Cy)+(Bx**2+By**2)*(Cy-Ay)+(Cx**2+Cy**2)*(Ay-By))/D
                Oy = ((Ax**2+Ay**2)*(Cx-Bx)+(Bx**2+By**2)*(Ax-Cx)+(Cx**2+Cy**2)*(Bx-Ax))/D
                Rsc = R*sc
                c.create_oval(tx(Ox)-Rsc,ty(Oy)-Rsc,tx(Ox)+Rsc,ty(Oy)+Rsc,
                              outline="#1d4ed8",width=1.5,dash=(6,4))
                c.create_oval(tx(Ox)-4,ty(Oy)-4,tx(Ox)+4,ty(Oy)+4,fill="#1d4ed8",outline="")
                c.create_text(tx(Ox)+6,ty(Oy)-8,text="O",fill="#1d4ed8",font=("Segoe UI",9,"bold"))

        # Incircle (nội tiếp)
        if self._show_options["noi"].get() and r>0:
            Ix = (a*Ax + b*Bx + cc*Cx)/(a+b+cc)
            Iy = (a*Ay + b*By + cc*Cy)/(a+b+cc)
            rsc = r*sc
            c.create_oval(tx(Ix)-rsc,ty(Iy)-rsc,tx(Ix)+rsc,ty(Iy)+rsc,
                          outline="#c2410c",width=1.5,dash=(6,4))
            c.create_oval(tx(Ix)-4,ty(Iy)-4,tx(Ix)+4,ty(Iy)+4,fill="#c2410c",outline="")
            c.create_text(tx(Ix)+6,ty(Iy)-8,text="I",fill="#c2410c",font=("Segoe UI",9,"bold"))

        # Altitudes
        if self._show_options["cao"].get():
            for (Px,Py),(Q1x,Q1y),(Q2x,Q2y),col in [
                ((Ax,Ay),(Bx,By),(Cx,Cy),"#16a34a"),
                ((Bx,By),(Ax,Ay),(Cx,Cy),"#16a34a"),
                ((Cx,Cy),(Ax,Ay),(Bx,By),"#16a34a"),
            ]:
                dx=Q2x-Q1x; dy=Q2y-Q1y; L=dx**2+dy**2
                if L<1e-12: continue
                t=((Px-Q1x)*dx+(Py-Q1y)*dy)/L
                Fx=Q1x+t*dx; Fy=Q1y+t*dy
                c.create_line(tx(Px),ty(Py),tx(Fx),ty(Fy),fill=col,width=1.2,dash=(4,3))

        # Medians
        if self._show_options["trung"].get():
            mids = [((Bx+Cx)/2,(By+Cy)/2),((Ax+Cx)/2,(Ay+Cy)/2),((Ax+Bx)/2,(Ay+By)/2)]
            verts = [(Ax,Ay),(Bx,By),(Cx,Cy)]
            for i in range(3):
                mx,my = mids[i]; vx,vy = verts[i]
                c.create_line(tx(vx),ty(vy),tx(mx),ty(my),fill="#7c3aed",width=1.2,dash=(4,3))
                c.create_oval(tx(mx)-3,ty(my)-3,tx(mx)+3,ty(my)+3,fill="#7c3aed",outline="")

        # Triangle sides
        pts_sc = [(tx(Ax),ty(Ay)),(tx(Bx),ty(By)),(tx(Cx),ty(Cy))]
        c.create_polygon(pts_sc,outline="#1d4ed8",fill="",width=2.5)

        # Angle arcs & labels
        def draw_angle_arc(vx,vy,p1x,p1y,p2x,p2y,lbl,ang_val):
            r_arc=22
            a1=_m.atan2(ty(p1y)-ty(vy),tx(p1x)-tx(vx)); a2=_m.atan2(ty(p2y)-ty(vy),tx(p2x)-tx(vx))
            a1d=_m.degrees(a1); a2d=_m.degrees(a2)
            start=min(a1d,a2d); extent=abs(a2d-a1d)
            if extent>180: start=max(a1d,a2d); extent=360-extent
            c.create_arc(tx(vx)-r_arc,ty(vy)-r_arc,tx(vx)+r_arc,ty(vy)+r_arc,
                         start=start,extent=extent,outline="#b45309",style="arc",width=1.5)
            mid_a=_m.radians(start+extent/2)
            lx=tx(vx)+40*_m.cos(mid_a); ly=ty(vy)+40*_m.sin(mid_a)
            c.create_text(lx,ly,text=f"{lbl}\n{ang_val:.1f}°",fill="#b45309",
                          font=("Segoe UI",8,"bold"),justify="center")

        draw_angle_arc(Ax,Ay,Bx,By,Cx,Cy,"A",kq["goc_A"])
        draw_angle_arc(Bx,By,Ax,Ay,Cx,Cy,"B",kq["goc_B"])
        draw_angle_arc(Cx,Cy,Ax,Ay,Bx,By,"C",kq["goc_C"])

        # Vertex circles & labels
        for (vx,vy),name,col in [(Ax,Ay,"A","#f87171"),(Bx,By,"B","#f87171"),(Cx,Cy,"C","#f87171")]:
            c.create_oval(tx(vx)-5,ty(vy)-5,tx(vx)+5,ty(vy)+5,fill=col,outline="white",width=1.5)
        c.create_text(tx(Ax),ty(Ay)-18,text="A",fill="#1e293b",font=("Segoe UI",11,"bold"))
        c.create_text(tx(Bx)-18,ty(By),text="B",fill="#1e293b",font=("Segoe UI",11,"bold"))
        c.create_text(tx(Cx)+18,ty(Cy),text="C",fill="#1e293b",font=("Segoe UI",11,"bold"))

        # Side labels
        def mid_label(x1,y1,x2,y2,txt,off=16):
            mx,my=(x1+x2)/2,(y1+y2)/2
            dx,dy=y2-y1,x1-x2; L=_m.sqrt(dx**2+dy**2)+1e-9
            c.create_text(mx+dx/L*off,my+dy/L*off,text=txt,fill="#475569",font=("Segoe UI",9))
        mid_label(tx(Bx),ty(By),tx(Cx),ty(Cy),f"a={a:.3f}")
        mid_label(tx(Ax),ty(Ay),tx(Cx),ty(Cy),f"b={b:.3f}")
        mid_label(tx(Ax),ty(Ay),tx(Bx),ty(By),f"c={cc:.3f}")

        # Info box
        pl = kq.get("phan_loai","")
        S_val = kq.get("dien_tich","?")
        c.create_rectangle(8,8,250,56,fill="#f1f5f9",outline="#cbd5e1",width=1)
        c.create_text(14,14,anchor="nw",text=f"Loại: {pl}",fill="#475569",font=("Segoe UI",9))
        c.create_text(14,30,anchor="nw",text=f"S={S_val:.4f}  R={kq.get('ban_kinh_ngoai_tiep_R',0):.4f}  r={kq.get('ban_kinh_noi_tiep_r',0):.4f}",
                      fill="#475569",font=("Segoe UI",9))

        # Legend
        legend = [("─── ","#1d4ed8","Cạnh tam giác"),
                  ("- - ","#16a34a","Đường cao"),
                  ("- - ","#7c3aed","Trung tuyến"),
                  ("○","#1d4ed8","Vòng ngoại tiếp"),
                  ("○","#c2410c","Vòng nội tiếp")]
        lx0=W-160; ly0=10
        c.create_rectangle(lx0-4,ly0-4,W-4,ly0+len(legend)*18+4,fill="#f1f5f9",outline="#cbd5e1")
        for i,(sym,col,txt) in enumerate(legend):
            c.create_text(lx0+2,ly0+i*18,anchor="nw",text=f"{sym} {txt}",fill=col,font=("Segoe UI",8))


# ============================================================
# CỬA SỔ MẠNG NGỮ NGHĨA
# ============================================================
class CuaSoMangNguNghia:
    CB="#f0f4f8"; CP="#ffffff"; CNI="#1a73e8"; CNG="#f59e0b"; CNS="#16a34a"
    CNA="#7c3aed"; CNM="#0891b2"; CE="#94a3b8"; CE_USED="#ef4444"
    CT="#1e293b"; CTT="#1557b0"; CAC="#d97706"; CF="#1e293b"
    CMY="#dbeafe"; CMH="#dbeafe"; CMO="#64748b"

    def __init__(self, parent, ket_qua=None, chuoi_ct=None, ket_qua2=None, chuoi_ct2=None):
        self.win = tk.Toplevel(parent)
        self.win.title("Mạng ngữ nghĩa — Tam giác")
        self.win.configure(bg=self.CB)
        self.win.state("zoomed")
        try: self.win.attributes("-zoomed",True)
        except: pass
        self.ket_qua  = ket_qua or {}
        self.chuoi_ct = chuoi_ct or []
        self.ket_qua2 = ket_qua2
        self.chuoi_ct2 = chuoi_ct2 or []
        m = MANG_NGU_NGHIA_TAM_GIAC
        self.nodes   = m["cac_node"]
        self.rb_list = m["rang_buoc"]
        self.ma_tran = m["ma_tran"]
        self.ct_da_dung = set()
        for nums_str,_ in self.chuoi_ct:
            for n in str(nums_str).split(","):
                n=n.strip()
                if n.isdigit(): self.ct_da_dung.add(n)
        self._build()

    def _build(self):
        ft=tk.Frame(self.win,bg=self.CP,pady=12); ft.pack(fill="x")
        tk.Label(ft,text="MẠNG NGỮ NGHĨA RÀNG BUỘC — TAM GIÁC",
                 font=("Segoe UI",17,"bold"),bg=self.CP,fg=self.CTT).pack()
        tk.Label(ft,text="60 công thức toán học (không trùng lặp)",
                 font=("Segoe UI",10),bg=self.CP,fg=self.CMO).pack()
        nb=ttk.Notebook(self.win); nb.pack(fill="both",expand=True,padx=10,pady=6)
        st=ttk.Style()
        st.configure("TNotebook",background=self.CB)
        st.configure("TNotebook.Tab",background="#e2e8f0",foreground=self.CT,
                     padding=[16,7],font=("Segoe UI",10,"bold"))
        st.map("TNotebook.Tab",background=[("selected",self.CP)],foreground=[("selected",self.CTT)])
        f1=tk.Frame(nb,bg=self.CB); nb.add(f1,text="  Đồ thị mạng ngữ nghĩa  "); self._tab_do_thi(f1)
        f2=tk.Frame(nb,bg=self.CB); nb.add(f2,text="  Ma trận ràng buộc  ");      self._tab_ma_tran(f2)
        f3=tk.Frame(nb,bg=self.CB); nb.add(f3,text="  Danh sách công thức  ");    self._tab_cong_thuc(f3)
        f4=tk.Frame(nb,bg=self.CB); nb.add(f4,text="  Chuỗi công thức đã dùng  ");self._tab_chuoi_cong_thuc(f4)
        if self.ket_qua2 and "loi" not in self.ket_qua2:
            f5=tk.Frame(nb,bg=self.CB); nb.add(f5,text="  ⭐ Nghiệm 2 (SSA)  "); self._tab_nghiem2(f5)
        tk.Button(self.win,text="×  ĐÓNG",font=("Segoe UI",10,"bold"),
                  bg="#e53935",fg="white",relief="flat",padx=20,pady=6,
                  cursor="hand2",command=self.win.destroy).pack(pady=8)

    def _tab_do_thi(self,frame):
        # --- CÁC BIẾN LƯU TRẠNG THÁI CHECKBOX CHO TỪNG NHÓM ---
        self.loc_canh = tk.BooleanVar(value=True)
        self.loc_goc = tk.BooleanVar(value=True)
        self.loc_dt_cv = tk.BooleanVar(value=True)
        self.loc_cao_bk = tk.BooleanVar(value=True)
        self.loc_tt_pg = tk.BooleanVar(value=True)

        fl=tk.Frame(frame,bg=self.CP,pady=8,padx=14); fl.pack(fill="x")
        
        # --- TẠO HÀNG CHECKBOX LỌC ---
        f_loc = tk.Frame(fl, bg=self.CP)
        f_loc.pack(side="top", fill="x", pady=(0, 5))
        tk.Label(f_loc, text="Hiển thị liên kết của:", font=("Segoe UI", 9, "bold"), bg=self.CP).pack(side="left", padx=(0, 10))
        
        opts = [
            ("Cạnh", self.loc_canh, self.CNI),
            ("Góc", self.loc_goc, self.CNG),
            ("Diện tích/Chu vi", self.loc_dt_cv, self.CNS),
            ("Đường cao/Bán kính", self.loc_cao_bk, self.CNA),
            ("Trung/Phân giác", self.loc_tt_pg, self.CNM)
        ]
        for text, var, color in opts:
            tk.Checkbutton(f_loc, text=text, variable=var, fg=color, bg=self.CP, 
                           activebackground=self.CP, selectcolor=self.CP, font=("Segoe UI", 9, "bold"),
                           command=lambda: self._render_graph(self.canvas.winfo_width(), self.canvas.winfo_height())).pack(side="left", padx=5)

        # --- HÀNG CHÚ THÍCH ---
        f_chu_thich = tk.Frame(fl, bg=self.CP)
        f_chu_thich.pack(side="top", fill="x")
        legs=[("\u25cf",self.CNI,"Cạnh"),("\u25cf",self.CNG,"Góc"),
              ("\u25cf",self.CNS,"Diện tích/Chu vi"),("\u25cf",self.CNA,"Đường cao/Bán kính"),
              ("\u25cf",self.CNM,"Trung tuyến/Phân giác"),("—",self.CE_USED,"Liên kết đã dùng")]
        for s,cl,l in legs:
            f=tk.Frame(f_chu_thich,bg=self.CP); f.pack(side="left",padx=10)
            tk.Label(f,text=s,fg=cl,bg=self.CP,font=("Segoe UI",15)).pack(side="left")
            tk.Label(f,text=l,fg=self.CT,bg=self.CP,font=("Segoe UI",9)).pack(side="left",padx=(2,0))

        self.canvas=tk.Canvas(frame,bg=self.CB,highlightthickness=0)
        sbx=ttk.Scrollbar(frame,orient="horizontal",command=self.canvas.xview)
        sby=ttk.Scrollbar(frame,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=sbx.set,yscrollcommand=sby.set)
        sbx.pack(side="bottom",fill="x"); sby.pack(side="right",fill="y")
        self.canvas.pack(fill="both",expand=True)
        self.canvas.bind("<Configure>",lambda e:self._render_graph(e.width,e.height))

    def _mau_node(self,nd):
        if nd.startswith("canh_"):  return self.CNI
        elif nd.startswith("goc_"): return self.CNG
        elif nd in ("dien_tich","chu_vi","ban_kinh_p"): return self.CNS
        elif nd in ("duong_cao_hA","duong_cao_hB","duong_cao_hC",
                    "ban_kinh_ngoai_tiep_R","ban_kinh_noi_tiep_r"): return self.CNA
        else: return self.CNM

    def _kiem_tra_hien_thi_node(self, nd):
        # Kiểm tra xem node hiện tại có thuộc nhóm đang được tick hay không
        if nd.startswith("canh_"): return self.loc_canh.get()
        elif nd.startswith("goc_"): return self.loc_goc.get()
        elif nd in ("dien_tich","chu_vi","ban_kinh_p"): return self.loc_dt_cv.get()
        elif nd in ("duong_cao_hA","duong_cao_hB","duong_cao_hC",
                    "ban_kinh_ngoai_tiep_R","ban_kinh_noi_tiep_r"): return self.loc_cao_bk.get()
        else: return self.loc_tt_pg.get()

    def _render_graph(self,W,H):
        self.canvas.delete("all")
        nodes=self.nodes; n=len(nodes)
        if n==0: return
        cx,cy=W/2,H/2
        rx,ry=min(W*0.40,400),min(H*0.38,290)
        pos={}
        for i,nd in enumerate(nodes):
            ang=2*_m.pi*i/n-_m.pi/2
            pos[nd]=(cx+rx*_m.cos(ang),cy+ry*_m.sin(ang))
            
        has_result=bool(self.ket_qua and "loi" not in self.ket_qua)
        used_edges=set()
        if has_result:
            for num,rel in self.ma_tran.items():
                if num in self.ct_da_dung and len(rel)>=2:
                    out_nd=rel[0]
                    for inp_nd in rel[1:]:
                        if out_nd in pos and inp_nd in pos:
                            used_edges.add(tuple(sorted([out_nd,inp_nd])))
                            
        drawn=set()
        for num,rel in self.ma_tran.items():
            if len(rel)<2: continue
            out_nd=rel[0]
            for inp_nd in rel[1:]:
                if out_nd not in pos or inp_nd not in pos: continue
                edge=tuple(sorted([out_nd,inp_nd]))
                if edge in drawn: continue
                
                # --- LOGIC LỌC LIÊN KẾT MỚI ---
                # Chỉ vẽ liên kết nếu ít nhất 1 trong 2 đầu của nó thuộc nhóm đang được tick
                hien_thi = self._kiem_tra_hien_thi_node(out_nd) or self._kiem_tra_hien_thi_node(inp_nd)
                if not hien_thi:
                    continue
                # ------------------------------

                drawn.add(edge)
                x1,y1=pos[out_nd]; x2,y2=pos[inp_nd]
                
                if has_result and edge in used_edges:
                    self.canvas.create_line(x1,y1,x2,y2,fill=self.CE_USED,width=2.5)
                else:
                    self.canvas.create_line(x1,y1,x2,y2,fill=self.CE,width=1,dash=(3,4))
                    
        r=38
        for nd in nodes:
            x,y=pos[nd]; col=self._mau_node(nd)
            has_val=nd in self.ket_qua and self.ket_qua[nd] is not None
            ow=3 if has_val else 1.5; oc="#1e293b" if has_val else "#94a3b8"
            self.canvas.create_oval(x-r+2,y-r+2,x+r+2,y+r+2,fill="#c8d0da",outline="")
            self.canvas.create_oval(x-r,y-r,x+r,y+r,fill=col,outline=oc,width=ow)
            short=TEN_HIEN_THI.get(nd,nd)
            short=short.replace("Bán kính ngoại tiếp","R\nngoại").replace("Bán kính nội tiếp","r\nnội")
            short=short.replace("Đường cao ","h").replace("Trung tuyến ","m")
            short=short.replace("Phân giác ","l").replace("Nửa chu vi","p")
            val=self.ket_qua.get(nd)
            if val is not None and isinstance(val,float): lbl=f"{short}\n{val:.3f}"
            elif val is not None: lbl=f"{short}\n{val}"
            else: lbl=short
            self.canvas.create_text(x,y,text=lbl,fill="white",
                                    font=("Segoe UI",7,"bold"),justify="center",width=r*2-8)
                                    
        self.canvas.create_oval(cx-62,cy-26,cx+62,cy+26,fill="#1557b0",outline="#0c3d80",width=2)
        self.canvas.create_text(cx,cy,text="Tam giác",fill="white",font=("Segoe UI",11,"bold"))
        self.canvas.configure(scrollregion=(0,0,W,H))

    def _tab_ma_tran(self,frame):
        nodes=self.nodes
        has_result=bool(self.ket_qua and "loi" not in self.ket_qua)
        ct_items=[]
        for rb in self.rb_list:
            parts=rb.strip().split('.')
            if parts and parts[0].strip().isdigit():
                ct_items.append((parts[0].strip(),rb))
        fc=tk.Frame(frame,bg="#e8edf2",pady=6,padx=12); fc.pack(fill="x",side="bottom")
        if has_result:
            tk.Label(fc,text="  [✓] = Công thức liên quan node này    [★] = Công thức đã dùng    [ ] = Không liên quan",
                     bg="#e8edf2",fg=self.CMO,font=("Segoe UI",9)).pack(anchor="w")
        else:
            tk.Label(fc,text="  Chưa có kết quả — Nhập số liệu và bấm TÍNH TOÁN để xem ma trận tích cực.",
                     bg="#e8edf2",fg="#e53935",font=("Segoe UI",9,"bold")).pack(anchor="w")
        outer=tk.Frame(frame,bg=self.CB); outer.pack(fill="both",expand=True)
        cmt=tk.Canvas(outer,bg=self.CB,highlightthickness=0)
        sbx=ttk.Scrollbar(outer,orient="horizontal",command=cmt.xview)
        sby=ttk.Scrollbar(outer,orient="vertical",command=cmt.yview)
        cmt.configure(xscrollcommand=sbx.set,yscrollcommand=sby.set)
        sbx.pack(side="bottom",fill="x"); sby.pack(side="right",fill="y")
        cmt.pack(fill="both",expand=True)
        fi=tk.Frame(cmt,bg=self.CB); cmt.create_window((0,0),window=fi,anchor="nw")
        fi.bind("<Configure>",lambda e:cmt.configure(scrollregion=cmt.bbox("all")))
        tk.Label(fi,text="Công thức / Node",bg=self.CMH,fg=self.CT,
                 font=("Segoe UI",9,"bold"),width=44,relief="flat",pady=6).grid(row=0,column=0,sticky="nsew",padx=1,pady=1)
        for j,nd in enumerate(nodes):
            ten=TEN_HIEN_THI.get(nd,nd)
            ten=ten.replace("Bán kính ngoại tiếp","R\nngoại").replace("Bán kính nội tiếp","r\nnội")
            ten=ten.replace("Đường cao ","h").replace("Trung tuyến ","m")
            ten=ten.replace("Phân giác ","l").replace("Nửa chu vi","p")
            tk.Label(fi,text=ten,bg=self.CMH,fg=self.CT,font=("Segoe UI",8,"bold"),
                     width=10,relief="flat",pady=4,wraplength=72,justify="center").grid(row=0,column=j+1,sticky="nsew",padx=1,pady=1)
        for i,(num,ct_text) in enumerate(ct_items):
            bg_row="#f8fafc" if i%2==0 else "#ffffff"
            related_nodes=self.ma_tran.get(num,[])
            is_used=num in self.ct_da_dung and has_result
            display_text=ct_text[:60]+"..." if len(ct_text)>60 else ct_text
            bg_ct="#fef3c7" if is_used else bg_row
            tk.Label(fi,text=display_text,bg=bg_ct,fg=self.CF,font=("Consolas",8),
                     anchor="w",padx=6,pady=3,width=52,relief="flat").grid(row=i+1,column=0,sticky="nsew",padx=1,pady=1)
            for j,nd in enumerate(nodes):
                if not has_result:
                    tk.Label(fi,text=" ",bg=bg_row,fg="#adb5bd",font=("Segoe UI",9),width=6,relief="flat").grid(
                        row=i+1,column=j+1,sticky="nsew",padx=1,pady=1)
                else:
                    if nd in related_nodes:
                        bg_c,txt,fg_c=("#fef08a","★","#b45309") if is_used else ("#dbeafe","✓","#1d4ed8")
                    else:
                        bg_c,txt,fg_c=bg_row," ","#cbd5e1"
                    tk.Label(fi,text=txt,bg=bg_c,fg=fg_c,font=("Segoe UI",9,"bold"),
                             width=6,relief="flat").grid(row=i+1,column=j+1,sticky="nsew",padx=1,pady=1)

    def _tab_cong_thuc(self,frame):
        txt=tk.Text(frame,font=("Consolas",10),bg=self.CP,fg=self.CF,
                    relief="flat",bd=0,padx=20,pady=16,state="disabled",wrap="word")
        sb=ttk.Scrollbar(frame,command=txt.yview)
        txt.configure(yscrollcommand=sb.set)
        sb.pack(side="right",fill="y"); txt.pack(fill="both",expand=True)
        txt.configure(state="normal")
        sections=[
            ("I. CƠ BẢN","1-7"),("II. DIỆN TÍCH","8-16"),("III. ĐỊNH LÝ SIN","17-19"),
            ("IV. ĐỊNH LÝ COS","20-25"),("V. TỪ ĐL SIN","26-29"),("VI. ĐƯỜNG CAO","30-38"),
            ("VII. BÁN KÍNH","39-44"),("VIII. DT NÂNG CAO","45"),("IX. TRUNG TUYẾN (GỘP)","46-48"),
            ("X. PHÂN GIÁC","49-51"),("XI. GÓC TỪ BK NỘI (MỚI)","52-54"),
            ("XII. HÌNH CHIẾU","55-57"),("XIII. ĐẶC BIỆT","58-60"),
        ]
        txt.tag_configure("head",font=("Segoe UI",11,"bold"),foreground=self.CTT)
        txt.tag_configure("ct",foreground=self.CF)
        sec_map={}
        for rb in self.rb_list:
            parts=rb.strip().split('.'); num=parts[0].strip()
            if num.isdigit(): sec_map[num]=rb
        cur_sec=None
        for num_str,rb in sec_map.items():
            # find section
            for sname,srange in sections:
                lo,hi=srange.split("-") if "-" in srange else (srange,srange)
                if int(lo)<=int(num_str)<=int(hi):
                    if sname!=cur_sec:
                        cur_sec=sname
                        txt.insert("end",f"\n{'═'*56}\n  {sname}\n{'═'*56}\n","head")
                    break
            txt.insert("end",f"  {rb}\n","ct")
        txt.configure(state="disabled")

    def _tab_chuoi_cong_thuc(self,frame):
        has_result=bool(self.ket_qua and "loi" not in self.ket_qua)
        fh=tk.Frame(frame,bg="#e8f0fe",pady=12,padx=16); fh.pack(fill="x")
        tk.Label(fh,text="🔗  Chuỗi công thức đã sử dụng trong tính toán",
                 font=("Segoe UI",12,"bold"),bg="#e8f0fe",fg=self.CTT).pack(anchor="w")
        canvas=tk.Canvas(frame,bg=self.CB,highlightthickness=0)
        sb=ttk.Scrollbar(frame,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right",fill="y"); canvas.pack(fill="both",expand=True)
        inner=tk.Frame(canvas,bg=self.CB); canvas.create_window((0,0),window=inner,anchor="nw")
        inner.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        if not has_result:
            tk.Label(inner,text="\n\n  ⚠  Chưa có kết quả tính toán.\n\n  Hãy nhập số liệu và bấm TÍNH TOÁN.",
                     font=("Segoe UI",12),bg=self.CB,fg="#e53935",justify="left").pack(pady=40,padx=30)
            return
        step_colors=["#dbeafe","#dcfce7","#fef3c7","#fce7f3","#e0e7ff","#f0fdf4","#fff7ed","#f0f9ff"]
        border_colors=["#93c5fd","#86efac","#fcd34d","#f9a8d4","#a5b4fc","#6ee7b7","#fdba74","#7dd3fc"]
        pad=20
        fbox=tk.Frame(inner,bg=self.CB,padx=pad,pady=10); fbox.pack(fill="x")
        vals_to_show=[(k,v) for k,v in self.ket_qua.items() if k not in ("phan_loai","loi") and v is not None]
        txt_parts=[]
        for k,v in vals_to_show[:8]:
            ten=TEN_HIEN_THI.get(k,k)
            if isinstance(v,float): txt_parts.append(f"{ten}={v:.4f}")
            else: txt_parts.append(f"{ten}={v}")
        input_frame=tk.Frame(fbox,bg="#e8f0fe",relief="solid",bd=1,padx=10,pady=8); input_frame.pack(fill="x",pady=(4,0))
        tk.Label(input_frame,text="  •  ".join(txt_parts[:4]),font=("Segoe UI",9),bg="#e8f0fe",fg=self.CT,wraplength=900,justify="left").pack(anchor="w")
        if len(txt_parts)>4:
            tk.Label(input_frame,text="  •  ".join(txt_parts[4:8]),font=("Segoe UI",9),bg="#e8f0fe",fg=self.CT,wraplength=900,justify="left").pack(anchor="w")
        tk.Label(inner,text="▼",font=("Segoe UI",16),bg=self.CB,fg="#94a3b8").pack()
        for i,(nums_str,mo_ta) in enumerate(self.chuoi_ct):
            color=step_colors[i%len(step_colors)]; b_color=border_colors[i%len(border_colors)]
            fstep=tk.Frame(inner,bg=self.CB,padx=pad,pady=4); fstep.pack(fill="x")
            fcard=tk.Frame(fstep,bg=color,relief="solid",bd=1,padx=14,pady=10); fcard.pack(fill="x")
            fbadge=tk.Frame(fcard,bg=b_color,padx=8,pady=4); fbadge.pack(side="left",anchor="n")
            tk.Label(fbadge,text=f"Bước\n{i+1}",font=("Segoe UI",9,"bold"),bg=b_color,fg="white").pack()
            fcontent=tk.Frame(fcard,bg=color); fcontent.pack(side="left",fill="x",expand=True,padx=12)
            nums_display=", ".join([f"CT.{n.strip()}" for n in str(nums_str).split(",")])
            tk.Label(fcontent,text=nums_display,font=("Segoe UI",9,"bold"),bg=color,fg="#1e40af").pack(anchor="w")
            tk.Label(fcontent,text=mo_ta,font=("Segoe UI",10),bg=color,fg=self.CT,wraplength=800,justify="left").pack(anchor="w")
            for n_str in str(nums_str).split(","):
                n=n_str.strip()
                if n.isdigit():
                    idx=int(n)-1
                    if 0<=idx<len(self.rb_list):
                        tk.Label(fcontent,text=f"    ↳ {self.rb_list[idx]}",font=("Consolas",9),bg=color,fg="#374151").pack(anchor="w")
            if i<len(self.chuoi_ct)-1:
                tk.Label(inner,text="▼",font=("Segoe UI",14),bg=self.CB,fg="#94a3b8").pack()
        tk.Label(inner,text="▼",font=("Segoe UI",16),bg=self.CB,fg="#94a3b8").pack()
        fout=tk.Frame(inner,bg=self.CB,padx=pad,pady=6); fout.pack(fill="x")
        fresult=tk.Frame(fout,bg="#f0fdf4",relief="solid",bd=2,padx=14,pady=10); fresult.pack(fill="x")
        tk.Label(fresult,text="✅  KẾT QUẢ",font=("Segoe UI",11,"bold"),bg="#f0fdf4",fg="#15803d").pack(anchor="w")
        pl=self.ket_qua.get("phan_loai","")
        tk.Label(fresult,text=f"Phân loại: {pl}  |  Đã tính {len(vals_to_show)} giá trị",
                 font=("Segoe UI",10),bg="#f0fdf4",fg="#374151").pack(anchor="w")

    def _tab_nghiem2(self,frame):
        fh=tk.Frame(frame,bg="#fff7ed",pady=12,padx=16); fh.pack(fill="x")
        tk.Label(fh,text="⭐  NGHIỆM 2 — Trường hợp SSA có 2 nghiệm",
                 font=("Segoe UI",12,"bold"),bg="#fff7ed",fg="#b45309").pack(anchor="w")
        tk.Label(fh,text="Khi biết 2 cạnh và góc đối một cạnh (SSA), có thể tồn tại 2 tam giác thỏa mãn điều kiện.",
                 font=("Segoe UI",9),bg="#fff7ed",fg="#92400e").pack(anchor="w")
        canvas=tk.Canvas(frame,bg="#fffbf5",highlightthickness=0)
        sb=ttk.Scrollbar(frame,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right",fill="y"); canvas.pack(fill="both",expand=True)
        inner=tk.Frame(canvas,bg="#fffbf5"); canvas.create_window((0,0),window=inner,anchor="nw")
        inner.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        kq=self.ket_qua2
        if not kq or "loi" in kq:
            tk.Label(inner,text="Không có nghiệm 2.",font=("Segoe UI",12),bg="#fffbf5",fg=self.CMO).pack(pady=40)
            return
        groups=[
            ("CẠNH & GÓC",[("Phân loại","phan_loai"),("Cạnh a","canh_a"),("Cạnh b","canh_b"),("Cạnh c","canh_c"),
                            ("Góc A (°)","goc_A"),("Góc B (°)","goc_B"),("Góc C (°)","goc_C")]),
            ("DIỆN TÍCH & CHU VI",[("Diện tích S","dien_tich"),("Chu vi P","chu_vi"),("Nửa chu vi p","ban_kinh_p")]),
            ("ĐƯỜNG CAO",[("h_a","duong_cao_hA"),("h_b","duong_cao_hB"),("h_c","duong_cao_hC")]),
            ("BÁN KÍNH",[("R","ban_kinh_ngoai_tiep_R"),("r","ban_kinh_noi_tiep_r")]),
            ("TRUNG TUYẾN",[("m_a","trung_tuyen_mA"),("m_b","trung_tuyen_mB"),("m_c","trung_tuyen_mC")]),
            ("PHÂN GIÁC",[("l_a","phan_giac_lA"),("l_b","phan_giac_lB"),("l_c","phan_giac_lC")]),
        ]
        for grp_title,fields in groups:
            fg=tk.Frame(inner,bg="#fff7ed",pady=4,padx=14); fg.pack(fill="x",pady=(6,0))
            tk.Label(fg,text=grp_title,font=("Segoe UI",9,"bold"),bg="#fff7ed",fg="#b45309").pack(anchor="w")
            for lbl,key in fields:
                row=tk.Frame(inner,bg="#fffbf5"); row.pack(fill="x",padx=28,pady=2)
                tk.Label(row,text=lbl,font=FONT_THUONG,bg="#fffbf5",fg=MAU_CHU,width=28,anchor="w").pack(side="left")
                val=kq.get(key,"—")
                txt=f"{val:.4f}" if isinstance(val,float) else str(val)
                tk.Label(row,text=txt,font=("Segoe UI",10,"bold"),bg="#fef3c7",fg="#92400e",
                         width=16,anchor="w",padx=6).pack(side="left")


# ============================================================
# ỨNG DỤNG CHÍNH
# ============================================================
class UngDungHinhHoc:
    def __init__(self,root):
        self.root=root
        self.root.title("Tính giá trị Tam giác — Mạng ngữ nghĩa (60 CT, SSA 2 nghiệm, Vẽ hình)")
        self.root.state("zoomed")
        try: self.root.attributes("-zoomed",True)
        except: pass
        self.root.configure(bg=MAU_NEN)
        self.root.minsize(950,620)
        self.entry_vars={}; self.output_vars={}
        self._ket_qua={}; self._chuoi_ct=[]
        self._ket_qua2=None; self._chuoi_ct2=[]
        # Unit settings
        self.var_unit_goc   = tk.StringVar(value="độ (°)")
        self.var_unit_canh  = tk.StringVar(value="đơn vị")
        self._build()

    def _build(self):
        # ── Header ──
        ft=tk.Frame(self.root,bg=MAU_PANEL,pady=10); ft.pack(fill="x")
        tk.Label(ft,text="TÍNH GIÁ TRỊ TAM GIÁC",font=FONT_TIEU_DE,bg=MAU_PANEL,fg=MAU_TIEU_DE).pack()
        tk.Label(ft,text="Mạng ngữ nghĩa ràng buộc — 60 CT | SSA 2 nghiệm | Đa đơn vị | Vẽ hình",
                 font=("Segoe UI",9),bg=MAU_PANEL,fg=MAU_CHU_MO).pack()
        # ── Toolbar ──
        fc=tk.Frame(self.root,bg=MAU_PANEL_NHAT,pady=8); fc.pack(fill="x")
        tk.Label(fc,text="  Tam giác — Nhập bất kỳ tổ hợp thông số bạn có:",
                 font=FONT_MUC,bg=MAU_PANEL_NHAT,fg=MAU_CHU).pack(side="left",padx=(16,10))
        # Unit dropdowns
        uf=tk.Frame(fc,bg=MAU_PANEL_NHAT); uf.pack(side="left",padx=8)
        tk.Label(uf,text="Góc:",font=("Segoe UI",9),bg=MAU_PANEL_NHAT,fg=MAU_CHU_MO).pack(side="left")
        cb_goc=ttk.Combobox(uf,textvariable=self.var_unit_goc,values=DON_VI_GOC_OPTS,
                            state="readonly",width=9,font=("Segoe UI",9))
        cb_goc.pack(side="left",padx=(2,8))
        tk.Label(uf,text="Cạnh:",font=("Segoe UI",9),bg=MAU_PANEL_NHAT,fg=MAU_CHU_MO).pack(side="left")
        cb_canh=ttk.Combobox(uf,textvariable=self.var_unit_canh,values=DON_VI_CANH_OPTS,
                             state="readonly",width=9,font=("Segoe UI",9))
        cb_canh.pack(side="left",padx=(2,0))
        cb_goc.bind("<<ComboboxSelected>>",lambda e:self._update_labels())
        cb_canh.bind("<<ComboboxSelected>>",lambda e:self._update_labels())
        # Buttons
        for txt,col,cmd in [
            ("  TÍNH TOÁN  ",MAU_NUT_TINH,self._tinh),
            ("  XÓA  ",MAU_NUT_XOA,self._xoa),
            ("  VẼ TAM GIÁC  ",MAU_NUT_VE,self._ve_tam_giac),
            ("  MẠNG NGỮ NGHĨA  ",MAU_NUT_MANG,self._xuat_mang),
        ]:
            tk.Button(fc,text=txt,font=("Segoe UI",10,"bold"),bg=col,fg="white",
                      relief="flat",cursor="hand2",padx=10,pady=5,command=cmd).pack(side="right",padx=(0,8))
        # ── Main area ──
        fm=tk.Frame(self.root,bg=MAU_NEN); fm.pack(fill="both",expand=True,padx=14,pady=10)
        fm.columnconfigure(0,weight=1); fm.columnconfigure(1,weight=1); fm.rowconfigure(0,weight=1)
        # Left: Input
        fl=tk.Frame(fm,bg=MAU_PANEL,highlightbackground=MAU_BORDER,highlightthickness=1)
        fl.grid(row=0,column=0,sticky="nsew",padx=(0,7))
        flt=tk.Frame(fl,bg=MAU_HIGHLIGHT,pady=8,padx=14); flt.pack(fill="x")
        tk.Label(flt,text="NHẬP DỮ LIỆU",font=FONT_MUC,bg=MAU_HIGHLIGHT,fg=MAU_TIEU_DE).pack(anchor="w")
        tk.Label(flt,text="Nhập các thông số bạn có (bỏ trống phần còn lại)",
                 font=("Segoe UI",9),bg=MAU_HIGHLIGHT,fg=MAU_CHU_MO).pack(anchor="w")
        canvas_l=tk.Canvas(fl,bg=MAU_PANEL,highlightthickness=0)
        scroll_l=ttk.Scrollbar(fl,orient="vertical",command=canvas_l.yview)
        canvas_l.configure(yscrollcommand=scroll_l.set)
        scroll_l.pack(side="right",fill="y"); canvas_l.pack(side="left",fill="both",expand=True)
        self.frame_nhap=tk.Frame(canvas_l,bg=MAU_PANEL)
        self._ff_id=canvas_l.create_window((0,0),window=self.frame_nhap,anchor="nw")
        self.frame_nhap.bind("<Configure>",lambda e:canvas_l.configure(scrollregion=canvas_l.bbox("all")))
        canvas_l.bind("<Configure>",lambda e:canvas_l.itemconfig(self._ff_id,width=e.width))
        canvas_l.bind_all("<MouseWheel>",lambda e:canvas_l.yview_scroll(int(-1*(e.delta/120)),"units"))
        # Right: Output
        fr=tk.Frame(fm,bg=MAU_PANEL,highlightbackground=MAU_BORDER,highlightthickness=1)
        fr.grid(row=0,column=1,sticky="nsew",padx=(7,0))
        frt=tk.Frame(fr,bg=MAU_HIGHLIGHT,pady=8,padx=14); frt.pack(fill="x")
        tk.Label(frt,text="KẾT QUẢ TÍNH TOÁN",font=FONT_MUC,bg=MAU_HIGHLIGHT,fg=MAU_TIEU_DE).pack(anchor="w")
        tk.Label(frt,text="Tất cả giá trị được tính tự động",
                 font=("Segoe UI",9),bg=MAU_HIGHLIGHT,fg=MAU_CHU_MO).pack(anchor="w")
        canvas_r=tk.Canvas(fr,bg=MAU_PANEL,highlightthickness=0)
        scroll_r=ttk.Scrollbar(fr,orient="vertical",command=canvas_r.yview)
        canvas_r.configure(yscrollcommand=scroll_r.set)
        scroll_r.pack(side="right",fill="y"); canvas_r.pack(side="left",fill="both",expand=True)
        self.frame_ketqua=tk.Frame(canvas_r,bg=MAU_PANEL)
        self._fr_id=canvas_r.create_window((0,0),window=self.frame_ketqua,anchor="nw")
        self.frame_ketqua.bind("<Configure>",lambda e:canvas_r.configure(scrollregion=canvas_r.bbox("all")))
        canvas_r.bind("<Configure>",lambda e:canvas_r.itemconfig(self._fr_id,width=e.width))
        # Status bar
        self.lbl_tt=tk.Label(self.root,text="  Sẵn sàng. Hãy nhập các thông số bạn có (tối thiểu 2–3 thông số).",
                              font=("Segoe UI",9),bg=MAU_THANH_TRANG,fg=MAU_CHU_MO,anchor="w",padx=10,pady=5)
        self.lbl_tt.pack(fill="x",side="bottom")
        self._build_fields()

    def _goc_label(self, base="Góc"):
        u = self.var_unit_goc.get()
        if "rad" in u.lower(): return f"{base} (rad)"
        return f"{base} (°)"

    def _canh_label(self, base):
        u = self.var_unit_canh.get()
        if u != "đơn vị": return f"{base} ({u})"
        return base

    def _update_labels(self):
        self._build_fields()

    def _build_fields(self):
        for w in self.frame_nhap.winfo_children(): w.destroy()
        for w in self.frame_ketqua.winfo_children(): w.destroy()
        self.entry_vars.clear(); self.output_vars.clear()
        self._lbl_entry_refs = {}  # store label widgets for unit update

        u_goc = "rad" if "rad" in self.var_unit_goc.get().lower() else "do"
        u_canh = self.var_unit_canh.get()
        def cu(base, k):
            if k.startswith("goc_"): return self._goc_label(base)
            if u_canh != "đơn vị" and k.startswith(("canh_","duong_","ban_","trung_","phan_g","chu_")): return f"{base} ({u_canh})"
            return base

        groups=[
            ("CÁC CẠNH",[("Cạnh a","canh_a"),("Cạnh b","canh_b"),("Cạnh c","canh_c")]),
            ("GÓC",[("Góc A","goc_A"),("Góc B","goc_B"),("Góc C","goc_C")]),
            ("DIỆN TÍCH & CHU VI",[("Diện tích S","dien_tich"),("Chu vi P","chu_vi")]),
            ("ĐƯỜNG CAO",[("Đường cao h_a","duong_cao_hA"),("Đường cao h_b","duong_cao_hB"),("Đường cao h_c","duong_cao_hC")]),
            ("BÁN KÍNH",[("Bán kính ngoại tiếp R","ban_kinh_ngoai_tiep_R"),("Bán kính nội tiếp r","ban_kinh_noi_tiep_r")]),
            ("TRUNG TUYẾN",[("Trung tuyến m_a","trung_tuyen_mA"),("Trung tuyến m_b","trung_tuyen_mB"),("Trung tuyến m_c","trung_tuyen_mC")]),
            ("PHÂN GIÁC",[("Phân giác l_a","phan_giac_lA"),("Phân giác l_b","phan_giac_lB"),("Phân giác l_c","phan_giac_lC")]),
        ]
        for grp_title,fields in groups:
            fg=tk.Frame(self.frame_nhap,bg=MAU_PANEL); fg.pack(fill="x",padx=14,pady=(8,0))
            tk.Label(fg,text=grp_title,font=("Segoe UI",9,"bold"),bg=MAU_PANEL,fg=MAU_TIEU_DE).pack(anchor="w",pady=(4,2))
            for lbl,key in fields:
                row=tk.Frame(self.frame_nhap,bg=MAU_PANEL); row.pack(fill="x",padx=22,pady=3)
                lbl_text=cu(lbl,key)
                lbl_w=tk.Label(row,text=lbl_text,font=FONT_THUONG,bg=MAU_PANEL,fg=MAU_CHU,width=28,anchor="w")
                lbl_w.pack(side="left")
                var=tk.StringVar(value="")
                e=tk.Entry(row,textvariable=var,font=FONT_THUONG,bg=MAU_ENTRY_BG,
                           fg=MAU_ENTRY_FG,insertbackground=MAU_CHU,relief="solid",bd=1,width=14)
                e.pack(side="left"); e.bind("<Return>",lambda ev:self._tinh())
                self.entry_vars[key]=var

        # Output panel
        result_groups=[
            ("CẠNH & GÓC",[
                ("Phân loại","phan_loai"),
                ("Cạnh a","canh_a"),("Cạnh b","canh_b"),("Cạnh c","canh_c"),
                ("Góc A","goc_A"),("Góc B","goc_B"),("Góc C","goc_C"),
            ]),
            ("DIỆN TÍCH & CHU VI",[
                ("Diện tích S","dien_tich"),("Chu vi P","chu_vi"),("Nửa chu vi p","ban_kinh_p"),
            ]),
            ("ĐƯỜNG CAO",[
                ("Đường cao h_a","duong_cao_hA"),("Đường cao h_b","duong_cao_hB"),("Đường cao h_c","duong_cao_hC"),
            ]),
            ("BÁN KÍNH",[
                ("Bán kính ngoại tiếp R","ban_kinh_ngoai_tiep_R"),("Bán kính nội tiếp r","ban_kinh_noi_tiep_r"),
            ]),
            ("TRUNG TUYẾN",[
                ("Trung tuyến m_a","trung_tuyen_mA"),("Trung tuyến m_b","trung_tuyen_mB"),("Trung tuyến m_c","trung_tuyen_mC"),
            ]),
            ("PHÂN GIÁC",[
                ("Phân giác l_a","phan_giac_lA"),("Phân giác l_b","phan_giac_lB"),("Phân giác l_c","phan_giac_lC"),
            ]),
        ]
        self._lbl_nghiem2 = None
        for grp_title,fields in result_groups:
            fg=tk.Frame(self.frame_ketqua,bg=MAU_PANEL); fg.pack(fill="x",padx=14,pady=(8,0))
            tk.Label(fg,text=grp_title,font=("Segoe UI",9,"bold"),bg=MAU_PANEL,fg=MAU_TIEU_DE).pack(anchor="w",pady=(4,2))
            for lbl,key in fields:
                row=tk.Frame(self.frame_ketqua,bg=MAU_PANEL); row.pack(fill="x",padx=22,pady=3)
                lbl_text=cu(lbl,key)
                tk.Label(row,text=lbl_text,font=FONT_THUONG,bg=MAU_PANEL,fg=MAU_CHU,width=28,anchor="w").pack(side="left")
                var=tk.StringVar(value="—")
                e=tk.Entry(row,textvariable=var,font=FONT_THUONG,
                           bg=MAU_ENTRY_DIS,fg=MAU_ENTRY_DIS_FG,relief="solid",bd=1,width=14,
                           state="readonly",readonlybackground=MAU_ENTRY_DIS)
                e.pack(side="left")
                self.output_vars[key]=var

        # Nghiệm 2 banner (hidden initially)
        self._frame_nghiem2_banner = tk.Frame(self.frame_ketqua,bg=MAU_NGHIEM2,
                                               highlightbackground=MAU_NGHIEM2_VIEN,highlightthickness=2)
        self._lbl_nghiem2 = tk.Label(self._frame_nghiem2_banner,
                                      text="",font=("Segoe UI",9,"bold"),
                                      bg=MAU_NGHIEM2,fg="#92400e",wraplength=280,justify="left")

    def _lay_gv(self):
        gv={}
        unit_goc = "rad" if "rad" in self.var_unit_goc.get().lower() else "do"
        for key,var in self.entry_vars.items():
            txt=var.get().strip()
            if txt:
                try:
                    v=float(txt)
                    # Validate
                    if key.startswith("goc_"):
                        if unit_goc=="do" and not (0 < v < 180):
                            raise ValueError(f"Góc phải trong khoảng (0°, 180°)!")
                        if unit_goc=="rad" and not (0 < v < _m.pi):
                            raise ValueError(f"Góc phải trong khoảng (0, π) radian!")
                    elif v < 0:
                        raise ValueError(f"Giá trị phải không âm!")
                    gv[key]=v
                except ValueError as ex:
                    raise ValueError(f"{TEN_HIEN_THI.get(key,key)}: {ex}")
        return gv, unit_goc

    def _format_val(self, key, val):
        if isinstance(val, float):
            u_goc = "rad" if "rad" in self.var_unit_goc.get().lower() else "do"
            u_canh = self.var_unit_canh.get()
            if key.startswith("goc_"):
                if u_goc == "rad":
                    return f"{_m.radians(val):.6f} rad"
                return f"{val:.4f} °"
            suffix = f" {u_canh}" if u_canh != "đơn vị" else ""
            if key == "dien_tich":
                suffix = f" {u_canh}²" if u_canh != "đơn vị" else ""
            return f"{val:.4f}{suffix}"
        return str(val)

    def _tinh(self):
        for var in self.output_vars.values(): var.set("—")
        if self._lbl_nghiem2:
            self._frame_nghiem2_banner.pack_forget()
        try: gv, unit_goc = self._lay_gv()
        except ValueError as e:
            messagebox.showerror("Lỗi nhập liệu",str(e)); return
        if len(gv)<2:
            messagebox.showwarning("Thiếu dữ liệu",
                "Vui lòng nhập ít nhất 2–3 thông số!\n"
                "Ví dụ: 3 cạnh, 2 cạnh + góc, 1 cạnh + 2 góc, ..."); return
        kq,chuoi,kq2,chuoi2 = giai_tam_giac_tu_du_lieu(gv, unit_goc)
        self._ket_qua=kq; self._chuoi_ct=chuoi; self._ket_qua2=kq2; self._chuoi_ct2=chuoi2
        if "loi" in kq:
            messagebox.showerror("Lỗi tính toán",kq["loi"])
            self.lbl_tt.configure(text=f"  ❌ Lỗi: {kq['loi'][:70]}",fg="#e53935",bg=MAU_THANH_TRANG)
        else:
            for key,var in self.output_vars.items():
                if key in kq and kq[key] is not None:
                    var.set(self._format_val(key,kq[key]))
            pl=kq.get("phan_loai","Tam giác")
            nv=len([k for k in kq if k not in ("phan_loai","loi")])
            nghiem2_txt=""
            if kq2 and "loi" not in kq2:
                nghiem2_txt=" | ⭐ SSA có 2 NGHIỆM"
                self._frame_nghiem2_banner.pack(fill="x",padx=14,pady=8,ipady=8)
                self._lbl_nghiem2.pack(padx=12,pady=6)
                self._lbl_nghiem2.configure(
                    text=f"⭐ SSA — Tồn tại NGHIỆM 2:\n"
                         f"a={kq2.get('canh_a',0):.4f}  b={kq2.get('canh_b',0):.4f}  c={kq2.get('canh_c',0):.4f}\n"
                         f"A={kq2.get('goc_A',0):.2f}°  B={kq2.get('goc_B',0):.2f}°  C={kq2.get('goc_C',0):.2f}°\n"
                         f"→ Xem chi tiết trong 'Mạng ngữ nghĩa → tab Nghiệm 2'")
            self.lbl_tt.configure(
                text=f"  ✅ Thành công!  Loại: {pl}  |  {nv} giá trị  |  {len(chuoi)} bước công thức{nghiem2_txt}",
                fg="#16a34a",bg=MAU_THANH_TRANG)

    def _xoa(self):
        for var in self.entry_vars.values(): var.set("")
        for var in self.output_vars.values(): var.set("—")
        if self._lbl_nghiem2: self._frame_nghiem2_banner.pack_forget()
        self._ket_qua={}; self._chuoi_ct=[]; self._ket_qua2=None; self._chuoi_ct2=[]
        self.lbl_tt.configure(text="  Đã xóa. Hãy nhập lại các thông số mới.",
                              fg=MAU_CHU_MO,bg=MAU_THANH_TRANG)

    def _ve_tam_giac(self):
        if not self._ket_qua or "loi" in self._ket_qua:
            messagebox.showwarning("Chưa có kết quả","Vui lòng TÍNH TOÁN trước khi vẽ!"); return
        CuaSoVeTamGiac(self.root, self._ket_qua)

    def _xuat_mang(self):
        CuaSoMangNguNghia(self.root, self._ket_qua, self._chuoi_ct, self._ket_qua2, self._chuoi_ct2)


# ============================================================
if __name__=="__main__":
    root=tk.Tk()
    st=ttk.Style()
    st.theme_use("clam")
    st.configure("TCombobox",fieldbackground=MAU_ENTRY_BG,background=MAU_ENTRY_BG,
                 foreground=MAU_ENTRY_FG,selectbackground=MAU_NUT_TINH,selectforeground="white")
    st.configure("TScrollbar",background=MAU_PANEL_NHAT,troughcolor=MAU_NEN,arrowcolor=MAU_CHU_MO)
    st.configure("TNotebook.Tab",padding=[14,6])
    app=UngDungHinhHoc(root)
    root.mainloop()