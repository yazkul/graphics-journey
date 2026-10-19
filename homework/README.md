# GAMES101 作业包（官方版 · Mac 已适配）

来源：games-cn.org 官方下载（2020 春季学期 Assignment1–8 + 2021 Homework6）
下载日期：2026-10-18

## 目录

| 目录 | 对应作业 | 内容 | 状态 |
|---|---|---|---|
| `pa0/` | 作业 0（热身） | 环境检查 | ✅ |
| `hw1/代码框架/` | HW1 变换 | Rasterizer | ✅ 已改 CMakeLists，已编译通过 |
| `hw2/代码框架/` | HW2 光栅化 | Rasterizer | ✅ 已改，已编译通过 |
| `hw3/Assignment3/` | HW3 着色 | Rasterizer + 模型/贴图 | ✅ 已改 |
| `hw4/code/` | HW4 Bézier | 2D 曲线 | ✅ 已改 |
| `hw5/Code/` | HW5 光线追踪 | RayTracing | ✅ 已改 |
| `hw6/Assignment6/` | HW6 BVH | RayTracing + BVH | ⚠️ CMakeLists 未改（不需要 OpenCV/Eigen） |
| `hw8/assignment8/` | HW8 弹簧质点 | CGL 框架 | ⚠️ 原版，未改 |
| ❌ HW7 路径追踪 | 官方包里没找到 | — | 待补 |

每个作业目录里都有一份 `AssignmentN.pdf`，**先读 PDF 再做作业**。

## 编译任意一个作业

```bash
cd hw1/代码框架          # 换成你要做的那次
mkdir -p build && cd build
cmake -DCMAKE_PREFIX_PATH=$(brew --prefix opencv) ..
make -j8
```

## 运行 HW1

```bash
./Rasterizer -r 30 output.png   # 无界面模式：转 30 度，存图
./Rasterizer                     # 交互模式：弹出窗口，按 a/d 旋转，ESC 退出
```

## 如果以后自己下载了新作业包

```bash
python3 mac_cmake.py <作业代码目录>
```

它会自动判断需不需要 OpenCV，并生成 Mac 可用的 `CMakeLists.txt`。

## 注意

- 原始 CMakeLists 备份为 `CMakeLists.txt.linux-orig`（Linux 路径 `/usr/local/include`，Mac 上会失败）
- macOS 上解压中文 zip 要用 `python3` 脚本或 `unar`，直接 `unzip` 会出现乱码目录名
