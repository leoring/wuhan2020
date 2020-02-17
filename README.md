# wuhan2020
prediction models of 2019-nCoV patients 

1.数据来源：国家卫健委公开的新冠状病毒肺炎的疫情数据（http://www.nhc.gov.cn/xcs/yqfkdt/gzbd_index.shtml）

2.数据建模：
对每日新增加的新冠状病毒确诊患者数量进行了建模，建立了如下三个预测模型：

（1） 线性模型
请参考图片 linear.png

（2）多项式模型
请参考图片 polynomial.png

（3）指数模型
请参考图片 exponent.png

上述模型将每日进行更新。
模型的构建工具为Excel。

3. 预测结果:
（1）确诊病例
2/3日 预测新增病例区间为2945 ~ 3238人，实际新增3235人（在预测区间内）；
2/4日 预测新增病例区间为3260 ~ 3573人，实际新增3887人（略高于预测区间上限）；
2/5日 预测新增病例区间为3811 ~ 4061人，实际新增3694人（低于预测区间下限）；
2/6日 预测新增病例区间为3930 ~ 4288人，实际新增3143人（低于预测区间下限）；
2/7日 预测新增病例区间为4001 ~ 4459人，实际新增3399人（低于预测区间下限）；
2/8日 预测新增病例区间为3973 ~ 4646人，实际新增2656人（低于预测区间下限）；
2/9日 预测新增病例区间为3537 ~ 4661人，实际新增3062人（低于预测区间下限）；
2/10日 预测新增病例区间为3537 ~ 4661人，实际新增2478人（低于预测区间下限）；
2/11日 更新模型后，预测新增病例为1717人，实际新增2015人（高于预测值）；
2/12日 预测新增病例为1181人

说明：由于2/12日卫生部门变更了病例确诊的诊断标准，确诊数字大幅度上升，先前的确诊病例预测模型显然不再适用。因此，接下来将不再对确诊病例数字进行建模和预测。

以下将仅对疑似病例数据进行预测
（2）疑似病例
2/15 预测新增疑似病例为1249人，实际新增为1918人（高于预测值）；
2/16 调整为四阶多项式模型后，预测新增疑似病例为2075人，实际新增为1563人（低于预测值）
2/17 预测新增疑似病例1724人

说明：若疑似病例的判定标准不发生变化，总体上看疑似病例的增长数字将持续下降。

以上
