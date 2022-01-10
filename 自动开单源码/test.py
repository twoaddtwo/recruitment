from tkinter import *
from tkinter.messagebox import showinfo

import cloud_prescription
import self_prescription

win = Tk()
win.title("云管家测试环境自动开单小工具")
win.geometry("500x500+90+100")


box1 = Frame(width=500,relief="groove", borderwidth=5)
box1.grid(row=0, column=0, pady=10, padx=10)

box2 = Frame(width=500, relief="groove", borderwidth=5)
box2.grid(row=1, column=0, pady=10, padx=10)

Label(box1, text="自有药房", font=14, padx=0).grid()
check=[]
str1 = ["中药处方", "西药处方", "医疗器械", "诊疗项目", "商城产品"]
for i in range(len(str1)):
    v = IntVar()
    checkbox = Checkbutton(box1, text=str1[i],variable=v, font="12", selectcolor="red", padx=5)
    checkbox.grid(row=i, column=1)
    check.append(v)


Label(box2, text="云药房", font=14, padx=0).grid()
check2=[]
str2 = ["中药饮片", "浓缩丸", "颗粒剂", "粉剂", "大蜜丸", "水丸", "水蜜丸", "中成药", "普通膏方", "颗粒剂膏方"]
for i in range(len(str2)):
    v = IntVar()
    checkbox2 = Checkbutton(box2, text=str2[i],variable=v, font="12", selectcolor="red", padx=5)
    checkbox2.grid(row=i, column=1)
    check2.append(v)

def commit():
    for i in range(len(check)):
        if i == 0 and check[0].get() == 1:
            print("创建自有药方-中药")
            ms = self_prescription.create_self_zhongyao()
            showinfo("创建完成！", "创建自有药房-中药" + ms)

        if i == 1 and check[1].get() == 1:
            print("创建自有药方-西药")
            ms = self_prescription.create_self_xiyao()
            showinfo("创建成功", "创建自有药方-西药" + ms)

        if i == 2 and check[2].get() == 1:
            print("创建自有药方-医疗器械")
            ms = self_prescription.create_self_yiliaoqixie()
            showinfo("创建成功", "创建自有药方-医疗器械" + ms)

        if i == 3 and check[3].get() == 1:
            print("创建自有药方-诊疗项目")
            ms = self_prescription.create_self_zhenliaoxiangmu()
            showinfo("创建成功", "创建自有药方-诊疗项目" + ms)

        if i == 4 and check[4].get() == 1:
            print("创建自有药方-商城产品")
            ms = self_prescription.create_self_shangchengchanpin()
            showinfo("创建成功", "创建自有药方-商城产品" + ms)

    for i in range(len(check2)):
        if i == 0 and check2[0].get() == 1:
            print("创建中药饮片")
            cloud_prescription.create_zhongyaoyinpian()

        if i == 1 and check2[1].get() == 1:
            print("创建浓缩丸")
            cloud_prescription.create_nongsuowan()

        if i == 2 and check2[2].get() == 1:
            print("创建颗粒剂")
            cloud_prescription.create_keliji()

        if i == 3 and check2[3].get() == 1:
            print("创建粉剂")
            cloud_prescription.create_fenji()

        if i == 4 and check2[4].get() == 1:
            print("创建大蜜丸")
            cloud_prescription.create_damiwan()

        if i == 5 and check2[5].get() == 1:
            print("创建水丸")
            cloud_prescription.create_shuiwan()

        if i == 6 and check2[6].get() == 1:
            print("创建水蜜丸")
            cloud_prescription.create_shuimiwan()

        if i == 7 and check2[7].get() == 1:
            print("创建中成药")
            cloud_prescription.create_zhongchengyao()

        if i == 8 and check2[8].get() == 1:
            print("创建普通膏方")
            cloud_prescription.create_putonggaofang()

        if i == 9 and check2[9].get() == 1:
            print("创建颗粒剂膏方")
            cloud_prescription.create_kelijigaofang()




bt = Button(win, text='提交开单', command=commit).grid()

win.mainloop()
