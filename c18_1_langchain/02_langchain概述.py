"""

langChain是由哈弗大学发起的一个开源框架，用于开发由大语言模型（LLM）驱动的应用程序.
比如：搭建智能体（agent），问答系统（QA），对话机器人，文档搜索系统，企业私有知识库等
为什么需要langChain：
    llm的缺点：
        数据截止到某一个季度
        无法连接互联网
        如何稳定输出
        无法对接外部工具
        如何接入私有数据
        不能调用第三方api
        没法查询数据库
    开发者不仅希望能使用这些模型，还希望能将他们灵活集成到自己的应用中，实现更强大的对话能力，检索增强生成（RAG），工具调用（Tool Calling），多轮推理等功能
    langChain优点：
        1.更简单，更高效，效果更好。对比原生的api调用来说
        2.学习成本更低
        3.现成的链式组装
langChain架构设计：


    架构层     langChain  langGraph

前置知识：
    1.python基础
    2.大语言模型基础
    3.相关环境安装：python或anaconda

基于RAG架构的开发
    背景：
        大模型的知识冻结
        大模型幻觉
    而RAG就可以非常精准的解决这两个问题
    RAG：检索增强生成
基于Agent架构的开发
    充分利用LLM的推理决策能力，通过规划，记忆和工具调用的能力，构造一个能独立思，逐步完成给定目标的智能体
    Agent = LLM + Memory + Tools + Planning + Action
大模型应用开发的4个场景
    1.纯prompt
    2.Agent + Function Calling
    3.RAG
    4.Fine-tuning（精调/微调）
    可以从下面思路思考需要什么场景：
        1.是否需要补充知识 RAG
        2.要对接其它系统   Function Calling
        3.值得尝试微调    用历史数据左Fine-tuning
开发思路：
    1.提示词模板的构建，不仅仅只包含用户输入
    2.模型调用与返回，参数上设置，返回内容的格式化输出
    3.知识库查询，这里会包含文档加载，切割，以及转化为词嵌入向量
    4.其它第三方工具调用，一般包含天气查询，google搜索，一些自定义的接口能力调用
    5.记忆获取，每一个对话都有上下文，在开启对话之前总得获取到之前的上下文吧
langChain核心组件：
    模型I/O：标准化各个大模型的输入和输出，包含输入模板，模型本身和格式化输出
    检索：对应着RAG，检索外部数据，然后在执行生成步骤时将其传递到LLM，步骤包括文档加载，切割，Embedding等
    链：用于将多个模块串联起来组成一个完整的流程，是langChain框架中最重要的模块
        例如：一个chain可能包含一个prompt模板，一个语言模型和一个输出解析器，他们一起工作以处理用户输入，生成响应并处理输出
        常见的chain类型：
            LLMChain：最基础的模型调用链
            SequentialChain：多个链串联执行
            RouterChain：自动分析用户的需求，引导到最适合的链
            RetrievalQA：集合向量数据库进行回答的链
    Agents：对应着智能体，是langChain的高阶能力，它可以自主选择工具并规划执行步骤
        AgentType：定义决策逻辑的工作流模型
        Tool：是一些内置的功能模块，如Api调用，搜索引擎，文本处理，数据查询等工具
            agents通过这些工具来执行特定的功能
        AgentExecutor：用来运行智能体并执行其决策的工具，负责协调智能体的决策和实际的工具执行
    记忆：记忆模块，用于保存对话历史或上下文信息，以便在后续对话中使用
        常见的Memory类型：
            ConversationBufferMemory：保存完整的对话历史
            ConversationSummaryMemory：保存对话内容的精简摘要（适合长对话）
            ConversationSummaryBufferMemory：混合型记忆机制，兼具上面两个类型的特点
            VectorStoreRetrieverMemory：保存对话历史存储在向量数据库中
    回调：允许连接到LLM应用程序的各个阶段，可以监控和分析LangChain的运行情况，比如日志记录，监控，流传输等，以优化性能
"""