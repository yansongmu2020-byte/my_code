import hou

# 打印 Houdini 版本确认身份
print("--- Houdini Python 联通成功 ---")
print(f"当前版本: {hou.applicationVersionString()}")

# 尝试创建一个简单的节点（在内存中）
<<<<<<< Updated upstream
node_count = len(hou.node("/").allItems())
=======
node_count = len(hou.node("/").allNodes())
>>>>>>> Stashed changes

print("--- 运行结束 ---")
hou.pwd()

node = hou.pwd()