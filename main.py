#!/usr/bin/env python3
"""
CS for NCU 项目入口脚本

本脚本提供了项目的常用操作命令，包括文档构建、开发服务器启动等功能。
适用于没有安装 uv 包管理器但有 Python 环境的情况。
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description=""):
    """运行命令并处理错误"""
    if description:
        print(f"🚀 {description}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, cwd=Path(__file__).parent)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"❌ 命令执行失败: {e}")
        return e.returncode


def serve():
    """启动 MkDocs 开发服务器"""
    print("📚 启动 CS for NCU 开发服务器...")
    print("🌐 访问地址: http://127.0.0.1:8000")
    print("💡 提示: 按 Ctrl+C 停止服务器")
    return run_command("mkdocs serve", "启动开发服务器")


def build():
    """构建静态网站"""
    return run_command("mkdocs build", "构建静态网站")


def clean():
    """清理构建文件"""
    return run_command("mkdocs build --clean", "清理并构建网站")


def deploy():
    """部署到 GitHub Pages（仅限维护者使用）"""
    print("⚠️  警告: 此命令仅限项目维护者使用")
    print("📝 推荐使用 GitHub Actions 进行自动部署")
    choice = input("是否继续? (y/N): ").strip().lower()
    if choice == 'y':
        return run_command("mkdocs gh-deploy", "部署到 GitHub Pages")
    else:
        print("✅ 操作已取消")
        return 0


def show_help():
    """显示帮助信息"""
    help_text = """
🎓 CS for NCU 项目工具

用法: python main.py <命令>

可用命令:
  serve    启动开发服务器 (默认)
  build    构建静态网站
  clean    清理并构建网站
  deploy   部署到 GitHub Pages
  help     显示此帮助信息

示例:
  python main.py serve    # 启动开发服务器
  python main.py build    # 构建网站
  python main.py clean    # 清理并构建

更多信息请参考: README.md
项目地址: https://github.com/NCUSCC/cs4ncu
"""
    print(help_text)


def main():
    """主函数"""
    # 检查是否在正确的目录
    if not Path("mkdocs.yml").exists():
        print("❌ 错误: 请在项目根目录下运行此脚本")
        sys.exit(1)
    
    # 解析命令行参数
    command = sys.argv[1] if len(sys.argv) > 1 else "serve"
    
    commands = {
        "serve": serve,
        "build": build,
        "clean": clean,
        "deploy": deploy,
        "help": show_help,
        "-h": show_help,
        "--help": show_help,
    }
    
    if command not in commands:
        print(f"❌ 未知命令: {command}")
        show_help()
        sys.exit(1)
    
    # 执行命令
    exit_code = commands[command]()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
