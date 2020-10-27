# 基于在线学习的分布式流量实时分析系统
&nbsp &nbsp 目前，各种类型的流量充满了网络空间，其中包含了正常上网业务，具有 CVE 编号的网络攻击、计算机病毒（邮件病毒、木马、蠕虫、勒索软件）等等。这些流量中既包含未加密的流量，也包含经过加密的流量，如广泛使用的安全传输层(TLS)协议。 如何开发出一个网络安全系统，能够有效抵对TLS加密与非加密的流量数据进行检测、分析与分类，并实时识别出网络上的恶意攻击行为成为现阶段面临的一个挑战。目前在工业界，已经已经有了基于网络端口映射的流量分类识别方法和基于有效载荷分析的流量分类识别方法等，但这些方法面临两个都面临了准确性和可靠性低的问题，且这两种方法是无法在加密流量上使用的，因此探究其他的流量检测方法显得格外重要。同时，CVE、恶意加密流量等网络攻击具有攻击量大、高并发的特点，对于检测系统更是提出了实时化与分布式部署的要求。

&nbsp &nbsp 我们提出将分布式网络系统与深度学习技术、虚拟化技术相结合，同时引入在线学习机制做到实时推断与模型动态更新。该系统具有以下特点：利用CyberFlood产生TLS加密与非加密的、不同种类的业务流量和恶意流量；利用Hive分布式数据库存储原始流量数据；通过Spark和Flink流量分别对流量进行并行批处理和流式处理；使用CNN+LSTM的时空深度学习网络对不同类型的流量进行分类；利用redis缓存加速实时流量的特征读取；利用Docker虚拟化容器对深度学习模型进行部署。该系统同时具有高隔离性、高容错性、高准确性和高实时性特点，可以解决传统安全系统所面临的的挑战。

&nbsp &nbsp目前我们的系统版本为V2.0，可以识别出包含加密与非加密的业务流量、恶意软件流量和网络攻击流量这三种流量类型，并进行动态流量数据的可视化呈现。

