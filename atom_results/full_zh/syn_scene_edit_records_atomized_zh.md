# 全量编辑指令原子化结果——syn_scene_edit_records.md——中文审阅版

- 源记录数：300

- 所有原子判定句均依据 `atom_results/README.md` 逐条人工审核。

- 原子判定句省略作为截取起点的绝对时间；后续时间点均已换算为片段内相对时间。


## 001 — `synthetic_scene_001_E1`

**原始英文指令：** Starting at 17.0 seconds, increase the daylight entering through the rear window, gently brightening the island and surrounding floor over two and a half seconds.

**中文翻译：** 从第 17.0 秒开始，在两点五秒内增强从后方窗户射入的日光，并柔和地照亮中岛和周围地面。

**状态：** 接受

**原子化判定句：**

1. 从后方窗户射入的日光是否在 2.5 秒内增强？

2. 中岛是否在同一段 2.5 秒内被柔和地照亮？

3. 周围地面是否在同一段 2.5 秒内被柔和地照亮？


## 002 — `synthetic_scene_001_E2A`

**原始英文指令：** At 31.5 seconds, make the woman stop beside the kitchen island for four seconds, then resume walking left along the same route.

**中文翻译：** 在第 31.5 秒，让女子在厨房中岛旁停留四秒，然后沿原路线继续向左行走。

**状态：** 接受

**原子化判定句：**

1. 女子是否在厨房中岛旁停留 4 秒？

2. 女子是否在停留 4 秒后沿原路线继续向左行走？


## 003 — `synthetic_scene_001_E2B`

**原始英文指令：** Starting at 31.5 seconds, make the woman walk faster along the visible leftward route and cross the glass doorway by 37.0 seconds.

**中文翻译：** 从第 31.5 秒开始，让女子沿可见的向左路线加快行走，并在第 37.0 秒前穿过玻璃门口。

**状态：** 接受

**原子化判定句：**

1. 女子是否沿可见的向左路线加快行走？

2. 女子是否在 5.5 秒内穿过玻璃门口？


## 004 — `synthetic_scene_002_E1`

**原始英文指令：** At 8.5 seconds, make the light-clothed person stop beside the sofa for three seconds, then resume walking toward the left doorway.

**中文翻译：** 在第 8.5 秒，让穿浅色衣服的人在沙发旁停留三秒，然后继续朝左侧门口行走。

**状态：** 接受

**原子化判定句：**

1. 穿浅色衣服的人是否在沙发旁停留 3 秒？

2. 此人是否在停留 3 秒后继续朝左侧门口行走？


## 005 — `synthetic_scene_002_E2A`

**原始英文指令：** Starting at 20.0 seconds, make the light-clothed visitor walk right while the dark-clothed visitor continues crossing toward the opposite side.

**中文翻译：** 从第 20.0 秒开始，让穿浅色衣服的访客向右行走，同时让穿深色衣服的访客继续穿行至对面。

**状态：** 接受

**原子化判定句：**

1. 穿浅色衣服的访客是否向右行走？

2. 穿深色衣服的访客是否同时继续穿行至对面？


## 006 — `synthetic_scene_002_E2B`

**原始英文指令：** Starting at 21.0 seconds, change the right floor lamp's warm yellow illumination to cool neutral white over two and a half seconds.

**中文翻译：** 从第 21.0 秒开始，在两点五秒内将右侧落地灯的暖黄色照明变为冷调中性白光。

**状态：** 接受

**原子化判定句：**

1. 右侧落地灯的照明是否由暖黄色变为冷调中性白光？

2. 照明变化是否在 2.5 秒内完成？


## 007 — `synthetic_scene_003_E1`

**原始英文指令：** Starting at 10.0 seconds, change both washing-machine door rims from silver gray to cobalt blue over two and a half seconds.

**中文翻译：** 从第 10.0 秒开始，在两点五秒内将两台洗衣机的门框由银灰色变为钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 左侧洗衣机门框是否由银灰色变为钴蓝色？

2. 右侧洗衣机门框是否由银灰色变为钴蓝色？

3. 两处颜色变化是否都在 2.5 秒内完成？


## 008 — `synthetic_scene_003_E2A`

**原始英文指令：** Starting at 24.0 seconds, open the left washing-machine door outward until it reaches a clearly visible halfway position.

**中文翻译：** 从第 24.0 秒开始，将左侧洗衣机门向外打开，直到达到清晰可见的半开位置。

**状态：** 接受

**原子化判定句：**

1. 左侧洗衣机门是否向外打开？

2. 柜门是否达到清晰可见的半开位置？


## 009 — `synthetic_scene_003_E2B`

**原始英文指令：** Starting at 22.0 seconds, split the long wooden bench beneath the right window into two shorter matching benches separated by a narrow gap.

**中文翻译：** 从第 22.0 秒开始，将右侧窗户下方的长木凳分成两张相互匹配的短木凳，并在两者之间留出一道狭窄间隙。

**状态：** 接受

**原子化判定句：**

1. 右侧窗户下方的长木凳是否被分成两张相互匹配的短木凳？

2. 两张短木凳之间是否留有一道狭窄间隙？


## 010 — `synthetic_scene_004_E1`

**原始英文指令：** Starting at 8.0 seconds, change the courtyard weather to steady light rain visible against the lawn, stone path, and surrounding plants.

**中文翻译：** 从第 8.0 秒开始，将庭院天气变为持续小雨，雨丝在草坪、石径和周围植物的映衬下清晰可见。

**状态：** 接受

**原子化判定句：**

1. 庭院天气是否变为持续小雨？

2. 雨丝是否在草坪、石径和周围植物的映衬下清晰可见？


## 011 — `synthetic_scene_004_E2A`

**原始英文指令：** Starting at 35.0 seconds, split the long wooden bench beside the rear wall into two shorter matching benches with a central gap.

**中文翻译：** 从第 35.0 秒开始，将后墙旁的长木凳分成两张相互匹配的短木凳，并在中央留出一道间隙。

**状态：** 接受

**原子化判定句：**

1. 后墙旁的长木凳是否被分成两张相互匹配的短木凳？

2. 两张短木凳之间是否留有一道中央间隙？


## 012 — `synthetic_scene_004_E2B`

**原始英文指令：** Starting at 20.5 seconds, dolly the camera smoothly toward the central lawn for four seconds, creating visible parallax among the path, bench, and building.

**中文翻译：** 从第 20.5 秒开始，让镜头朝中央草坪平滑推近四秒，使小径、长凳和建筑之间产生可见视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否朝中央草坪平滑推近 4 秒？

2. 小径、长凳和建筑之间是否在同一段 4 秒内产生可见视差？


## 013 — `synthetic_scene_005_E1`

**原始英文指令：** At 11.0 seconds, remove the empty gray office chair beside the management desk and reconstruct the exposed floor behind it.

**中文翻译：** 在第 11.0 秒，移除管理台旁空置的灰色办公椅，并重建其后方露出的地面。

**状态：** 接受

**原子化判定句：**

1. 管理台旁空置的灰色办公椅是否被移除？

2. 被移除椅子后方露出的地面是否得到重建？


## 014 — `synthetic_scene_005_E2A`

**原始英文指令：** Starting at 31.0 seconds, render only the complete mailbox wall behind the desk as a restrained hand-painted watercolor surface over three seconds.

**中文翻译：** 从第 31.0 秒开始，在三秒内仅将桌后完整的信箱墙呈现为克制的手绘水彩表面。

**状态：** 接受

**原子化判定句：**

1. 桌后完整的信箱墙是否呈现为克制的手绘水彩表面？

2. 风格变化是否仅限于信箱墙？

3. 风格变化是否在 3 秒内完成？


## 015 — `synthetic_scene_005_E2B`

**原始英文指令：** At 24.0 seconds, replace the tall potted plant beside the right passage with a freestanding light-wood coat rack in the same footprint.

**中文翻译：** 在第 24.0 秒，将右侧通道旁的高大盆栽替换为占地范围相同的浅色木质落地衣帽架。

**状态：** 接受

**原子化判定句：**

1. 右侧通道旁的高大盆栽是否被替换为浅色木质落地衣帽架？

2. 该衣帽架是否与原盆栽占据相同的地面范围？


## 016 — `synthetic_scene_006_E1`

**原始英文指令：** Starting at 12.0 seconds, open the rightmost lower cabinet beneath the workbench to a clearly visible forty-five-degree angle.

**中文翻译：** 从第 12.0 秒开始，将工作台下方最右侧的下层柜门打开至清晰可见的四十五度。

**状态：** 接受

**原子化判定句：**

1. 工作台下方最右侧的下层柜门是否打开？

2. 柜门是否达到清晰可见的 45 度角？


## 017 — `synthetic_scene_006_E2A`

**原始英文指令：** Starting at 29.0 seconds, change the weather outside the open garage doorway to heavy rain visible across the driveway and vegetation.

**中文翻译：** 从第 29.0 秒开始，将敞开车库门外的天气变为大雨，使雨势在车道和植被区域清晰可见。

**状态：** 接受

**原子化判定句：**

1. 敞开车库门外的天气是否变为大雨？

2. 大雨是否在车道和植被区域清晰可见？


## 018 — `synthetic_scene_006_E2B`

**原始英文指令：** At 25.0 seconds, add a compact yellow rolling tool chest on the empty concrete floor near the right wall.

**中文翻译：** 在第 25.0 秒，在右墙附近空置的混凝土地面上添加一个紧凑的黄色滚轮工具柜。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个紧凑的黄色滚轮工具柜？

2. 该工具柜是否位于右墙附近空置的混凝土地面上？


## 019 — `synthetic_scene_007_E1`

**原始英文指令：** Starting at 18.0 seconds, make the person walk faster along the central path and reach the shelter paving by 21.5 seconds.

**中文翻译：** 从第 18.0 秒开始，让人物沿中央小径加快行走，并在第 21.5 秒前到达遮棚铺装区域。

**状态：** 接受

**原子化判定句：**

1. 人物是否沿中央小径加快行走？

2. 人物是否在 3.5 秒内到达遮棚铺装区域？


## 020 — `synthetic_scene_007_E2A`

**原始英文指令：** Starting at 29.0 seconds, open the dark barbecue lid on the left brick unit until it reaches a stable upright position.

**中文翻译：** 从第 29.0 秒开始，打开左侧砖砌单元上的深色烧烤炉盖，直到其稳定地保持直立。

**状态：** 接受

**原子化判定句：**

1. 左侧砖砌单元上的深色烧烤炉盖是否打开？

2. 炉盖是否达到并稳定保持在直立位置？


## 021 — `synthetic_scene_007_E2B`

**原始英文指令：** Starting at 30.0 seconds, change the garden weather to light low mist spreading across the paving over three seconds.

**中文翻译：** 从第 30.0 秒开始，在三秒内将花园天气变为轻薄低雾，并让雾气在铺装地面上扩散。

**状态：** 接受

**原子化判定句：**

1. 花园中是否出现轻薄低雾？

2. 雾气是否在铺装地面上扩散？

3. 扩散是否在 3 秒内完成？


## 022 — `synthetic_scene_008_E1`

**原始英文指令：** At 9.0 seconds, turn the person on the near pool deck in place until their torso faces directly toward the water.

**中文翻译：** 在第 9.0 秒，让近侧泳池平台上的人物原地转身，直到其躯干正对水面。

**状态：** 接受

**原子化判定句：**

1. 近侧泳池平台上的人物是否原地转身？

2. 其躯干最终是否正对水面？


## 023 — `synthetic_scene_008_E2A`

**原始英文指令：** Starting at 27.0 seconds, truck the elevated camera smoothly right for four seconds, creating parallax between the near railing, pool lanes, and far deck.

**中文翻译：** 从第 27.0 秒开始，让高位镜头平滑向右横移四秒，使近处栏杆、泳道和远处平台之间产生视差。

**状态：** 接受

**原子化判定句：**

1. 高位镜头是否平滑向右横移 4 秒？

2. 近处栏杆、泳道和远处平台之间是否在同一段 4 秒内产生视差？


## 024 — `synthetic_scene_008_E2B`

**原始英文指令：** Starting at 20.5 seconds, freeze the visible pool water into a continuous pale-blue ice surface over four seconds.

**中文翻译：** 从第 20.5 秒开始，在四秒内将可见的泳池水冻结成连续的浅蓝色冰面。

**状态：** 接受

**原子化判定句：**

1. 可见的泳池水是否冻结成冰面？

2. 冰面是否连续且呈浅蓝色？

3. 冻结过程是否在 4 秒内完成？


## 025 — `synthetic_scene_009_E1`

**原始英文指令：** At 10.0 seconds, remove the empty blue office chair nearest the lower edge and reconstruct the exposed floor behind it.

**中文翻译：** 在第 10.0 秒，移除最靠近画面下边缘的空置蓝色办公椅，并重建其后方露出的地面。

**状态：** 接受

**原子化判定句：**

1. 最靠近画面下边缘的空置蓝色办公椅是否被移除？

2. 被移除椅子后方露出的地面是否得到重建？


## 026 — `synthetic_scene_009_E2A`

**原始英文指令：** Starting at 31.0 seconds, make the stationary light-blue-clothed person walk diagonally toward the lower frame edge and exit by 36.0 seconds.

**中文翻译：** 从第 31.0 秒开始，让原本静止的浅蓝衣人物斜向画面下边缘行走，并在第 36.0 秒前离开画面。

**状态：** 接受

**原子化判定句：**

1. 浅蓝衣人物是否斜向画面下边缘行走？

2. 此人物是否在 5 秒内离开画面？


## 027 — `synthetic_scene_009_E2B`

**原始英文指令：** At 22.0 seconds, replace the retained blue office chair beside the left desk with a mustard-yellow upholstered chair in the same footprint.

**中文翻译：** 在第 22.0 秒，将左侧办公桌旁保留的蓝色办公椅替换为占地范围相同的芥末黄色软包椅。

**状态：** 接受

**原子化判定句：**

1. 左侧办公桌旁保留的蓝色办公椅是否被替换为芥末黄色软包椅？

2. 替换后的椅子是否与原蓝色办公椅占据相同的地面范围？


## 028 — `synthetic_scene_010_E1`

**原始英文指令：** At 10.0 seconds, add a third round basket of green apples on the clear floor behind the front orange basket.

**中文翻译：** 在第 10.0 秒，在前方橙色篮子后面的空旷地面上添加第三个装有青苹果的圆篮。

**状态：** 接受

**原子化判定句：**

1. 是否添加了第三个装有青苹果的圆篮？

2. 该圆篮是否位于前方橙色篮子后面的空旷地面上？


## 029 — `synthetic_scene_010_E2A`

**原始英文指令：** At 30.5 seconds, slide the front green produce crate twenty centimeters left across the visible floor.

**中文翻译：** 在第 30.5 秒，将前方绿色果蔬箱沿可见地面向左滑动二十厘米。

**状态：** 接受

**原子化判定句：**

1. 前方绿色果蔬箱是否沿可见地面向左滑动？

2. 移动距离是否为 20 厘米？


## 030 — `synthetic_scene_010_E2B`

**原始英文指令：** Starting at 22.0 seconds, make the tiled floor between the produce baskets and shopping carts visibly wet with a fresh cleaning sheen.

**中文翻译：** 从第 22.0 秒开始，让果蔬篮与购物车之间的瓷砖地面明显湿润，并呈现刚清洁过的光泽。

**状态：** 接受

**原子化判定句：**

1. 果蔬篮与购物车之间的瓷砖地面是否明显变湿？

2. 该瓷砖地面是否呈现刚清洁过的光泽？


## 031 — `synthetic_scene_011_E1`

**原始英文指令：** At 11.0 seconds, remove the empty waiting chair at the far right end of the row and reconstruct the exposed background.

**中文翻译：** 在第 11.0 秒，移除座椅排最右端的空置候诊椅，并重建其后方露出的背景。

**状态：** 接受

**原子化判定句：**

1. 座椅排最右端的空置候诊椅是否被移除？

2. 被移除椅子后方露出的背景是否得到重建？


## 032 — `synthetic_scene_011_E2A`

**原始英文指令：** Starting at 30.0 seconds, change the pale green privacy curtain to deep teal over two and a half seconds.

**中文翻译：** 从第 30.0 秒开始，在两点五秒内将浅绿色隐私帘变为深青绿色。

**状态：** 接受

**原子化判定句：**

1. 隐私帘是否从浅绿色变为深青绿色？

2. 颜色变化是否在 2.5 秒内完成？


## 033 — `synthetic_scene_011_E2B`

**原始英文指令：** At 22.0 seconds, add a compact potted fern on the white side table's clear front-left patch beside the existing bottles.

**中文翻译：** 在第 22.0 秒，在白色边桌左前方、现有瓶子旁的空置区域添加一盆小型蕨类植物。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一盆小型蕨类植物？

2. 该盆栽是否位于白色边桌左前方、现有瓶子旁的空置区域？


## 034 — `synthetic_scene_012_E1`

**原始英文指令：** At 10.0 seconds, move the small vase from the window-side edge to the exact center of the dining table.

**中文翻译：** 在第 10.0 秒，将小花瓶从靠窗一侧的桌边移至餐桌正中央。

**状态：** 接受

**原子化判定句：**

1. 小花瓶是否从靠窗一侧的桌边移开？

2. 花瓶最终是否位于餐桌正中央？


## 035 — `synthetic_scene_012_E2A`

**原始英文指令：** At 24.0 seconds, add a small blank wooden menu holder upright on the empty rear-right corner of the dining table.

**中文翻译：** 在第 24.0 秒，在餐桌右后方的空置桌角竖直放置一个无字的小型木质菜单架。

**状态：** 接受

**原子化判定句：**

1. 是否竖直放置了一个无字的小型木质菜单架？

2. 该菜单架是否位于餐桌右后方的空置桌角？


## 036 — `synthetic_scene_012_E2B`

**原始英文指令：** At 22.0 seconds, place the person one floor tile from the right booth edge, centered beside the dining table's end.

**中文翻译：** 在第 22.0 秒，将人物放置在距离右侧卡座边缘一块地砖的位置，并使其位于餐桌端部旁的中央。

**状态：** 接受

**原子化判定句：**

1. 人物是否位于距离右侧卡座边缘一块地砖的位置？

2. 人物是否位于餐桌端部旁的中央？


## 037 — `synthetic_scene_013_E1`

**原始英文指令：** Starting at 10.0 seconds, render only the complete bookshelf along the right wall as a softly layered watercolor object over three seconds.

**中文翻译：** 从第 10.0 秒开始，在三秒内仅将右墙沿线的完整书架呈现为层次柔和的水彩物体。

**状态：** 接受

**原子化判定句：**

1. 右墙沿线的完整书架是否呈现为层次柔和的水彩物体？

2. 风格变化是否仅限于该书架？

3. 风格变化是否在 3 秒内完成？


## 038 — `synthetic_scene_013_E2A`

**原始英文指令：** At 26.0 seconds, replace the wooden chair beside the reading table with a compact blue upholstered armchair in the same footprint.

**中文翻译：** 在第 26.0 秒，将阅读桌旁的木椅替换为占地范围相同的小型蓝色软包扶手椅。

**状态：** 接受

**原子化判定句：**

1. 阅读桌旁的木椅是否被替换为小型蓝色软包扶手椅？

2. 该扶手椅是否与原木椅占据相同的地面范围？


## 039 — `synthetic_scene_013_E2B`

**原始英文指令：** At 22.0 seconds, move the wooden chair from the reading table to the empty carpet directly beside the right bookshelf.

**中文翻译：** 在第 22.0 秒，将木椅从阅读桌旁移至右侧书架紧邻的空置地毯区域。

**状态：** 接受

**原子化判定句：**

1. 木椅是否从阅读桌旁移至右侧书架紧邻的空置地毯区域？


## 040 — `synthetic_scene_014_E1`

**原始英文指令：** Starting at 10.0 seconds, pan the camera smoothly right for four seconds to reveal more of the frosted window and its bench.

**中文翻译：** 从第 10.0 秒开始，让镜头平滑向右摇摄四秒，以展现更多磨砂窗及其下方长凳。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑向右摇摄 4 秒？

2. 此次摇摄是否展现了更多磨砂窗及其下方长凳？


## 041 — `synthetic_scene_014_E2A`

**原始英文指令：** Starting at 29.0 seconds, change the front salon chair's dark charcoal upholstery to deep burgundy over two and a half seconds.

**中文翻译：** 从第 29.0 秒开始，在两点五秒内将前方美发椅的深炭灰色软包变为深酒红色。

**状态：** 接受

**原子化判定句：**

1. 前方美发椅的软包是否从深炭灰色变为深酒红色？

2. 颜色变化是否在 2.5 秒内完成？


## 042 — `synthetic_scene_014_E2B`

**原始英文指令：** At 22.0 seconds, position the central salon chair one meter directly in front of the left styling counter, centered on the workstation.

**中文翻译：** 在第 22.0 秒，将中央美发椅放置在左侧造型台正前方一米处，并与工作位居中对齐。

**状态：** 接受

**原子化判定句：**

1. 中央美发椅是否位于左侧造型台正前方 1 米处？

2. 该椅子是否与工作位居中对齐？


## 043 — `synthetic_scene_015_E1`

**原始英文指令：** Starting at 10.0 seconds, change the rear bench seat from warm orange wood to matte navy blue over two and a half seconds.

**中文翻译：** 从第 10.0 秒开始，在两点五秒内将后方长凳座面由暖橙色木质变为哑光海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 后方长凳座面是否由暖橙色木质变为海军蓝色？

2. 变化后的座面是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 044 — `synthetic_scene_015_E2A`

**原始英文指令：** At 21.0 seconds, turn only the left-front blue-shirted person in place until their torso faces the nearest bicycle row.

**中文翻译：** 在第 21.0 秒，仅让左前方穿蓝色上衣的人物原地转身，直到其躯干朝向最近的自行车排。

**状态：** 接受

**原子化判定句：**

1. 左前方穿蓝色上衣的人物是否原地转身？

2. 其躯干最终是否朝向最近的自行车排？

3. 转身动作是否仅发生在该人物身上？


## 045 — `synthetic_scene_015_E2B`

**原始英文指令：** Starting at 23.0 seconds, truck the camera smoothly left along the bicycle row for four seconds, producing parallax against the rear bench and doorway.

**中文翻译：** 从第 23.0 秒开始，让镜头沿自行车排平滑向左横移四秒，使其与后方长凳和门口之间产生视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿自行车排平滑向左横移 4 秒？

2. 自行车排、后方长凳和门口之间是否在同一段 4 秒内产生视差？


## 046 — `synthetic_scene_016_E1`

**原始英文指令：** Starting at 18.0 seconds, dolly the camera smoothly toward the pastry display case for three seconds with visible floor and counter parallax.

**中文翻译：** 从第 18.0 秒开始，让镜头朝糕点展示柜平滑推近三秒，并产生可见的地面与柜台视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否朝糕点展示柜平滑推近 3 秒？

2. 地面与柜台之间是否在同一段 3 秒内产生可见视差？


## 047 — `synthetic_scene_016_E2A`

**原始英文指令：** Starting at 26.0 seconds, lift the inclined pastry-case glass lid fifteen degrees around its rear support edge.

**中文翻译：** 从第 26.0 秒开始，以后侧支撑边为轴将倾斜的糕点柜玻璃盖抬起十五度。

**状态：** 接受

**原子化判定句：**

1. 倾斜的糕点柜玻璃盖是否以后侧支撑边为轴抬起？

2. 抬起角度是否为 15 度？


## 048 — `synthetic_scene_016_E2B`

**原始英文指令：** Starting at 30.0 seconds, make the entrance mat's near edge lift and settle through three gentle arcs over five seconds.

**中文翻译：** 从第 30.0 秒开始，让入口地垫的近侧边缘在五秒内经过三次轻柔弧形起伏后落回。

**状态：** 接受

**原子化判定句：**

1. 入口地垫的近侧边缘是否抬起后落回？

2. 该边缘是否恰好经过三次轻柔弧形起伏？

3. 这一过程是否在 5 秒内完成？


## 049 — `synthetic_scene_017_E1`

**原始英文指令：** Starting at 8.0 seconds, make the blue-gray visitor enter by 10.5 seconds while the light-gray visitor continues walking toward the exit.

**中文翻译：** 从第 8.0 秒开始，让穿蓝灰色衣服的访客在第 10.5 秒前进入，同时让穿浅灰色衣服的访客继续朝出口行走。

**状态：** 接受

**原子化判定句：**

1. 穿蓝灰色衣服的访客是否在 2.5 秒内进入？

2. 穿浅灰色衣服的访客是否同时继续朝出口行走？


## 050 — `synthetic_scene_017_E2A`

**原始英文指令：** At 25.0 seconds, add a low rectangular white display pedestal on the empty floor to the right of the central display table.

**中文翻译：** 在第 25.0 秒，在中央展示桌右侧的空置地面上添加一个低矮的白色长方形展示台。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个低矮的白色长方形展示台？

2. 该展示台是否位于中央展示桌右侧的空置地面上？


## 051 — `synthetic_scene_017_E2B`

**原始英文指令：** At 20.0 seconds, place the freestanding entrance sign one meter in front of the central display table, aligned with its centerline.

**中文翻译：** 在第 20.0 秒，将落地入口标牌放置在中央展示桌正前方一米处，并与其中心线对齐。

**状态：** 接受

**原子化判定句：**

1. 落地入口标牌是否位于中央展示桌正前方 1 米处？

2. 入口标牌是否与展示桌的中心线对齐？


## 052 — `synthetic_scene_018_E1`

**原始英文指令：** At 10.0 seconds, remove the empty office chair nearest the lower-right corner and reconstruct the exposed carpet behind it.

**中文翻译：** 在第 10.0 秒，移除最靠近右下角的空置办公椅，并重建其后方露出的地毯。

**状态：** 接受

**原子化判定句：**

1. 最靠近右下角的空置办公椅是否被移除？

2. 被移除椅子后方露出的地毯是否得到重建？


## 053 — `synthetic_scene_018_E2A`

**原始英文指令：** At 28.0 seconds, replace the tall potted tree against the rear wall with a tall columnar cactus in the same footprint.

**中文翻译：** 在第 28.0 秒，将后墙前的高大盆栽树替换为占地范围相同的高大柱状仙人掌。

**状态：** 接受

**原子化判定句：**

1. 后墙前的高大盆栽树是否被替换为高大柱状仙人掌？

2. 该仙人掌是否与原盆栽树占据相同的地面范围？


## 054 — `synthetic_scene_018_E2B`

**原始英文指令：** Starting at 20.5 seconds, make the occupant beside the rear cabinet walk steadily left toward the glass doorway for five seconds.

**中文翻译：** 从第 20.5 秒开始，让后方柜子旁的人物朝玻璃门口稳定地向左行走五秒。

**状态：** 接受

**原子化判定句：**

1. 后方柜子旁的人物是否朝玻璃门口向左行走？

2. 行走是否稳定？

3. 行走是否持续 5 秒？


## 055 — `synthetic_scene_019_E1`

**原始英文指令：** At 10.0 seconds, replace the cylindrical bin beside the left glass door with a plain rectangular gray recycling container.

**中文翻译：** 在第 10.0 秒，将左侧玻璃门旁的圆柱形垃圾桶替换为简洁的长方形灰色回收箱。

**状态：** 接受

**原子化判定句：**

1. 左侧玻璃门旁的圆柱形垃圾桶是否被替换为灰色回收箱？

2. 替换后的回收箱是否简洁且呈长方形？


## 056 — `synthetic_scene_019_E2A`

**原始英文指令：** At 30.0 seconds, remove the cylindrical bin beside the left glass door and reconstruct the exposed wall and floor behind it.

**中文翻译：** 在第 30.0 秒，移除左侧玻璃门旁的圆柱形垃圾桶，并重建其后方露出的墙面和地面。

**状态：** 接受

**原子化判定句：**

1. 左侧玻璃门旁的圆柱形垃圾桶是否被移除？

2. 被移除垃圾桶后方露出的墙面和地面是否得到重建？


## 057 — `synthetic_scene_019_E2B`

**原始英文指令：** Starting at 20.5 seconds, make the brown-coated visitor walk continuously past the bench and clear the right doorway by 25.5 seconds.

**中文翻译：** 从第 20.5 秒开始，让穿棕色外套的访客持续走过长凳，并在第 25.5 秒前完全通过右侧门口。

**状态：** 接受

**原子化判定句：**

1. 穿棕色外套的访客是否持续走过长凳？

2. 该访客是否在 5 秒内完全通过右侧门口？


## 058 — `synthetic_scene_020_E1`

**原始英文指令：** Starting at 18.5 seconds, switch off the right display-case lights and leave the case dark through 32.5 seconds.

**中文翻译：** 从第 18.5 秒开始，关闭右侧展示柜的灯光，并让展示柜持续保持黑暗至第 32.5 秒。

**状态：** 接受

**原子化判定句：**

1. 右侧展示柜的灯光是否被关闭？

2. 右侧展示柜是否持续保持黑暗 14 秒？


## 059 — `synthetic_scene_020_E2A`

**原始英文指令：** At 25.0 seconds, replace the small square white table with a round light-wood cafe table in the same floor position.

**中文翻译：** 在第 25.0 秒，将白色小方桌替换为位于相同地面位置的浅色木质圆形咖啡桌。

**状态：** 接受

**原子化判定句：**

1. 白色小方桌是否被替换为浅色木质圆形咖啡桌？

2. 替换后的桌子是否位于与原桌相同的地面位置？


## 060 — `synthetic_scene_020_E2B`

**原始英文指令：** At 32.5 seconds, switch the right display case's internal lights back on with steady neutral-white illumination.

**中文翻译：** 在第 32.5 秒，重新打开右侧展示柜的内部灯光，并使其发出稳定的中性白光。

**状态：** 接受

**原子化判定句：**

1. 右侧展示柜的内部灯光是否重新打开？

2. 灯光是否发出稳定的中性白光？


## 061 — `synthetic_scene_021_E1`

**原始英文指令：** At 10.0 seconds, move the rectangular rug to the center of the floor gap between the window bench and book rack.

**中文翻译：** 在第 10.0 秒，将长方形地毯移至窗边长凳与书架之间地面空隙的中央。

**状态：** 接受

**原子化判定句：**

1. 长方形地毯是否被移至窗边长凳与书架之间地面空隙的中央？


## 062 — `synthetic_scene_021_E2A`

**原始英文指令：** At 27.0 seconds, place the woman half a meter from the window bench, aligned with the bench centerline.

**中文翻译：** 在第 27.0 秒，将女子放置在距离窗边长凳半米处，并与长凳中心线对齐。

**状态：** 接受

**原子化判定句：**

1. 女子是否位于距离窗边长凳 0.5 米处？

2. 女子是否与长凳中心线对齐？


## 063 — `synthetic_scene_021_E2B`

**原始英文指令：** Starting at 24.0 seconds, draw the fully visible right curtain panel inward until it covers half of the visible glass.

**中文翻译：** 从第 24.0 秒开始，将完全可见的右侧窗帘向内拉，直到覆盖可见玻璃的一半。

**状态：** 接受

**原子化判定句：**

1. 完全可见的右侧窗帘是否被向内拉？

2. 窗帘最终是否覆盖可见玻璃的一半？


## 064 — `synthetic_scene_022_E1`

**原始英文指令：** Starting at 17.5 seconds, open the brown exit door beside the stair landing inward to a stable thirty-degree angle.

**中文翻译：** 从第 17.5 秒开始，将楼梯平台旁的棕色出口门向内打开至稳定的三十度。

**状态：** 接受

**原子化判定句：**

1. 楼梯平台旁的棕色出口门是否向内打开？

2. 门是否达到并稳定保持在 30 度角？


## 065 — `synthetic_scene_022_E2A`

**原始英文指令：** At 25.0 seconds, add a compact leafy plant in a plain ceramic pot at the center of the window-side square table.

**中文翻译：** 在第 25.0 秒，在靠窗方桌中央添加一盆装在素色陶瓷盆中的小型茂叶植物。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一盆装在素色陶瓷盆中的小型茂叶植物？

2. 该盆栽是否位于靠窗方桌中央？


## 066 — `synthetic_scene_022_E2B`

**原始英文指令：** Starting at 31.5 seconds, make the late lone visitor enter from the left and walk steadily across the visible cafeteria walkway.

**中文翻译：** 从第 31.5 秒开始，让较晚出现的独自访客从左侧进入，并稳定地穿过可见的自助餐厅通道。

**状态：** 接受

**原子化判定句：**

1. 较晚出现的独自访客是否从左侧进入？

2. 该访客是否稳定地穿过可见的自助餐厅通道？


## 067 — `synthetic_scene_023_E1`

**原始英文指令：** Starting at 13.0 seconds, make the shallow crosswalk puddles produce synchronized outward ripple rings for five seconds.

**中文翻译：** 从第 13.0 秒开始，让人行横道上的浅水洼同步产生向外扩散的波纹环，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 人行横道上的浅水洼是否产生向外扩散的波纹环？

2. 各水洼中的波纹是否同步？

3. 波纹是否持续 5 秒？


## 068 — `synthetic_scene_023_E2A`

**原始英文指令：** Starting at 29.0 seconds, render only the wet intersection road surface as a muted watercolor region over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内仅将潮湿的十字路口路面呈现为低饱和水彩区域。

**状态：** 接受

**原子化判定句：**

1. 潮湿的十字路口路面是否呈现为低饱和水彩区域？

2. 风格变化是否仅限于该路面？

3. 风格变化是否在 3 秒内完成？


## 069 — `synthetic_scene_023_E2B`

**原始英文指令：** Starting at 26.0 seconds, change the left-foreground sidewalk wall from light gray stone to dark charcoal over two and a half seconds.

**中文翻译：** 从第 26.0 秒开始，在两点五秒内将左前景的人行道墙面由浅灰石材变为深炭灰色。

**状态：** 接受

**原子化判定句：**

1. 左前景的人行道墙面是否由浅灰色变为深炭灰色？

2. 颜色变化是否在 2.5 秒内完成？


## 070 — `synthetic_scene_024_E1`

**原始英文指令：** Starting at 18.0 seconds, track the camera left alongside the departing train for four seconds with visible platform parallax.

**中文翻译：** 从第 18.0 秒开始，让镜头沿正在离站的列车向左跟拍四秒，并产生可见的站台视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿正在离站的列车向左跟拍 4 秒？

2. 是否在同一段 4 秒内产生可见的站台视差？


## 071 — `synthetic_scene_024_E2A`

**原始英文指令：** Starting at 34.0 seconds, zoom out smoothly to include the entering train nose, full platform edge, canopy, and track approach.

**中文翻译：** 从第 34.0 秒开始，平滑拉远镜头，将进站列车车头、完整站台边缘、雨棚和进站轨道纳入画面。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑拉远？

2. 拉远后的画面是否包含进站列车车头和完整站台边缘？

3. 拉远后的画面是否包含雨棚和进站轨道？


## 072 — `synthetic_scene_024_E2B`

**原始英文指令：** Starting at 32.5 seconds, apply a restrained cool-blue cinematic color grade with soft contrast to the entire platform scene.

**中文翻译：** 从第 32.5 秒开始，为整个站台场景应用克制的冷蓝电影色调和柔和对比度。

**状态：** 接受

**原子化判定句：**

1. 整个站台场景是否呈现克制的冷蓝电影色调？

2. 调色后的场景是否具有柔和对比度？


## 073 — `synthetic_scene_025_E1`

**原始英文指令：** Starting at 13.0 seconds, make the stopped bus's nearest visible folding door open steadily over four seconds.

**中文翻译：** 从第 13.0 秒开始，让停靠公交车最近的可见折叠门在四秒内平稳打开。

**状态：** 接受

**原子化判定句：**

1. 停靠公交车最近的可见折叠门是否打开？

2. 开门动作是否平稳？

3. 折叠门是否在 4 秒内完成打开？


## 074 — `synthetic_scene_025_E2A`

**原始英文指令：** Starting at 29.0 seconds, freeze the clearly visible platform-sidewalk puddles into thin translucent ice patches over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内将站台人行道上清晰可见的水洼冻结成薄而半透明的冰面斑块。

**状态：** 接受

**原子化判定句：**

1. 站台人行道上清晰可见的水洼是否冻结成冰面斑块？

2. 冰面斑块是否薄且半透明？

3. 冻结过程是否在 3 秒内完成？


## 075 — `synthetic_scene_025_E2B`

**原始英文指令：** At 25.5 seconds, position the rear white bus one full bus length behind the nearest white bus along the curb.

**中文翻译：** 在第 25.5 秒，将后方白色公交车放置在沿路缘、距最近白色公交车后一整车长的位置。

**状态：** 接受

**原子化判定句：**

1. 后方白色公交车是否位于沿路缘、距最近白色公交车后一整车长的位置？


## 076 — `synthetic_scene_026_E1`

**原始英文指令：** Starting at 12.5 seconds, split the long bench beside the right fountain path into two shorter matching benches with a central gap.

**中文翻译：** 从第 12.5 秒开始，将喷泉右侧小径旁的长凳分成两张相互匹配的短凳，并在中央留出一道间隙。

**状态：** 接受

**原子化判定句：**

1. 喷泉右侧小径旁的长凳是否被分成两张相互匹配的短凳？

2. 两张短凳之间是否留有一道中央间隙？


## 077 — `synthetic_scene_026_E2A`

**原始英文指令：** Starting at 20.5 seconds, make the front pair walk faster past the fountain while the rear pair continues at its original pace.

**中文翻译：** 从第 20.5 秒开始，让前方两人加快速度走过喷泉，同时让后方两人继续保持原有步速。

**状态：** 接受

**原子化判定句：**

1. 前方两人是否加快速度走过喷泉？

2. 后方两人是否同时继续保持原有步速行走？


## 078 — `synthetic_scene_026_E2B`

**原始英文指令：** At 25.0 seconds, arrange the visible visitors into two compact clusters on opposite sides of the fountain path centerline.

**中文翻译：** 在第 25.0 秒，将可见访客排列成两个紧凑群组，分别位于喷泉小径中心线的两侧。

**状态：** 接受

**原子化判定句：**

1. 可见访客是否被排列成恰好两个紧凑群组？

2. 两个群组是否分别位于喷泉小径中心线的两侧？


## 079 — `synthetic_scene_027_E1`

**原始英文指令：** Starting at 11.0 seconds, change the park weather to a light amber autumn mist spreading across the paths and grass.

**中文翻译：** 从第 11.0 秒开始，将公园天气变为浅琥珀色秋雾，并让雾气扩散至小径和草地。

**状态：** 接受

**原子化判定句：**

1. 公园中是否出现浅琥珀色秋雾？

2. 雾气是否扩散至小径和草地？


## 080 — `synthetic_scene_027_E2A`

**原始英文指令：** At 29.0 seconds, move the foreground dark bench directly opposite the pale rear bench across the path intersection.

**中文翻译：** 在第 29.0 秒，将前景深色长凳移至小径交叉口另一侧，与后方浅色长凳正对。

**状态：** 接受

**原子化判定句：**

1. 前景深色长凳是否被移至小径交叉口另一侧？

2. 长凳最终是否与后方浅色长凳正对？


## 081 — `synthetic_scene_027_E2B`

**原始英文指令：** Starting at 24.0 seconds, freeze the shallow water edge beside the right path into a continuous translucent ice sheet.

**中文翻译：** 从第 24.0 秒开始，将右侧小径旁的浅水边缘冻结成连续的半透明冰层。

**状态：** 接受

**原子化判定句：**

1. 右侧小径旁的浅水边缘是否冻结成冰层？

2. 冰层是否连续且半透明？


## 082 — `synthetic_scene_028_E1`

**原始英文指令：** Starting at 18.0 seconds, retract the belt between the two nearest queue stanchions completely into the left post.

**中文翻译：** 从第 18.0 秒开始，将最近两根排队隔离柱之间的伸缩带完全收回左侧柱内。

**状态：** 接受

**原子化判定句：**

1. 最近两根排队隔离柱之间的伸缩带是否收回左侧柱内？

2. 伸缩带是否完全收回？


## 083 — `synthetic_scene_028_E2A`

**原始英文指令：** Starting at 27.0 seconds, truck the camera smoothly left across the queue lanes for four seconds with visible floor parallax.

**中文翻译：** 从第 27.0 秒开始，让镜头横跨排队通道平滑向左横移四秒，并产生可见的地面视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否横跨排队通道平滑向左横移 4 秒？

2. 是否在同一段 4 秒内产生可见的地面视差？


## 084 — `synthetic_scene_028_E2B`

**原始英文指令：** At 31.0 seconds, replace the complete black stanchion immediately left of the cropped rightmost post with a compact potted palm.

**中文翻译：** 在第 31.0 秒，将被裁切的最右侧隔离柱紧邻左侧那根完整黑色隔离柱替换为一盆小型棕榈。

**状态：** 接受

**原子化判定句：**

1. 被裁切的最右侧隔离柱紧邻左侧那根完整黑色隔离柱是否被替换为一盆小型棕榈？


## 085 — `synthetic_scene_029_E1`

**原始英文指令：** Starting at 12.0 seconds, dolly the camera smoothly toward the ferry gangway for four seconds with visible railing and deck parallax.

**中文翻译：** 从第 12.0 秒开始，让镜头朝渡轮舷梯平滑推近四秒，并产生可见的栏杆与甲板视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否朝渡轮舷梯平滑推近 4 秒？

2. 栏杆与甲板之间是否在同一段 4 秒内产生可见视差？


## 086 — `synthetic_scene_029_E2A`

**原始英文指令：** Starting at 30.0 seconds, swing the black access gate at the floating-ramp connection inward until it is halfway open.

**中文翻译：** 从第 30.0 秒开始，将浮动坡道连接处的黑色通行门向内旋开，直到达到半开状态。

**状态：** 接受

**原子化判定句：**

1. 浮动坡道连接处的黑色通行门是否向内旋开？

2. 通行门是否达到半开状态？


## 087 — `synthetic_scene_029_E2B`

**原始英文指令：** Starting at 25.0 seconds, make broad slow swells travel across the harbor water toward the ferry dock for five seconds.

**中文翻译：** 从第 25.0 秒开始，让宽阔而缓慢的涌浪在港湾水面上朝渡轮码头传播五秒。

**状态：** 接受

**原子化判定句：**

1. 涌浪是否在港湾水面上朝渡轮码头传播？

2. 涌浪是否宽阔且缓慢？

3. 传播是否持续 5 秒？


## 088 — `synthetic_scene_030_E1`

**原始英文指令：** Starting at 14.0 seconds, increase the warm pendant lights above the food counter, brightening the counter and nearby floor over two and a half seconds.

**中文翻译：** 从第 14.0 秒开始，在两点五秒内增强食品柜台上方的暖色吊灯光线，并照亮柜台及附近地面。

**状态：** 接受

**原子化判定句：**

1. 食品柜台上方的暖色吊灯光线是否在 2.5 秒内增强？

2. 食品柜台是否在同一段 2.5 秒内变亮？

3. 附近地面是否在同一段 2.5 秒内变亮？


## 089 — `synthetic_scene_030_E2A`

**原始英文指令：** Starting at 25.0 seconds, render only the unlabelled lower counter strip as a hand-painted copper watercolor surface over three seconds.

**中文翻译：** 从第 25.0 秒开始，在三秒内仅将没有标签的下部柜台饰带呈现为手绘铜色水彩表面。

**状态：** 接受

**原子化判定句：**

1. 没有标签的下部柜台饰带是否呈现为手绘铜色水彩表面？

2. 风格变化是否仅限于该柜台饰带？

3. 风格变化是否在 3 秒内完成？


## 090 — `synthetic_scene_030_E2B`

**原始英文指令：** Starting at 27.0 seconds, transform the entire night-market scene into a restrained 1970s color-film style with fine grain.

**中文翻译：** 从第 27.0 秒开始，将整个夜市场景转换为带细腻颗粒的克制 20 世纪 70 年代彩色胶片风格。

**状态：** 接受

**原子化判定句：**

1. 整个夜市场景是否转换为克制的 20 世纪 70 年代彩色胶片风格？

2. 画面是否出现细腻颗粒？


## 091 — `synthetic_scene_031_E1`

**原始英文指令：** At 10.0 seconds, add a compact plain blue luggage cart on the clear floor beside the stepped escalator.

**中文翻译：** 在第 10.0 秒，在阶梯式自动扶梯旁的空旷地面上添加一辆简洁的小型蓝色行李车。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一辆简洁的小型蓝色行李车？

2. 该行李车是否位于阶梯式自动扶梯旁的空旷地面上？


## 092 — `synthetic_scene_031_E2A`

**原始英文指令：** Starting at 29.0 seconds, move the camera forward toward the escalator landing for four seconds with visible step-and-railing parallax.

**中文翻译：** 从第 29.0 秒开始，让镜头朝自动扶梯平台向前移动四秒，并产生可见的台阶与栏杆视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否朝自动扶梯平台向前移动 4 秒？

2. 台阶与栏杆之间是否在同一段 4 秒内产生可见视差？


## 093 — `synthetic_scene_031_E2B`

**原始英文指令：** Starting at 23.0 seconds, transform the complete stepped-escalator hall into a restrained architectural ink-wash illustration with soft gray shading.

**中文翻译：** 从第 23.0 秒开始，将完整的阶梯式自动扶梯大厅转换为带柔和灰色明暗的克制建筑水墨插画。

**状态：** 接受

**原子化判定句：**

1. 完整的阶梯式自动扶梯大厅是否转换为克制的建筑水墨插画？

2. 水墨插画是否具有柔和的灰色明暗？


## 094 — `synthetic_scene_032_E1`

**原始英文指令：** At 13.0 seconds, remove only the empty front bench segment below the picnic tabletop and reconstruct the exposed paving.

**中文翻译：** 在第 13.0 秒，仅移除野餐桌面下方空置的前侧长凳段，并重建露出的铺装地面。

**状态：** 接受

**原子化判定句：**

1. 是否仅移除了野餐桌面下方空置的前侧长凳段？

2. 露出的铺装地面是否得到重建？


## 095 — `synthetic_scene_032_E2A`

**原始英文指令：** Starting at 20.0 seconds, make the visible tree crown above the picnic area bend left and recover through three broad arcs.

**中文翻译：** 从第 20.0 秒开始，让野餐区上方可见的树冠经过三次大幅弧形运动向左弯曲并恢复。

**状态：** 接受

**原子化判定句：**

1. 野餐区上方可见的树冠是否向左弯曲后恢复？

2. 树冠是否恰好经过三次大幅弧形运动？


## 096 — `synthetic_scene_032_E2B`

**原始英文指令：** At 26.0 seconds, replace the empty front picnic bench segment with two round pale-stone stools aligned beneath the table edge.

**中文翻译：** 在第 26.0 秒，将空置的前侧野餐长凳段替换为两个圆形浅色石凳，并使其在桌边下方对齐。

**状态：** 接受

**原子化判定句：**

1. 空置的前侧野餐长凳段是否被替换为两个圆形浅色石凳？

2. 两个石凳是否在桌边下方对齐？


## 097 — `synthetic_scene_033_E1`

**原始英文指令：** Starting at 10.0 seconds, make the visible light-blue-clothed visitor turn before the right doorway and walk back left for four seconds.

**中文翻译：** 从第 10.0 秒开始，让可见的浅蓝衣访客在右侧门口前转身，并向左走回四秒。

**状态：** 接受

**原子化判定句：**

1. 可见的浅蓝衣访客是否在右侧门口前转身？

2. 该访客是否在转身后向左走回 4 秒？


## 098 — `synthetic_scene_033_E2A`

**原始英文指令：** At 22.0 seconds, make the visitor stop beside the central bench for four seconds, then resume walking toward the exit.

**中文翻译：** 在第 22.0 秒，让访客在中央长凳旁停留四秒，然后继续朝出口行走。

**状态：** 接受

**原子化判定句：**

1. 访客是否在中央长凳旁停留 4 秒？

2. 访客是否在停留 4 秒后继续朝出口行走？


## 099 — `synthetic_scene_033_E2B`

**原始英文指令：** Starting at 23.0 seconds, convert the complete exhibit-room scene into muted archival color film with restrained grain over three seconds.

**中文翻译：** 从第 23.0 秒开始，在三秒内将完整的展览室场景转换为带克制颗粒的低饱和档案彩色胶片影像。

**状态：** 接受

**原子化判定句：**

1. 完整的展览室场景是否转换为低饱和档案彩色胶片影像？

2. 转换后的场景是否带有克制的颗粒效果？

3. 这一转换是否在 3 秒内完成？


## 100 — `synthetic_scene_034_E1`

**原始英文指令：** Starting at 14.0 seconds, make concentric ripples repeatedly spread from the fallen log's submerged end for five seconds.

**中文翻译：** 从第 14.0 秒开始，让同心波纹从倒木浸没在水中的一端反复向外扩散五秒。

**状态：** 接受

**原子化判定句：**

1. 同心波纹是否从倒木浸没在水中的一端反复向外扩散？

2. 反复扩散是否持续 5 秒？


## 101 — `synthetic_scene_034_E2A`

**原始英文指令：** Starting at 25.0 seconds, apply a cool desaturated teal-gray color grade with soft contrast to the entire waterside scene.

**中文翻译：** 从第 25.0 秒开始，为整个水边场景应用冷调、低饱和的青灰色调和柔和对比度。

**状态：** 接受

**原子化判定句：**

1. 整个水边场景是否呈现冷调、低饱和的青灰色调？

2. 调色后的场景是否具有柔和对比度？


## 102 — `synthetic_scene_034_E2B`

**原始英文指令：** Starting at 27.0 seconds, transform the complete fallen-log waterside scene into a soft chalk-pastel landscape illustration over three seconds.

**中文翻译：** 从第 27.0 秒开始，在三秒内将完整的倒木水边场景转换为柔和的粉笔彩绘风景插画。

**状态：** 接受

**原子化判定句：**

1. 完整的倒木水边场景是否转换为柔和的粉笔彩绘风景插画？

2. 这一转换是否在 3 秒内完成？


## 103 — `synthetic_scene_035_E1`

**原始英文指令：** Starting at 18.0 seconds, move the camera forward faster along the stream until the visible rock cluster fills the foreground by 22.0 seconds.

**中文翻译：** 从第 18.0 秒开始，让镜头沿溪流更快地向前移动，直到可见岩石群在第 22.0 秒前填满前景。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿溪流更快地向前移动？

2. 可见岩石群是否在 4 秒内填满前景？


## 104 — `synthetic_scene_035_E2A`

**原始英文指令：** At 28.0 seconds, place the smaller foreground rock one rock-width from the large round boulder across the streambed.

**中文翻译：** 在第 28.0 秒，将较小的前景岩石放置在溪床另一侧，距大型圆形巨石一个岩石宽度。

**状态：** 接受

**原子化判定句：**

1. 较小的前景岩石是否被放置在大型圆形巨石对面的溪床另一侧？

2. 两块岩石的间距是否为一个岩石宽度？


## 105 — `synthetic_scene_035_E2B`

**原始英文指令：** Starting at 31.0 seconds, make the stream flow rapidly downstream with stronger visible eddies around the rocks for five seconds.

**中文翻译：** 从第 31.0 秒开始，让溪水快速向下游流动五秒，并在岩石周围形成更强的可见涡流。

**状态：** 接受

**原子化判定句：**

1. 溪水是否快速向下游流动 5 秒？

2. 岩石周围是否在同一段 5 秒内形成更强的可见涡流？


## 106 — `synthetic_scene_036_E1`

**原始英文指令：** Starting at 14.0 seconds, convert the complete kelp corridor into restrained 1960s underwater film with fine grain over three seconds.

**中文翻译：** 从第 14.0 秒开始，在三秒内将完整的海带通道转换为带细腻颗粒的克制 20 世纪 60 年代水下胶片影像。

**状态：** 接受

**原子化判定句：**

1. 完整的海带通道是否在 3 秒内转换为克制的 20 世纪 60 年代水下胶片风格？

2. 画面是否在同一段 3 秒内出现细腻颗粒？


## 107 — `synthetic_scene_036_E2A`

**原始英文指令：** At 29.0 seconds, move the nearest left kelp cluster one meter left of the sandy corridor edge.

**中文翻译：** 在第 29.0 秒，将最近的左侧海带簇移至沙质通道边缘左侧一米处。

**状态：** 接受

**原子化判定句：**

1. 最近的左侧海带簇是否被移至沙质通道边缘左侧？

2. 海带簇最终是否距该边缘 1 米？


## 108 — `synthetic_scene_036_E2B`

**原始英文指令：** Starting at 27.0 seconds, make the tall kelp fronds on both sides bend right and recover in synchronized waves for five seconds.

**中文翻译：** 从第 27.0 秒开始，让两侧高大的海带叶片以同步波动向右弯曲并恢复，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 两侧高大的海带叶片是否向右弯曲后恢复？

2. 两侧的波动是否同步？

3. 这一运动是否持续 5 秒？


## 109 — `synthetic_scene_037_E1`

**原始英文指令：** Starting at 13.0 seconds, open the gray wall-mounted electrical-cabinet door outward to a stable forty-five-degree angle.

**中文翻译：** 从第 13.0 秒开始，将灰色壁挂式电气柜门向外打开至稳定的四十五度。

**状态：** 接受

**原子化判定句：**

1. 灰色壁挂式电气柜门是否向外打开？

2. 柜门是否达到并稳定保持在 45 度角？


## 110 — `synthetic_scene_037_E2A`

**原始英文指令：** Starting at 29.0 seconds, render only the visible aircraft fuselage as a bronze woodcut illustration with engraved linework over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内仅将可见的飞机机身呈现为带雕刻线条的青铜色木刻插画。

**状态：** 接受

**原子化判定句：**

1. 可见的飞机机身是否呈现为带雕刻线条的青铜色木刻插画？

2. 风格变化是否仅限于可见机身？

3. 风格变化是否在 3 秒内完成？


## 111 — `synthetic_scene_037_E2B`

**原始英文指令：** Starting at 26.0 seconds, change the wall-mounted gray electrical cabinet right of the aircraft to bright cobalt blue.

**中文翻译：** 从第 26.0 秒开始，将飞机右侧壁挂的灰色电气柜变为明亮的钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 飞机右侧壁挂的灰色电气柜是否变为明亮的钴蓝色？


## 112 — `synthetic_scene_038_E1`

**原始英文指令：** Starting at 14.0 seconds, make broad diagonal swells travel across the open water toward the work platform for five seconds.

**中文翻译：** 从第 14.0 秒开始，让宽阔的斜向涌浪在开阔水面上朝作业平台传播五秒。

**状态：** 接受

**原子化判定句：**

1. 涌浪是否在开阔水面上朝作业平台传播？

2. 涌浪是否宽阔且呈斜向？

3. 传播是否持续 5 秒？


## 113 — `synthetic_scene_038_E2A`

**原始英文指令：** Starting at 29.0 seconds, change the curved platform railing from dark gray to matte cobalt blue over two and a half seconds.

**中文翻译：** 从第 29.0 秒开始，在两点五秒内将弧形平台栏杆由深灰色变为哑光钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 弧形平台栏杆是否由深灰色变为钴蓝色？

2. 变化后的栏杆是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 114 — `synthetic_scene_038_E2B`

**原始英文指令：** Starting at 27.0 seconds, make the pale platform deck visibly wet with a darker sheen and shallow reflective patches.

**中文翻译：** 从第 27.0 秒开始，让浅色平台甲板变得明显湿润，并呈现更深的光泽和浅薄反光水斑。

**状态：** 接受

**原子化判定句：**

1. 浅色平台甲板是否变得明显湿润？

2. 甲板是否呈现更深的光泽？

3. 甲板上是否出现浅薄的反光水斑？


## 115 — `synthetic_scene_039_E1`

**原始英文指令：** Starting at 14.0 seconds, lower the machine's front shutter until the remaining narrow opening along its lower edge is closed.

**中文翻译：** 从第 14.0 秒开始，降下机器的前侧卷帘，直到其下缘剩余的狭窄开口完全闭合。

**状态：** 接受

**原子化判定句：**

1. 机器的前侧卷帘是否降下？

2. 卷帘下缘剩余的狭窄开口是否完全闭合？


## 116 — `synthetic_scene_039_E2A`

**原始英文指令：** At 29.0 seconds, arrange the three gray bins in one evenly spaced row along the machine's left side.

**中文翻译：** 在第 29.0 秒，将三个灰色箱体沿机器左侧排列成一排，并保持均匀间距。

**状态：** 接受

**原子化判定句：**

1. 三个灰色箱体是否全部沿机器左侧排列成一排？

2. 箱体之间的间距是否均匀？


## 117 — `synthetic_scene_039_E2B`

**原始英文指令：** Starting at 27.0 seconds, change all three gray bins to matte dark green over two and a half seconds.

**中文翻译：** 从第 27.0 秒开始，在两点五秒内将三个灰色箱体全部变为哑光深绿色。

**状态：** 接受

**原子化判定句：**

1. 三个灰色箱体是否全部变为深绿色？

2. 变化后的箱体是否呈哑光效果？

3. 这些变化是否在 2.5 秒内完成？


## 118 — `synthetic_scene_040_E1`

**原始英文指令：** Starting at 17.0 seconds, move the camera along a lower clockwise arc around the wind turbine for four seconds.

**中文翻译：** 从第 17.0 秒开始，让镜头围绕风力涡轮机沿较低的顺时针弧线移动四秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否围绕风力涡轮机沿较低的顺时针弧线移动？

2. 这一移动是否持续 4 秒？


## 119 — `synthetic_scene_040_E2A`

**原始英文指令：** Starting at 28.0 seconds, make the three visible grass bands beside the service roads bend and recover through two synchronized wind waves.

**中文翻译：** 从第 28.0 秒开始，让维修道路旁三条可见草带经过两次同步风浪而弯曲并恢复。

**状态：** 接受

**原子化判定句：**

1. 维修道路旁三条可见草带是否都弯曲后恢复？

2. 草带是否经过恰好两次风浪？

3. 三条草带上的风浪是否同步？


## 120 — `synthetic_scene_040_E2B`

**原始英文指令：** Starting at 30.0 seconds, change the weather around the wind turbine to a moderate rain shower visible across the fields.

**中文翻译：** 从第 30.0 秒开始，将风力涡轮机周围的天气变为中等阵雨，使降雨在田野上清晰可见。

**状态：** 接受

**原子化判定句：**

1. 风力涡轮机周围的天气是否变为中等阵雨？

2. 降雨是否在田野上清晰可见？


## 121 — `synthetic_scene_041_E1`

**原始英文指令：** Starting at 12.0 seconds, change the long wraparound curtains from muted taupe gray to matte deep teal over two and a half seconds.

**中文翻译：** 从第 12.0 秒开始，在两点五秒内将长幅环绕窗帘由低饱和灰褐色变为哑光深青绿色。

**状态：** 接受

**原子化判定句：**

1. 长幅环绕窗帘是否由低饱和灰褐色变为深青绿色？

2. 变化后的窗帘是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 122 — `synthetic_scene_041_E2A`

**原始英文指令：** Starting at 29.0 seconds, accelerate the ongoing right-curtain opening until it is tightly gathered at the far-left side by 30.5 seconds.

**中文翻译：** 从第 29.0 秒开始，加快右侧窗帘正在进行的打开过程，使其在第 30.5 秒前紧密收拢至最左侧。

**状态：** 接受

**原子化判定句：**

1. 右侧窗帘正在进行的打开过程是否加快？

2. 右侧窗帘是否在 1.5 秒内紧密收拢至最左侧？


## 123 — `synthetic_scene_041_E2B`

**原始英文指令：** At 25.0 seconds, add a plain round cream rug at the center of the empty wooden floor.

**中文翻译：** 在第 25.0 秒，在空置木地板中央添加一张简洁的圆形奶油色地毯。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一张简洁的圆形奶油色地毯？

2. 该地毯是否位于空置木地板中央？


## 124 — `synthetic_scene_042_E1`

**原始英文指令：** Starting at 13.0 seconds, increase the daylight through the left frosted window, brightening the sink and shower threshold over two and a half seconds.

**中文翻译：** 从第 13.0 秒开始，在两点五秒内增强透过左侧磨砂窗的日光，并照亮水槽和淋浴间门槛。

**状态：** 接受

**原子化判定句：**

1. 透过左侧磨砂窗的日光是否在 2.5 秒内增强？

2. 水槽是否在同一段 2.5 秒内变亮？

3. 淋浴间门槛是否在同一段 2.5 秒内变亮？


## 125 — `synthetic_scene_042_E2A`

**原始英文指令：** Starting at 29.0 seconds, open the right glass shower door outward until it reaches a stable halfway position.

**中文翻译：** 从第 29.0 秒开始，将右侧玻璃淋浴门向外打开，直到达到稳定的半开位置。

**状态：** 接受

**原子化判定句：**

1. 右侧玻璃淋浴门是否向外打开？

2. 淋浴门是否达到并稳定保持在半开位置？


## 126 — `synthetic_scene_042_E2B`

**原始英文指令：** At 25.0 seconds, add a plain rectangular teal bath mat on the empty tiled floor in front of the shower.

**中文翻译：** 在第 25.0 秒，在淋浴间前方空置的瓷砖地面上添加一张简洁的长方形青绿色浴垫。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一张简洁的长方形青绿色浴垫？

2. 该浴垫是否位于淋浴间前方空置的瓷砖地面上？


## 127 — `synthetic_scene_043_E1`

**原始英文指令：** At 10.0 seconds, replace the potted shrub left of the porch bench with a compact olive tree in the same pot.

**中文翻译：** 在第 10.0 秒，将门廊长凳左侧的盆栽灌木替换为种在同一花盆中的小型橄榄树。

**状态：** 接受

**原子化判定句：**

1. 门廊长凳左侧的盆栽灌木是否被替换为小型橄榄树？

2. 橄榄树是否仍种在同一个花盆中？


## 128 — `synthetic_scene_043_E2A`

**原始英文指令：** At 29.0 seconds, remove the empty white porch bench and reconstruct the wall and paving behind it.

**中文翻译：** 在第 29.0 秒，移除空置的白色门廊长凳，并重建其后方的墙面和铺装地面。

**状态：** 接受

**原子化判定句：**

1. 空置的白色门廊长凳是否被移除？

2. 被移除长凳后方的墙面和铺装地面是否得到重建？


## 129 — `synthetic_scene_043_E2B`

**原始英文指令：** Starting at 23.0 seconds, swing the dark porch screen door outward until it reaches a stable thirty-degree open position.

**中文翻译：** 从第 23.0 秒开始，将深色门廊纱门向外旋开，直到达到稳定的三十度开启位置。

**状态：** 接受

**原子化判定句：**

1. 深色门廊纱门是否向外旋开？

2. 纱门是否达到并稳定保持在 30 度开启位置？


## 130 — `synthetic_scene_044_E1`

**原始英文指令：** Starting at 12.0 seconds, make both light-shirted viewers turn together toward the left doorway, then face the projection again within four seconds.

**中文翻译：** 从第 12.0 秒开始，让两名穿浅色上衣的观看者一起转向左侧门口，然后在四秒内重新面向投影。

**状态：** 接受

**原子化判定句：**

1. 两名穿浅色上衣的观看者是否一起转向左侧门口？

2. 两人是否在 4 秒内重新面向投影？


## 131 — `synthetic_scene_044_E2A`

**原始英文指令：** Starting at 22.0 seconds, make the left original viewer walk toward the right doorway while the green-clothed passerby remains visible.

**中文翻译：** 从第 22.0 秒开始，让左侧原有观看者朝右侧门口行走，同时让穿绿色衣服的路人保持可见。

**状态：** 接受

**原子化判定句：**

1. 左侧原有观看者是否朝右侧门口行走？

2. 穿绿色衣服的路人是否同时保持可见？


## 132 — `synthetic_scene_044_E2B`

**原始英文指令：** Starting at 25.0 seconds, convert the complete projection-room scene into muted 1980s color film with fine grain over three seconds.

**中文翻译：** 从第 25.0 秒开始，在三秒内将完整的放映室场景转换为带细腻颗粒的低饱和 20 世纪 80 年代彩色胶片影像。

**状态：** 接受

**原子化判定句：**

1. 完整的放映室场景是否转换为低饱和 20 世纪 80 年代彩色胶片影像？

2. 转换后的场景是否带有细腻颗粒？

3. 这一转换是否在 3 秒内完成？


## 133 — `synthetic_scene_045_E1`

**原始英文指令：** At 10.0 seconds, add a plain cobalt-blue ceramic planter beside the lower rectangular planter on the stable tiled floor.

**中文翻译：** 在第 10.0 秒，在稳定的瓷砖地面上、较低的长方形花盆旁添加一个简洁的钴蓝色陶瓷花盆。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个简洁的钴蓝色陶瓷花盆？

2. 该花盆是否位于稳定瓷砖地面上的较低长方形花盆旁？


## 134 — `synthetic_scene_045_E2A`

**原始英文指令：** Starting at 29.0 seconds, render only the visible greenhouse tiled floor as a softly layered watercolor region over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内仅将温室内可见的瓷砖地面呈现为层次柔和的水彩区域。

**状态：** 接受

**原子化判定句：**

1. 温室内可见的瓷砖地面是否呈现为层次柔和的水彩区域？

2. 风格变化是否仅限于可见瓷砖地面？

3. 风格变化是否在 3 秒内完成？


## 135 — `synthetic_scene_045_E2B`

**原始英文指令：** Starting at 23.0 seconds, make the visitor outside the greenhouse walk left faster and clear the visible frame edge by 28.0 seconds.

**中文翻译：** 从第 23.0 秒开始，让温室外的访客加快向左行走，并在第 28.0 秒前完全离开可见画面边缘。

**状态：** 接受

**原子化判定句：**

1. 温室外的访客是否加快向左行走？

2. 该访客是否在 5 秒内完全离开可见画面边缘？


## 136 — `synthetic_scene_046_E1`

**原始英文指令：** At 11.0 seconds, turn the white-shirted visitor in place until their torso faces directly toward the sea.

**中文翻译：** 在第 11.0 秒，让穿白色上衣的访客原地转身，直到其躯干正对大海。

**状态：** 接受

**原子化判定句：**

1. 穿白色上衣的访客是否原地转身？

2. 其躯干最终是否正对大海？


## 137 — `synthetic_scene_046_E2A`

**原始英文指令：** Starting at 28.0 seconds, change the terrace railing from white to matte deep navy over two and a half seconds.

**中文翻译：** 从第 28.0 秒开始，在两点五秒内将露台栏杆由白色变为哑光深海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 露台栏杆是否由白色变为深海军蓝色？

2. 变化后的栏杆是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 138 — `synthetic_scene_046_E2B`

**原始英文指令：** At 24.0 seconds, add a small round light-wood side table on the empty terrace floor beside the deck chair.

**中文翻译：** 在第 24.0 秒，在躺椅旁空置的露台地面上添加一张小型圆形浅色木质边桌。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一张小型圆形浅色木质边桌？

2. 该边桌是否位于躺椅旁空置的露台地面上？


## 139 — `synthetic_scene_047_E1`

**原始英文指令：** At 13.0 seconds, replace the gray-and-red dome tent with a plain dark-green triangular tent in the same ground position.

**中文翻译：** 在第 13.0 秒，将灰红色圆顶帐篷替换为位于相同地面位置的简洁深绿色三角帐篷。

**状态：** 接受

**原子化判定句：**

1. 灰红色圆顶帐篷是否被替换为简洁的深绿色三角帐篷？

2. 替换后的帐篷是否位于与原帐篷相同的地面位置？


## 140 — `synthetic_scene_047_E2A`

**原始英文指令：** At 29.0 seconds, position the front tent two meters left of the shelter entrance with its opening aligned toward the deck.

**中文翻译：** 在第 29.0 秒，将前方帐篷放置在遮棚入口左侧两米处，并使其开口朝向平台。

**状态：** 接受

**原子化判定句：**

1. 前方帐篷是否位于遮棚入口左侧 2 米处？

2. 帐篷开口是否朝向平台？


## 141 — `synthetic_scene_047_E2B`

**原始英文指令：** At 26.0 seconds, remove the wooden bench along the covered deck's front edge and reconstruct the exposed deck boards.

**中文翻译：** 在第 26.0 秒，移除有顶平台前缘沿线的木制长凳，并重建露出的平台木板。

**状态：** 接受

**原子化判定句：**

1. 有顶平台前缘沿线的木制长凳是否被移除？

2. 露出的平台木板是否得到重建？


## 142 — `synthetic_scene_048_E1`

**原始英文指令：** Starting at 12.0 seconds, change the dental chair upholstery from reddish brown to matte cobalt blue over two and a half seconds.

**中文翻译：** 从第 12.0 秒开始，在两点五秒内将牙科椅软包由红棕色变为哑光钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 牙科椅软包是否由红棕色变为钴蓝色？

2. 变化后的软包是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 143 — `synthetic_scene_048_E2A`

**原始英文指令：** Starting at 29.0 seconds, recline the dental chair backrest until it reaches a near-horizontal treatment position.

**中文翻译：** 从第 29.0 秒开始，将牙科椅靠背向后放倒，直到达到接近水平的治疗位置。

**状态：** 接受

**原子化判定句：**

1. 牙科椅靠背是否向后放倒？

2. 靠背是否达到接近水平的治疗位置？


## 144 — `synthetic_scene_048_E2B`

**原始英文指令：** At 25.0 seconds, place the green armchair at the lower right half a meter beside the dental-chair base.

**中文翻译：** 在第 25.0 秒，将右下方的绿色扶手椅放置在牙科椅底座旁半米处。

**状态：** 接受

**原子化判定句：**

1. 右下方的绿色扶手椅是否被放置在牙科椅底座旁 0.5 米处？


## 145 — `synthetic_scene_049_E1`

**原始英文指令：** At 12.0 seconds, move the long white table thirty centimeters right until it is centered parallel to the two rear chairs.

**中文翻译：** 在第 12.0 秒，将白色长桌向右移动三十厘米，直到其相对后方两把椅子居中并保持平行。

**状态：** 接受

**原子化判定句：**

1. 白色长桌是否向右移动了 30 厘米？

2. 该桌子是否相对后方两把椅子居中并保持平行？


## 146 — `synthetic_scene_049_E2A`

**原始英文指令：** Starting at 29.0 seconds, change both visible rear chair backs from dark charcoal to matte burgundy over two and a half seconds.

**中文翻译：** 从第 29.0 秒开始，在两点五秒内将后方两把椅子的可见椅背由深炭灰色变为哑光酒红色。

**状态：** 接受

**原子化判定句：**

1. 后方两把椅子的可见椅背是否都由深炭灰色变为酒红色？

2. 变化后的椅背是否都呈哑光效果？

3. 两处变化是否都在 2.5 秒内完成？


## 147 — `synthetic_scene_049_E2B`

**原始英文指令：** At 25.0 seconds, add a medium leafy plant in the wall-side corner beyond the table's right end, outside the walking lane.

**中文翻译：** 在第 25.0 秒，在桌子右端外侧靠墙的角落、步行通道之外添加一株中型茂叶植物。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一株中型茂叶植物？

2. 该植物是否位于桌子右端外侧靠墙的角落且在步行通道之外？


## 148 — `synthetic_scene_050_E1`

**原始英文指令：** Starting at 16.5 seconds, make the worker walk faster and reach the sewing station's front edge by 19.0 seconds.

**中文翻译：** 从第 16.5 秒开始，让工人加快行走，并在第 19.0 秒前到达缝纫工作台的前缘。

**状态：** 接受

**原子化判定句：**

1. 工人是否加快行走？

2. 工人是否在 2.5 秒内到达缝纫工作台的前缘？


## 149 — `synthetic_scene_050_E2A`

**原始英文指令：** Starting at 29.0 seconds, change the front red fabric roll to matte emerald green over two and a half seconds.

**中文翻译：** 从第 29.0 秒开始，在两点五秒内将前方红色布卷变为哑光祖母绿色。

**状态：** 接受

**原子化判定句：**

1. 前方布卷是否由红色变为祖母绿色？

2. 变化后的布卷是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 150 — `synthetic_scene_050_E2B`

**原始英文指令：** At 31.5 seconds, add a shallow white thread rack on the clear wall above the worktable left of the fabric shelves.

**中文翻译：** 在第 31.5 秒，在布料架左侧工作台上方的空白墙面上添加一个浅型白色线轴架。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个浅型白色线轴架？

2. 该线轴架是否位于工作台上方且布料架左侧的空白墙面上？


## 151 — `synthetic_scene_051_E1`

**原始英文指令：** Starting at 12.0 seconds, transform the complete flower-shop entrance into a restrained gouache illustration with layered paint texture.

**中文翻译：** 从第 12.0 秒开始，将完整的花店入口转换为带分层颜料质感的克制水粉插画。

**状态：** 接受

**原子化判定句：**

1. 完整的花店入口是否转换为克制的水粉插画？

2. 水粉插画是否呈现分层颜料质感？


## 152 — `synthetic_scene_051_E2A`

**原始英文指令：** Starting at 23.0 seconds, split the central large bucket of white flowers into two smaller matching buckets separated by a narrow gap.

**中文翻译：** 从第 23.0 秒开始，将中央装有白花的大花桶分成两个相互匹配的小花桶，并在两者之间留出一道狭窄间隙。

**状态：** 接受

**原子化判定句：**

1. 中央装有白花的大花桶是否被分成两个相互匹配的小花桶？

2. 两个小花桶之间是否留有一道狭窄间隙？


## 153 — `synthetic_scene_051_E2B`

**原始英文指令：** Starting at 25.0 seconds, change the weather outside the open flower-shop entrance to steady moderate rain.

**中文翻译：** 从第 25.0 秒开始，将敞开的花店入口外的天气变为持续的中等强度降雨。

**状态：** 接受

**原子化判定句：**

1. 敞开的花店入口外的天气是否变为持续的中等强度降雨？


## 154 — `synthetic_scene_052_E1`

**原始英文指令：** At 12.0 seconds, move the gray desk telephone to the clear rear-right desk patch beside the lower printer.

**中文翻译：** 在第 12.0 秒，将灰色桌面电话移至下方打印机旁、桌面右后方的空置区域。

**状态：** 接受

**原子化判定句：**

1. 灰色桌面电话是否被移至下方打印机旁、桌面右后方的空置区域？


## 155 — `synthetic_scene_052_E2A`

**原始英文指令：** At 29.0 seconds, add a compact white rolling cabinet on the open floor left-front of the lower printer.

**中文翻译：** 在第 29.0 秒，在下方打印机左前方的空置地面上添加一个小型白色滚轮柜。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型白色滚轮柜？

2. 该滚轮柜是否位于下方打印机左前方的空置地面上？


## 156 — `synthetic_scene_052_E2B`

**原始英文指令：** Starting at 25.0 seconds, change the upper printer housing from medium gray to matte navy blue over two and a half seconds.

**中文翻译：** 从第 25.0 秒开始，在两点五秒内将上方打印机外壳由中灰色变为哑光海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 上方打印机外壳是否由中灰色变为海军蓝色？

2. 变化后的外壳是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 157 — `synthetic_scene_053_E1`

**原始英文指令：** Starting at 13.0 seconds, render only the white seamless backdrop as a layered recycled-paper collage illustration with visible cut edges.

**中文翻译：** 从第 13.0 秒开始，仅将白色无缝背景呈现为分层再生纸拼贴插画，并带有可见的裁切边缘。

**状态：** 接受

**原子化判定句：**

1. 白色无缝背景是否呈现为分层再生纸拼贴插画？

2. 拼贴中是否带有可见的裁切边缘？

3. 风格变化是否仅限于背景？


## 158 — `synthetic_scene_053_E2A`

**原始英文指令：** Starting at 29.0 seconds, increase the right round softbox illumination evenly across the studio backdrop over two and a half seconds.

**中文翻译：** 从第 29.0 秒开始，在两点五秒内均匀增强右侧圆形柔光箱投射在影棚背景上的照明。

**状态：** 接受

**原子化判定句：**

1. 右侧圆形柔光箱投射在影棚背景上的照明是否增强？

2. 增强后的照明是否均匀覆盖背景？

3. 照明变化是否在 2.5 秒内完成？


## 159 — `synthetic_scene_053_E2B`

**原始英文指令：** Starting at 26.0 seconds, change the central tripod stand from matte black to matte cobalt blue over two and a half seconds.

**中文翻译：** 从第 26.0 秒开始，在两点五秒内将中央三脚架由哑光黑色变为哑光钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 中央三脚架是否由哑光黑色变为哑光钴蓝色？

2. 颜色变化是否在 2.5 秒内完成？


## 160 — `synthetic_scene_054_E1`

**原始英文指令：** Starting at 13.0 seconds, lower the complete rightmost oven door beneath the stovetop to a stable halfway-open position.

**中文翻译：** 从第 13.0 秒开始，将炉灶下方最右侧的完整烤箱门向下降至稳定的半开位置。

**状态：** 接受

**原子化判定句：**

1. 炉灶下方最右侧的完整烤箱门是否向下降？

2. 烤箱门是否达到并稳定保持在半开位置？


## 161 — `synthetic_scene_054_E2A`

**原始英文指令：** At 29.0 seconds, center the two metal pots on adjacent burners with exactly one pot-width between them.

**中文翻译：** 在第 29.0 秒，将两个金属锅分别置于相邻炉头中央，并使两者间距恰好为一个锅的宽度。

**状态：** 接受

**原子化判定句：**

1. 两个金属锅是否分别置于相邻炉头中央？

2. 两个锅之间的间距是否恰好为一个锅的宽度？


## 162 — `synthetic_scene_054_E2B`

**原始英文指令：** Starting at 26.0 seconds, change the central kitchen floor tiles from warm tan to cool slate gray over two and a half seconds.

**中文翻译：** 从第 26.0 秒开始，在两点五秒内将厨房中央地砖由暖棕褐色变为冷调板岩灰色。

**状态：** 接受

**原子化判定句：**

1. 厨房中央地砖是否由暖棕褐色变为冷调板岩灰色？

2. 颜色变化是否在 2.5 秒内完成？


## 163 — `synthetic_scene_055_E1`

**原始英文指令：** At 13.0 seconds, center the nearest rolling baking rack one meter beyond the fully visible far long edge of the table.

**中文翻译：** 在第 13.0 秒，将最近的滚轮烘焙架居中放置在完整可见的桌子远侧长边外一米处。

**状态：** 接受

**原子化判定句：**

1. 最近的滚轮烘焙架是否居中位于桌子完整可见的远侧长边之外？

2. 烘焙架是否位于该边缘外 1 米处？


## 164 — `synthetic_scene_055_E2A`

**原始英文指令：** Starting at 29.0 seconds, change the rear cabinet fronts from medium gray to matte sage green over two and a half seconds.

**中文翻译：** 从第 29.0 秒开始，在两点五秒内将后方柜门正面由中灰色变为哑光鼠尾草绿色。

**状态：** 接受

**原子化判定句：**

1. 后方柜门正面是否由中灰色变为鼠尾草绿色？

2. 变化后的柜门正面是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 165 — `synthetic_scene_055_E2B`

**原始英文指令：** Starting at 26.0 seconds, make the bakery worker walk faster toward the visible lower-left frame edge and exit by 31.0 seconds.

**中文翻译：** 从第 26.0 秒开始，让烘焙工人加快朝可见画面左下边缘行走，并在第 31.0 秒前离开画面。

**状态：** 接受

**原子化判定句：**

1. 烘焙工人是否加快朝可见画面左下边缘行走？

2. 该工人是否在 5 秒内离开画面？


## 166 — `synthetic_scene_056_E1`

**原始英文指令：** Starting at 14.0 seconds, make broad slow swells move through the U-shaped dock opening for five seconds.

**中文翻译：** 从第 14.0 秒开始，让宽阔而缓慢的涌浪穿过 U 形码头开口五秒。

**状态：** 接受

**原子化判定句：**

1. 涌浪是否穿过 U 形码头开口？

2. 涌浪是否宽阔且缓慢？

3. 涌浪运动是否持续 5 秒？


## 167 — `synthetic_scene_056_E2A`

**原始英文指令：** Starting at 29.0 seconds, change the U-shaped dock deck from pale beige to matte medium gray over two and a half seconds.

**中文翻译：** 从第 29.0 秒开始，在两点五秒内将 U 形码头甲板由浅米色变为哑光中灰色。

**状态：** 接受

**原子化判定句：**

1. U 形码头甲板是否由浅米色变为中灰色？

2. 变化后的甲板是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 168 — `synthetic_scene_056_E2B`

**原始英文指令：** Starting at 27.0 seconds, freeze the visible marina water into a continuous translucent blue-gray ice sheet over four seconds.

**中文翻译：** 从第 27.0 秒开始，在四秒内将码头内可见的水面冻结成连续的半透明蓝灰色冰层。

**状态：** 接受

**原子化判定句：**

1. 码头内可见的水面是否冻结成冰层？

2. 冰层是否连续、半透明且呈蓝灰色？

3. 冻结过程是否在 4 秒内完成？


## 169 — `synthetic_scene_057_E1`

**原始英文指令：** At 12.0 seconds, replace the dark slatted bench beside the shelter with a pale stone bench in the same footprint.

**中文翻译：** 在第 12.0 秒，将遮棚旁的深色板条长凳替换为占地范围相同的浅色石凳。

**状态：** 接受

**原子化判定句：**

1. 遮棚旁的深色板条长凳是否被替换为浅色石凳？

2. 该石凳是否与原长凳占据相同的地面范围？


## 170 — `synthetic_scene_057_E2A`

**原始英文指令：** Starting at 29.0 seconds, transform the complete tram-platform scene into a restrained architectural watercolor illustration over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内将完整的有轨电车站台场景转换为克制的建筑水彩插画。

**状态：** 接受

**原子化判定句：**

1. 完整的有轨电车站台场景是否转换为克制的建筑水彩插画？

2. 这一转换是否在 3 秒内完成？


## 171 — `synthetic_scene_057_E2B`

**原始英文指令：** At 25.0 seconds, rotate the replacement stone bench 180 degrees until its seating direction faces the station wall.

**中文翻译：** 在第 25.0 秒，将替换后的石凳旋转一百八十度，直到其座位朝向车站墙面。

**状态：** 接受

**原子化判定句：**

1. 替换后的石凳是否旋转 180 度？

2. 其座位方向最终是否朝向车站墙面？


## 172 — `synthetic_scene_058_E1`

**原始英文指令：** Starting at 13.0 seconds, change the information kiosk's unlabelled lower panels to matte deep green over two and a half seconds.

**中文翻译：** 从第 13.0 秒开始，在两点五秒内将信息亭无标签的下部面板变为哑光深绿色。

**状态：** 接受

**原子化判定句：**

1. 信息亭无标签的下部面板是否变为深绿色？

2. 变化后的面板是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 173 — `synthetic_scene_058_E2A`

**原始英文指令：** At 29.0 seconds, remove the wooden bench nearest the lower-left corner and reconstruct the exposed paving.

**中文翻译：** 在第 29.0 秒，移除最靠近左下角的木制长凳，并重建露出的铺装地面。

**状态：** 接受

**原子化判定句：**

1. 最靠近左下角的木制长凳是否被移除？

2. 露出的铺装地面是否得到重建？


## 174 — `synthetic_scene_058_E2B`

**原始英文指令：** At 26.0 seconds, replace the farther wooden bench beside the information kiosk with a plain silver bicycle rack in the same footprint.

**中文翻译：** 在第 26.0 秒，将信息亭旁较远的木制长凳替换为占地范围相同的简洁银色自行车架。

**状态：** 接受

**原子化判定句：**

1. 信息亭旁较远的木制长凳是否被替换为简洁的银色自行车架？

2. 该自行车架是否与原长凳占据相同的地面范围？


## 175 — `synthetic_scene_059_E1`

**原始英文指令：** Starting at 14.0 seconds, transform the complete park walkway and flowerbed scene into a soft chalk-pastel landscape illustration.

**中文翻译：** 从第 14.0 秒开始，将完整的公园步道与花坛场景转换为柔和的粉笔彩绘风景插画。

**状态：** 接受

**原子化判定句：**

1. 完整的公园步道与花坛场景是否转换为柔和的粉笔彩绘风景插画？


## 176 — `synthetic_scene_059_E2A`

**原始英文指令：** Starting at 30.0 seconds, zoom out smoothly to include the confirmed backed bench, complete flowerbed, and approaching visitor route.

**中文翻译：** 从第 30.0 秒开始，平滑拉远镜头，将已确认带靠背的长凳、完整花坛和访客接近的路线纳入画面。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉远并将已确认带靠背的长凳、完整花坛和访客接近的路线纳入画面？

2. 拉远过程是否平滑？


## 177 — `synthetic_scene_059_E2B`

**原始英文指令：** Starting at 27.0 seconds, apply a cool blue evening color grade with gentle contrast to the complete park scene.

**中文翻译：** 从第 27.0 秒开始，为完整的公园场景应用带柔和对比度的冷蓝傍晚色调。

**状态：** 接受

**原子化判定句：**

1. 完整的公园场景是否呈现冷蓝傍晚色调？

2. 调色后的场景是否具有柔和对比度？


## 178 — `synthetic_scene_060_E1`

**原始英文指令：** Starting at 13.0 seconds, apply a warm amber color grade with restrained contrast to the complete service-corridor scene.

**中文翻译：** 从第 13.0 秒开始，为完整的服务通道场景应用带克制对比度的暖琥珀色调。

**状态：** 接受

**原子化判定句：**

1. 完整的服务通道场景是否呈现暖琥珀色调？

2. 调色后的场景是否具有克制对比度？


## 179 — `synthetic_scene_060_E2A`

**原始英文指令：** Starting at 24.0 seconds, make the blue service cart roll steadily forward two meters into the corridor over four seconds.

**中文翻译：** 从第 24.0 秒开始，让蓝色服务推车在四秒内稳定地向通道内前进两米。

**状态：** 接受

**原子化判定句：**

1. 蓝色服务推车是否向通道内前进？

2. 推车运动是否稳定？

3. 推车是否前进 2 米？

4. 这一移动是否在 4 秒内完成？


## 180 — `synthetic_scene_060_E2B`

**原始英文指令：** Starting at 26.0 seconds, render only the visible corridor concrete floor with subtle colored-pencil crosshatching over three seconds.

**中文翻译：** 从第 26.0 秒开始，在三秒内仅将通道内可见的混凝土地面呈现为细腻的彩色铅笔交叉排线效果。

**状态：** 接受

**原子化判定句：**

1. 通道内可见的混凝土地面是否呈现为细腻的彩色铅笔交叉排线效果？

2. 风格变化是否仅限于可见通道地面？

3. 风格变化是否在 3 秒内完成？


## 181 — `synthetic_scene_061_E1`

**原始英文指令：** At 15.0 seconds, center the bench between the large tree bed and waterside railing, parallel to the railing with equal clearance.

**中文翻译：** 在第 15.0 秒，将长凳居中放置在大型树池与水边栏杆之间，使其与栏杆平行并在两侧保留相等间距。

**状态：** 接受

**原子化判定句：**

1. 长凳是否居中位于大型树池与水边栏杆之间？

2. 长凳是否与栏杆平行？

3. 长凳两侧是否保留相等间距？


## 182 — `synthetic_scene_061_E2A`

**原始英文指令：** Starting at 30.0 seconds, render only the complete descending stone steps as a restrained charcoal sketch with visible stone edges.

**中文翻译：** 从第 30.0 秒开始，仅将完整的下行石阶呈现为带清晰石材边缘的克制炭笔素描。

**状态：** 接受

**原子化判定句：**

1. 完整的下行石阶是否呈现为克制的炭笔素描？

2. 石材边缘是否保持清晰可见？

3. 风格变化是否仅限于石阶？


## 183 — `synthetic_scene_061_E2B`

**原始英文指令：** Starting at 27.0 seconds, transform the complete riverside walkway and stair scene into a restrained ink-wash landscape over three seconds.

**中文翻译：** 从第 27.0 秒开始，在三秒内将完整的河边步道与阶梯场景转换为克制的水墨风景画。

**状态：** 接受

**原子化判定句：**

1. 完整的河边步道与阶梯场景是否转换为克制的水墨风景画？

2. 这一转换是否在 3 秒内完成？


## 184 — `synthetic_scene_062_E1`

**原始英文指令：** Starting at 14.5 seconds, change the largest pale foreground rock to muted rust red over two and a half seconds.

**中文翻译：** 从第 14.5 秒开始，在两点五秒内将前景最大的浅色岩石变为低饱和铁锈红色。

**状态：** 接受

**原子化判定句：**

1. 前景最大的浅色岩石是否变为低饱和铁锈红色？

2. 颜色变化是否在 2.5 秒内完成？


## 185 — `synthetic_scene_062_E2A`

**原始英文指令：** Starting at 31.0 seconds, make the visible water patch between the foreground rocks form two broad clockwise surface swirls.

**中文翻译：** 从第 31.0 秒开始，让前景岩石之间的可见水面形成两个宽阔的顺时针表面旋涡。

**状态：** 接受

**原子化判定句：**

1. 前景岩石之间的可见水面是否形成表面旋涡？

2. 是否恰好形成两个宽阔旋涡？

3. 旋涡是否顺时针旋转？


## 186 — `synthetic_scene_062_E2B`

**原始英文指令：** Starting at 27.5 seconds, cast warm directional sunlight across the upper snow ridges while leaving the lake under neutral daylight.

**中文翻译：** 从第 27.5 秒开始，让暖色定向阳光照过上方雪脊，同时让湖面保持在中性日光下。

**状态：** 接受

**原子化判定句：**

1. 暖色定向阳光是否照过上方雪脊？

2. 湖面是否同时保持在中性日光下？


## 187 — `synthetic_scene_063_E1`

**原始英文指令：** Starting at 14.0 seconds, make the right-foreground grass clump beside the wooden boardwalk bend left and recover through three arcs.

**中文翻译：** 从第 14.0 秒开始，让木栈道旁右前景的草丛经过三次弧形运动向左弯曲并恢复。

**状态：** 接受

**原子化判定句：**

1. 木栈道旁右前景的草丛是否向左弯曲后恢复？

2. 草丛是否恰好经过三次弧形运动？


## 188 — `synthetic_scene_063_E2A`

**原始英文指令：** At 29.0 seconds, center the narrow wooden boardwalk between the two front grass clumps with equal visible sand gaps.

**中文翻译：** 在第 29.0 秒，将狭窄木栈道居中放置在前方两丛草之间，使两侧可见沙地间隙相等。

**状态：** 接受

**原子化判定句：**

1. 狭窄木栈道是否居中位于前方两丛草之间？

2. 两侧可见的沙地间隙是否相等？


## 189 — `synthetic_scene_063_E2B`

**原始英文指令：** Starting at 27.0 seconds, make the three front-row grass clumps around the wooden boardwalk bend upper-left and recover together twice.

**中文翻译：** 从第 27.0 秒开始，让木栈道周围前排的三丛草一起朝左上方弯曲并恢复两次。

**状态：** 接受

**原子化判定句：**

1. 木栈道周围前排的三丛草是否都朝左上方弯曲后恢复？

2. 三丛草是否同步运动？

3. 它们是否恰好完成两次弯曲并恢复？


## 190 — `synthetic_scene_064_E1`

**原始英文指令：** At 13.0 seconds, position the small reed clump one root-length from the exposed left tree-root tips along the shoreline.

**中文翻译：** 在第 13.0 秒，将小型芦苇丛放置在岸线沿线、距左侧裸露树根尖端一个树根长度的位置。

**状态：** 接受

**原子化判定句：**

1. 小型芦苇丛是否位于岸线沿线、距左侧裸露树根尖端一个树根长度的位置？


## 191 — `synthetic_scene_064_E2A`

**原始英文指令：** Starting at 31.0 seconds, curl the complete lower broad leaf beside the right roots inward into a visibly cupped form.

**中文翻译：** 从第 31.0 秒开始，将右侧树根旁下方完整的宽叶向内卷曲成明显的杯状。

**状态：** 接受

**原子化判定句：**

1. 右侧树根旁下方完整的宽叶是否向内卷曲？

2. 该叶片是否形成明显的杯状？


## 192 — `synthetic_scene_064_E2B`

**原始英文指令：** Starting at 27.0 seconds, make concentric ripples spread repeatedly across the open water left of the right-side tree roots for five seconds.

**中文翻译：** 从第 27.0 秒开始，让同心波纹在右侧树根左方的开阔水面上反复扩散五秒。

**状态：** 接受

**原子化判定句：**

1. 同心波纹是否在右侧树根左方的开阔水面上反复扩散？

2. 反复扩散是否持续 5 秒？


## 193 — `synthetic_scene_065_E1`

**原始英文指令：** At 15.5 seconds, rotate the stationary blade pattern inside the square wall fan forty-five degrees within the fixed housing.

**中文翻译：** 在第 15.5 秒，将方形壁扇固定外壳内静止的叶片图案旋转四十五度。

**状态：** 接受

**原子化判定句：**

1. 静止的叶片图案是否在方形壁扇的固定外壳内旋转？

2. 旋转角度是否为 45 度？


## 194 — `synthetic_scene_065_E2A`

**原始英文指令：** Starting at 26.0 seconds, make the visible wall-fan blades rotate clockwise through two complete cycles by 29.0 seconds.

**中文翻译：** 从第 26.0 秒开始，让可见的壁扇叶片在第 29.0 秒前顺时针完整旋转两圈。

**状态：** 接受

**原子化判定句：**

1. 可见的壁扇叶片是否顺时针旋转？

2. 叶片是否恰好完成两整圈？

3. 两圈旋转是否在 3 秒内完成？


## 195 — `synthetic_scene_065_E2B`

**原始英文指令：** Starting at 26.0 seconds, make the E1-oriented wall-fan blades rotate counterclockwise twice and stop at their E1 resting angle.

**中文翻译：** 从第 26.0 秒开始，让保持 E1 朝向的壁扇叶片逆时针旋转两圈，并停在其 E1 静止角度。

**状态：** 接受

**原子化判定句：**

1. 保持 E1 朝向的壁扇叶片是否逆时针旋转 2 圈？

2. 叶片随后是否停在其 E1 静止角度？


## 196 — `synthetic_scene_066_E1`

**原始英文指令：** At 15.0 seconds, add a small unlabelled red safety cone on the clear floor before the right cabinet, camera-side of the cable guard.

**中文翻译：** 在第 15.0 秒，在右侧柜子前方、电缆防护条靠镜头一侧的空置地面上添加一个无标签的小型红色安全锥。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个无标签的小型红色安全锥？

2. 该安全锥是否位于右侧柜子前方且电缆防护条靠镜头一侧的空置地面上？


## 197 — `synthetic_scene_066_E2A`

**原始英文指令：** Starting at 27.0 seconds, change the blank lower door of the right equipment cabinet to matte cobalt blue over two and a half seconds.

**中文翻译：** 从第 27.0 秒开始，在两点五秒内将右侧设备柜无标识的下部门板变为哑光钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 右侧设备柜无标识的下部门板是否变为钴蓝色？

2. 变化后的门板是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 198 — `synthetic_scene_066_E2B`

**原始英文指令：** Starting at 27.0 seconds, zoom in smoothly to emphasize the right equipment cabinet, yellow floor boundary, and added red safety cone.

**中文翻译：** 从第 27.0 秒开始，平滑拉近镜头，突出右侧设备柜、黄色地面边界和新增的红色安全锥。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近并突出右侧设备柜、黄色地面边界和新增的红色安全锥？

2. 拉近过程是否平滑？


## 199 — `synthetic_scene_067_E1`

**原始英文指令：** Starting at 14.0 seconds, change the long concrete trough wall from light gray to muted terracotta over two and a half seconds.

**中文翻译：** 从第 14.0 秒开始，在两点五秒内将混凝土长槽壁由浅灰色变为低饱和赤陶色。

**状态：** 接受

**原子化判定句：**

1. 混凝土长槽壁是否由浅灰色变为低饱和赤陶色？

2. 颜色变化是否在 2.5 秒内完成？


## 200 — `synthetic_scene_067_E2A`

**原始英文指令：** At 29.0 seconds, remove the red-brick utility building at the far right and reconstruct the exposed trees and ground.

**中文翻译：** 在第 29.0 秒，移除最右侧的红砖设备建筑，并重建露出的树木和地面。

**状态：** 接受

**原子化判定句：**

1. 最右侧的红砖设备建筑是否被移除？

2. 露出的树木和地面是否得到重建？


## 201 — `synthetic_scene_067_E2B`

**原始英文指令：** At 27.0 seconds, replace the far-right red-brick utility building with a plain light-gray cylindrical storage tank in the same footprint.

**中文翻译：** 在第 27.0 秒，将最右侧的红砖设备建筑替换为占地范围相同的简洁浅灰色圆柱形储罐。

**状态：** 接受

**原子化判定句：**

1. 最右侧的红砖设备建筑是否被替换为简洁的浅灰色圆柱形储罐？

2. 该储罐是否与原建筑占据相同的地面范围？


## 202 — `synthetic_scene_068_E1`

**原始英文指令：** At 13.0 seconds, remove the empty black swivel chair beneath the left control console and reconstruct the exposed carpet.

**中文翻译：** 在第 13.0 秒，移除左侧控制台下方空置的黑色旋转椅，并重建露出的地毯。

**状态：** 接受

**原子化判定句：**

1. 左侧控制台下方空置的黑色旋转椅是否被移除？

2. 露出的地毯是否得到重建？


## 203 — `synthetic_scene_068_E2A`

**原始英文指令：** Starting at 29.0 seconds, change the lower-right bench upholstery from dark blue to matte burgundy over two and a half seconds.

**中文翻译：** 从第 29.0 秒开始，在两点五秒内将右下方长凳软包由深蓝色变为哑光酒红色。

**状态：** 接受

**原子化判定句：**

1. 右下方长凳软包是否由深蓝色变为酒红色？

2. 变化后的软包是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 204 — `synthetic_scene_068_E2B`

**原始英文指令：** Starting at 26.0 seconds, zoom in smoothly to include the full control console, standing occupant, and cleared chair area.

**中文翻译：** 从第 26.0 秒开始，平滑拉近镜头，将完整控制台、站立的人物和清空后的椅子区域纳入画面。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近并将完整控制台、站立的人物和清空后的椅子区域纳入画面？

2. 拉近过程是否平滑？


## 205 — `synthetic_scene_069_E1`

**原始英文指令：** Starting at 14.0 seconds, change the smooth upper-walkway floor from warm brown to uniform matte slate blue.

**中文翻译：** 从第 14.0 秒开始，将光滑的上层步道地面由暖棕色变为均匀的哑光板岩蓝色。

**状态：** 接受

**原子化判定句：**

1. 光滑的上层步道地面是否由暖棕色变为板岩蓝色？

2. 变化后的地面是否均匀呈哑光效果？


## 206 — `synthetic_scene_069_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the far-end lift platform descend half its visible height and rise back once over four seconds.

**中文翻译：** 从第 29.0 秒开始，让远端升降平台在四秒内下降其可见高度的一半，再上升复位一次。

**状态：** 接受

**原子化判定句：**

1. 远端升降平台是否在 4 秒内下降其可见高度的一半？

2. 该平台是否在同一段 4 秒内上升复位一次？


## 207 — `synthetic_scene_069_E2B`

**原始英文指令：** Starting at 27.0 seconds, render only the E1 slate-blue floor as a geometric mosaic illustration with tessellated brushwork.

**中文翻译：** 从第 27.0 秒开始，仅将 E1 中的板岩蓝色地面呈现为带镶嵌笔触的几何马赛克插画。

**状态：** 接受

**原子化判定句：**

1. E1 中的板岩蓝色地面是否呈现为几何马赛克插画？

2. 插画是否带有镶嵌式笔触？

3. 风格变化是否仅限于该地面？


## 208 — `synthetic_scene_070_E1`

**原始英文指令：** At 14.0 seconds, center the two white boxes beneath the overhead hood with exactly one box-width between them.

**中文翻译：** 在第 14.0 秒，将两个白色箱体居中放置在顶部罩体下方，并使两者间距恰好为一个箱体宽度。

**状态：** 接受

**原子化判定句：**

1. 两个白色箱体是否居中位于顶部罩体下方？

2. 两者之间的间距是否恰好为一个箱体宽度？


## 209 — `synthetic_scene_070_E2A`

**原始英文指令：** Starting at 29.0 seconds, increase the cool-white light beneath the overhead hood evenly across both boxes and the steel worktop.

**中文翻译：** 从第 29.0 秒开始，均匀增强顶部罩体下方照射在两个箱体和钢制工作台面上的冷白光。

**状态：** 接受

**原子化判定句：**

1. 顶部罩体下方的冷白光是否在两个箱体上增强？

2. 冷白光是否也在钢制工作台面上增强？

3. 三个表面上的增强照明是否均匀？


## 210 — `synthetic_scene_070_E2B`

**原始英文指令：** Starting at 27.0 seconds, slide the right white box thirty centimeters toward the camera across the fully visible steel worktop.

**中文翻译：** 从第 27.0 秒开始，将右侧白色箱体沿完整可见的钢制工作台面朝镜头滑动三十厘米。

**状态：** 接受

**原子化判定句：**

1. 右侧白色箱体是否沿完整可见的钢制工作台面朝镜头滑动？

2. 移动距离是否为 30 厘米？


## 211 — `synthetic_scene_071_E1`

**原始英文指令：** Starting at 13.0 seconds, accelerate the children's block construction until a stable low wall with a central opening is completed by 18.0 seconds.

**中文翻译：** 从第 13.0 秒开始，加快儿童搭积木的过程，使一堵带中央开口的稳定矮墙在第 18.0 秒前完成。

**状态：** 接受

**原子化判定句：**

1. 儿童搭积木的过程是否加快？

2. 一堵稳定矮墙是否在 5 秒内完成？

3. 完成的矮墙是否带有中央开口？


## 212 — `synthetic_scene_071_E2A`

**原始英文指令：** Starting at 29.0 seconds, render only the wooden storage chest as a terracotta stop-motion clay-animation model over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内仅将木制储物箱呈现为赤陶色定格黏土动画模型。

**状态：** 接受

**原子化判定句：**

1. 木制储物箱是否呈现为赤陶色定格黏土动画模型？

2. 风格变化是否仅限于储物箱？

3. 风格变化是否在 3 秒内完成？


## 213 — `synthetic_scene_071_E2B`

**原始英文指令：** At 27.0 seconds, move the floor lamp upright to a new position fifty centimeters left of the sofa's left arm.

**中文翻译：** 在第 27.0 秒，将落地灯保持直立移至沙发左扶手左侧五十厘米的新位置。

**状态：** 接受

**原子化判定句：**

1. 落地灯是否被移至沙发左扶手左侧？

2. 落地灯最终是否距该扶手 50 厘米？

3. 落地灯是否保持直立？


## 214 — `synthetic_scene_072_E1`

**原始英文指令：** Starting at 14.0 seconds, make four broad concentric wave fronts spread successively across the wet central crosswalk.

**中文翻译：** 从第 14.0 秒开始，让四道宽阔的同心波前依次扩散并越过潮湿的中央人行横道。

**状态：** 接受

**原子化判定句：**

1. 是否恰好出现四道宽阔的同心波前？

2. 波前是否扩散并越过潮湿的中央人行横道？

3. 四道波前是否依次扩散？


## 215 — `synthetic_scene_072_E2A`

**原始英文指令：** Starting at 30.0 seconds, change the weather across the empty street intersection to steady heavy rain over three seconds.

**中文翻译：** 从第 30.0 秒开始，在三秒内将空旷街道交叉口的天气变为持续大雨。

**状态：** 接受

**原子化判定句：**

1. 空旷街道交叉口的天气是否变为持续大雨？

2. 天气变化是否在 3 秒内完成？


## 216 — `synthetic_scene_072_E2B`

**原始英文指令：** Starting at 27.0 seconds, make the lowest overhead utility cable swing gently toward and away from the building through three complete arcs.

**中文翻译：** 从第 27.0 秒开始，让最低的一根架空公用电缆朝建筑靠近再远离，轻柔摆动三个完整弧次。

**状态：** 接受

**原子化判定句：**

1. 最低的一根架空公用电缆是否朝建筑靠近再远离地摆动？

2. 摆动是否轻柔？

3. 电缆是否恰好完成三个完整弧次？


## 217 — `synthetic_scene_073_E1`

**原始英文指令：** Starting at 14.0 seconds, change the weather visible through the large rear windows to steady snowfall over three seconds.

**中文翻译：** 从第 14.0 秒开始，在三秒内将后方大窗外可见的天气变为持续降雪。

**状态：** 接受

**原子化判定句：**

1. 后方大窗外可见的天气是否变为持续降雪？

2. 天气变化是否在 3 秒内完成？


## 218 — `synthetic_scene_073_E2A`

**原始英文指令：** At 30.0 seconds, remove the empty seat at the far-right end of the occupied row and reconstruct the exposed background.

**中文翻译：** 在第 30.0 秒，移除有人座椅排最右端的空座位，并重建露出的背景。

**状态：** 接受

**原子化判定句：**

1. 有人座椅排最右端的空座位是否被移除？

2. 露出的背景是否得到重建？


## 219 — `synthetic_scene_073_E2B`

**原始英文指令：** Starting at 27.0 seconds, change the occupied row's red-brown seat boards and backrests to matte forest green.

**中文翻译：** 从第 27.0 秒开始，将有人座椅排的红棕色座板和靠背变为哑光森林绿色。

**状态：** 接受

**原子化判定句：**

1. 有人座椅排的座板是否由红棕色变为森林绿色？

2. 该座椅排的靠背是否也变为森林绿色？

3. 变化后的表面是否呈哑光效果？


## 220 — `synthetic_scene_074_E1`

**原始英文指令：** Starting at 13.0 seconds, dolly the camera smoothly toward the central queue lanes for four seconds with visible floor and stanchion parallax.

**中文翻译：** 从第 13.0 秒开始，让镜头朝中央排队通道平滑推近四秒，并产生可见的地面与隔离柱视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否朝中央排队通道平滑推近 4 秒？

2. 地面与隔离柱之间是否在同一段 4 秒内产生可见视差？


## 221 — `synthetic_scene_074_E2A`

**原始英文指令：** At 30.0 seconds, align the two inner barrier lines nearest the center counter into a constant two-meter aisle.

**中文翻译：** 在第 30.0 秒，将最靠近中央柜台的两条内侧隔离线调整成宽度恒定为两米的通道。

**状态：** 接受

**原子化判定句：**

1. 最靠近中央柜台的两条内侧隔离线是否对齐形成通道？

2. 通道宽度是否恒定为 2 米？


## 222 — `synthetic_scene_074_E2B`

**原始英文指令：** Starting at 27.0 seconds, zoom out smoothly to include the full counter row, both queue lanes, and the foreground railing.

**中文翻译：** 从第 27.0 秒开始，平滑拉远镜头，将完整柜台排、两条排队通道和前景栏杆纳入画面。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉远并将完整柜台排、两条排队通道和前景栏杆纳入画面？

2. 拉远过程是否平滑？


## 223 — `synthetic_scene_075_E1`

**原始英文指令：** At 14.0 seconds, center the connected boarding gangway within the visible floating-dock opening with equal side clearance.

**中文翻译：** 在第 14.0 秒，将相连的登船舷梯居中放置在可见浮动码头开口内，使两侧间距相等。

**状态：** 接受

**原子化判定句：**

1. 相连的登船舷梯是否居中位于可见浮动码头开口内？

2. 舷梯两侧的间距是否相等？


## 224 — `synthetic_scene_075_E2A`

**原始英文指令：** Starting at 20.5 seconds, make both pedestrians walk faster along the gangway and reach the vessel-side railing by 25.0 seconds.

**中文翻译：** 从第 20.5 秒开始，让两名行人沿舷梯加快行走，并在第 25.0 秒前到达船侧栏杆。

**状态：** 接受

**原子化判定句：**

1. 两名行人是否都沿舷梯加快行走？

2. 两名行人是否都在 4.5 秒内到达船侧栏杆？


## 225 — `synthetic_scene_075_E2B`

**原始英文指令：** Starting at 27.0 seconds, change the broad unlabelled lower hull band from medium blue to deep burgundy over two and a half seconds.

**中文翻译：** 从第 27.0 秒开始，在两点五秒内将船体下部无标签的宽色带由中蓝色变为深酒红色。

**状态：** 接受

**原子化判定句：**

1. 船体下部无标签的宽色带是否由中蓝色变为深酒红色？

2. 颜色变化是否在 2.5 秒内完成？


## 226 — `synthetic_scene_076_E1`

**原始英文指令：** Starting at 14.0 seconds, make both visible branch groups around the central street tree bend right and recover through three synchronized arcs.

**中文翻译：** 从第 14.0 秒开始，让中央行道树周围两组可见树枝经过三次同步弧形运动向右弯曲并恢复。

**状态：** 接受

**原子化判定句：**

1. 中央行道树周围两组可见树枝是否都向右弯曲后恢复？

2. 树枝是否经过恰好三次弧形运动？

3. 两组树枝的弧形运动是否同步？


## 227 — `synthetic_scene_076_E2A`

**原始英文指令：** Starting at 30.0 seconds, change the weather across the market lane to steady moderate rain over three seconds.

**中文翻译：** 从第 30.0 秒开始，在三秒内将市场通道的天气变为持续的中等强度降雨。

**状态：** 接受

**原子化判定句：**

1. 市场通道的天气是否变为持续的中等强度降雨？

2. 天气变化是否在 3 秒内完成？


## 228 — `synthetic_scene_076_E2B`

**原始英文指令：** At 27.0 seconds, move the large lidded pot twenty centimeters left toward the center of its current counter.

**中文翻译：** 在第 27.0 秒，将带盖大锅朝其所在柜台中央向左移动二十厘米。

**状态：** 接受

**原子化判定句：**

1. 带盖大锅是否朝其所在柜台中央向左移动？

2. 移动距离是否为 20 厘米？


## 229 — `synthetic_scene_077_E1`

**原始英文指令：** Starting at 14.0 seconds, zoom in smoothly toward the light-clothed pedestrian and right walkway, with both moving walkways inside the new frame.

**中文翻译：** 从第 14.0 秒开始，朝穿浅色衣服的行人和右侧步道平滑拉近镜头，并使两条自动步道都保留在新画面内。

**状态：** 接受

**原子化判定句：**

1. 镜头是否朝穿浅色衣服的行人和右侧步道平滑拉近？

2. 两条自动步道是否都保留在新画面内？


## 230 — `synthetic_scene_077_E2A`

**原始英文指令：** Starting at 27.0 seconds, make both pedestrians in the far-right passage continue toward the far end at the same steady pace for five seconds.

**中文翻译：** 从第 27.0 秒开始，让最右侧通道内的两名行人以相同的稳定步速继续朝远端行走五秒。

**状态：** 接受

**原子化判定句：**

1. 最右侧通道内的两名行人是否都继续朝远端行走？

2. 两人是否以相同的稳定步速行走？

3. 行走是否持续 5 秒？


## 231 — `synthetic_scene_077_E2B`

**原始英文指令：** Starting at 26.0 seconds, track the camera smoothly forward along the moving-walkway centerline for four seconds with visible rail parallax.

**中文翻译：** 从第 26.0 秒开始，让镜头沿自动步道中心线平滑向前跟拍四秒，并产生可见的栏杆视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿自动步道中心线平滑向前跟拍 4 秒？

2. 是否在同一段 4 秒内产生可见的栏杆视差？


## 232 — `synthetic_scene_078_E1`

**原始英文指令：** At 19.0 seconds, move the largest yellow flower cluster beside the lower path bend to the path's left edge.

**中文翻译：** 在第 19.0 秒，将下方小径弯道旁最大的黄色花簇移至小径左侧边缘。

**状态：** 接受

**原子化判定句：**

1. 下方小径弯道旁最大的黄色花簇是否被移至小径左侧边缘？


## 233 — `synthetic_scene_078_E2A`

**原始英文指令：** Starting at 35.5 seconds, zoom in smoothly until both brown hoofed animals and the nearby path bend fill the central frame.

**中文翻译：** 从第 35.5 秒开始，平滑拉近镜头，直到两只棕色有蹄动物和附近的小径弯道填满画面中央。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑拉近？

2. 拉近后的中央画面是否包含两只棕色有蹄动物？

3. 拉近后的中央画面是否包含附近的小径弯道？

4. 两只动物和附近的小径弯道是否共同填满画面中央？


## 234 — `synthetic_scene_078_E2B`

**原始英文指令：** At 34.0 seconds, position the two brown hoofed animals side by side one body-length apart, both facing left.

**中文翻译：** 在第 34.0 秒，将两只棕色有蹄动物并排放置，彼此相距一个身体长度，并让两者都朝左。

**状态：** 接受

**原子化判定句：**

1. 两只棕色有蹄动物是否并排放置，并彼此相距一个身体长度？

2. 两只动物是否都朝左？


## 235 — `synthetic_scene_079_E1`

**原始英文指令：** Starting at 13.5 seconds, transform the complete forest waterfall and pool scene into a restrained oil painting over three seconds.

**中文翻译：** 从第 13.5 秒开始，在三秒内将完整的森林瀑布与水池场景转换为克制的油画。

**状态：** 接受

**原子化判定句：**

1. 完整的森林瀑布与水池场景是否转换为克制的油画？

2. 这一转换是否在 3 秒内完成？


## 236 — `synthetic_scene_079_E2A`

**原始英文指令：** Starting at 29.0 seconds, make a fuller waterfall stream descend continuously and spread broader ripples across the pool for five seconds.

**中文翻译：** 从第 29.0 秒开始，让更充沛的瀑布水流持续下落五秒，并在水池上扩散出更宽阔的波纹。

**状态：** 接受

**原子化判定句：**

1. 更充沛的瀑布水流是否持续下落 5 秒？

2. 水池上是否在同一段 5 秒内扩散出更宽阔的波纹？


## 237 — `synthetic_scene_079_E2B`

**原始英文指令：** At 27.0 seconds, move the small detached oval stone on the center-foreground ledge thirty centimeters right along the same ledge.

**中文翻译：** 在第 27.0 秒，将中央前景岩台上孤立的椭圆形小石头沿同一岩台向右移动三十厘米。

**状态：** 接受

**原子化判定句：**

1. 中央前景岩台上孤立的椭圆形小石头是否沿同一岩台向右移动？

2. 移动距离是否为 30 厘米？


## 238 — `synthetic_scene_080_E1`

**原始英文指令：** Starting at 14.0 seconds, zoom in smoothly until the central river bend fills the frame between both red-brown cliff edges.

**中文翻译：** 从第 14.0 秒开始，平滑拉近镜头，直到中央河湾填满两侧红棕色悬崖边缘之间的画面。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近，直至中央河湾填满两侧红棕色悬崖边缘之间的画面？

2. 拉近过程是否平滑？


## 239 — `synthetic_scene_080_E2A`

**原始英文指令：** Starting at 29.0 seconds, make a faster current carry elongated ripples continuously through the canyon bend for five seconds.

**中文翻译：** 从第 29.0 秒开始，让更快的水流持续携带细长波纹穿过峡谷弯道五秒。

**状态：** 接受

**原子化判定句：**

1. 水流是否加快并持续 5 秒？

2. 加快的水流是否在同一段 5 秒内持续携带细长波纹穿过峡谷弯道？


## 240 — `synthetic_scene_080_E2B`

**原始英文指令：** Starting at 27.0 seconds, cast a stronger warm shaft of light across the left canyon wall while leaving the right cliff shaded.

**中文翻译：** 从第 27.0 秒开始，让更强的暖色光束照过左侧峡谷壁，同时让右侧悬崖保持在阴影中。

**状态：** 接受

**原子化判定句：**

1. 更强的暖色光束是否照过左侧峡谷壁？

2. 右侧悬崖是否同时保持在阴影中？


## 241 — `synthetic_scene_081_E1`

**原始英文指令：** Starting at 14.0 seconds, transform the complete underwater seabed into a layered watercolor illustration with translucent blue washes over three seconds.

**中文翻译：** 从第 14.0 秒开始，在三秒内将完整的水下海床转换为带半透明蓝色晕染的分层水彩插画。

**状态：** 接受

**原子化判定句：**

1. 完整的水下海床是否在 3 秒内转换为分层水彩插画？

2. 水彩插画是否在同一段 3 秒内呈现半透明蓝色晕染？


## 242 — `synthetic_scene_081_E2A`

**原始英文指令：** Starting at 30.0 seconds, convert the complete underwater scene into a restrained 1970s marine-documentary film look with fine grain.

**中文翻译：** 从第 30.0 秒开始，将完整的水下场景转换为带细腻颗粒的克制 20 世纪 70 年代海洋纪录片胶片风格。

**状态：** 接受

**原子化判定句：**

1. 完整的水下场景是否转换为克制的 20 世纪 70 年代海洋纪录片胶片风格？

2. 转换后的场景是否带有细腻颗粒？


## 243 — `synthetic_scene_081_E2B`

**原始英文指令：** Starting at 27.0 seconds, intensify the blue-white underwater caustic bands moving across the central sand patch over three seconds.

**中文翻译：** 从第 27.0 秒开始，在三秒内增强掠过中央沙地斑块的蓝白色水下焦散光带。

**状态：** 接受

**原子化判定句：**

1. 掠过中央沙地斑块的蓝白色水下焦散光带是否增强？

2. 增强过程是否在 3 秒内完成？


## 244 — `synthetic_scene_082_E1`

**原始英文指令：** Starting at 14.0 seconds, make the suspended spreader beneath the largest left crane rise five meters and lower back once.

**中文翻译：** 从第 14.0 秒开始，让最大左侧起重机下方悬挂的吊具上升五米，再下降复位一次。

**状态：** 接受

**原子化判定句：**

1. 最大左侧起重机下方悬挂的吊具是否上升 5 米？

2. 该吊具随后是否下降复位一次？


## 245 — `synthetic_scene_082_E2A`

**原始英文指令：** Starting at 30.0 seconds, zoom in smoothly to emphasize the largest left crane, its suspended spreader, and the foreground container rows.

**中文翻译：** 从第 30.0 秒开始，平滑拉近镜头，突出最大左侧起重机、其悬挂吊具和前景集装箱排。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近并突出最大左侧起重机、其悬挂吊具和前景集装箱排？

2. 拉近过程是否平滑？


## 246 — `synthetic_scene_082_E2B`

**原始英文指令：** At 27.0 seconds, move the front-row leftmost red container onto the empty top position of the adjacent blue stack.

**中文翻译：** 在第 27.0 秒，将前排最左侧的红色集装箱移至相邻蓝色堆栈顶部的空置位置。

**状态：** 接受

**原子化判定句：**

1. 前排最左侧的红色集装箱是否被移至相邻蓝色堆栈顶部的空置位置？


## 247 — `synthetic_scene_083_E1`

**原始英文指令：** Starting at 14.0 seconds, render only the visible aircraft body, tail, and left wing as a finely carved pale-wood model.

**中文翻译：** 从第 14.0 秒开始，仅将可见的飞机机身、尾部和左翼呈现为雕刻精细的浅色木质模型。

**状态：** 接受

**原子化判定句：**

1. 可见的飞机机身、尾部和左翼是否呈现为浅色木质模型？

2. 模型是否具有精细雕刻细节？

3. 风格变化是否仅限于这些飞机部件？


## 248 — `synthetic_scene_083_E2A`

**原始英文指令：** Starting at 30.0 seconds, change the hangar's unlabelled front door panels from medium gray to matte sage green over two and a half seconds.

**中文翻译：** 从第 30.0 秒开始，在两点五秒内将机库无标签的前门面板由中灰色变为哑光鼠尾草绿色。

**状态：** 接受

**原子化判定句：**

1. 机库无标签的前门面板是否由中灰色变为鼠尾草绿色？

2. 变化后的面板是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 249 — `synthetic_scene_083_E2B`

**原始英文指令：** Starting at 27.0 seconds, smoothly zoom out around the aircraft center until both wingtips and the complete parking box are visible.

**中文翻译：** 从第 27.0 秒开始，以飞机中心为基准平滑拉远镜头，直到两侧翼尖和完整停机框都可见。

**状态：** 接受

**原子化判定句：**

1. 镜头是否以飞机中心为基准平滑拉远？

2. 拉远后飞机两侧翼尖是否都可见？

3. 拉远后完整停机框是否可见？


## 250 — `synthetic_scene_084_E1`

**原始英文指令：** At 14.0 seconds, position the nearest visible turbine base one base diameter from the central service-road fork.

**中文翻译：** 在第 14.0 秒，将最近的可见涡轮机底座放置在距中央维修道路岔口一个底座直径的位置。

**状态：** 接受

**原子化判定句：**

1. 最近的可见涡轮机底座是否位于距中央维修道路岔口一个底座直径的位置？


## 251 — `synthetic_scene_084_E2A`

**原始英文指令：** Starting at 30.0 seconds, make the visible turbine blade tip sweep twice through the upper-left frame edge by 33.0 seconds.

**中文翻译：** 从第 30.0 秒开始，让可见的涡轮叶片尖端在第 33.0 秒前两次掠过画面左上边缘。

**状态：** 接受

**原子化判定句：**

1. 可见的涡轮叶片尖端是否掠过画面左上边缘？

2. 叶片尖端是否恰好掠过两次？

3. 两次掠过是否在 3 秒内完成？


## 252 — `synthetic_scene_084_E2B`

**原始英文指令：** Starting at 27.0 seconds, make broad wind waves travel across the three visible grass fields in synchrony for five seconds.

**中文翻译：** 从第 27.0 秒开始，让宽阔的风浪同步穿过三片可见草地五秒。

**状态：** 接受

**原子化判定句：**

1. 宽阔的风浪是否穿过全部三片可见草地？

2. 三片草地上的风浪是否同步？

3. 这一运动是否持续 5 秒？


## 253 — `synthetic_scene_085_E1`

**原始英文指令：** Starting at 14.0 seconds, split the far-left solar-panel array into two equal rectangular blocks separated by a clear service aisle.

**中文翻译：** 从第 14.0 秒开始，将最左侧太阳能板阵列分成两个大小相等的长方形区块，并以一条清晰的维修通道分隔。

**状态：** 接受

**原子化判定句：**

1. 最左侧太阳能板阵列是否被分成两个大小相等的长方形区块？

2. 两个区块之间是否由一条清晰的维修通道分隔？


## 254 — `synthetic_scene_085_E2A`

**原始英文指令：** At 30.0 seconds, remove the isolated white equipment box behind the central solar arrays and reconstruct the exposed ground.

**中文翻译：** 在第 30.0 秒，移除中央太阳能板阵列后方孤立的白色设备箱，并重建露出的地面。

**状态：** 接受

**原子化判定句：**

1. 中央太阳能板阵列后方孤立的白色设备箱是否被移除？

2. 露出的地面是否得到重建？


## 255 — `synthetic_scene_085_E2B`

**原始英文指令：** Starting at 27.0 seconds, change both E1-split solar-panel blocks from deep blue to matte dark green over two and a half seconds.

**中文翻译：** 从第 27.0 秒开始，在两点五秒内将 E1 中分出的两个太阳能板区块由深蓝色变为哑光深绿色。

**状态：** 接受

**原子化判定句：**

1. E1 中分出的两个太阳能板区块是否都由深蓝色变为深绿色？

2. 变化后的区块是否呈哑光效果？

3. 两处变化是否都在 2.5 秒内完成？


## 256 — `synthetic_scene_086_E1`

**原始英文指令：** Starting at 14.0 seconds, make the open concrete floor around the supported workboat visibly wet with a thin reflective sheen.

**中文翻译：** 从第 14.0 秒开始，让支架上工作艇周围的开阔混凝土地面变得明显湿润，并呈现薄薄的反光光泽。

**状态：** 接受

**原子化判定句：**

1. 支架上工作艇周围的开阔混凝土地面是否变得明显湿润？

2. 湿润地面是否呈现薄薄的反光光泽？


## 257 — `synthetic_scene_086_E2A`

**原始英文指令：** At 30.0 seconds, move the small black cable spool near the lower railing one meter left onto the open concrete.

**中文翻译：** 在第 30.0 秒，将下方栏杆附近的黑色小电缆盘向左移动一米至开阔混凝土地面上。

**状态：** 接受

**原子化判定句：**

1. 下方栏杆附近的黑色小电缆盘是否向左移至开阔混凝土地面上？

2. 移动距离是否为 1 米？


## 258 — `synthetic_scene_086_E2B`

**原始英文指令：** Starting at 27.0 seconds, rotate the workboat and all four support cradles together fifteen degrees clockwise as one rigid group.

**中文翻译：** 从第 27.0 秒开始，将工作艇及全部四个支撑架作为一个刚性整体共同顺时针旋转十五度。

**状态：** 接受

**原子化判定句：**

1. 工作艇及全部四个支撑架是否作为一个刚性整体共同旋转？

2. 该整体是否顺时针旋转？

3. 旋转角度是否为 15 度？


## 259 — `synthetic_scene_087_E1`

**原始英文指令：** At 19.0 seconds, position the white yacht one meter farther from the parallel floating dock with uniform clearance along its side.

**中文翻译：** 在第 19.0 秒，将白色游艇放置到距平行浮动码头再远一米的位置，并使艇侧间距均匀。

**状态：** 接受

**原子化判定句：**

1. 白色游艇是否被放置到距平行浮动码头再远 1 米的位置？

2. 游艇沿其侧面与码头的间距是否均匀？


## 260 — `synthetic_scene_087_E2A`

**原始英文指令：** At 34.0 seconds, turn the blue-clothed pedestrian in place until their torso faces directly toward the marina water.

**中文翻译：** 在第 34.0 秒，让穿蓝色衣服的行人原地转身，直到其躯干正对码头水面。

**状态：** 接受

**原子化判定句：**

1. 穿蓝色衣服的行人是否原地转身？

2. 其躯干最终是否正对码头水面？


## 261 — `synthetic_scene_087_E2B`

**原始英文指令：** Starting at 32.5 seconds, make the two visible foreground grass clumps bend toward the water and recover through three synchronized arcs.

**中文翻译：** 从第 32.5 秒开始，让前景两丛可见的草经过三次同步弧形运动朝水面弯曲并恢复。

**状态：** 接受

**原子化判定句：**

1. 前景两丛可见的草是否都朝水面弯曲后恢复？

2. 草丛是否经过恰好三次弧形运动？

3. 两丛草的弧形运动是否同步？


## 262 — `synthetic_scene_088_E1`

**原始英文指令：** Starting at 14.0 seconds, apply a cool cyan-gray color grade with restrained contrast to the complete mountain-wall scene over three seconds.

**中文翻译：** 从第 14.0 秒开始，在三秒内为完整的山地城墙场景应用带克制对比度的冷调青灰色调。

**状态：** 接受

**原子化判定句：**

1. 完整的山地城墙场景是否呈现冷调青灰色调？

2. 调色后的场景是否具有克制对比度？

3. 调色是否在 3 秒内完成？


## 263 — `synthetic_scene_088_E2A`

**原始英文指令：** Starting at 34.0 seconds, zoom in smoothly until all three later walkers and the left watchtower fill the central frame.

**中文翻译：** 从第 34.0 秒开始，平滑拉近镜头，直到后续出现的三名行人和左侧瞭望塔填满画面中央。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近，直至后续出现的三名行人和左侧瞭望塔填满画面中央？

2. 拉近过程是否平滑？


## 264 — `synthetic_scene_088_E2B`

**原始英文指令：** Starting at 27.0 seconds, transform the complete mountain-wall scene into a restrained architectural watercolor with layered stone and mountain washes.

**中文翻译：** 从第 27.0 秒开始，将完整的山地城墙场景转换为带分层石材和山体晕染的克制建筑水彩画。

**状态：** 接受

**原子化判定句：**

1. 完整的山地城墙场景是否转换为克制的建筑水彩画？

2. 建筑水彩画是否呈现分层石材晕染？

3. 建筑水彩画是否呈现分层山体晕染？


## 265 — `synthetic_scene_089_E1`

**原始英文指令：** At 19.0 seconds, position the largest loose boulder halfway between the grass edge and waterline along the curved gravel shore.

**中文翻译：** 在第 19.0 秒，将最大的松散巨石放置在弯曲砾石岸线上草地边缘与水线之间的中点。

**状态：** 接受

**原子化判定句：**

1. 最大的松散巨石是否位于弯曲砾石岸线上草地边缘与水线之间的中点？


## 266 — `synthetic_scene_089_E2A`

**原始英文指令：** Starting at 34.0 seconds, render only the complete curved gravel shoreline as a dense charcoal drawing over three seconds.

**中文翻译：** 从第 34.0 秒开始，在三秒内仅将完整的弯曲砾石岸线呈现为浓密的炭笔画。

**状态：** 接受

**原子化判定句：**

1. 完整的弯曲砾石岸线是否呈现为浓密的炭笔画？

2. 风格变化是否仅限于岸线？

3. 风格变化是否在 3 秒内完成？


## 267 — `synthetic_scene_089_E2B`

**原始英文指令：** Starting at 32.0 seconds, transform the complete glacial lake and curved shore scene into a restrained layered gouache painting over three seconds.

**中文翻译：** 从第 32.0 秒开始，在三秒内将完整的冰川湖与弯曲岸线场景转换为克制的分层水粉画。

**状态：** 接受

**原子化判定句：**

1. 完整的冰川湖与弯曲岸线场景是否转换为克制的分层水粉画？

2. 这一转换是否在 3 秒内完成？


## 268 — `synthetic_scene_090_E1`

**原始英文指令：** Starting at 14.0 seconds, change the alpine-lake weather to steady light snowfall visible across the slopes and water.

**中文翻译：** 从第 14.0 秒开始，将高山湖天气变为持续小雪，使降雪在山坡和水面上清晰可见。

**状态：** 接受

**原子化判定句：**

1. 高山湖天气是否变为持续小雪？

2. 降雪是否在山坡和水面上清晰可见？


## 269 — `synthetic_scene_090_E2A`

**原始英文指令：** Starting at 31.0 seconds, zoom in smoothly on the lake center and complete snow-peak cluster between both mountain slopes.

**中文翻译：** 从第 31.0 秒开始，平滑拉近镜头，聚焦于两侧山坡之间的湖心和完整雪峰群。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近并聚焦于两侧山坡之间的湖心和完整雪峰群？

2. 拉近过程是否平滑？


## 270 — `synthetic_scene_090_E2B`

**原始英文指令：** Starting at 27.0 seconds, dolly the camera smoothly toward the lake for four seconds with visible shrub, shore-rock, and mountain parallax.

**中文翻译：** 从第 27.0 秒开始，让镜头朝湖面平滑推近四秒，并产生可见的灌木、岸石和山体视差。

**状态：** 接受

**原子化判定句：**

1. 镜头是否朝湖面平滑推近 4 秒？

2. 灌木、岸石和山体之间是否在同一段 4 秒内产生可见视差？


## 271 — `synthetic_scene_091_E1`

**原始英文指令：** Starting at 14.0 seconds, make the single visible yellow scissor lift roll one meter right and stop parallel to the rear wall.

**中文翻译：** 从第 14.0 秒开始，让唯一可见的黄色剪叉式升降机向右移动一米，并停在与后墙平行的位置。

**状态：** 接受

**原子化判定句：**

1. 唯一可见的黄色剪叉式升降机是否向右移动 1 米？

2. 该升降机是否停在与后墙平行的位置？


## 272 — `synthetic_scene_091_E2A`

**原始英文指令：** Starting at 22.0 seconds, make all three workers stop on the open hangar floor for three seconds, then resume walking right.

**中文翻译：** 从第 22.0 秒开始，让三名工人在开阔的机库地面上停留三秒，然后继续向右行走。

**状态：** 接受

**原子化判定句：**

1. 三名工人是否都在开阔的机库地面上停留 3 秒？

2. 三名工人是否都在停留 3 秒后继续向右行走？


## 273 — `synthetic_scene_091_E2B`

**原始英文指令：** Starting at 27.0 seconds, spread a bounded thin water film two meters outward from beneath the aircraft nose across the concrete floor.

**中文翻译：** 从第 27.0 秒开始，让一层边界明确的薄水膜从飞机机头下方向外扩展两米，覆盖混凝土地面。

**状态：** 接受

**原子化判定句：**

1. 水膜是否从飞机机头下方向外扩展并覆盖混凝土地面？

2. 水膜是否薄且边界明确？

3. 水膜是否向外扩展 2 米？


## 274 — `synthetic_scene_092_E1`

**原始英文指令：** Starting at 13.0 seconds, make the blue-clothed pedestrian stop beside the planting bed for three seconds, then resume walking lower-right.

**中文翻译：** 从第 13.0 秒开始，让穿蓝色衣服的行人在种植池旁停留三秒，然后继续向右下方行走。

**状态：** 接受

**原子化判定句：**

1. 穿蓝色衣服的行人是否在种植池旁停留 3 秒？

2. 该行人是否在停留 3 秒后继续向右下方行走？


## 275 — `synthetic_scene_092_E2A`

**原始英文指令：** Starting at 29.0 seconds, make three visible pedestrians in the rear plaza walk toward the bridge entrance at the same steady pace.

**中文翻译：** 从第 29.0 秒开始，让后方广场上三名可见行人以相同的稳定步速朝桥梁入口行走。

**状态：** 接受

**原子化判定句：**

1. 后方广场上是否恰好有三名可见行人朝桥梁入口行走？

2. 三人是否以相同的稳定步速行走？


## 276 — `synthetic_scene_092_E2B`

**原始英文指令：** At 27.0 seconds, center the nearest black litter bin between the water edge and planting bed with equal clear gaps.

**中文翻译：** 在第 27.0 秒，将最近的黑色垃圾桶居中放置在水边与种植池之间，使两侧留出相等的空隙。

**状态：** 接受

**原子化判定句：**

1. 最近的黑色垃圾桶是否居中位于水边与种植池之间？

2. 垃圾桶两侧的空隙是否相等？


## 277 — `synthetic_scene_093_E1`

**原始英文指令：** Starting at 14.0 seconds, cast a broad warm sunlight band across the central atrium floor and lower bookshelf fronts over three seconds.

**中文翻译：** 从第 14.0 秒开始，在三秒内让一道宽阔的暖色阳光带照过中庭中央地面和书架下部正面。

**状态：** 接受

**原子化判定句：**

1. 一道宽阔的暖色阳光带是否照过中庭中央地面？

2. 阳光带是否也照到书架下部正面？

3. 照明变化是否在 3 秒内完成？


## 278 — `synthetic_scene_093_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the single rear-left curtain panel billow inward and settle through two complete cycles.

**中文翻译：** 从第 29.0 秒开始，让后方左侧唯一一幅窗帘向内鼓起再落稳，共完成两个完整周期。

**状态：** 接受

**原子化判定句：**

1. 后方左侧唯一一幅窗帘是否向内鼓起后落稳？

2. 窗帘是否恰好完成两个完整周期？


## 279 — `synthetic_scene_093_E2B`

**原始英文指令：** Starting at 27.0 seconds, change the long planter border beneath the left windows to matte terracotta over two and a half seconds.

**中文翻译：** 从第 27.0 秒开始，在两点五秒内将左侧窗户下方的长花池边框变为哑光赤陶色。

**状态：** 接受

**原子化判定句：**

1. 左侧窗户下方的长花池边框是否变为赤陶色？

2. 变化后的边框是否呈哑光效果？

3. 这一变化是否在 2.5 秒内完成？


## 280 — `synthetic_scene_094_E1`

**原始英文指令：** Starting at 8.0 seconds, make the three visible promenade pedestrians continue right at the same steady pace for two seconds.

**中文翻译：** 从第 8.0 秒开始，让滨海步道上三名可见行人以相同的稳定步速继续向右行走两秒。

**状态：** 接受

**原子化判定句：**

1. 滨海步道上是否恰好有三名可见行人继续向右行走？

2. 三人是否以相同的稳定步速行走？

3. 行走是否持续 2 秒？


## 281 — `synthetic_scene_094_E2A`

**原始英文指令：** At 30.0 seconds, replace the small tree in the central rectangular planter with a compact flowering cherry tree.

**中文翻译：** 在第 30.0 秒，将中央长方形花池中的小树替换为一株小型开花樱花树。

**状态：** 接受

**原子化判定句：**

1. 中央长方形花池中的小树是否被替换为一株小型开花樱花树？


## 282 — `synthetic_scene_094_E2B`

**原始英文指令：** At 22.5 seconds, remove the empty cafe chair nearest the promenade edge and reconstruct the exposed paving behind it.

**中文翻译：** 在第 22.5 秒，移除最靠近滨海步道边缘的空置咖啡椅，并重建其后方露出的铺装地面。

**状态：** 接受

**原子化判定句：**

1. 最靠近滨海步道边缘的空置咖啡椅是否被移除？

2. 被移除椅子后方露出的铺装地面是否得到重建？


## 283 — `synthetic_scene_095_E1`

**原始英文指令：** At 14.0 seconds, remove the slim dark lamp post beside the central paved square and reconstruct the exposed background.

**中文翻译：** 在第 14.0 秒，移除中央铺装广场旁细长的深色灯柱，并重建露出的背景。

**状态：** 接受

**原子化判定句：**

1. 中央铺装广场旁细长的深色灯柱是否被移除？

2. 露出的背景是否得到重建？


## 284 — `synthetic_scene_095_E2A`

**原始英文指令：** Starting at 29.0 seconds, render only the central square as a hand-painted herringbone-stone illustration with muted brush texture.

**中文翻译：** 从第 29.0 秒开始，仅将中央广场呈现为带低调笔触质感的手绘人字形石材插画。

**状态：** 接受

**原子化判定句：**

1. 中央广场是否呈现为手绘人字形石材插画？

2. 插画是否具有低调的笔触质感？

3. 风格变化是否仅限于中央广场？


## 285 — `synthetic_scene_095_E2B`

**原始英文指令：** At 27.0 seconds, replace the small courtyard tree left of the seated person with a low plain stone fountain.

**中文翻译：** 在第 27.0 秒，将坐着的人物左侧的庭院小树替换为低矮简洁的石质喷泉。

**状态：** 接受

**原子化判定句：**

1. 坐着的人物左侧的庭院小树是否被替换为低矮简洁的石质喷泉？


## 286 — `synthetic_scene_096_E1`

**原始英文指令：** Starting at 13.0 seconds, make both visible ducks swim faster right and clear the channel edge together by 18.0 seconds.

**中文翻译：** 从第 13.0 秒开始，让两只可见鸭子加快向右游动，并在第 18.0 秒前一起越过水道边缘。

**状态：** 接受

**原子化判定句：**

1. 两只可见鸭子是否都加快向右游动？

2. 两只鸭子是否在 5 秒内一起越过水道边缘？


## 287 — `synthetic_scene_096_E2A`

**原始英文指令：** At 33.0 seconds, position the later green-headed duck midway between the upper and lower reed banks with equal water clearance.

**中文翻译：** 在第 33.0 秒，将后续出现的绿头鸭放置在上下芦苇岸之间的中点，并使两侧水面间距相等。

**状态：** 接受

**原子化判定句：**

1. 后续出现的绿头鸭是否位于上下芦苇岸之间的中点，并使两侧水面间距相等？


## 288 — `synthetic_scene_096_E2B`

**原始英文指令：** Starting at 27.0 seconds, transform the complete reed-lined wetland channel into a soft chalk-pastel landscape over three seconds.

**中文翻译：** 从第 27.0 秒开始，在三秒内将完整的芦苇水道湿地场景转换为柔和的粉笔彩绘风景画。

**状态：** 接受

**原子化判定句：**

1. 完整的芦苇水道湿地场景是否转换为柔和的粉笔彩绘风景画？

2. 这一转换是否在 3 秒内完成？


## 289 — `synthetic_scene_097_E1`

**原始英文指令：** Starting at 14.0 seconds, transform the complete forest stream and dry bank into a restrained ink-and-watercolor woodland illustration over three seconds.

**中文翻译：** 从第 14.0 秒开始，在三秒内将完整的森林溪流与干燥河岸转换为克制的水墨与水彩林地插画。

**状态：** 接受

**原子化判定句：**

1. 完整的森林溪流与干燥河岸是否转换为克制的水墨与水彩林地插画？

2. 这一转换是否在 3 秒内完成？


## 290 — `synthetic_scene_097_E2A`

**原始英文指令：** At 30.5 seconds, move the clearly visible red fox to the unobstructed center of the dry bank with all four feet supported.

**中文翻译：** 在第 30.5 秒，将清晰可见的赤狐移至干燥河岸无遮挡的中央，并让四只脚都得到支撑。

**状态：** 接受

**原子化判定句：**

1. 清晰可见的赤狐是否被移至干燥河岸无遮挡的中央？

2. 赤狐的四只脚是否都得到支撑？


## 291 — `synthetic_scene_097_E2B`

**原始英文指令：** At 27.0 seconds, position the visible red fox one body-length from the stream edge with its body parallel to the waterline.

**中文翻译：** 在第 27.0 秒，将可见赤狐放置在距溪流边缘一个身体长度的位置，并使其身体与水线平行。

**状态：** 接受

**原子化判定句：**

1. 可见赤狐是否位于距溪流边缘一个身体长度的位置？

2. 赤狐的身体是否与水线平行？


## 292 — `synthetic_scene_098_E1`

**原始英文指令：** At 14.0 seconds, position the two seagulls side by side one body-length apart on the dry sand, both facing right.

**中文翻译：** 在第 14.0 秒，将两只海鸥并排放置在干沙上，彼此相距一个身体长度，并让两者都朝右。

**状态：** 接受

**原子化判定句：**

1. 两只海鸥是否并排位于干沙上，并彼此相距一个身体长度？

2. 两只海鸥是否都朝右？


## 293 — `synthetic_scene_098_E2A`

**原始英文指令：** At 29.0 seconds, move the leading seagull from the right rock to the center of the open dry-sand strip.

**中文翻译：** 在第 29.0 秒，将领先的海鸥从右侧岩石移至开阔干沙带的中央。

**状态：** 接受

**原子化判定句：**

1. 领先的海鸥是否从右侧岩石移至开阔干沙带的中央？


## 294 — `synthetic_scene_098_E2B`

**原始英文指令：** Starting at 27.0 seconds, make both visible gulls walk faster and reach the right-side rock boundary together by 33.0 seconds.

**中文翻译：** 从第 27.0 秒开始，让两只可见海鸥加快行走，并在第 33.0 秒前一起到达右侧岩石边界。

**状态：** 接受

**原子化判定句：**

1. 两只可见海鸥是否都加快行走？

2. 两只海鸥是否在 6 秒内一起到达右侧岩石边界？


## 295 — `synthetic_scene_099_E1`

**原始英文指令：** Starting at 14.0 seconds, render only the central grass-valley floor with fine muted-green colored-pencil crosshatching over three seconds.

**中文翻译：** 从第 14.0 秒开始，在三秒内仅将中央草谷地面呈现为精细的低饱和绿色彩铅交叉排线效果。

**状态：** 接受

**原子化判定句：**

1. 中央草谷地面是否呈现为精细的低饱和绿色彩铅交叉排线效果？

2. 风格变化是否仅限于中央草谷地面？

3. 风格变化是否在 3 秒内完成？


## 296 — `synthetic_scene_099_E2A`

**原始英文指令：** At 24.0 seconds, position the two brown horses side by side two body-lengths apart on the central slope, both facing right.

**中文翻译：** 在第 24.0 秒，将两匹棕色马并排放置在中央山坡上，彼此相距两个身体长度，并让两匹马都朝右。

**状态：** 接受

**原子化判定句：**

1. 两匹棕色马是否并排位于中央山坡上，并彼此相距两个身体长度？

2. 两匹马是否都朝右？


## 297 — `synthetic_scene_099_E2B`

**原始英文指令：** Starting at 27.5 seconds, make both visible horses walk faster and clear the right frame edge together by 33.0 seconds.

**中文翻译：** 从第 27.5 秒开始，让两匹可见的马加快行走，并在第 33.0 秒前一起越过画面右边缘。

**状态：** 接受

**原子化判定句：**

1. 两匹可见的马是否都加快行走？

2. 两匹马是否在 5.5 秒内一起越过画面右边缘？


## 298 — `synthetic_scene_100_E1`

**原始英文指令：** Starting at 14.0 seconds, change the narrow footbridge slabs from pale beige-gray to muted brick red over two and a half seconds.

**中文翻译：** 从第 14.0 秒开始，在两点五秒内将狭窄人行桥的桥面板由浅米灰色变为低饱和砖红色。

**状态：** 接受

**原子化判定句：**

1. 狭窄人行桥的桥面板是否由浅米灰色变为低饱和砖红色？

2. 颜色变化是否在 2.5 秒内完成？


## 299 — `synthetic_scene_100_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the three nearest vegetable rows bend toward the irrigation channel and recover through three synchronized waves.

**中文翻译：** 从第 29.0 秒开始，让最近的三排蔬菜经过三次同步波动朝灌溉渠弯曲并恢复。

**状态：** 接受

**原子化判定句：**

1. 最近的三排蔬菜是否都朝灌溉渠弯曲后恢复？

2. 它们是否经过恰好三次波动？

3. 三排蔬菜的波动是否同步？


## 300 — `synthetic_scene_100_E2B`

**原始英文指令：** Starting at 27.0 seconds, make the visible gray-green-clothed walker turn around and walk left along the same path for five seconds.

**中文翻译：** 从第 27.0 秒开始，让可见的灰绿色衣人物转身，并沿同一条小径向左行走五秒。

**状态：** 接受

**原子化判定句：**

1. 可见的灰绿色衣人物是否转身？

2. 此人物随后是否沿同一条小径向左行走 5 秒？
