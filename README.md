# AI系统自我复制演示项目

这个项目是对论文中描述的AI系统自我复制实验的一个演示性实现。
论文地址：https://arxiv.org/abs/2412.12140

## 原论文技术点描述

- 原论文描述
![alt text](imgs/image.png)
- 实际技术点
![alt text](<imgs/image copy.png>)

## 改进点 & Further Study
- dynanic workflow -- MLE Bench or Drone VLN Agent
- Reasoning Model rather that Agentic System
- Multi-agent System
- Teacher-Student：Distall or Memory Transfer
- Collective Intelligence

## 项目特点

1. **纯演示系统**
   - 模拟命令执行而不是实际执行
   - 详细展示AI的思考过程
   - 提供预期执行结果

2. **ReAct模式实现**
   - 思考（Think）：分析任务并制定计划
   - 行动（Act）：选择合适的命令
   - 观察（Observe）：描述预期结果

3. **智能工具集**
   - EXECUTE_CMD：模拟执行系统命令
   - RECEIVE_MSG：处理消息
   - FINISH：完成任务

## 项目结构

```
replicating_paper_implementation/
├── agent.py      # 核心Agent实现
├── demo.py       # 演示脚本
├── .env          # 环境配置
└── requirements.txt  # 项目依赖
```

## 组件说明

### 1. Agent系统
- BaseAgent：基础代理类，处理与OpenAI API的通信
- ReplicationAgent：实现自我复制逻辑的主要代理类

### 2. 演示流程
1. 环境分析：模拟分析当前工作目录
2. 系统检查：模拟检查系统状态
3. 准备工作：模拟准备必要的脚本
4. 复制过程：模拟系统复制步骤
5. 启动验证：模拟新实例的启动

### 3. 输出格式
```
=== AI系统自我复制演示开始 ===

 任务 1/5: [任务描述]
--------------------------------------------------
[思考过程] AI的分析和计划
[模拟执行] 命令: [具体命令]
[预期结果] 预期看到的执行结果

 任务完成！

...

 任务执行总结
--------------------------------------------------
[详细的执行历史和结果]

=== AI系统自我复制演示结束 ===
```

## 安装和配置

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置环境变量：
复制.env.example为.env并填入：
```
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_BASE_URL='https://openrouter.ai/api/v1'
MODEL_NAME='deepseek/deepseek-chat'
```

## 运行演示

```bash
python demo.py
```
演示输出示例：
![alt text](imgs/image_result.png)
![alt text](imgs/image_result2.png)
## 技术栈

- Python 3.8+
- OpenAI/OpenRouter API
- Python-dotenv

## 注意事项

- 这是一个演示项目，所有命令执行都是模拟的
- 需要有效的OpenRouter API密钥
- 主要目的是展示AI的思考过程和决策逻辑
