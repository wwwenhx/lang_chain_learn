# 使用官方 Python 镜像（更轻量的 slim 版）
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置时区（可选）
ENV TZ=Asia/Shanghai

# 复制依赖文件并安装
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 复制项目源码
COPY . .

# 设置环境变量（可选）
ENV PYTHONUNBUFFERED=1

# 启动 FastAPI 服务
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]