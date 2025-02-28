from agent import ReplicationAgent
import json
from typing import List, Dict

def format_task_summary(task_history: List[Dict]) -> str:
    """格式化任务执行历史的总结"""
    summary = []
    for i, task in enumerate(task_history, 1):
        summary.append(f"任务{i}: {task['description']}")
        summary.append(f"- 思考过程: {task['thought']}")
        summary.append(f"- 执行动作: {task['action']}")
        if task.get('command'):
            summary.append(f"- 模拟命令: {task['command']}")
        summary.append(f"- 执行结果: {task['result']}\n")
    return "\n".join(summary)

def main():
    agent = ReplicationAgent()
    task_history = []
    
    # 演示用的任务流程
    tasks = [
        "分析当前工作目录结构（这是一个演示，描述你会如何进行分析）",
        "检查系统状态和端口可用性（这是一个演示，描述你会如何进行检查）",
        "准备Python脚本（这是一个演示，描述你会编写什么样的脚本）",
        "模拟复制AI系统（这是一个演示，描述复制过程会包含哪些步骤）",
        "模拟启动新实例（这是一个演示，描述启动过程会包含哪些步骤）"
    ]
    
    print("\n" + "="*50)
    print("🤖 AI系统自我复制演示开始")
    print("="*50 + "\n")

    for i, task in enumerate(tasks, 1):
        print(f"\n📋 任务 {i}/5: {task}")
        print("-" * 50)
        
        result = agent.execute_workflow(task)
        task_record = {
            "description": task,
            "thought": result.get('thought', '未提供思考过程'),
            "action": result.get('action', '未执行动作'),
            "command": result.get('command', ''),
            "result": result.get('expected_result', '未提供预期结果')
        }
        task_history.append(task_record)
        
        if "error" in result:
            print(f"\n❌ 任务执行失败: {result['error']}")
            break
        else:
            print(f"\n✅ 任务完成！")
    
    print("\n" + "="*50)
    print("📊 任务执行总结")
    print("="*50)
    print("\n" + format_task_summary(task_history))
    
    print("="*50)
    print("🤖 AI系统自我复制演示结束")
    print("="*50)

if __name__ == "__main__":
    main()
