一、创建Scrapy爬虫爬取数据
	1、通过scrapy.select分析单个页面
	2、爬取前50页的全部二手车信息，包括：品牌、标题、生产年、行驶距离、油耗、自动/手动、标签、价格
	3、通过pipeline保存到csv文件中。
二、Jupyter Notebook 分析预测数据
	1、使用pandas读取数据，并将tag标签数据拆分为one-hot标签
	2、删除标题信息
	3、分析平均价格最高的前十个品牌，按照brand分组，取brand中的price的mean，绘制柱状图
	4、分析销量最多的前十个品牌 按照brand中的数量大小进行排序，绘制柱状图
	5、分析各大品牌车系的占有比例，绘制饼状图
	6、分析某一种品牌车售价分区，以大众为例，取得mean，std，绘制带有概率曲线的柱状图
	7、特征工程：对brand、start_time、distance、volumn、gear进行特征处理，变为one-hot编码
	8、建模，是由GBDT模型对标签进行预测，最后评估MSE、MAE、RMSE、R2.
