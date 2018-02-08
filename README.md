# Rains

1. 寻找一副雨滴图像, 并创建一系列整齐排列的雨滴. 让这些雨滴往下落, 直到达到屏幕底端后消失.
2. 连绵细雨: 修改之前代码, 使得一行雨滴消失在屏幕底端后, 屏幕顶端又出现一行新雨滴, 并开始往下落.

## 静态雨幕

4个文件:

- `raining.py`: 游戏主文件
- `game_functions.py`: 生成雨幕的相关函数
- `rain_drop.py`: 一个雨滴的类
- `settings.py`: 游戏相关配置(目前只有screen的2个配置:高度/宽度/背景色)

### `raining.py`

#### 主函数`main()`

1. `pygame.init()`
2. 初始化游戏相关配置的类: `settings.Settings()`
3. 创建游戏屏幕(高度宽度)
4. 初始化雨滴 Group()
5. 调用`game_functions.py`生成雨滴的Group.
6. 游戏主循环
    1. 检查事件(遇到QUIT则退出)
    2. 屏幕填充背景色
    3. 绘制所有的雨滴到screen上.
    4. 雨滴优先显示

###  `game_functions.py`

1. 导入`rain_drop.py`的雨滴类
2. 计算一行/一列能容纳几个雨滴
3. 生成雨滴Group的函数
    1. 初始化一个示例雨滴(获取雨滴宽度/高度)
    2. 调用上边的2个函数分别计算处一行/一列容纳多少雨滴
    3. 使用2重嵌套for循环
        1. 外层负责绘制多行
        2. 内层负责一行中的各列
            1. 初始化一个雨滴
            2. 计算并修改雨滴的rect的(x, y)属性
            3. 将雨滴添加到rains的Group中

### `rain_drop.py`

雨滴类

#### 初始化

1. **调用`super(RainDrop, self).__init__()`初始化**
2. 初始化screen
3. 加载图片, 返回雨滴的Surface
4. 利用Surface返回rect
5. 雨滴初始的rect的(x, y)为(0, 0)

#### 绘制

`self.screen.blit(self.image, self.rect)`

## 动态雨幕

### 阵雨

效果: 下过一批雨就没了.

#### `settings.py`

添加雨滴坠落速度

#### `rain_drop.py`

添加`update()`方法: 如果雨滴的rect的top还小于屏幕height, 就根据速度更新雨滴的y坐标.

#### `game_functions.py`

添加`update_rains()`函数:

1. 遍历rains Group中的所有雨滴对象
2. 如果雨滴已经在屏幕外, 从Group中移除
3. 调用雨滴对象的`update()`方法, 更新每个雨滴对象的位置.

#### `raining.py`

在绘制rains之前, 调用`game_functions.py`中的`update_rains()`, 更新雨滴位置.

### 连绵细雨

如果雨滴 Gruop长度不够, 就重绘一行.

