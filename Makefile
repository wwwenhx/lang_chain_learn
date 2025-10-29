# 镜像名
IMAGE_NAME=langchain-agent
# 版本号（时间戳）
TAG=$(shell date +%Y%m%d%H%M)
# 服务器信息
SERVER_USER=root
SERVER_IP=your.server.ip
SERVER_PATH=/opt/langchain-agent

# 1️⃣ 构建 Docker 镜像
docker-build:
	docker build -t $(IMAGE_NAME):$(TAG) .

# 停止并删除旧容器
docker-stop:
	docker stop $(IMAGE_NAME) || true
	docker rm $(IMAGE_NAME) || true

# 2️⃣ 运行本地容器（测试）
docker-run: docker-stop
	docker run -d -p 8000:8000 --network napcat-net --name $(IMAGE_NAME) --pull=never $(IMAGE_NAME):$(TAG)

# 4️⃣ 在服务器上运行容器（自动停止旧容器）
deploy:
	ssh $(SERVER_USER)@$(SERVER_IP) '\
		docker stop $(IMAGE_NAME) || true && \
		docker rm $(IMAGE_NAME) || true && \
		docker run -d -p 8000:8000 --name $(IMAGE_NAME) $(IMAGE_NAME):$(TAG)'

# 一条命令完成构建 + 上传 + 部署
all: build push deploy
