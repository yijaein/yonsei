from Tools.csv_search import Per_dicom, Csv_data

# accno, diagnosis
isangmi_list = [
    ["1510201925", "aki"], ["1511278732", "aki"],
    ["1611224677", "aki"], ["1704042416", "aki"],
    ["1705109833", "aki"], ["1707271727", "aki"],

    ["1406115440", "ckd"], ["1504237440", "ckd"],
    ["1505140095", "ckd"], ["1509297909", "ckd"],
    ["1509313382", "ckd"], ["1510299374", "ckd"],
    ["1512012210", "ckd"], ["1601081840", "ckd"],
    ["1602014843", "ckd"], ["1603112332", "ckd"],
    ["1603374400", "ckd"], ["1604149457", "ckd"],
    ["1605119602", "ckd"], ["1605304657", "ckd"],
    ["1607110868", "ckd"], ["1609106232", "ckd"],
    ["1701014162", "ckd"], ["1701146758", "ckd"],
    ["1704026532", "ckd"], ["1704248494", "ckd"],
    ["1706254531", "ckd"], ["1709068883", "ckd"],
    ["1709143919", "ckd"],

    ["1401143131", "normal"], ["1604307774", "normal"],
    ["1604330063", "normal"], ["1605197062", "normal"],
    ["1608143415", "normal"], ["1609325227", "normal"],
    ["1702001450", "normal"], ["1702125801", "normal"],
    ["1706322448", "normal"], ["1707211552", "normal"],
    ["1707311002", "normal"], ["1708193790", "normal"],
    ["1712006741", "normal"], ["1712068741", "normal"],
    ["1712245042", "normal"], ["1712421090", "normal"]]


# 파일 별 질병명 구성
match_name_diagnosis = dict()
for dicom in Per_dicom():
    Name = dicom['File'][:-4]
    Diagnosis = dicom['Diagnosis'].lower()
    match_name_diagnosis[Name] = Diagnosis


match_name_accno = dict()
#...

# train, val 구별

istrain = 'val' if name in match_name_accno else 'train'




# 파일 복사 디렉토리 구성(정상, 만성, 급성)
diag = match_name_diagnosis[name]

copy_path = os.path.join(save_path, istrain, diag)
if not os.path.exist(copy_path):
    os.makedirs(copy_path)

shutil.copy(file, copy_path)