# 全量编辑指令原子化结果——embodied_edit_records_test_100.md——中文审阅版

- 源记录数：300

- 所有原子判定句均依据 `atom_results/README.md` 逐条人工审核。

- 原子判定句省略作为截取起点的绝对时间；后续时间点均已换算为片段内相对时间。


## 001 — `embodied_001_E1`

**原始英文指令：** At 15.0 seconds, replace the milk carton with a clear handled storage jug in the same task location.

**中文翻译：** 在第 15.0 秒，将牛奶纸盒替换为一个带透明把手的储物壶，并将其放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 牛奶纸盒是否被替换为一个带透明把手的储物壶？

2. 替换后的储物壶是否位于牛奶纸盒原本所在的任务位置？


## 002 — `embodied_001_E2A`

**原始英文指令：** At 30.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during pouring milk into the cereal bowl.

**中文翻译：** 在第 30.0 秒，在把牛奶倒入麦片碗时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 是否将牛奶倒入麦片碗？

2. 在倒牛奶时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 003 — `embodied_001_E2B`

**原始英文指令：** At 30.0 seconds, make the exterior of the yellow bowl visibly chilled with a thin, even condensation layer for the rest of the visible scene.

**中文翻译：** 在第 30.0 秒，使黄色碗的外表面呈现明显冰凉的状态，并带有一层薄而均匀的冷凝水，且该状态保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 黄色碗的外表面是否呈现明显冰凉的状态并出现一层薄冷凝水？

2. 冷凝水层在碗的可见外表面上是否分布均匀？

3. 冰凉且带冷凝水的外观是否保持至可见场景结束？


## 004 — `embodied_003_E1`

**原始英文指令：** Starting at 9.0 seconds, steer the embodied vehicle along the inside edge of the visible left bend for four seconds.

**中文翻译：** 从第 9.0 秒开始，操纵第一人称载具沿可见左弯道的内侧边缘行驶四秒。

**状态：** 接受

**原子化判定句：**

1. 第一人称载具是否沿可见左弯道行驶？

2. 载具是否沿弯道的内侧边缘行驶？

3. 该行驶过程是否持续 4 秒？


## 005 — `embodied_003_E2A`

**原始英文指令：** Starting at 30.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the right-side white car over 4 seconds.

**中文翻译：** 从第 30.0 秒开始，在四秒内将第一人称视点朝右侧白色汽车方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 4 秒内向右移动半米？

2. 第一人称视点是否在同一段 4 秒内降低二十五厘米？

3. 视点是否朝右侧的白色汽车方向移动？


## 006 — `embodied_003_E2B`

**原始英文指令：** Starting at 24.0 seconds, make the white car decelerate smoothly in its current lane and fall one car length farther behind over four seconds.

**中文翻译：** 从第 24.0 秒开始，让白色汽车在当前车道内平稳减速，并在四秒内再落后一个车身长度。

**状态：** 接受

**原子化判定句：**

1. 白色汽车是否平稳减速并持续 4 秒？

2. 白色汽车在减速时是否保持在当前车道内？

3. 白色汽车是否在同一段 4 秒内再落后一个车身长度？


## 007 — `embodied_006_E1`

**原始英文指令：** At 14.0 seconds, change the non-text surfaces of the transparent glass to matte cobalt blue for the rest of the scene.

**中文翻译：** 在第 14.0 秒，将透明玻璃上不含文字的表面变为哑光钴蓝色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 透明玻璃上不含文字的表面是否变为钴蓝色？

2. 发生变化的表面是否呈哑光质感？

3. 哑光钴蓝色外观是否保持至场景结束？


## 008 — `embodied_006_E2A`

**原始英文指令：** At 34.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during carrying the cup between the table and sink.

**中文翻译：** 在第 34.0 秒，在桌子与水槽之间搬运杯子时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 杯子是否在桌子与水槽之间被搬运？

2. 在搬运杯子时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 009 — `embodied_006_E2B`

**原始英文指令：** Starting at 29.0 seconds, lean the trunk twenty centimeters toward the white cooking pot over two seconds, then return over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将躯干朝白色烹饪锅倾斜二十厘米，然后用两秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝白色烹饪锅倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内回到原位？


## 010 — `embodied_010_E1`

**原始英文指令：** At 10.0 seconds, make the flask exterior visibly chilled with a thin, even condensation layer for the rest of its visible scene.

**中文翻译：** 在第 10.0 秒，使烧瓶外表面呈现明显冰凉的状态，并带有一层薄而均匀的冷凝水，且该状态保持至烧瓶可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 烧瓶外表面是否呈现明显冰凉的状态并出现一层薄冷凝水？

2. 冷凝水层在烧瓶的可见外表面上是否分布均匀？

3. 冰凉且带冷凝水的外观是否保持至烧瓶可见场景结束？


## 011 — `embodied_010_E2A`

**原始英文指令：** Starting at 36.0 seconds, lean the trunk twenty centimeters toward the black apparatus knob over 2 seconds, then return along the same path over 2 seconds.

**中文翻译：** 从第 36.0 秒开始，在两秒内将躯干朝黑色仪器旋钮倾斜二十厘米，然后用两秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝黑色仪器旋钮倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内沿原路径返回？


## 012 — `embodied_010_E2B`

**原始英文指令：** Starting at 25.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the fixed glass apparatus over four seconds.

**中文翻译：** 从第 25.0 秒开始，在四秒内将第一人称视点朝固定玻璃仪器方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 4 秒内向右移动半米？

2. 第一人称视点是否在同一段 4 秒内降低二十五厘米？

3. 视点是否朝固定玻璃仪器方向移动？


## 013 — `embodied_013_E1`

**原始英文指令：** At 13.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during rotating and rinsing the yellow bowl.

**中文翻译：** 在第 13.0 秒，在转动并冲洗黄色碗时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 黄色碗是否被转动？

2. 黄色碗是否被冲洗？

3. 在转动并冲洗黄色碗时，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 014 — `embodied_013_E2A`

**原始英文指令：** At 28.0 seconds, render only the visible hands and forearms with cel-shaded game-character treatment during scrubbing a metal utensil with the sponge.

**中文翻译：** 在第 28.0 秒，在用海绵擦洗金属器具时，仅将可见的双手和前臂渲染为卡通渲染的游戏角色风格。

**状态：** 接受

**原子化判定句：**

1. 是否使用海绵擦洗金属器具？

2. 在擦洗过程中，可见的双手和前臂是否被渲染为卡通渲染的游戏角色风格？

3. 卡通渲染效果是否仅作用于可见的双手和前臂？


## 015 — `embodied_013_E2B`

**原始英文指令：** At 28.0 seconds, make the green sponge visibly saturated with dense white foam for the rest of the visible scene.

**中文翻译：** 在第 28.0 秒，使绿色海绵明显浸满浓密的白色泡沫，并保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 绿色海绵是否明显浸满浓密的白色泡沫？

2. 浸满泡沫的外观是否保持至可见场景结束？


## 016 — `embodied_014_E1`

**原始英文指令：** Starting at 10.0 seconds, use the left hand to lift and rotate the long-bone model along a smooth rising inspection arc over four seconds.

**中文翻译：** 从第 10.0 秒开始，用左手在四秒内沿平滑上升的观察弧线抬起并转动长骨模型。

**状态：** 接受

**原子化判定句：**

1. 左手是否抬起长骨模型？

2. 左手是否在抬起长骨模型的同时转动它？

3. 抬起和转动动作是否沿平滑上升的观察弧线进行，并在 4 秒内完成？


## 017 — `embodied_014_E2A`

**原始英文指令：** At 30.0 seconds, position the probe-holding right wrist in the lower-right frame quadrant.

**中文翻译：** 在第 30.0 秒，将握持探针的右手腕放置在画面右下象限。

**状态：** 接受

**原子化判定句：**

1. 握持探针的右手腕是否被放置在画面右下象限？


## 018 — `embodied_014_E2B`

**原始英文指令：** At 25.0 seconds, replace the model shaft with a transparent acrylic anatomical shaft model in the same task location.

**中文翻译：** 在第 25.0 秒，将模型骨干替换为透明的亚克力解剖骨干模型，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 模型骨干是否被替换为透明的亚克力解剖骨干模型？

2. 替换后的亚克力骨干模型是否位于原模型骨干所在的任务位置？


## 019 — `embodied_015_E1`

**原始英文指令：** Starting at 19.0 seconds, lean the trunk twenty centimeters toward the vegetable counter over two seconds, then return over two seconds.

**中文翻译：** 从第 19.0 秒开始，在两秒内将躯干朝蔬菜柜台倾斜二十厘米，然后用两秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝蔬菜柜台倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内回到原位？


## 020 — `embodied_015_E2A`

**原始英文指令：** At 30.0 seconds, remove the yellow pepper completely from the visible scene during displaying and arranging the colored peppers on the counter.

**中文翻译：** 在第 30.0 秒，在展示并摆放柜台上的彩椒时，将黄色甜椒从可见场景中完全移除。

**状态：** 接受

**原子化判定句：**

1. 彩椒是否在柜台上被展示？

2. 彩椒是否在柜台上被摆放？

3. 在展示并摆放彩椒时，黄色甜椒是否从可见场景中被完全移除？


## 021 — `embodied_015_E2B`

**原始英文指令：** Starting at 30.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the yellow pepper over 4 seconds.

**中文翻译：** 从第 30.0 秒开始，在四秒内将第一人称视点朝黄色甜椒方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 4 秒内向右移动半米？

2. 第一人称视点是否在同一段 4 秒内降低二十五厘米？

3. 视点是否朝黄色甜椒方向移动？


## 022 — `embodied_016_E1`

**原始英文指令：** At 12.0 seconds, pause the initial head-oval and guide-line drawing for three seconds, then resume from the same visible state at 15.0 seconds.

**中文翻译：** 在第 12.0 秒，暂停头部椭圆和辅助线的初始绘制三秒，然后在第 15.0 秒从相同的可见状态继续绘制。

**状态：** 接受

**原子化判定句：**

1. 头部椭圆和辅助线的初始绘制是否暂停 3 秒？

2. 绘制是否在 3 秒后恢复？

3. 绘制是否从暂停时相同的可见状态继续？


## 023 — `embodied_016_E2A`

**原始英文指令：** At 30.0 seconds, position the drawing pencil tip exactly at the visible intersection of the jawline and neck contour.

**中文翻译：** 在第 30.0 秒，将绘图铅笔的笔尖准确放置在下颌线与颈部轮廓线的可见交点上。

**状态：** 接受

**原子化判定句：**

1. 绘图铅笔的笔尖是否被准确放置在下颌线与颈部轮廓线的可见交点上？


## 024 — `embodied_016_E2B`

**原始英文指令：** Starting at 27.0 seconds, perform a two-second optical push-in to a stable close-up centered on the drawn jaw and neck.

**中文翻译：** 从第 27.0 秒开始，进行一次持续两秒的光学推进，最终形成以画出的下颌和颈部为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以画出的下颌和颈部为中心的稳定特写？


## 025 — `embodied_017_E1`

**原始英文指令：** Starting at 19.0 seconds, perform a two-second optical push-in to a stable close-up centered on the handheld probe.

**中文翻译：** 从第 19.0 秒开始，进行一次持续两秒的光学推进，最终形成以手持探针为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以手持探针为中心的稳定特写？


## 026 — `embodied_017_E2A`

**原始英文指令：** At 35.0 seconds, replace the red taillight with a same-size smoked-red LED taillight unit in the same task location.

**中文翻译：** 在第 35.0 秒，将红色尾灯替换为一个同样大小的烟熏红色 LED 尾灯单元，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 红色尾灯是否被替换为烟熏红色 LED 尾灯单元？

2. 替换后的尾灯是否与原红色尾灯大小相同？

3. 替换后的尾灯是否位于原尾灯所在的任务位置？


## 027 — `embodied_017_E2B`

**原始英文指令：** Starting at 34.0 seconds, trace the taillight-to-bumper seam with one smooth left-to-right hand sweep over four seconds.

**中文翻译：** 从第 34.0 秒开始，用手在四秒内从左向右平滑扫过一次，沿尾灯与保险杠之间的接缝描划。

**状态：** 接受

**原子化判定句：**

1. 手是否沿尾灯与保险杠之间的接缝完成描划？

2. 描划是否通过一次从左向右的平滑扫动完成？

3. 描划是否在 4 秒内完成？


## 028 — `embodied_019_E1`

**原始英文指令：** At 19.0 seconds, apply a high-contrast monochrome graphic treatment across the full visible scene.

**中文翻译：** 在第 19.0 秒，为整个可见场景应用高对比度的单色图形化效果。

**状态：** 接受

**原子化判定句：**

1. 整个可见场景是否应用单色图形化效果？

2. 该单色图形化效果是否具有高对比度？


## 029 — `embodied_019_E2A`

**原始英文指令：** Starting at 26.0 seconds, perform a two-second optical push-in to a stable close-up centered on the cartoon worker.

**中文翻译：** 从第 26.0 秒开始，进行一次持续两秒的光学推进，最终形成以卡通工人为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以卡通工人为中心的稳定特写？


## 030 — `embodied_019_E2B`

**原始英文指令：** At 34.0 seconds, render only the white canvas areas surrounding the safety graphics as lightly textured recycled paper.

**中文翻译：** 在第 34.0 秒，仅将安全图形周围的白色画布区域渲染为带有轻微纹理的再生纸。

**状态：** 接受

**原子化判定句：**

1. 安全图形周围的白色画布区域是否被渲染为带有轻微纹理的再生纸？

2. 再生纸渲染是否仅作用于这些白色画布区域？


## 031 — `embodied_025_E1`

**原始英文指令：** Starting at 19.0 seconds, smooth the newly added clay along the figure's torso side seam in one clockwise hand pass over four seconds.

**中文翻译：** 从第 19.0 秒开始，用手沿人物躯干侧缝顺时针扫过一次，在四秒内抹平新添加的黏土。

**状态：** 接受

**原子化判定句：**

1. 新增黏土是否沿人物躯干侧缝被抹平？

2. 抹平是否通过一次顺时针手部扫动完成？

3. 抹平是否在 4 秒内完成？


## 032 — `embodied_025_E2A`

**原始英文指令：** At 30.0 seconds, position the right index fingertip two centimeters to the right of the figure's waist.

**中文翻译：** 在第 30.0 秒，将右手食指指尖放在人物腰部右侧两厘米处。

**状态：** 接受

**原子化判定句：**

1. 右手食指指尖是否被放在人物腰部右侧两厘米处？


## 033 — `embodied_025_E2B`

**原始英文指令：** At 34.0 seconds, replace the visible metal sculpting tool with a blue-handled precision tool in the same task position.

**中文翻译：** 在第 34.0 秒，将可见的金属雕塑工具替换为一件蓝色手柄的精密工具，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 可见的金属雕塑工具是否被替换为一件蓝色手柄的精密工具？

2. 替换后的工具是否位于原金属雕塑工具所在的任务位置？


## 034 — `embodied_026_E1`

**原始英文指令：** Starting at 14.0 seconds, point first to the white shredded ingredient bowl and then to the dark dairy bowl over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内先指向装有白色碎料的碗，再指向深色乳制品碗。

**状态：** 接受

**原子化判定句：**

1. 是否先指向装有白色碎料的碗？

2. 是否随后指向深色乳制品碗，并在 2 秒内完成整个指示顺序？


## 035 — `embodied_026_E2A`

**原始英文指令：** At 32.0 seconds, make the exterior of the glass mixing bowl visibly chilled with a thin, even condensation layer for the rest of the visible scene.

**中文翻译：** 在第 32.0 秒，使玻璃搅拌碗的外表面呈现明显冰凉的状态，并带有一层薄而均匀的冷凝水，且该状态保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 玻璃搅拌碗的外表面是否呈现明显冰凉的状态并出现一层薄冷凝水？

2. 冷凝水层在碗的可见外表面上是否分布均匀？

3. 冰凉且带冷凝水的外观是否保持至可见场景结束？


## 036 — `embodied_026_E2B`

**原始英文指令：** At 29.0 seconds, place the glass mixing bowl directly left of the white shredded-ingredient bowl with a half-bowl-width gap.

**中文翻译：** 在第 29.0 秒，将玻璃搅拌碗放在白色碎料碗的正左侧，两碗之间留出半个碗宽的间距。

**状态：** 接受

**原子化判定句：**

1. 玻璃搅拌碗是否被放在白色碎料碗的正左侧？

2. 两个碗之间是否留有半个碗宽的间距？


## 037 — `embodied_027_E1`

**原始英文指令：** At 19.0 seconds, position the visible pointing index fingertip two centimeters above the silver coin group below the deposit bag.

**中文翻译：** 在第 19.0 秒，将可见的指示食指指尖放在存款袋下方银币组上方两厘米处。

**状态：** 接受

**原子化判定句：**

1. 可见的指示食指指尖是否被放在存款袋下方银币组上方两厘米处？


## 038 — `embodied_027_E2A`

**原始英文指令：** At 35.0 seconds, render the full visible scene as a restrained watercolor illustration during rotating the small silver coin near the arranged group.

**中文翻译：** 在第 35.0 秒，在转动已排列硬币组附近的小银币时，将整个可见场景渲染为色彩克制的水彩插画。

**状态：** 接受

**原子化判定句：**

1. 已排列硬币组附近的小银币是否被转动？

2. 在转动该硬币时，整个可见场景是否被渲染为色彩克制的水彩插画？


## 039 — `embodied_027_E2B`

**原始英文指令：** At 34.0 seconds, change the non-text surfaces of the arranged coin group to satin forest green for the rest of the scene.

**中文翻译：** 在第 34.0 秒，将已排列硬币组上不含文字的表面变为缎面森林绿色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 已排列硬币组上不含文字的表面是否变为森林绿色？

2. 发生变化的表面是否呈缎面质感？

3. 缎面森林绿色外观是否保持至场景结束？


## 040 — `embodied_028_E1`

**原始英文指令：** At 18.0 seconds, split the isolated light-gray piece outside the board's right edge into two equal fragments placed side by side with a clear gap.

**中文翻译：** 在第 18.0 秒，将棋盘右边缘外侧孤立的浅灰色块拆分为两个大小相等的碎片，并排放置且留有清晰间隙。

**状态：** 接受

**原子化判定句：**

1. 棋盘右边缘外侧孤立的浅灰色块是否被拆分为两个碎片？

2. 两个碎片的大小是否相等？

3. 两个碎片是否并排放置？

4. 两个碎片之间是否留有清晰间隙？


## 041 — `embodied_028_E2A`

**原始英文指令：** Starting at 33.0 seconds, perform a two-second optical push-in to a stable close-up centered on the partially completed puzzle.

**中文翻译：** 从第 33.0 秒开始，进行一次持续两秒的光学推进，最终形成以部分完成的拼图为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以部分完成的拼图为中心的稳定特写？


## 042 — `embodied_028_E2B`

**原始英文指令：** At 33.0 seconds, change only the unprinted white puzzle-board surface around the loose pieces to soft coral red.

**中文翻译：** 在第 33.0 秒，仅将散落拼块周围未印刷的白色拼图板表面变为柔和的珊瑚红色。

**状态：** 接受

**原子化判定句：**

1. 散落拼块周围未印刷的白色拼图板表面是否变为柔和的珊瑚红色？

2. 颜色变化是否仅作用于该未印刷的白色表面？


## 043 — `embodied_030_E1`

**原始英文指令：** At 18.0 seconds, change the non-text surfaces of the transparent phone case to matte cobalt blue for the rest of the scene.

**中文翻译：** 在第 18.0 秒，将透明手机壳上不含文字的表面变为哑光钴蓝色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 透明手机壳上不含文字的表面是否变为钴蓝色？

2. 发生变化的表面是否呈哑光质感？

3. 哑光钴蓝色外观是否保持至场景结束？


## 044 — `embodied_030_E2A`

**原始英文指令：** Starting at 32.0 seconds, pinch the film's upper-right corner and peel it from the smartphone along one smooth rising arc over four seconds.

**中文翻译：** 从第 32.0 秒开始，捏住保护膜的右上角，并沿一条平滑上升的弧线在四秒内将其从智能手机上揭下。

**状态：** 接受

**原子化判定句：**

1. 保护膜的右上角是否被捏住？

2. 保护膜是否随后从智能手机上被揭下？

3. 揭膜动作是否沿一条平滑上升的弧线进行，并在 4 秒内完成？


## 045 — `embodied_030_E2B`

**原始英文指令：** At 33.0 seconds, place the active right hand in the lower-right frame quadrant, one palm-width from the protective film.

**中文翻译：** 在第 33.0 秒，将正在操作的右手放在画面右下象限，并与保护膜相距一个手掌宽。

**状态：** 接受

**原子化判定句：**

1. 正在操作的右手是否被放在画面右下象限？

2. 右手与保护膜之间是否相距一个手掌宽？


## 046 — `embodied_032_E1`

**原始英文指令：** At 14.0 seconds, place the smartphone directly below the sound-level meter with a one-phone-width vertical gap.

**中文翻译：** 在第 14.0 秒，将智能手机放在声级计正下方，两者之间留出一个手机宽的垂直间距。

**状态：** 接受

**原子化判定句：**

1. 智能手机是否被放在声级计正下方？

2. 智能手机与声级计之间是否留有一个手机宽的垂直间距？


## 047 — `embodied_032_E2A`

**原始英文指令：** Starting at 33.0 seconds, move the right hand from above the smartphone toward the sound-level meter along a rightward arc over three seconds.

**中文翻译：** 从第 33.0 秒开始，让右手从智能手机上方向声级计移动，并在三秒内沿一条向右的弧线完成动作。

**状态：** 接受

**原子化判定句：**

1. 右手是否从智能手机上方向声级计移动？

2. 右手是否沿一条向右的弧线移动？

3. 该移动是否在 3 秒内完成？


## 048 — `embodied_032_E2B`

**原始英文指令：** Starting at 29.0 seconds, perform a two-second optical push-in to a stable close-up centered on the white phone stand.

**中文翻译：** 从第 29.0 秒开始，进行一次持续两秒的光学推进，最终形成以白色手机支架为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以白色手机支架为中心的稳定特写？


## 049 — `embodied_033_E1`

**原始英文指令：** Starting at 17.0 seconds, lean the trunk twenty centimeters toward the wooden cargo shelf over two seconds, then return over two seconds.

**中文翻译：** 从第 17.0 秒开始，在两秒内将躯干朝木制货物架倾斜二十厘米，然后用两秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝木制货物架倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内回到原位？


## 050 — `embodied_033_E2A`

**原始英文指令：** Starting at 30.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the stacked storage bins over 4 seconds.

**中文翻译：** 从第 30.0 秒开始，在四秒内将第一人称视点朝堆叠的储物箱方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 4 秒内向右移动半米？

2. 第一人称视点是否在同一段 4 秒内降低二十五厘米？

3. 视点是否朝堆叠的储物箱方向移动？


## 051 — `embodied_033_E2B`

**原始英文指令：** At 28.0 seconds, position the visible left index fingertip two centimeters above the open tailgate's inner edge.

**中文翻译：** 在第 28.0 秒，将可见的左手食指指尖放在打开的尾门内侧边缘上方两厘米处。

**状态：** 接受

**原子化判定句：**

1. 可见的左手食指指尖是否被放在打开的尾门内侧边缘上方两厘米处？


## 052 — `embodied_035_E1`

**原始英文指令：** At 13.0 seconds, split the crochet fabric into equal left and right panels with a clear gap, leaving the active loop attached to the right panel.

**中文翻译：** 在第 13.0 秒，将钩针织物拆分为大小相等的左右两片，中间留出清晰间隙，并让活动线圈继续连接在右片上。

**状态：** 接受

**原子化判定句：**

1. 钩针织物是否被拆分为左右两片？

2. 左右两片的大小是否相等？

3. 两片之间是否留有清晰间隙？

4. 活动线圈是否仍连接在右片上？


## 053 — `embodied_035_E2A`

**原始英文指令：** At 28.0 seconds, position the entire connected blue-gray crochet fabric in the left third of the tabletop.

**中文翻译：** 在第 28.0 秒，将整块相连的蓝灰色钩针织物放在桌面的左侧三分之一区域。

**状态：** 接受

**原子化判定句：**

1. 整块相连的蓝灰色钩针织物是否被放在桌面的左侧三分之一区域？


## 054 — `embodied_035_E2B`

**原始英文指令：** Starting at 28.0 seconds, pull the right panel's active yarn loop through its next stitch along a wider hook-guided arc over four seconds.

**中文翻译：** 从第 28.0 秒开始，在四秒内沿较宽的钩针引导弧线，将右片的活动线圈穿过下一个针目。

**状态：** 接受

**原子化判定句：**

1. 右片的活动线圈是否被拉过下一个针目？

2. 线圈是否沿较宽的钩针引导弧线移动，并在 4 秒内完成？


## 055 — `embodied_039_E1`

**原始英文指令：** At 19.0 seconds, add one small stainless-steel prep bowl on the empty rear-right stovetop area beside the heated pan.

**中文翻译：** 在第 19.0 秒，在加热锅旁边空置的炉灶右后区域添加一个小型不锈钢备料碗。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型不锈钢备料碗？

2. 备料碗是否被放在加热锅旁边空置的炉灶右后区域？


## 056 — `embodied_039_E2A`

**原始英文指令：** At 34.0 seconds, illuminate the visible working area with soft neutral overhead light at an even exposure during adding herbs and chopped ingredients to a cooking pan.

**中文翻译：** 在第 34.0 秒，在向烹饪锅中加入香草和切碎食材时，用柔和的中性顶光均匀照亮可见工作区域。

**状态：** 接受

**原子化判定句：**

1. 香草是否被加入烹饪锅？

2. 切碎的食材是否被加入烹饪锅？

3. 在加入香草和切碎食材时，可见工作区域是否受到柔和中性顶光的均匀照明？


## 057 — `embodied_039_E2B`

**原始英文指令：** At 34.0 seconds, coat the exposed upper inner wall of the heated pan with thick, visibly textured orange-brown sauce residue.

**中文翻译：** 在第 34.0 秒，使加热锅暴露的上部内壁覆盖一层厚实、纹理明显的橙褐色酱汁残留物。

**状态：** 接受

**原子化判定句：**

1. 加热锅暴露的上部内壁是否覆盖有橙褐色酱汁残留物？

2. 酱汁残留物是否厚实且纹理明显？


## 058 — `embodied_040_E1`

**原始英文指令：** Starting at 15.0 seconds, make the small rodent roll upright and travel smoothly toward the entering orange food scoop over three seconds.

**中文翻译：** 从第 15.0 秒开始，让小型啮齿动物翻滚至直立状态，并在三秒内平稳地朝正在进入画面的橙色食物铲移动。

**状态：** 接受

**原子化判定句：**

1. 小型啮齿动物是否翻滚至直立状态？

2. 直立后，啮齿动物是否平稳地朝正在进入画面的橙色食物铲移动，并在 3 秒内完成？


## 059 — `embodied_040_E2A`

**原始英文指令：** At 33.0 seconds, add one shallow ceramic treat dish on the wooden surface immediately to the orange food scoop's right.

**中文翻译：** 在第 33.0 秒，在橙色食物铲正右侧的木质表面上添加一个浅陶瓷零食盘。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个浅陶瓷零食盘？

2. 零食盘是否被放在橙色食物铲正右侧的木质表面上？


## 060 — `embodied_040_E2B`

**原始英文指令：** At 30.0 seconds, change the red cue stick's non-text surfaces to deep violet when the stick next appears near 40.0 seconds.

**中文翻译：** 在第 30.0 秒进行编辑，并在红色球杆于接近第 40.0 秒再次出现时，将其不含文字的表面变为深紫色。

**状态：** 接受

**原子化判定句：**

1. 红色球杆是否在片段开始约 10 秒后再次出现？

2. 球杆再次出现时，其不含文字的表面是否变为深紫色？


## 061 — `embodied_045_E1`

**原始英文指令：** At 18.0 seconds, illuminate the visible working area with soft neutral overhead light at an even exposure during presenting ingredients and slicing garlic.

**中文翻译：** 在第 18.0 秒，在展示食材和切蒜时，用柔和的中性顶光均匀照亮可见工作区域。

**状态：** 接受

**原子化判定句：**

1. 食材是否被展示？

2. 大蒜是否被切片？

3. 在展示食材和切蒜时，可见工作区域是否受到柔和中性顶光的均匀照明？


## 062 — `embodied_045_E2A`

**原始英文指令：** At 33.0 seconds, add one small stainless-steel prep bowl on the cutting board immediately above and left of the sliced garlic.

**中文翻译：** 在第 33.0 秒，在切片大蒜左上方紧邻的砧板位置添加一个小型不锈钢备料碗。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型不锈钢备料碗？

2. 备料碗是否被放在切片大蒜左上方紧邻的砧板位置？


## 063 — `embodied_045_E2B`

**原始英文指令：** At 33.0 seconds, make the exterior of the white bowl visibly chilled with a thin, even condensation layer for the rest of the visible scene.

**中文翻译：** 在第 33.0 秒，使白色碗的外表面呈现明显冰凉的状态，并带有一层薄而均匀的冷凝水，且该状态保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 白色碗的外表面是否呈现明显冰凉的状态并出现一层薄冷凝水？

2. 冷凝水层在碗的可见外表面上是否分布均匀？

3. 冰凉且带冷凝水的外观是否保持至可见场景结束？


## 064 — `embodied_048_E1`

**原始英文指令：** At 17.0 seconds, make the exposed outer wall of the small metal pot water-repellent so remaining moisture forms beads that roll away.

**中文翻译：** 在第 17.0 秒，使小金属锅暴露的外壁具有拒水性，让剩余水分形成水珠并滚落。

**状态：** 接受

**原子化判定句：**

1. 小金属锅暴露的外壁是否变得具有拒水性？

2. 剩余水分是否在锅的外壁上形成水珠？

3. 形成的水珠是否滚落？


## 065 — `embodied_048_E2A`

**原始英文指令：** Starting at 32.0 seconds, lean the trunk twenty centimeters toward the metal lid over 2 seconds, then return along the same path over 2 seconds.

**中文翻译：** 从第 32.0 秒开始，在两秒内将躯干朝金属锅盖倾斜二十厘米，然后用两秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝金属锅盖倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内沿原路径返回？


## 066 — `embodied_048_E2B`

**原始英文指令：** Starting at 32.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the lower cabinet over 4 seconds.

**中文翻译：** 从第 32.0 秒开始，在四秒内将第一人称视点朝下层橱柜方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 4 秒内向右移动半米？

2. 第一人称视点是否在同一段 4 秒内降低二十五厘米？

3. 视点是否朝下层橱柜方向移动？


## 067 — `embodied_049_E1`

**原始英文指令：** At 15.0 seconds, make the wet coffee-pot part water-repellent so visible droplets bead and roll off immediately.

**中文翻译：** 在第 15.0 秒，使咖啡壶的湿润部件具有拒水性，让可见水滴聚成水珠并立即滚落。

**状态：** 接受

**原子化判定句：**

1. 咖啡壶的湿润部件是否变得具有拒水性？

2. 可见水滴是否在该部件上聚成水珠？

3. 形成的水珠是否立即滚落？


## 068 — `embodied_049_E2A`

**原始英文指令：** Starting at 34.0 seconds, lean the trunk twenty centimeters toward the striped cloth over 2 seconds, then return along the same path over 2 seconds.

**中文翻译：** 从第 34.0 秒开始，在两秒内将躯干朝条纹布倾斜二十厘米，然后用两秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝条纹布倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内沿原路径返回？


## 069 — `embodied_049_E2B`

**原始英文指令：** Starting at 30.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the striped cloth over three seconds.

**中文翻译：** 从第 30.0 秒开始，在三秒内将第一人称视点朝条纹布方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 3 秒内向右移动半米？

2. 第一人称视点是否在同一段 3 秒内降低二十五厘米？

3. 视点是否朝条纹布方向移动？


## 070 — `embodied_051_E1`

**原始英文指令：** At 19.0 seconds, illuminate the visible courtyard work area with soft overcast daylight at an even exposure.

**中文翻译：** 在第 19.0 秒，用柔和的阴天日光以均匀曝光照亮可见的庭院工作区。

**状态：** 接受

**原子化判定句：**

1. 是否使用柔和的阴天日光照明？

2. 可见的庭院工作区是否均匀受到照明？


## 071 — `embodied_051_E2A`

**原始英文指令：** At 33.0 seconds, add one shallow ceramic treat dish on the concrete immediately left of the white plastic basin.

**中文翻译：** 在第 33.0 秒，在白色塑料盆正左侧的混凝土地面上添加一个浅陶瓷零食盘。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个浅陶瓷零食盘？

2. 零食盘是否被放在白色塑料盆正左侧的混凝土地面上？


## 072 — `embodied_051_E2B`

**原始英文指令：** At 34.0 seconds, orient the small mottled lizard toward frame-left with its head leading along its body axis.

**中文翻译：** 在第 34.0 秒，将小型斑驳蜥蜴朝向画面左侧，并让头部沿身体轴线位于前方。

**状态：** 接受

**原子化判定句：**

1. 小型斑驳蜥蜴是否朝向画面左侧？

2. 蜥蜴的头部是否沿身体轴线位于前方？


## 073 — `embodied_052_E1`

**原始英文指令：** Starting at 9.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the empty dark frying pan over three seconds.

**中文翻译：** 从第 9.0 秒开始，在三秒内将第一人称视点朝空的深色平底锅方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 3 秒内向右移动半米？

2. 第一人称视点是否在同一段 3 秒内降低二十五厘米？

3. 视点是否朝空的深色平底锅方向移动？


## 074 — `embodied_052_E2A`

**原始英文指令：** At 42.0 seconds, make the exterior of the small seasoning jar visibly chilled with a thin, even condensation layer for the rest of the visible scene.

**中文翻译：** 在第 42.0 秒，使小调味罐的外表面呈现明显冰凉的状态，并带有一层薄而均匀的冷凝水，且该状态保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 小调味罐的外表面是否呈现明显冰凉的状态并出现一层薄冷凝水？

2. 冷凝水层在调味罐的可见外表面上是否分布均匀？

3. 冰凉且带冷凝水的外观是否保持至可见场景结束？


## 075 — `embodied_052_E2B`

**原始英文指令：** Starting at 24.0 seconds, lean the trunk twenty centimeters toward the open utensil drawer over 1.5 seconds, then return over 1.5 seconds.

**中文翻译：** 从第 24.0 秒开始，在 1.5 秒内将躯干朝打开的餐具抽屉倾斜二十厘米，然后用 1.5 秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 1.5 秒内朝打开的餐具抽屉倾斜二十厘米？

2. 躯干是否随后在接下来的 1.5 秒内回到原位？


## 076 — `embodied_053_E1`

**原始英文指令：** At 15.0 seconds, change the non-text surface of the blue pen barrel to matte emerald green for the rest of the scene.

**中文翻译：** 在第 15.0 秒，将蓝色笔杆上不含文字的表面变为哑光祖母绿色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 蓝色笔杆上不含文字的表面是否变为祖母绿色？

2. 发生变化的表面是否呈哑光质感？

3. 哑光祖母绿色外观是否保持至场景结束？


## 077 — `embodied_053_E2A`

**原始英文指令：** Starting at 30.0 seconds, guide the blue pen around the smaller silver coin in a wider clockwise comparison pass over 4 seconds.

**中文翻译：** 从第 30.0 秒开始，引导蓝色笔围绕较小的银币进行一次更宽的顺时针对比扫动，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 蓝色笔是否围绕较小的银币完成一次对比扫动？

2. 该扫动是否为顺时针方向？

3. 该扫动的幅度是否更宽？

4. 该扫动是否在 4 秒内完成？


## 078 — `embodied_053_E2B`

**原始英文指令：** At 30.0 seconds, position the pen tip in the lower-left frame quadrant, one centimeter left of the smaller coin.

**中文翻译：** 在第 30.0 秒，将笔尖放在画面左下象限，并位于较小硬币左侧一厘米处。

**状态：** 接受

**原子化判定句：**

1. 笔尖是否被放在画面左下象限？

2. 笔尖是否位于较小硬币左侧一厘米处？


## 079 — `embodied_056_E1`

**原始英文指令：** At 17.0 seconds, position the nearest visible gloved index fingertip two centimeters above the green-coated panel.

**中文翻译：** 在第 17.0 秒，将最近的可见戴手套食指指尖放在绿色涂层面板上方两厘米处。

**状态：** 接受

**原子化判定句：**

1. 最近的可见戴手套食指指尖是否被放在绿色涂层面板上方两厘米处？


## 080 — `embodied_056_E2A`

**原始英文指令：** At 34.0 seconds, replace the white perforated template with a same-size aluminum perforated alignment stencil in the same task location.

**中文翻译：** 在第 34.0 秒，将白色穿孔模板替换为一个同样大小的铝制穿孔对齐模板，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 白色穿孔模板是否被替换为铝制穿孔对齐模板？

2. 替换后的模板是否与原白色模板大小相同？

3. 替换后的模板是否位于原白色模板所在的任务位置？


## 081 — `embodied_056_E2B`

**原始英文指令：** Starting at 32.0 seconds, trace the upper-left template holes with the pointed tool in a wider clockwise inspection pass over four seconds.

**中文翻译：** 从第 32.0 秒开始，用尖头工具沿左上方模板孔进行一次更宽的顺时针检查扫动，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 尖头工具是否沿左上方模板孔描划？

2. 描划是否采用一次更宽的顺时针检查扫动，并在 4 秒内完成？


## 082 — `embodied_057_E1`

**原始英文指令：** At 16.0 seconds, add one sealed clear collection vial lying flat on the visible upper-right rim of the black water tub.

**中文翻译：** 在第 16.0 秒，在黑色水槽可见的右上边缘添加一个密封透明的收集瓶，并使其平放。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个密封透明的收集瓶？

2. 收集瓶是否平放？

3. 收集瓶是否位于黑色水槽可见的右上边缘？


## 083 — `embodied_057_E2A`

**原始英文指令：** Starting at 31.0 seconds, make the water in the black tub circulate clockwise in one visible current for 4 seconds during rotating the pan as gravel concentrates along the grooves.

**中文翻译：** 从第 31.0 秒开始，在转动淘洗盘、砂砾沿沟槽聚集时，让黑色水槽中的水形成一股可见的顺时针水流并循环四秒。

**状态：** 接受

**原子化判定句：**

1. 淘洗盘是否被转动？

2. 转动淘洗盘时，砂砾是否沿沟槽聚集？

3. 在这些动作期间，黑色水槽中的水是否形成一股可见的顺时针水流并循环 4 秒？


## 084 — `embodied_057_E2B`

**原始英文指令：** At 31.0 seconds, position the entire concentrated dark gravel patch in the left third of the pan floor, one patch-width below the riffles.

**中文翻译：** 在第 31.0 秒，将整片聚集的深色砂砾放在淘洗盘底部左侧三分之一区域，并位于凸条下方一个砂砾斑块宽的位置。

**状态：** 接受

**原子化判定句：**

1. 整片聚集的深色砂砾是否被放在淘洗盘底部左侧三分之一区域？

2. 砂砾斑块是否位于凸条下方一个斑块宽的位置？


## 085 — `embodied_058_E1`

**原始英文指令：** At 19.0 seconds, position the held partially painted miniature figure in the left third of the frame at its current working depth.

**中文翻译：** 在第 19.0 秒，将手持的半成品上色微缩人偶放在画面左侧三分之一区域，并保持当前工作景深。

**状态：** 接受

**原子化判定句：**

1. 手持的半成品上色微缩人偶是否被放在画面左侧三分之一区域？

2. 该微缩人偶是否保持当前工作景深？


## 086 — `embodied_058_E2A`

**原始英文指令：** At 32.0 seconds, change the non-text surfaces of the brown cape to matte cobalt blue for the rest of the scene.

**中文翻译：** 在第 32.0 秒，将棕色斗篷上不含文字的表面变为哑光钴蓝色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 棕色斗篷上不含文字的表面是否变为钴蓝色？

2. 发生变化的表面是否呈哑光质感？

3. 哑光钴蓝色外观是否保持至场景结束？


## 087 — `embodied_058_E2B`

**原始英文指令：** Starting at 34.0 seconds, paint one continuous diagonal stroke along the visible right cape fold over three seconds.

**中文翻译：** 从第 34.0 秒开始，沿可见的斗篷右侧褶皱画出一条连续的对角线笔触，并在三秒内完成。

**状态：** 接受

**原子化判定句：**

1. 是否沿可见的斗篷右侧褶皱画出一条连续笔触？

2. 该笔触是否呈对角线方向？

3. 该笔触是否在 3 秒内完成？


## 088 — `embodied_059_E1`

**原始英文指令：** Starting at 15.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the partially opened dairy package over three seconds.

**中文翻译：** 从第 15.0 秒开始，在三秒内将第一人称视点朝部分打开的乳制品包装方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 3 秒内向右移动半米？

2. 第一人称视点是否在同一段 3 秒内降低二十五厘米？

3. 视点是否朝部分打开的乳制品包装方向移动？


## 089 — `embodied_059_E2A`

**原始英文指令：** At 30.0 seconds, make the deformed package opening rigid and self-supporting in its current open shape for the rest of the visible scene.

**中文翻译：** 在第 30.0 秒，使变形的包装开口变得刚硬，并能自行维持当前张开的形状，且保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 变形的包装开口是否变得刚硬？

2. 该开口是否能自行维持当前张开的形状？

3. 刚硬且能自我支撑的张开形状是否保持至可见场景结束？


## 090 — `embodied_059_E2B`

**原始英文指令：** Starting at 30.0 seconds, lean the trunk twenty centimeters toward the deformed package opening over 2 seconds, then return along the same path over 2 seconds.

**中文翻译：** 从第 30.0 秒开始，在两秒内将躯干朝变形的包装开口倾斜二十厘米，然后用两秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝变形的包装开口倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内沿原路径返回？


## 091 — `embodied_061_E1`

**原始英文指令：** Starting at 17.0 seconds, lean the trunk twenty centimeters toward the black frying pan over 2 seconds, then return along the same path over 2 seconds.

**中文翻译：** 从第 17.0 秒开始，在两秒内将躯干朝黑色平底锅倾斜二十厘米，然后用两秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝黑色平底锅倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内沿原路径返回？


## 092 — `embodied_061_E2A`

**原始英文指令：** At 32.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during scrubbing the pan interior edge and exterior.

**中文翻译：** 在第 32.0 秒，在擦洗平底锅内侧边缘和外表面时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 平底锅的内侧边缘是否被擦洗？

2. 平底锅的外表面是否被擦洗？

3. 在擦洗平底锅内侧边缘和外表面时，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 093 — `embodied_061_E2B`

**原始英文指令：** At 32.0 seconds, make the yellow-green sponge visibly saturated with dense white foam for the rest of the visible scene.

**中文翻译：** 在第 32.0 秒，使黄绿色海绵明显浸满浓密的白色泡沫，并保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 黄绿色海绵是否明显浸满浓密的白色泡沫？

2. 浸满泡沫的外观是否保持至可见场景结束？


## 094 — `embodied_065_E1`

**原始英文指令：** At 17.0 seconds, position the visible hand nearest the clear ball opening in the lower-right frame quadrant, one palm-width away.

**中文翻译：** 在第 17.0 秒，将距离透明球开口最近的可见手放在画面右下象限，并与开口相距一个手掌宽。

**状态：** 接受

**原子化判定句：**

1. 距离透明球开口最近的可见手是否被放在画面右下象限？

2. 该手与透明球开口之间是否相距一个手掌宽？


## 095 — `embodied_065_E2A`

**原始英文指令：** At 32.0 seconds, render the full scene with a 1990s home-video treatment during watching the lizard extend its head through the opening.

**中文翻译：** 在第 32.0 秒，在观看蜥蜴将头伸出开口时，为整个场景应用 1990 年代家庭录像风格。

**状态：** 接受

**原子化判定句：**

1. 蜥蜴是否将头伸出开口？

2. 在观看蜥蜴伸头动作时，整个场景是否被渲染为 1990 年代家庭录像风格？


## 096 — `embodied_065_E2B`

**原始英文指令：** At 32.0 seconds, remove the dark rectangular electronic device on the cabinet behind the ball completely from the visible scene during watching the lizard extend its head through the opening.

**中文翻译：** 在第 32.0 秒，在观看蜥蜴将头伸出开口时，将球后方柜子上的深色长方形电子设备从可见场景中完全移除。

**状态：** 接受

**原子化判定句：**

1. 蜥蜴是否将头伸出开口？

2. 在观看蜥蜴伸头动作时，球后方柜子上的深色长方形电子设备是否从可见场景中被完全移除？


## 097 — `embodied_069_E1`

**原始英文指令：** At 19.0 seconds, replace the knitted sample with a same-gauge blue knitted swatch with intact edge loops in the same task location.

**中文翻译：** 在第 19.0 秒，将针织样品替换为针距相同、边缘线圈完整的蓝色针织样片，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 针织样品是否被替换为蓝色针织样片？

2. 替换后的样片是否与原样品针距相同？

3. 替换后样片的边缘线圈是否完整？

4. 替换后的样片是否位于原针织样品所在的任务位置？


## 098 — `embodied_069_E2A`

**原始英文指令：** At 34.0 seconds, position the entire visible knitted sample in the left third of the frame at its current working depth.

**中文翻译：** 在第 34.0 秒，将整个可见针织样品放在画面左侧三分之一区域，并保持当前工作景深。

**状态：** 接受

**原子化判定句：**

1. 整个可见针织样品是否被放在画面左侧三分之一区域？

2. 该针织样品是否保持当前工作景深？


## 099 — `embodied_069_E2B`

**原始英文指令：** At 34.0 seconds, change the non-text surfaces of the wooden needle to satin forest green for the rest of the scene.

**中文翻译：** 在第 34.0 秒，将木针上不含文字的表面变为缎面森林绿色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 木针上不含文字的表面是否变为森林绿色？

2. 发生变化的表面是否呈缎面质感？

3. 缎面森林绿色外观是否保持至场景结束？


## 100 — `embodied_071_E1`

**原始英文指令：** At 18.0 seconds, position the free gloved hand nearest the bin's lower-right corner one palm-width from the supported opossum.

**中文翻译：** 在第 18.0 秒，将空闲的戴手套的手放在最靠近箱子右下角的位置，并与被托住的负鼠保持一个手掌宽的距离。

**状态：** 接受

**原子化判定句：**

1. 空闲的戴手套的手是否被放在最靠近箱子右下角的位置？

2. 该手与被托住的负鼠之间是否相距一个手掌宽？


## 101 — `embodied_071_E2A`

**原始英文指令：** Starting at 33.0 seconds, support and reposition the small opossum along one smooth lifting-and-lowering arc over 4 seconds.

**中文翻译：** 从第 33.0 秒开始，托住小负鼠，并在四秒内沿一条平滑的抬起—放下弧线重新调整其位置。

**状态：** 接受

**原子化判定句：**

1. 小负鼠是否被托住？

2. 被托住的小负鼠是否沿一条平滑的抬起—放下弧线在 4 秒内完成位置调整？


## 102 — `embodied_071_E2B`

**原始英文指令：** At 33.0 seconds, illuminate the visible environment with soft overcast daylight at an even exposure during restraining and repositioning a small opossum in a bin.

**中文翻译：** 在第 33.0 秒，在箱内约束并重新调整小负鼠的位置时，用柔和的阴天日光以均匀曝光照亮可见环境。

**状态：** 接受

**原子化判定句：**

1. 小负鼠是否在箱内受到约束？

2. 小负鼠在箱内的位置是否被重新调整？

3. 在约束并调整负鼠位置时，可见环境是否受到柔和阴天日光的均匀照明？


## 103 — `embodied_073_E1`

**原始英文指令：** At 18.0 seconds, render the full visible scene as a restrained watercolor illustration during shaking and turning the capped bottle.

**中文翻译：** 在第 18.0 秒，在摇晃并转动带盖瓶子时，将整个可见场景渲染为色彩克制的水彩插画。

**状态：** 接受

**原子化判定句：**

1. 带盖瓶子是否被摇晃？

2. 带盖瓶子是否被转动？

3. 在摇晃并转动瓶子时，整个可见场景是否被渲染为色彩克制的水彩插画？


## 104 — `embodied_073_E2A`

**原始英文指令：** Starting at 33.0 seconds, perform a two-second optical push-in to a stable close-up centered on the red pointed cap.

**中文翻译：** 从第 33.0 秒开始，进行一次持续两秒的光学推进，最终形成以红色尖盖为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以红色尖盖为中心的稳定特写？


## 105 — `embodied_073_E2B`

**原始英文指令：** At 33.0 seconds, add one small clear sample vial upright at the center of the empty black table tile below the shaking bottle.

**中文翻译：** 在第 33.0 秒，在正在摇晃的瓶子下方空白黑色桌面格中央添加一个直立的小型透明样品瓶。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型透明样品瓶？

2. 样品瓶是否直立？

3. 样品瓶是否位于正在摇晃的瓶子下方空白黑色桌面格中央？


## 106 — `embodied_075_E1`

**原始英文指令：** At 15.0 seconds, position the held standard twisty cube in the left third of the frame at its current working depth.

**中文翻译：** 在第 15.0 秒，将手持的标准扭转魔方放在画面左侧三分之一区域，并保持当前工作景深。

**状态：** 接受

**原子化判定句：**

1. 手持的标准扭转魔方是否被放在画面左侧三分之一区域？

2. 该魔方是否保持当前工作景深？


## 107 — `embodied_075_E2A`

**原始英文指令：** At 30.0 seconds, change the non-text surfaces of the held standard twisty cube to warm ivory for the rest of the scene.

**中文翻译：** 在第 30.0 秒，将手持标准扭转魔方上不含文字的表面变为暖象牙色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 手持标准扭转魔方上不含文字的表面是否变为暖象牙色？

2. 暖象牙色外观是否保持至场景结束？


## 108 — `embodied_075_E2B`

**原始英文指令：** Starting at 30.0 seconds, lift and turn the standard twisty cube through one smooth rising inspection arc over four seconds.

**中文翻译：** 从第 30.0 秒开始，在四秒内沿一条平滑上升的观察弧线抬起并转动标准扭转魔方。

**状态：** 接受

**原子化判定句：**

1. 标准扭转魔方是否被抬起？

2. 魔方是否在被抬起的同时转动？

3. 抬起和转动是否沿一条平滑上升的观察弧线进行，并在 4 秒内完成？


## 109 — `embodied_077_E1`

**原始英文指令：** Starting at 19.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the wide kitchen knife over four seconds.

**中文翻译：** 从第 19.0 秒开始，在四秒内将第一人称视点朝宽刃厨刀方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 4 秒内向右移动半米？

2. 第一人称视点是否在同一段 4 秒内降低二十五厘米？

3. 视点是否朝宽刃厨刀方向移动？


## 110 — `embodied_077_E2A`

**原始英文指令：** At 40.0 seconds, make the exterior of the cleaning-liquid bottle visibly chilled with a thin, even condensation layer for the rest of the visible scene.

**中文翻译：** 在第 40.0 秒，使清洁液瓶的外表面呈现明显冰凉的状态，并带有一层薄而均匀的冷凝水，且该状态保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 清洁液瓶的外表面是否呈现明显冰凉的状态并出现一层薄冷凝水？

2. 冷凝水层在瓶子的可见外表面上是否分布均匀？

3. 冰凉且带冷凝水的外观是否保持至可见场景结束？


## 111 — `embodied_077_E2B`

**原始英文指令：** Starting at 34.0 seconds, lean the trunk twenty centimeters toward the rear-counter cleaning bottle over 1.5 seconds, then return over 1.5 seconds.

**中文翻译：** 从第 34.0 秒开始，在 1.5 秒内将躯干朝后方台面上的清洁瓶倾斜二十厘米，然后用 1.5 秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 1.5 秒内朝后方台面上的清洁瓶倾斜二十厘米？

2. 躯干是否随后在接下来的 1.5 秒内回到原位？


## 112 — `embodied_078_E1`

**原始英文指令：** At 19.0 seconds, remove the black device front completely from the visible scene.

**中文翻译：** 在第 19.0 秒，将黑色设备正面从可见场景中完全移除。

**状态：** 接受

**原子化判定句：**

1. 黑色设备正面是否从可见场景中被完全移除？


## 113 — `embodied_078_E2A`

**原始英文指令：** At 42.0 seconds, position the nearest visible fingertip two centimeters above the white mounting plate.

**中文翻译：** 在第 42.0 秒，将最近的可见指尖放在白色安装板上方两厘米处。

**状态：** 接受

**原子化判定句：**

1. 最近的可见指尖是否被放在白色安装板上方两厘米处？


## 114 — `embodied_078_E2B`

**原始英文指令：** Starting at 32.0 seconds, rotate the upper circular fastener on the white backing plate clockwise through one wider arc over three seconds.

**中文翻译：** 从第 32.0 秒开始，在三秒内沿一条更宽的弧线顺时针转动白色背板上的上方圆形紧固件。

**状态：** 接受

**原子化判定句：**

1. 白色背板上的上方圆形紧固件是否顺时针旋转？

2. 紧固件是否转过一条更宽的弧线？

3. 旋转是否在 3 秒内完成？


## 115 — `embodied_079_E1`

**原始英文指令：** Starting at 18.0 seconds, perform a two-second optical push-in to a stable close-up centered on the charging case.

**中文翻译：** 从第 18.0 秒开始，进行一次持续两秒的光学推进，最终形成以充电盒为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以充电盒为中心的稳定特写？


## 116 — `embodied_079_E2A`

**原始英文指令：** At 33.0 seconds, render the full visible scene as a restrained watercolor illustration during pointing among the phone earbuds and charging case.

**中文翻译：** 在第 33.0 秒，在手机、耳机和充电盒之间进行指示时，将整个可见场景渲染为色彩克制的水彩插画。

**状态：** 接受

**原子化判定句：**

1. 是否在手机、耳机和充电盒之间进行指示？

2. 在进行指示时，整个可见场景是否被渲染为色彩克制的水彩插画？


## 117 — `embodied_079_E2B`

**原始英文指令：** Starting at 33.0 seconds, sweep the active hand from the smartphone's left edge to its right edge over 4 seconds.

**中文翻译：** 从第 33.0 秒开始，让正在操作的手从智能手机左边缘扫向右边缘，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 正在操作的手是否从智能手机左边缘扫向右边缘？

2. 该扫动是否在 4 秒内完成？


## 118 — `embodied_080_E1`

**原始英文指令：** At 18.0 seconds, split the keycap cube vertically into equal independent left and right components, placed side by side with a clear gap.

**中文翻译：** 在第 18.0 秒，将键帽立方体竖直拆分为大小相等且彼此独立的左右两个部件，并排放置且留有清晰间隙。

**状态：** 接受

**原子化判定句：**

1. 键帽立方体是否被竖直拆分为彼此独立的左右两个部件？

2. 两个部件的大小是否相等？

3. 两个部件是否并排放置？

4. 两个部件之间是否留有清晰间隙？


## 119 — `embodied_080_E2A`

**原始英文指令：** At 33.0 seconds, orient the misaligned keycap layers so all exposed front faces point thirty degrees toward frame-left.

**中文翻译：** 在第 33.0 秒，调整错位的键帽层，使所有暴露的正面朝画面左侧偏转三十度。

**状态：** 接受

**原子化判定句：**

1. 错位的键帽层是否被重新调整朝向？

2. 调整后，所有暴露的正面是否朝画面左侧偏转三十度？


## 120 — `embodied_080_E2B`

**原始英文指令：** Starting at 33.0 seconds, press the right split component's misaligned keycap layers into alignment in one wider clockwise seating pass over three seconds.

**中文翻译：** 从第 33.0 秒开始，用一次更宽的顺时针压合动作，在三秒内将右侧拆分部件上错位的键帽层压至对齐。

**状态：** 接受

**原子化判定句：**

1. 右侧拆分部件上错位的键帽层是否被压至对齐？

2. 对齐是否通过一次更宽的顺时针压合动作在 3 秒内完成？


## 121 — `embodied_081_E1`

**原始英文指令：** At 17.0 seconds, place the green plaid paper on the left third of the gray cutting mat, one paper-width below the trimmer.

**中文翻译：** 在第 17.0 秒，将绿色格纹纸放在灰色切割垫左侧三分之一区域，并位于裁纸器下方一个纸张宽的位置。

**状态：** 接受

**原子化判定句：**

1. 绿色格纹纸是否被放在灰色切割垫左侧三分之一区域？

2. 该纸张是否位于裁纸器下方一个纸张宽的位置？


## 122 — `embodied_081_E2A`

**原始英文指令：** At 41.0 seconds, apply a high-contrast monochrome graphic treatment across the full scene during trimming and aligning the journaling strip with the photo layers.

**中文翻译：** 在第 41.0 秒，在裁剪日记装饰条并将其与照片图层对齐时，为整个场景应用高对比度的单色图形化效果。

**状态：** 接受

**原子化判定句：**

1. 日记装饰条是否被裁剪？

2. 日记装饰条是否与照片图层对齐？

3. 在裁剪并对齐装饰条时，整个场景是否应用了高对比度的单色图形化效果？


## 123 — `embodied_081_E2B`

**原始英文指令：** At 32.0 seconds, add one capped graphite pencil vertically on the clear gray cutting-mat strip to the right of the scrapbook page.

**中文翻译：** 在第 32.0 秒，在剪贴簿页面右侧清晰可见的灰色切割垫条带上，竖直添加一支带帽石墨铅笔。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一支带帽石墨铅笔？

2. 铅笔是否竖直放置？

3. 铅笔是否位于剪贴簿页面右侧清晰可见的灰色切割垫条带上？


## 124 — `embodied_082_E1`

**原始英文指令：** At 16.0 seconds, place the hand nearest the metal dish in the lower-left quadrant, one palm-width left of the transparent cup.

**中文翻译：** 在第 16.0 秒，将距离金属碟最近的手放在画面左下象限，并位于透明杯左侧一个手掌宽处。

**状态：** 接受

**原子化判定句：**

1. 距离金属碟最近的手是否被放在画面左下象限？

2. 该手是否位于透明杯左侧一个手掌宽处？


## 125 — `embodied_082_E2A`

**原始英文指令：** Starting at 31.0 seconds, press around the inverted cup rim in one wider clockwise path over 4 seconds.

**中文翻译：** 从第 31.0 秒开始，沿一条更宽的顺时针路径按压倒置杯子的杯口边缘，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 是否沿倒置杯子的杯口边缘进行按压？

2. 按压是否沿顺时针路径进行？

3. 按压路径是否更宽？

4. 按压是否在 4 秒内完成？


## 126 — `embodied_082_E2B`

**原始英文指令：** At 31.0 seconds, remove the red curtain backdrop completely from the visible scene during pressing around the inverted cup during the coin demonstration.

**中文翻译：** 在第 31.0 秒，在硬币演示中围绕倒置杯子按压时，将红色幕布背景从可见场景中完全移除。

**状态：** 接受

**原子化判定句：**

1. 在硬币演示中，是否围绕倒置杯子进行按压？

2. 在该按压动作期间，红色幕布背景是否从可见场景中被完全移除？


## 127 — `embodied_083_E1`

**原始英文指令：** At 17.0 seconds, make the chopped white onion on the cutting board visibly dry, crisp-edged, and separated into distinct pieces.

**中文翻译：** 在第 17.0 秒，使砧板上的白色碎洋葱呈现明显干燥、边缘清晰且彼此分离成独立小块的状态。

**状态：** 接受

**原子化判定句：**

1. 砧板上的白色碎洋葱是否呈现明显干燥的状态？

2. 洋葱碎块的边缘是否清晰？

3. 洋葱碎块是否彼此分离成独立小块？


## 128 — `embodied_083_E2A`

**原始英文指令：** Starting at 42.0 seconds, lean the trunk twenty centimeters toward the cheese block over 1.5 seconds, then return along the same path over 1.5 seconds.

**中文翻译：** 从第 42.0 秒开始，在 1.5 秒内将躯干朝奶酪块倾斜二十厘米，然后用 1.5 秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 1.5 秒内朝奶酪块倾斜二十厘米？

2. 躯干是否随后在接下来的 1.5 秒内沿原路径返回？


## 129 — `embodied_083_E2B`

**原始英文指令：** Starting at 32.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the small metal grater over three seconds.

**中文翻译：** 从第 32.0 秒开始，在三秒内将第一人称视点朝小型金属刨丝器方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 3 秒内向右移动半米？

2. 第一人称视点是否在同一段 3 秒内降低二十五厘米？

3. 视点是否朝小型金属刨丝器方向移动？


## 130 — `embodied_085_E1`

**原始英文指令：** Starting at 19.0 seconds, make the small spotted lizard travel rightward in one smooth arc over 4 seconds during watching the animal walk and turn in the container.

**中文翻译：** 从第 19.0 秒开始，在观看小型斑点蜥蜴在容器中行走和转身时，让它沿一条平滑弧线向右移动，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 小型斑点蜥蜴是否在容器中行走？

2. 蜥蜴是否在容器中转身？

3. 在观看该动物时，它是否沿一条平滑弧线向右移动，并在 4 秒内完成？


## 131 — `embodied_085_E2A`

**原始英文指令：** At 26.0 seconds, replace the small spotted lizard with a small pond turtle in the same task location.

**中文翻译：** 在第 26.0 秒，将小型斑点蜥蜴替换为一只小型池龟，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 小型斑点蜥蜴是否被替换为一只小型池龟？

2. 池龟是否位于斑点蜥蜴原本所在的任务位置？


## 132 — `embodied_085_E2B`

**原始英文指令：** Starting at 34.0 seconds, make successive circular ripples propagate outward from the spotted lizard's feet for four seconds.

**中文翻译：** 从第 34.0 秒开始，让连续的圆形波纹从斑点蜥蜴脚部向外扩散四秒。

**状态：** 接受

**原子化判定句：**

1. 斑点蜥蜴脚部是否形成连续的圆形波纹？

2. 波纹是否向外扩散？

3. 波纹扩散是否持续 4 秒？


## 133 — `embodied_088_E1`

**原始英文指令：** Starting at 19.0 seconds, rotate the selected cylindrical puzzle segment through one wider clockwise turn over four seconds.

**中文翻译：** 从第 19.0 秒开始，让选中的圆柱形拼图段完成一次更宽幅度的顺时针转动，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 选中的圆柱形拼图段是否顺时针转动？

2. 该拼图段是否完成一次更宽幅度的转动？

3. 旋转是否在 4 秒内完成？


## 134 — `embodied_088_E2A`

**原始英文指令：** At 41.0 seconds, render only the visible tabletop behind the segmented puzzle as a faceted low-poly work surface.

**中文翻译：** 在第 41.0 秒，仅将分块拼图后方可见的桌面渲染为带有切面的低多边形工作台表面。

**状态：** 接受

**原子化判定句：**

1. 分块拼图后方可见的桌面是否被渲染为带有切面的低多边形工作台表面？

2. 低多边形渲染是否仅作用于该可见桌面？


## 135 — `embodied_088_E2B`

**原始英文指令：** At 34.0 seconds, split the cylinder puzzle along its central segment seam into equal independent components placed side by side with a clear gap.

**中文翻译：** 在第 34.0 秒，沿中央拼接缝将圆柱拼图拆分为大小相等且彼此独立的部件，并排放置且留有清晰间隙。

**状态：** 接受

**原子化判定句：**

1. 圆柱拼图是否沿中央拼接缝被拆分为彼此独立的部件？

2. 拆分后的部件大小是否相等？

3. 这些部件是否并排放置？

4. 部件之间是否留有清晰间隙？


## 136 — `embodied_089_E1`

**原始英文指令：** Starting at 16.0 seconds, slow the black flywheel smoothly to one-quarter of its source angular speed over four seconds.

**中文翻译：** 从第 16.0 秒开始，在四秒内将黑色飞轮平稳减速至原角速度的四分之一。

**状态：** 接受

**原子化判定句：**

1. 黑色飞轮是否平稳减速？

2. 飞轮是否在 4 秒内降至原角速度的四分之一？


## 137 — `embodied_089_E2A`

**原始英文指令：** At 31.0 seconds, remove the small loose brass-colored object on the tabletop left of the model completely from the visible scene during turning the model sideways to inspect its linkage.

**中文翻译：** 在第 31.0 秒，在将模型侧向转动以检查其连杆时，将模型左侧桌面上的小型松散黄铜色物体从可见场景中完全移除。

**状态：** 接受

**原子化判定句：**

1. 模型是否被侧向转动？

2. 模型被转动后，其连杆是否受到检查？

3. 在这些动作期间，模型左侧桌面上的小型松散黄铜色物体是否从可见场景中被完全移除？


## 138 — `embodied_089_E2B`

**原始英文指令：** At 27.0 seconds, position the nearest active fingertip two centimeters to frame-left of the black engine base.

**中文翻译：** 在第 27.0 秒，将最近的活动指尖放在黑色发动机底座画面左侧两厘米处。

**状态：** 接受

**原子化判定句：**

1. 最近的活动指尖是否被放在黑色发动机底座画面左侧两厘米处？


## 139 — `embodied_092_E1`

**原始英文指令：** At 17.0 seconds, change the non-text surfaces of the pan exterior to soft coral red for the rest of the scene.

**中文翻译：** 在第 17.0 秒，将平底锅外部不含文字的表面变为柔和的珊瑚红色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 平底锅外部不含文字的表面是否变为柔和的珊瑚红色？

2. 柔和的珊瑚红色外观是否保持至场景结束？


## 140 — `embodied_092_E2A`

**原始英文指令：** At 32.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during bringing the small pot near the pan and resuming stirring.

**中文翻译：** 在第 32.0 秒，在将小锅移近平底锅并恢复搅拌时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 小锅是否被移近平底锅？

2. 搅拌是否恢复？

3. 在小锅被移近且搅拌恢复时，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 141 — `embodied_092_E2B`

**原始英文指令：** Starting at 32.0 seconds, lean the trunk twenty centimeters toward the black frying pan over 1.5 seconds, then return over 1.5 seconds.

**中文翻译：** 从第 32.0 秒开始，在 1.5 秒内将躯干朝黑色平底锅倾斜二十厘米，然后用 1.5 秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 1.5 秒内朝黑色平底锅倾斜二十厘米？

2. 躯干是否随后在接下来的 1.5 秒内回到原位？


## 142 — `embodied_093_E1`

**原始英文指令：** Starting at 18.0 seconds, lift one selected coin along a smooth rising arc and return it to the grouping over 4 seconds.

**中文翻译：** 从第 18.0 秒开始，沿一条平滑上升的弧线抬起一枚选中的硬币，并在四秒内将其放回硬币组。

**状态：** 接受

**原子化判定句：**

1. 一枚选中的硬币是否沿一条平滑上升的弧线被抬起？

2. 该硬币是否随后被放回硬币组，并在 4 秒内完成整个动作过程？


## 143 — `embodied_093_E2A`

**原始英文指令：** At 33.0 seconds, position the top-entering hand's fingertips two coin-diameters above the midpoint of the horizontal coin row.

**中文翻译：** 在第 33.0 秒，将从画面上方进入的手指尖放在水平硬币排中点上方两个硬币直径处。

**状态：** 接受

**原子化判定句：**

1. 从画面上方进入的手指尖是否被放在水平硬币排中点上方两个硬币直径处？


## 144 — `embodied_093_E2B`

**原始英文指令：** At 33.0 seconds, illuminate the visible environment with soft overcast daylight at an even exposure during sorting and regrouping mixed coins on a wooden rail.

**中文翻译：** 在第 33.0 秒，在木质轨道上分类并重新组合混合硬币时，用柔和的阴天日光以均匀曝光照亮可见环境。

**状态：** 接受

**原子化判定句：**

1. 混合硬币是否在木质轨道上被分类？

2. 硬币是否在木质轨道上被重新组合？

3. 在分类并重新组合硬币时，可见环境是否受到柔和阴天日光的均匀照明？


## 145 — `embodied_096_E1`

**原始英文指令：** At 19.0 seconds, replace the cooked white rice with an equal volume of cooked brown rice in the same clear storage container.

**中文翻译：** 在第 19.0 秒，将熟白米饭替换为等体积的熟糙米饭，并放在同一个透明储存容器中。

**状态：** 接受

**原子化判定句：**

1. 熟白米饭是否被替换为熟糙米饭？

2. 熟糙米饭的体积是否与原白米饭相等？

3. 替换后的米饭是否位于同一个透明储存容器中？


## 146 — `embodied_096_E2A`

**原始英文指令：** At 42.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during serving cooked pieces from the frying pan onto the plate.

**中文翻译：** 在第 42.0 秒，在将熟食块从平底锅盛到盘子上时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 熟食块是否从平底锅盛到盘子上？

2. 在盛出熟食块时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 147 — `embodied_096_E2B`

**原始英文指令：** At 34.0 seconds, cover the wet inner surface of the round metal strainer with dense white soap foam.

**中文翻译：** 在第 34.0 秒，让圆形金属滤网湿润的内表面覆盖浓密的白色肥皂泡沫。

**状态：** 接受

**原子化判定句：**

1. 圆形金属滤网的湿润内表面是否被白色肥皂泡沫覆盖？

2. 覆盖内表面的白色肥皂泡沫是否浓密？


## 148 — `embodied_097_E1`

**原始英文指令：** At 17.0 seconds, add one small brass bulldog clip fastening the upper-left edge of the portrait sheet.

**中文翻译：** 在第 17.0 秒，添加一个小型黄铜长尾夹，用于夹住肖像纸的左上边缘。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型黄铜长尾夹？

2. 该夹子是否夹住肖像纸的左上边缘？


## 149 — `embodied_097_E2A`

**原始英文指令：** At 32.0 seconds, change the painted portrait sleeve on frame-right to brushed silver for the rest of the scene.

**中文翻译：** 在第 32.0 秒，将画面右侧肖像中的衣袖变为拉丝银色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 画面右侧肖像中的衣袖是否变为拉丝银色？

2. 拉丝银色外观是否保持至场景结束？


## 150 — `embodied_097_E2B`

**原始英文指令：** Starting at 32.0 seconds, paint the frame-right sleeve highlights along one wider curve following the fabric contour over four seconds.

**中文翻译：** 从第 32.0 秒开始，沿一条顺着布料轮廓的更宽曲线绘制画面右侧衣袖的高光，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 画面右侧衣袖的高光是否被重新绘制？

2. 高光是否沿一条顺着布料轮廓的更宽曲线绘制？

3. 绘制是否在 4 秒内完成？


## 151 — `embodied_104_E1`

**原始英文指令：** At 19.0 seconds, change only the outer rim of the transparent mixing bowl to soft coral red for the rest of the scene.

**中文翻译：** 在第 19.0 秒，仅将透明搅拌碗的外缘变为柔和的珊瑚红色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 透明搅拌碗的外缘是否变为柔和的珊瑚红色？

2. 颜色变化是否仅作用于外缘？

3. 柔和的珊瑚红色外观是否保持至场景结束？


## 152 — `embodied_104_E2A`

**原始英文指令：** At 34.0 seconds, render only the visible hands and forearms with cel-shaded game-character treatment during rinsing the bowl as remaining foam washes away.

**中文翻译：** 在第 34.0 秒，在冲洗碗并让剩余泡沫流走时，仅将可见的双手和前臂渲染为卡通渲染的游戏角色风格。

**状态：** 接受

**原子化判定句：**

1. 碗是否被冲洗？

2. 剩余泡沫是否在冲洗时流走？

3. 在冲洗过程中，可见的双手和前臂是否被渲染为卡通渲染的游戏角色风格？

4. 卡通渲染效果是否仅作用于可见的双手和前臂？


## 153 — `embodied_104_E2B`

**原始英文指令：** At 34.0 seconds, make the pink-purple sponge visibly saturated with dense white foam for the rest of the visible scene.

**中文翻译：** 在第 34.0 秒，使粉紫色海绵明显浸满浓密的白色泡沫，并保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 粉紫色海绵是否明显浸满浓密的白色泡沫？

2. 浸满泡沫的外观是否保持至可见场景结束？


## 154 — `embodied_105_E1`

**原始英文指令：** At 19.0 seconds, render the full scene with a 1990s home-video treatment while the first orange-white fish swims alone in the basin.

**中文翻译：** 在第 19.0 秒，当第一条橙白色鱼独自在盆中游动时，为整个场景应用 1990 年代家庭录像风格。

**状态：** 接受

**原子化判定句：**

1. 第一条橙白色鱼是否独自在盆中游动？

2. 当该鱼独自游动时，整个场景是否被渲染为 1990 年代家庭录像风格？


## 155 — `embodied_105_E2A`

**原始英文指令：** At 34.0 seconds, place the rounder orange-white fish directly frame-left of the slimmer fish, with half a fish-width between them.

**中文翻译：** 在第 34.0 秒，将较圆的橙白色鱼放在较瘦鱼的画面正左侧，两者之间留出半个鱼身宽的距离。

**状态：** 接受

**原子化判定句：**

1. 较圆的橙白色鱼是否被放在较瘦鱼的画面正左侧？

2. 两条鱼之间是否留有半个鱼身宽的距离？


## 156 — `embodied_105_E2B`

**原始英文指令：** At 34.0 seconds, remove the slimmer orange-white fish swimming in the upper half of the basin from the visible scene.

**中文翻译：** 在第 34.0 秒，将正在盆中上半区域游动的较瘦橙白色鱼从可见场景中移除。

**状态：** 接受

**原子化判定句：**

1. 正在盆中上半区域游动的较瘦橙白色鱼是否从可见场景中被移除？


## 157 — `embodied_106_E1`

**原始英文指令：** Starting at 19.0 seconds, flex and rotate the long orange watchband through one wider clockwise display arc over four seconds.

**中文翻译：** 从第 19.0 秒开始，在四秒内沿一条更宽的顺时针展示弧线弯曲并转动长橙色表带。

**状态：** 接受

**原子化判定句：**

1. 长橙色表带是否被弯曲？

2. 表带是否在弯曲的同时被转动？

3. 弯曲和转动是否沿一条更宽的顺时针展示弧线进行，并在 4 秒内完成？


## 158 — `embodied_106_E2A`

**原始英文指令：** At 42.0 seconds, remove the loose orange watchband half lying horizontally below the watch from the visible scene.

**中文翻译：** 在第 42.0 秒，将水平放置在手表下方的松散橙色半截表带从可见场景中移除。

**状态：** 接受

**原子化判定句：**

1. 水平放置在手表下方的松散橙色半截表带是否从可见场景中被移除？


## 159 — `embodied_106_E2B`

**原始英文指令：** At 34.0 seconds, position the nearest visible index fingertip one centimeter directly above the exposed metal connector between the orange band halves.

**中文翻译：** 在第 34.0 秒，将最近的可见食指指尖放在两段橙色表带之间裸露金属连接件正上方一厘米处。

**状态：** 接受

**原子化判定句：**

1. 最近的可见食指指尖是否被放在两段橙色表带之间裸露金属连接件正上方一厘米处？


## 160 — `embodied_108_E1`

**原始英文指令：** Starting at 19.0 seconds, make the black formula car directly ahead accelerate one car length within its current lane over four seconds.

**中文翻译：** 从第 19.0 秒开始，让正前方的黑色方程式赛车在四秒内沿当前车道加速前进一个车身长度。

**状态：** 接受

**原子化判定句：**

1. 正前方的黑色方程式赛车是否在 4 秒内加速前进一个车身长度？

2. 赛车在加速时是否保持在当前车道内？


## 161 — `embodied_108_E2A`

**原始英文指令：** Starting at 40.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters upward toward the elevated trackside floodlights over four seconds.

**中文翻译：** 从第 40.0 秒开始，在四秒内将第一人称视点朝高架赛道边泛光灯方向向右移动半米，并升高二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 4 秒内向右移动半米？

2. 第一人称视点是否在同一段 4 秒内升高二十五厘米？

3. 视点是否朝高架赛道边泛光灯方向移动？


## 162 — `embodied_108_E2B`

**原始英文指令：** At 34.0 seconds, add one upright orange safety cone at the center of the empty blue run-off strip beside the frame-right track edge.

**中文翻译：** 在第 34.0 秒，在画面右侧赛道边缘旁空置的蓝色缓冲带中央添加一个直立的橙色安全锥。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个橙色安全锥？

2. 安全锥是否直立？

3. 安全锥是否位于画面右侧赛道边缘旁空置蓝色缓冲带的中央？


## 163 — `embodied_109_E1`

**原始英文指令：** At 19.0 seconds, place the untouched lower-left cracker one cracker-width directly frame-left of the lower-right cracker.

**中文翻译：** 在第 19.0 秒，将左下方未动过的饼干放在右下方饼干的画面正左侧，相距一个饼干宽。

**状态：** 接受

**原子化判定句：**

1. 左下方未动过的饼干是否放在右下方饼干的画面正左侧？

2. 两块饼干之间是否相距一个饼干宽？


## 164 — `embodied_109_E2A`

**原始英文指令：** At 40.0 seconds, coat the working face of the table knife with a thin, even layer of orange spread.

**中文翻译：** 在第 40.0 秒，在餐刀的工作面上均匀覆盖一层薄薄的橙色涂抹酱。

**状态：** 接受

**原子化判定句：**

1. 餐刀的工作面是否覆盖有一层薄薄的橙色涂抹酱？

2. 橙色涂抹酱层是否均匀？


## 165 — `embodied_109_E2B`

**原始英文指令：** At 34.0 seconds, render only the table knife with a hand-painted illustration treatment for the remaining footage.

**中文翻译：** 在第 34.0 秒，仅将餐刀渲染为手绘插画风格，并保持至剩余视频结束。

**状态：** 接受

**原子化判定句：**

1. 餐刀是否被渲染为手绘插画风格？

2. 手绘效果是否仅作用于餐刀？

3. 该效果是否保持至剩余视频结束？


## 166 — `embodied_110_E1`

**原始英文指令：** At 13.0 seconds, cover the visible interior of the large black frying pan with a thick layer of white soap foam.

**中文翻译：** 在第 13.0 秒，让黑色大平底锅的可见内表面覆盖一层厚厚的白色肥皂泡沫。

**状态：** 接受

**原子化判定句：**

1. 黑色大平底锅的可见内表面是否被白色肥皂泡沫覆盖？

2. 白色肥皂泡沫层是否厚实？


## 167 — `embodied_110_E2A`

**原始英文指令：** At 26.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during placing the frying pan and smaller cookware into the rack.

**中文翻译：** 在第 26.0 秒，在将平底锅和较小炊具放入架子时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 平底锅是否被放入架子？

2. 较小的炊具是否被放入架子？

3. 在放置炊具时，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 168 — `embodied_110_E2B`

**原始英文指令：** Starting at 26.0 seconds, bend the trunk steadily toward the open lower cookware rack for four seconds while lowering the pan.

**中文翻译：** 从第 26.0 秒开始，躯干持续四秒稳定地向打开的下层炊具架弯下，同时放低平底锅。

**状态：** 接受

**原子化判定句：**

1. 躯干是否朝打开的下层炊具架稳定地弯下并持续 4 秒？

2. 在躯干弯向炊具架的同时，平底锅是否被放低？


## 169 — `embodied_111_E1`

**原始英文指令：** At 16.0 seconds, make the raw ground meat evenly browned with no visible raw areas for the rest of the visible scene.

**中文翻译：** 在第 16.0 秒，使生绞肉均匀变成褐色，不留任何可见的生肉区域，并保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 生绞肉是否均匀变成褐色且不留任何可见的生肉区域？

2. 完全变褐的外观是否保持至可见场景结束？


## 170 — `embodied_111_E2A`

**原始英文指令：** At 31.0 seconds, terminate the pre-adjustment stirring phase at exactly 33.0 seconds instead of 34.0 seconds.

**中文翻译：** 在第 31.0 秒进行编辑，使调整前的搅拌阶段在第 33.0 秒而非第 34.0 秒准确结束。

**状态：** 接受

**原子化判定句：**

1. 调整前的搅拌阶段是否发生？

2. 该搅拌阶段是否在片段开始后恰好 2 秒结束，而不是在 3 秒后结束？


## 171 — `embodied_111_E2B`

**原始英文指令：** At 31.0 seconds, place the orange-capped seasoning jar one full jar-width directly frame-left of the green-capped jar nearest the pan.

**中文翻译：** 在第 31.0 秒，将橙色瓶盖调味罐放在距锅最近的绿色瓶盖调味罐画面正左侧一个完整罐宽处。

**状态：** 接受

**原子化判定句：**

1. 橙色瓶盖调味罐是否放在距锅最近的绿色瓶盖调味罐画面正左侧？

2. 两个调味罐之间是否相距一个完整罐宽？


## 172 — `embodied_112_E1`

**原始英文指令：** At 15.0 seconds, remove the engine cover completely from the visible scene during pointing across the engine cover and blue wiring.

**中文翻译：** 在第 15.0 秒，在对发动机盖和蓝色线路进行指示时，将发动机盖从可见场景中完全移除。

**状态：** 接受

**原子化判定句：**

1. 是否对发动机盖进行指示？

2. 是否对蓝色线路进行指示？

3. 在进行指示时，发动机盖是否从可见场景中被完全移除？


## 173 — `embodied_112_E2A`

**原始英文指令：** At 30.0 seconds, illuminate the visible environment with soft overcast daylight at an even exposure during pointing out components in an open engine bay.

**中文翻译：** 在第 30.0 秒，在指出打开的发动机舱内各个部件时，用柔和的阴天日光以均匀曝光照亮可见环境。

**状态：** 接受

**原子化判定句：**

1. 打开的发动机舱内各个部件是否被指出？

2. 在指出这些部件时，可见环境是否受到柔和阴天日光的均匀照明？


## 174 — `embodied_112_E2B`

**原始英文指令：** At 30.0 seconds, position the visible index fingertip two centimeters directly above the curved silver intake pipe.

**中文翻译：** 在第 30.0 秒，将可见的食指指尖放在弯曲银色进气管正上方两厘米处。

**状态：** 接受

**原子化判定句：**

1. 可见的食指指尖是否被放在弯曲银色进气管正上方两厘米处？


## 175 — `embodied_115_E1`

**原始英文指令：** Starting at 15.0 seconds, guide the pencil in one deliberate left-to-right pointing sweep across the diagram over 4 seconds.

**中文翻译：** 从第 15.0 秒开始，引导铅笔在四秒内沿图示完成一次明确的从左向右指示扫动。

**状态：** 接受

**原子化判定句：**

1. 铅笔是否沿图示完成一次明确的从左向右指示扫动？

2. 该扫动是否在 4 秒内完成？


## 176 — `embodied_115_E2A`

**原始英文指令：** At 30.0 seconds, render only the fine pencil with a hand-painted illustration treatment for the remaining footage.

**中文翻译：** 在第 30.0 秒，仅将细铅笔渲染为手绘插画风格，并保持至剩余视频结束。

**状态：** 接受

**原子化判定句：**

1. 细铅笔是否被渲染为手绘插画风格？

2. 手绘效果是否仅作用于细铅笔？

3. 该效果是否保持至剩余视频结束？


## 177 — `embodied_115_E2B`

**原始英文指令：** At 30.0 seconds, change the non-text surfaces of the fine pencil to warm ivory for the rest of the scene.

**中文翻译：** 在第 30.0 秒，将细铅笔上不含文字的表面变为暖象牙色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 细铅笔上不含文字的表面是否变为暖象牙色？

2. 暖象牙色外观是否保持至场景结束？


## 178 — `embodied_119_E1`

**原始英文指令：** Starting at 18.0 seconds, continue riding straight along the center of the current lane for four seconds while following the bus.

**中文翻译：** 从第 18.0 秒开始，在跟随公交车的同时，继续沿当前车道中央直行四秒。

**状态：** 接受

**原子化判定句：**

1. 骑行者是否继续沿当前车道中央直行并持续 4 秒？

2. 在这 4 秒内是否一直跟随公交车？


## 179 — `embodied_119_E2A`

**原始英文指令：** Starting at 33.0 seconds, make the white-yellow bus accelerate forward by two bus lengths within its current lane over four seconds.

**中文翻译：** 从第 33.0 秒开始，让白黄色公交车在四秒内沿当前车道加速前进两个车身长度。

**状态：** 接受

**原子化判定句：**

1. 白黄色公交车是否在 4 秒内加速前进两个车身长度？

2. 公交车在加速时是否保持在当前车道内？


## 180 — `embodied_119_E2B`

**原始英文指令：** Starting at 33.0 seconds, make the white-yellow bus decelerate within its current lane until its front falls one car length behind the motorcycle over four seconds.

**中文翻译：** 从第 33.0 秒开始，让白黄色公交车在当前车道内减速，并在四秒内使车头落到摩托车后方一个车身长度处。

**状态：** 接受

**原子化判定句：**

1. 白黄色公交车是否减速并持续 4 秒？

2. 公交车在减速时是否保持在当前车道内？

3. 公交车车头是否在这 4 秒内落到摩托车后方一个车身长度处？


## 181 — `embodied_122_E1`

**原始英文指令：** At 17.0 seconds, place the cooked meat pile beside the noodle mound in the wok with a gap equal to half the meat pile's width.

**中文翻译：** 在第 17.0 秒，将熟肉堆放在炒锅中的面条堆旁边，两者之间留出相当于半个肉堆宽度的间隙。

**状态：** 接受

**原子化判定句：**

1. 熟肉堆是否被放在炒锅中的面条堆旁边？

2. 两者之间的间隙是否等于半个肉堆宽度？


## 182 — `embodied_122_E2A`

**原始英文指令：** Starting at 32.0 seconds, slow transferring more cooked noodles from the basket into the wok so the amount of cooked noodles transferred into the wok at 37.0 seconds is reached at 41.0 seconds.

**中文翻译：** 从第 32.0 秒开始，减慢将更多熟面条从篮子转移到炒锅中的速度，使原本在第 37.0 秒达到的转移量延后到第 41.0 秒达到。

**状态：** 接受

**原子化判定句：**

1. 是否将更多熟面条从篮子转移到炒锅中？

2. 转移速度是否被减慢，使原本在片段开始后 5 秒达到的转移量改为在 9 秒后达到？


## 183 — `embodied_122_E2B`

**原始英文指令：** At 32.0 seconds, remove the small metal pot containing the remaining cooked meat at the upper-right edge from the visible scene.

**中文翻译：** 在第 32.0 秒，将右上边缘装有剩余熟肉的小金属锅从可见场景中移除。

**状态：** 接受

**原子化判定句：**

1. 右上边缘装有剩余熟肉的小金属锅是否从可见场景中被移除？


## 184 — `embodied_123_E1`

**原始英文指令：** At 14.0 seconds, render only the visible hands and forearms with cel-shaded game-character treatment during lifting and supporting the moving lizard.

**中文翻译：** 在第 14.0 秒，在抬起并托住正在移动的蜥蜴时，仅将可见的双手和前臂渲染为卡通渲染的游戏角色风格。

**状态：** 接受

**原子化判定句：**

1. 正在移动的蜥蜴是否被抬起？

2. 蜥蜴在移动时是否被托住？

3. 在这些动作期间，可见的双手和前臂是否被渲染为卡通渲染的游戏角色风格？

4. 卡通渲染效果是否仅作用于可见的双手和前臂？


## 185 — `embodied_123_E2A`

**原始英文指令：** Starting at 29.0 seconds, walk steadily along the visible room path while supporting the large patterned lizard for 4 seconds.

**中文翻译：** 从第 29.0 秒开始，沿房间中可见的路径稳定行走四秒，同时托住大型花纹蜥蜴。

**状态：** 接受

**原子化判定句：**

1. 人物是否沿房间中可见的路径稳定行走并持续 4 秒？

2. 人物行走时是否托住大型花纹蜥蜴？


## 186 — `embodied_123_E2B`

**原始英文指令：** At 29.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during carrying the lizard across the room before the camera loses it.

**中文翻译：** 在第 29.0 秒，在相机失去蜥蜴踪迹之前将其抱过房间时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 在相机失去蜥蜴踪迹之前，蜥蜴是否被抱过房间？

2. 相机随后是否失去蜥蜴的踪迹？

3. 在抱着蜥蜴移动时，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 187 — `embodied_124_E1`

**原始英文指令：** At 15.0 seconds, position the seated woman's nearest visible fingertip two centimeters above the young fox's shoulder.

**中文翻译：** 在第 15.0 秒，将坐着的女子最近的可见指尖放在幼狐肩部上方两厘米处。

**状态：** 接受

**原子化判定句：**

1. 坐着的女子最近的可见指尖是否被放在幼狐肩部上方两厘米处？


## 188 — `embodied_124_E2A`

**原始英文指令：** At 41.0 seconds, add one shallow ceramic treat dish immediately beside the woman's trousered leg during following a young red fox as it explores a room.

**中文翻译：** 在第 41.0 秒，在跟随一只探索房间的幼年红狐时，紧邻女子穿裤子的腿旁添加一个浅陶瓷零食盘。

**状态：** 接受

**原子化判定句：**

1. 幼年红狐是否探索房间？

2. 红狐探索时是否被跟随？

3. 在跟随红狐时，是否紧邻女子穿裤子的腿旁添加了一个浅陶瓷零食盘？


## 189 — `embodied_124_E2B`

**原始英文指令：** Starting at 29.0 seconds, advance the foreground hand toward the fox's nose in one smooth arc over two seconds, then retract over one second.

**中文翻译：** 从第 29.0 秒开始，让前景中的手沿一条平滑弧线在两秒内伸向狐狸鼻子，然后用一秒缩回。

**状态：** 接受

**原子化判定句：**

1. 前景中的手是否沿一条平滑弧线在 2 秒内伸向狐狸鼻子？

2. 该手是否随后在接下来的 1 秒内缩回？


## 190 — `embodied_126_E1`

**原始英文指令：** At 19.0 seconds, switch to a third-person viewpoint behind the observer's right shoulder while the standing angler holds the large fish upright at the bow.

**中文翻译：** 在第 19.0 秒，当站立的垂钓者在船头竖直举着大鱼时，将视角切换为位于观察者右肩后方的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 站立的垂钓者是否在船头竖直举着大鱼？

2. 在竖直举鱼时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方？


## 191 — `embodied_126_E2A`

**原始英文指令：** Starting at 39.0 seconds, make the boat-edge water circulate clockwise in one visible current for 4 seconds during casting the fishing rod toward the wooded shore.

**中文翻译：** 从第 39.0 秒开始，在将鱼竿抛向林木岸边时，让船边的水形成一股可见的顺时针水流并循环四秒。

**状态：** 接受

**原子化判定句：**

1. 鱼竿是否被抛向林木岸边？

2. 在抛竿时，船边的水是否形成一股可见的顺时针水流并循环 4 秒？


## 192 — `embodied_126_E2B`

**原始英文指令：** Starting at 34.0 seconds, make the water along the boat's left edge circulate counterclockwise in one visible current for four seconds.

**中文翻译：** 从第 34.0 秒开始，让船左侧边缘的水形成一股可见的逆时针水流并循环四秒。

**状态：** 接受

**原子化判定句：**

1. 船左侧边缘的水是否形成一股可见水流并循环？

2. 水流是否沿逆时针方向循环？

3. 循环是否持续 4 秒？


## 193 — `embodied_127_E1`

**原始英文指令：** At 19.0 seconds, switch to a third-person viewpoint behind the observer's right shoulder during the final close display of the boxed model cars.

**中文翻译：** 在第 19.0 秒，在最后近距离展示盒装模型车时，将视角切换为位于观察者右肩后方的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 盒装模型车是否进行最后的近距离展示？

2. 在最后近距离展示时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方？


## 194 — `embodied_127_E2A`

**原始英文指令：** At 28.0 seconds, change only the clear protective sleeves around the bagged comics to translucent smoke gray for the rest of the scene.

**中文翻译：** 在第 28.0 秒，仅将袋装漫画外的透明保护套变为半透明烟灰色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 袋装漫画外的透明保护套是否变为半透明烟灰色？

2. 该变化是否仅作用于这些保护套？

3. 半透明烟灰色外观是否保持至场景结束？


## 195 — `embodied_127_E2B`

**原始英文指令：** At 34.0 seconds, position the visible hand in the lower-right frame quadrant, one palm-width from the black outer frame around the red insert.

**中文翻译：** 在第 34.0 秒，将可见的手放在画面右下象限，并与红色嵌件周围的黑色外框相距一个手掌宽。

**状态：** 接受

**原子化判定句：**

1. 可见的手是否被放在画面右下象限？

2. 该手与红色嵌件周围的黑色外框之间是否相距一个手掌宽？


## 196 — `embodied_128_E1`

**原始英文指令：** At 19.8 seconds, make the small ceramic cup water-repellent so visible droplets bead and roll off immediately.

**中文翻译：** 在第 19.8 秒，使小陶瓷杯具有拒水性，让可见水滴聚成水珠并立即滚落。

**状态：** 接受

**原子化判定句：**

1. 小陶瓷杯是否变得具有拒水性？

2. 可见水滴是否在杯子上聚成水珠？

3. 形成的水珠是否立即滚落？


## 197 — `embodied_128_E2A`

**原始英文指令：** Starting at 39.0 seconds, lean the trunk twenty centimeters toward the drinking glass over 2 seconds, then return along the same path over 2 seconds.

**中文翻译：** 从第 39.0 秒开始，在两秒内将躯干朝饮水玻璃杯倾斜二十厘米，然后用两秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝饮水玻璃杯倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内沿原路径返回？


## 198 — `embodied_128_E2B`

**原始英文指令：** At 34.8 seconds, position the center of the striped dish towel directly below the horizontal silver drawer handle with a two-centimeter vertical gap.

**中文翻译：** 在第 34.8 秒，将条纹餐巾的中心放在水平银色抽屉把手正下方，并留出两厘米的垂直间距。

**状态：** 接受

**原子化判定句：**

1. 条纹餐巾的中心是否被放在水平银色抽屉把手正下方？

2. 餐巾中心与把手之间是否留有两厘米的垂直间距？


## 199 — `embodied_130_E1`

**原始英文指令：** Starting at 17.0 seconds, perform a two-second optical push-in to a stable close-up centered on the orange frame arm.

**中文翻译：** 从第 17.0 秒开始，进行一次持续两秒的光学推进，最终形成以橙色框架臂为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以橙色框架臂为中心的稳定特写？


## 200 — `embodied_130_E2A`

**原始英文指令：** At 32.0 seconds, split the white upper plate into two equal rectangular modules with clean matching inner edges.

**中文翻译：** 在第 32.0 秒，将白色上板拆分为两个大小相等的矩形模块，并形成干净且相互匹配的内侧边缘。

**状态：** 接受

**原子化判定句：**

1. 白色上板是否被拆分为两个矩形模块？

2. 两个模块的大小是否相等？

3. 两个模块的内侧边缘是否干净？

4. 两条内侧边缘是否彼此匹配？


## 201 — `embodied_130_E2B`

**原始英文指令：** At 32.0 seconds, render the full visible scene as a restrained watercolor illustration during installing black spool units around the upper corners.

**中文翻译：** 在第 32.0 秒，在上方各角安装黑色线轴单元时，将整个可见场景渲染为色彩克制的水彩插画。

**状态：** 接受

**原子化判定句：**

1. 黑色线轴单元是否被安装在上方各角？

2. 在安装过程中，整个可见场景是否被渲染为色彩克制的水彩插画？


## 202 — `embodied_133_E1`

**原始英文指令：** At 15.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during moving the cooked mixture into serving position.

**中文翻译：** 在第 15.0 秒，在将熟制混合物移到上菜位置时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 熟制混合物是否被移到上菜位置？

2. 在移动熟制混合物时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 203 — `embodied_133_E2A`

**原始英文指令：** At 30.0 seconds, coat the working face of the long-handled spoon with a thin, even film of cooking juices.

**中文翻译：** 在第 30.0 秒，在长柄勺的工作面上覆盖一层薄而均匀的烹饪汁液。

**状态：** 接受

**原子化判定句：**

1. 长柄勺的工作面是否覆盖有一层薄薄的烹饪汁液？

2. 烹饪汁液膜是否均匀？


## 204 — `embodied_133_E2B`

**原始英文指令：** Starting at 30.0 seconds, lean the trunk twenty centimeters toward the two white plates over 2 seconds, then return along the same path over 2 seconds.

**中文翻译：** 从第 30.0 秒开始，在两秒内将躯干朝两个白色盘子倾斜二十厘米，然后用两秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝两个白色盘子倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内沿原路径返回？


## 205 — `embodied_137_E1`

**原始英文指令：** At 19.0 seconds, replace the orange-faced cube with a same-size wooden three-layer twisty cube with orange, white, blue, and green faces in the same task location.

**中文翻译：** 在第 19.0 秒，将带橙色面的立方体替换为一个同样大小、具有橙白蓝绿各色面的木制三层扭转魔方，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 带橙色面的立方体是否被替换为具有橙白蓝绿各色面的木制三层扭转魔方？

2. 替换后的魔方是否与原立方体大小相同？

3. 替换后的魔方是否具有三层结构？

4. 替换后的魔方是否位于原立方体所在的任务位置？


## 206 — `embodied_137_E2A`

**原始英文指令：** At 34.0 seconds, position the cube's orange tiled face in the right third of the frame at its current working depth.

**中文翻译：** 在第 34.0 秒，将魔方的橙色拼块面放在画面右侧三分之一区域，并保持当前工作景深。

**状态：** 接受

**原子化判定句：**

1. 魔方的橙色拼块面是否被放在画面右侧三分之一区域？

2. 魔方是否保持当前工作景深？


## 207 — `embodied_137_E2B`

**原始英文指令：** At 34.0 seconds, change only the recessed grid seams between the front-facing orange wooden tiles to brushed silver.

**中文翻译：** 在第 34.0 秒，仅将朝向画面的橙色木质拼块之间凹陷的网格接缝变为拉丝银色。

**状态：** 接受

**原子化判定句：**

1. 朝向画面的橙色木质拼块之间凹陷的网格接缝是否变为拉丝银色？

2. 拉丝银色变化是否仅作用于这些凹陷的网格接缝？


## 208 — `embodied_138_E1`

**原始英文指令：** At 15.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during pointing across plant fragments seeds and gourds.

**中文翻译：** 在第 15.0 秒，在依次指示植物碎片、种子和葫芦时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 是否依次指示了植物碎片、种子和葫芦？

2. 在进行指示时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 209 — `embodied_138_E2A`

**原始英文指令：** Starting at 30.0 seconds, lean the trunk twenty centimeters toward the large double-lobed gourd over 2 seconds, then return along the same path over 2 seconds.

**中文翻译：** 从第 30.0 秒开始，在两秒内将躯干朝大型双叶形葫芦倾斜二十厘米，然后用两秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝大型双叶形葫芦倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内沿原路径返回？


## 210 — `embodied_138_E2B`

**原始英文指令：** At 30.0 seconds, illuminate the visible working area with soft neutral overhead light at an even exposure during presenting dried plant material and a hollow gourd.

**中文翻译：** 在第 30.0 秒，在展示干燥植物材料和空心葫芦时，用柔和的中性顶光均匀照亮可见工作区域。

**状态：** 接受

**原子化判定句：**

1. 干燥植物材料是否被展示？

2. 空心葫芦是否被展示？

3. 在展示过程中，可见工作区域是否受到柔和中性顶光的均匀照明？


## 211 — `embodied_141_E1`

**原始英文指令：** At 15.5 seconds, position the nearest visible fingertip two centimeters above the open cap of the rightmost dark-blue bottle.

**中文翻译：** 在第 15.5 秒，将最近的可见指尖放在最右侧深蓝色瓶子打开的瓶盖上方两厘米处。

**状态：** 接受

**原子化判定句：**

1. 最近的可见指尖是否被放在最右侧深蓝色瓶子打开的瓶盖上方两厘米处？


## 212 — `embodied_141_E2A`

**原始英文指令：** At 42.0 seconds, merge the white drinking tube with the green lid connector into one continuous fitted assembly.

**中文翻译：** 在第 42.0 秒，将白色饮水管与绿色盖子连接件合并为一个连续贴合的组件。

**状态：** 接受

**原子化判定句：**

1. 白色饮水管与绿色盖子连接件是否合并为一个组件？

2. 合并后的组件是否连续且相互贴合？


## 213 — `embodied_141_E2B`

**原始英文指令：** At 30.5 seconds, cover the exterior of the orange drink bottle with a thin, even layer of visible condensation.

**中文翻译：** 在第 30.5 秒，让橙色饮料瓶的外表面覆盖一层薄而均匀的可见冷凝水。

**状态：** 接受

**原子化判定句：**

1. 橙色饮料瓶的外表面是否覆盖有一层薄薄的可见冷凝水？

2. 冷凝水层是否均匀？


## 214 — `embodied_142_E1`

**原始英文指令：** At 15.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during reeling slowly with the rod aimed over the lake.

**中文翻译：** 在第 15.0 秒，在鱼竿指向湖面并缓慢收线时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 鱼竿是否指向湖面？

2. 鱼线是否被缓慢收回？

3. 在缓慢收线时，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 215 — `embodied_142_E2A`

**原始英文指令：** At 30.0 seconds, make the lake surface completely calm and mirror-smooth with no visible ripples for the rest of the visible scene.

**中文翻译：** 在第 30.0 秒，使湖面完全平静且如镜面般光滑，不出现任何可见波纹，并保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 湖面是否变得完全平静且如镜面般光滑？

2. 湖面上是否没有任何可见波纹？

3. 该状态是否保持至可见场景结束？


## 216 — `embodied_142_E2B`

**原始英文指令：** Starting at 30.0 seconds, rotate the torso twenty degrees toward the casting side over two seconds, then return over two seconds.

**中文翻译：** 从第 30.0 秒开始，在两秒内将躯干朝抛竿侧转动二十度，然后用两秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝抛竿侧转动二十度？

2. 躯干是否随后在接下来的 2 秒内恢复原朝向？


## 217 — `embodied_143_E1`

**原始英文指令：** At 19.0 seconds, switch to a third-person viewpoint behind the observer's right shoulder while the remaining onion and utensils are handled on the board.

**中文翻译：** 在第 19.0 秒，在砧板上处理剩余洋葱和厨具时，将视角切换为位于观察者右肩后方的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 剩余洋葱是否在砧板上被处理？

2. 厨具是否在砧板上被操作？

3. 在这些动作期间，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方？


## 218 — `embodied_143_E2A`

**原始英文指令：** At 42.0 seconds, make the exterior of the cleaner bottle visibly chilled with a thin, even condensation layer for the rest of the visible scene.

**中文翻译：** 在第 42.0 秒，使清洁剂瓶的外表面呈现明显冰凉的状态，并带有一层薄而均匀的冷凝水，且该状态保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 清洁剂瓶的外表面是否呈现明显冰凉的状态并出现一层薄冷凝水？

2. 冷凝水层在瓶子的可见外表面上是否分布均匀？

3. 冰凉且带冷凝水的外观是否保持至可见场景结束？


## 219 — `embodied_143_E2B`

**原始英文指令：** Starting at 30.0 seconds, lean the torso twenty centimeters toward the sink-side yellow cleaner bottle over 1.5 seconds, then return over 1.5 seconds.

**中文翻译：** 从第 30.0 秒开始，在 1.5 秒内将躯干朝水槽旁的黄色清洁剂瓶倾斜二十厘米，然后用 1.5 秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 1.5 秒内朝水槽旁的黄色清洁剂瓶倾斜二十厘米？

2. 躯干是否随后在接下来的 1.5 秒内回到原位？


## 220 — `embodied_147_E1`

**原始英文指令：** At 16.0 seconds, add one small clear sample vial on the work surface below the shaking bottle.

**中文翻译：** 在第 16.0 秒，在正在摇晃的瓶子下方工作台面上添加一个小型透明样品瓶。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型透明样品瓶？

2. 样品瓶是否位于正在摇晃的瓶子下方工作台面上？


## 221 — `embodied_147_E2A`

**原始英文指令：** At 31.0 seconds, make the liquid uniformly clouded with dense, fine suspended bubbles during the remaining shaking.

**中文翻译：** 在第 31.0 秒，在剩余摇晃过程中，使液体因浓密细小的悬浮气泡而均匀浑浊。

**状态：** 接受

**原子化判定句：**

1. 瓶子是否继续被摇晃？

2. 在剩余摇晃过程中，液体是否因浓密细小的悬浮气泡而变得均匀浑浊？


## 222 — `embodied_147_E2B`

**原始英文指令：** At 31.0 seconds, orient the clear bottle and attached blue cap with their shared longitudinal axis thirty degrees toward frame-left during subsequent shaking.

**中文翻译：** 在第 31.0 秒，在后续摇晃过程中，将透明瓶和相连蓝色瓶盖的共同纵轴朝画面左侧偏转三十度。

**状态：** 接受

**原子化判定句：**

1. 后续摇晃是否发生？

2. 在摇晃过程中，透明瓶和相连蓝色瓶盖的共同纵轴是否朝画面左侧偏转三十度？


## 223 — `embodied_148_E1`

**原始英文指令：** At 19.0 seconds, switch to a third-person viewpoint behind the observer's right shoulder while moving toward the sink with the yellow packet.

**中文翻译：** 在第 19.0 秒，在拿着黄色包装袋走向水槽时，将视角切换为位于观察者右肩后方的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 观察者是否拿着黄色包装袋走向水槽？

2. 在该移动过程中，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方？


## 224 — `embodied_148_E2A`

**原始英文指令：** At 36.0 seconds, replace the yellow seasoning packet with a clear resealable food pouch in the same task location.

**中文翻译：** 在第 36.0 秒，将黄色调味料包装袋替换为透明可重复密封食品袋，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 黄色调味料包装袋是否被替换为透明可重复密封食品袋？

2. 替换后的食品袋是否位于原调味料包装袋所在的任务位置？


## 225 — `embodied_148_E2B`

**原始英文指令：** Starting at 34.0 seconds, lean the torso twenty centimeters toward the yellow seasoning packet over two seconds, then return over two seconds.

**中文翻译：** 从第 34.0 秒开始，在两秒内将躯干朝黄色调味料包装袋倾斜二十厘米，然后用两秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝黄色调味料包装袋倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内回到原位？


## 226 — `embodied_151_E1`

**原始英文指令：** At 19.5 seconds, remove the isolated oval plant leaf immediately to frame-right of the chameleon's head from the visible scene.

**中文翻译：** 在第 19.5 秒，将紧邻变色龙头部画面右侧的孤立椭圆形植物叶片从可见场景中移除。

**状态：** 接受

**原子化判定句：**

1. 紧邻变色龙头部画面右侧的孤立椭圆形植物叶片是否从可见场景中被移除？


## 227 — `embodied_151_E2A`

**原始英文指令：** Starting at 30.0 seconds, walk steadily along the visible room path toward the sunlit window plant for five seconds with the chameleon supported on the hand.

**中文翻译：** 从第 30.0 秒开始，沿房间中可见的路径朝阳光照射的窗边植物稳定行走五秒，同时用手托住变色龙。

**状态：** 接受

**原子化判定句：**

1. 人物是否沿房间中可见的路径朝阳光照射的窗边植物稳定行走并持续 5 秒？

2. 人物行走时，变色龙是否被托在手上？


## 228 — `embodied_151_E2B`

**原始英文指令：** At 34.5 seconds, render only the visible hands and forearms carrying the chameleon with a cel-shaded game-character treatment.

**中文翻译：** 在第 34.5 秒，在双手和前臂携带变色龙时，仅将这些可见部位渲染为卡通渲染的游戏角色风格。

**状态：** 接受

**原子化判定句：**

1. 变色龙是否由可见的双手和前臂携带？

2. 在携带变色龙时，可见的双手和前臂是否被渲染为卡通渲染的游戏角色风格？

3. 卡通渲染效果是否仅作用于可见的双手和前臂？


## 229 — `embodied_152_E1`

**原始英文指令：** Starting at 19.0 seconds, lean the torso twenty centimeters toward the green stalks on the cutting board over 1.5 seconds, then return over 1.5 seconds.

**中文翻译：** 从第 19.0 秒开始，在 1.5 秒内将躯干朝砧板上的绿色茎秆倾斜二十厘米，然后用 1.5 秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 1.5 秒内朝砧板上的绿色茎秆倾斜二十厘米？

2. 躯干是否随后在接下来的 1.5 秒内回到原位？


## 230 — `embodied_152_E2A`

**原始英文指令：** At 30.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during chopping and transferring the small pieces into the nearby pot.

**中文翻译：** 在第 30.0 秒，在切碎并将小块转移到附近锅中时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 小块是否被切碎？

2. 切碎的小块是否被转移到附近的锅中？

3. 在切碎和转移过程中，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 231 — `embodied_152_E2B`

**原始英文指令：** At 34.0 seconds, coat the working face of the kitchen knife with a thin, even film of green vegetable moisture.

**中文翻译：** 在第 34.0 秒，在厨刀的工作面上覆盖一层薄而均匀的绿色蔬菜汁液。

**状态：** 接受

**原子化判定句：**

1. 厨刀的工作面是否覆盖有一层薄薄的绿色蔬菜汁液？

2. 蔬菜汁液膜是否均匀？


## 232 — `embodied_153_E1`

**原始英文指令：** At 17.0 seconds, render the full visible scene as a restrained watercolor illustration during lowering and turning the net around the animal.

**中文翻译：** 在第 17.0 秒，在动物周围放低并转动网具时，将整个可见场景渲染为色彩克制的水彩插画。

**状态：** 接受

**原子化判定句：**

1. 网具是否在动物周围被放低？

2. 网具是否在动物周围被转动？

3. 在这些动作期间，整个可见场景是否被渲染为色彩克制的水彩插画？


## 233 — `embodied_153_E2A`

**原始英文指令：** At 32.0 seconds, add soft warm side lighting from frame-left across the amphibian, green net, and surrounding grass.

**中文翻译：** 在第 32.0 秒，从画面左侧加入柔和的暖色侧光，照亮两栖动物、绿色网具和周围草地。

**状态：** 接受

**原子化判定句：**

1. 场景中是否加入柔和的暖色侧光？

2. 新增光线是否来自画面左侧？

3. 新增光线是否覆盖两栖动物、绿色网具和周围草地？


## 234 — `embodied_153_E2B`

**原始英文指令：** At 32.0 seconds, add one shallow ceramic dish on the clear grass immediately outside the frame-left side of the white net hoop.

**中文翻译：** 在第 32.0 秒，在白色网圈画面左侧正外方的空旷草地上添加一个浅陶瓷盘。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个浅陶瓷盘？

2. 该盘是否被放在白色网圈画面左侧正外方的空旷草地上？


## 235 — `embodied_157_E1`

**原始英文指令：** At 19.0 seconds, remove the tiny green chameleon standing on the supporting thumb from the visible scene.

**中文翻译：** 在第 19.0 秒，将站在支撑拇指上的微小绿色变色龙从可见场景中移除。

**状态：** 接受

**原子化判定句：**

1. 站在支撑拇指上的微小绿色变色龙是否从可见场景中被移除？


## 236 — `embodied_157_E2A`

**原始英文指令：** At 34.0 seconds, position the nearest free fingertip two centimeters beside the tiny green chameleon.

**中文翻译：** 在第 34.0 秒，将最近的空闲指尖放在微小绿色变色龙旁边两厘米处。

**状态：** 接受

**原子化判定句：**

1. 最近的空闲指尖是否被放在微小绿色变色龙旁边两厘米处？


## 237 — `embodied_157_E2B`

**原始英文指令：** At 34.0 seconds, change the visible thumbnail of the supporting hand to glossy coral red.

**中文翻译：** 在第 34.0 秒，将支撑手可见的拇指甲变为有光泽的珊瑚红色。

**状态：** 接受

**原子化判定句：**

1. 支撑手可见的拇指甲是否变为珊瑚红色？

2. 变色后的拇指甲是否具有光泽？


## 238 — `embodied_160_E1`

**原始英文指令：** At 19.0 seconds, change the graphite linework of the first drawn eye and brow to deep violet.

**中文翻译：** 在第 19.0 秒，将第一个画出的眼睛和眉毛的石墨线条变为深紫色。

**状态：** 接受

**原子化判定句：**

1. 第一个画出的眼睛的石墨线条是否变为深紫色？

2. 第一个画出的眉毛的石墨线条是否变为深紫色？


## 239 — `embodied_160_E2A`

**原始英文指令：** At 43.0 seconds, place the active black pen tip at the midpoint of the second eye's lower eyelid line.

**中文翻译：** 在第 43.0 秒，将正在使用的黑色笔尖放在第二只眼睛下眼睑线的中点。

**状态：** 接受

**原子化判定句：**

1. 正在使用的黑色笔尖是否被放在第二只眼睛下眼睑线的中点？


## 240 — `embodied_160_E2B`

**原始英文指令：** At 34.0 seconds, slow the second-eye drawing when it begins near 41.0 seconds so the linework visible at 44.0 seconds is reached at 45.0 seconds.

**中文翻译：** 在第 34.0 秒进行编辑，当第二只眼睛的绘制在接近第 41.0 秒开始时将其减慢，使原本第 44.0 秒可见的线条状态延后到第 45.0 秒达到。

**状态：** 接受

**原子化判定句：**

1. 第二只眼睛的绘制是否在片段开始约 7 秒后开始？

2. 第二只眼睛开始绘制时，绘制速度是否被减慢？

3. 原本在片段开始后 10 秒可见的线条状态是否改为在 11 秒后达到？


## 241 — `embodied_161_E1`

**原始英文指令：** At 19.0 seconds, make the visible wet region near the green bottle neck form a thin, even transparent film without downward streaks.

**中文翻译：** 在第 19.0 秒，使绿色瓶颈附近可见的湿润区域形成一层薄而均匀的透明膜，且不出现向下流痕。

**状态：** 接受

**原子化判定句：**

1. 绿色瓶颈附近可见的湿润区域是否形成一层薄透明膜？

2. 透明膜是否均匀？

3. 透明膜中是否没有向下流痕？


## 242 — `embodied_161_E2A`

**原始英文指令：** Starting at 34.0 seconds, sweep the blue-handled brush downward across the green bottle shoulder in one broad controlled stroke over 4 seconds.

**中文翻译：** 从第 34.0 秒开始，用蓝色手柄刷沿绿色瓶肩向下完成一次宽幅受控的扫动，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 蓝色手柄刷是否沿绿色瓶肩向下扫动？

2. 该动作是否为一次宽幅受控的笔触？

3. 该笔触是否在 4 秒内完成？


## 243 — `embodied_161_E2B`

**原始英文指令：** At 34.0 seconds, place the blue-handled brush tip against the upper-right shoulder of the green bottle.

**中文翻译：** 在第 34.0 秒，将蓝色手柄刷的刷尖贴在绿色瓶子的右上肩部。

**状态：** 接受

**原子化判定句：**

1. 蓝色手柄刷的刷尖是否贴在绿色瓶子的右上肩部？


## 244 — `embodied_166_E1`

**原始英文指令：** At 15.0 seconds, render only the blank whiteboard canvas behind the animated graphics as lightly textured recycled paper.

**中文翻译：** 在第 15.0 秒，仅将动画图形后方空白的白板画布渲染为带有轻微纹理的再生纸。

**状态：** 接受

**原子化判定句：**

1. 动画图形后方空白的白板画布是否被渲染为带有轻微纹理的再生纸？

2. 再生纸渲染是否仅作用于空白白板画布？


## 245 — `embodied_166_E2A`

**原始英文指令：** Starting at 30.0 seconds, perform a two-second optical push-in to a stable close-up centered on the passport graphic.

**中文翻译：** 从第 30.0 秒开始，进行一次持续两秒的光学推进，最终形成以护照图形为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以护照图形为中心的稳定特写？


## 246 — `embodied_166_E2B`

**原始英文指令：** At 30.0 seconds, apply a high-contrast monochrome graphic treatment across the full scene during revealing passport and document graphics beside the building.

**中文翻译：** 在第 30.0 秒，在建筑旁揭示护照和文件图形时，为整个场景应用高对比度的单色图形化效果。

**状态：** 接受

**原子化判定句：**

1. 护照图形是否在建筑旁被揭示？

2. 文件图形是否在建筑旁被揭示？

3. 在揭示过程中，整个场景是否应用了高对比度的单色图形化效果？


## 247 — `embodied_169_E1`

**原始英文指令：** Starting at 19.0 seconds, shift the torso twenty centimeters toward the firing line over 1.5 seconds, then return over 1.5 seconds.

**中文翻译：** 从第 19.0 秒开始，在 1.5 秒内将躯干朝射击线移动二十厘米，然后用 1.5 秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 1.5 秒内朝射击线移动二十厘米？

2. 躯干是否随后在接下来的 1.5 秒内回到原位？


## 248 — `embodied_169_E2A`

**原始英文指令：** At 34.0 seconds, position the long firearm front sight directly below the central orange target with one target-height of vertical separation.

**中文翻译：** 在第 34.0 秒，将长枪前准星放在中央橙色靶标正下方，并保持一个靶标高度的垂直间距。

**状态：** 接受

**原子化判定句：**

1. 长枪前准星是否被放在中央橙色靶标正下方？

2. 两者的垂直间距是否等于一个靶标高度？


## 249 — `embodied_169_E2B`

**原始英文指令：** At 34.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder during firing the long firearm before lowering it near the equipment table.

**中文翻译：** 在第 34.0 秒，在发射长枪并随后将其放低到设备桌附近时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 长枪是否被发射？

2. 长枪是否随后被放低到设备桌附近？

3. 在发射且尚未放低长枪时，视角是否切换为第三人称视角？

4. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 250 — `embodied_171_E1`

**原始英文指令：** Starting at 17.0 seconds, ride steadily forward within the current lane toward the red bus for 4 seconds.

**中文翻译：** 从第 17.0 秒开始，在当前车道内朝红色公交车稳定向前骑行四秒。

**状态：** 接受

**原子化判定句：**

1. 骑行者是否朝红色公交车稳定向前骑行？

2. 骑行者是否保持在当前车道内？

3. 骑行是否持续 4 秒？


## 251 — `embodied_171_E2A`

**原始英文指令：** Starting at 32.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the motorcycle handlebars over 4 seconds.

**中文翻译：** 从第 32.0 秒开始，在四秒内将第一人称视点朝摩托车车把方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 4 秒内向右移动半米？

2. 第一人称视点是否在同一段 4 秒内降低二十五厘米？

3. 视点是否朝摩托车车把方向移动？


## 252 — `embodied_171_E2B`

**原始英文指令：** At 32.0 seconds, change the non-text surfaces of the motorcycle handlebars to satin forest green for the rest of the scene.

**中文翻译：** 在第 32.0 秒，将摩托车车把上不含文字的表面变为缎面森林绿色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 摩托车车把上不含文字的表面是否变为森林绿色？

2. 发生变化的表面是否呈缎面质感？

3. 缎面森林绿色外观是否保持至场景结束？


## 253 — `embodied_172_E1`

**原始英文指令：** At 19.0 seconds, change the non-text surfaces of the black molded panel to deep violet for the rest of the scene.

**中文翻译：** 在第 19.0 秒，将黑色模制面板上不含文字的表面变为深紫色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 黑色模制面板上不含文字的表面是否变为深紫色？

2. 深紫色外观是否保持至场景结束？


## 254 — `embodied_172_E2A`

**原始英文指令：** Starting at 24.0 seconds, slide the small black retaining clip downward along the molded panel edge over 3 seconds.

**中文翻译：** 从第 24.0 秒开始，让黑色小固定夹沿模制面板边缘向下滑动，并在三秒内完成。

**状态：** 接受

**原子化判定句：**

1. 黑色小固定夹是否向下滑动？

2. 固定夹是否沿模制面板边缘滑动？

3. 滑动是否在 3 秒内完成？


## 255 — `embodied_172_E2B`

**原始英文指令：** At 34.0 seconds, split the black molded panel into two separate equal-sized panels with a clean dividing edge.

**中文翻译：** 在第 34.0 秒，将黑色模制面板拆分为两个彼此分离、大小相等且分割边缘干净的面板。

**状态：** 接受

**原子化判定句：**

1. 黑色模制面板是否被拆分为两个面板？

2. 拆分后的两个面板是否彼此分离？

3. 两个面板的大小是否相等？

4. 分割边缘是否干净？


## 256 — `embodied_174_E1`

**原始英文指令：** Starting at 19.0 seconds, rotate the mounted black circular rear-axle accessory clockwise through one wider calibration arc over 4 seconds.

**中文翻译：** 从第 19.0 秒开始，让已安装的黑色圆形后轴附件沿一条更宽的校准弧线顺时针转动，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 已安装的黑色圆形后轴附件是否顺时针旋转？

2. 该附件是否转过一条更宽的校准弧线？

3. 旋转是否在 4 秒内完成？


## 257 — `embodied_174_E2A`

**原始英文指令：** At 32.0 seconds, remove the left bicycle pedal outside the rear-axle work area completely from the visible scene during tightening and orienting the accessory outside the rear axle.

**中文翻译：** 在第 32.0 秒，在后轴外侧拧紧并调整附件朝向时，将后轴工作区外的左侧自行车踏板从可见场景中完全移除。

**状态：** 接受

**原子化判定句：**

1. 后轴外侧的附件是否被拧紧？

2. 后轴外侧附件的朝向是否被调整？

3. 在这些动作期间，后轴工作区外的左侧自行车踏板是否从可见场景中被完全移除？


## 258 — `embodied_174_E2B`

**原始英文指令：** At 34.0 seconds, pause tightening and orienting the rear-axle accessory for three seconds, then resume from the same visible task state at 37.0 seconds.

**中文翻译：** 在第 34.0 秒，将拧紧和调整后轴附件朝向的动作暂停三秒，然后在第 37.0 秒从相同的可见任务状态恢复。

**状态：** 接受

**原子化判定句：**

1. 拧紧后轴附件的动作是否暂停 3 秒？

2. 调整后轴附件朝向的动作是否也暂停 3 秒？

3. 两个动作是否在 3 秒后恢复？

4. 这些动作是否从暂停时相同的可见任务状态恢复？


## 259 — `embodied_175_E1`

**原始英文指令：** Starting at 18.0 seconds, continue riding forward within the current highway lane along the visible gentle curve for 4 seconds.

**中文翻译：** 从第 18.0 秒开始，继续沿可见的缓弯在当前公路车道内向前骑行四秒。

**状态：** 接受

**原子化判定句：**

1. 骑行者是否继续沿可见的缓弯向前骑行？

2. 骑行者是否保持在当前公路车道内？

3. 骑行是否持续 4 秒？


## 260 — `embodied_175_E2A`

**原始英文指令：** At 30.5 seconds, remove the gray passenger van passing in the adjacent left lane from the visible scene.

**中文翻译：** 在第 30.5 秒，将正在相邻左车道驶过的灰色客运厢式车从可见场景中移除。

**状态：** 接受

**原子化判定句：**

1. 正在相邻左车道驶过的灰色客运厢式车是否从可见场景中被移除？


## 261 — `embodied_175_E2B`

**原始英文指令：** At 33.0 seconds, switch to a chase viewpoint three meters behind and one meter above the embodied vehicle during passing cars and vans while following the long bend.

**中文翻译：** 在第 33.0 秒，在沿长弯道行驶并超过轿车和厢式车时，将视角切换为位于第一人称载具后方三米、上方一米的追逐视角。

**状态：** 接受

**原子化判定句：**

1. 第一人称载具是否超过轿车和厢式车？

2. 载具是否沿长弯道行驶？

3. 在这些动作期间，视角是否切换为追逐视角？

4. 追逐视角是否位于载具后方三米、上方一米？


## 262 — `embodied_178_E1`

**原始英文指令：** At 19.0 seconds, position the drawing marker horizontally with its tip at the head circle's right edge.

**中文翻译：** 在第 19.0 秒，将绘图马克笔水平放置，并使笔尖位于头部圆形的右边缘。

**状态：** 接受

**原子化判定句：**

1. 绘图马克笔是否水平放置？

2. 马克笔笔尖是否位于头部圆形的右边缘？


## 263 — `embodied_178_E2A`

**原始英文指令：** Starting at 36.0 seconds, guide the marker clockwise from the drawn eyes toward the mouth while adding the facial features over 4 seconds.

**中文翻译：** 从第 36.0 秒开始，在添加面部特征时，引导马克笔从画出的眼睛顺时针移向嘴部，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 面部特征是否被添加？

2. 在添加面部特征时，马克笔是否从画出的眼睛顺时针移向嘴部，并在 4 秒内完成？


## 264 — `embodied_178_E2B`

**原始英文指令：** At 34.0 seconds, delay the onset of drawing the small curved mouth from 42.0 seconds until exactly 43.0 seconds.

**中文翻译：** 在第 34.0 秒进行编辑，将绘制小弧形嘴巴的开始时间从第 42.0 秒推迟到恰好第 43.0 秒。

**状态：** 接受

**原子化判定句：**

1. 小弧形嘴巴是否被画出？

2. 绘制开始时间是否从片段开始后 8 秒推迟到恰好 9 秒？


## 265 — `embodied_179_E1`

**原始英文指令：** Starting at 19.0 seconds, lift the center paper cup along one smooth rising arc and return it to the mat over 4 seconds.

**中文翻译：** 从第 19.0 秒开始，沿一条平滑上升的弧线抬起中央纸杯，并在四秒内将其放回垫子上。

**状态：** 接受

**原子化判定句：**

1. 中央纸杯是否沿一条平滑上升的弧线被抬起？

2. 纸杯是否随后被放回垫子上，并在 4 秒内完成整个动作过程？


## 266 — `embodied_179_E2A`

**原始英文指令：** At 44.5 seconds, place the small wristwatch-like object directly beside the black mat with a gap equal to half the object's width.

**中文翻译：** 在第 44.5 秒，将小型腕表状物体放在黑色垫子正旁边，并留出相当于该物体半个宽度的间隙。

**状态：** 接受

**原子化判定句：**

1. 小型腕表状物体是否被放在黑色垫子正旁边？

2. 两者之间的间隙是否等于该物体宽度的一半？


## 267 — `embodied_179_E2B`

**原始英文指令：** At 34.0 seconds, replace the black mat with a same-size dark-gray close-up performance mat in the same task location.

**中文翻译：** 在第 34.0 秒，将黑色垫子替换为一个同样大小的深灰色近景表演垫，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 黑色垫子是否被替换为深灰色近景表演垫？

2. 替换后的垫子是否与原黑色垫子大小相同？

3. 替换后的垫子是否位于原黑色垫子的任务位置？


## 268 — `embodied_180_E1`

**原始英文指令：** At 19.0 seconds, make the exposed cut edge of the ring-shaped bread visibly moist and glossy.

**中文翻译：** 在第 19.0 秒，使环形面包暴露的切口边缘呈现明显湿润且有光泽的状态。

**状态：** 接受

**原子化判定句：**

1. 环形面包暴露的切口边缘是否变得明显湿润？

2. 该切口边缘是否呈现有光泽的外观？


## 269 — `embodied_180_E2A`

**原始英文指令：** Starting at 42.0 seconds, lean the trunk twenty centimeters toward the two bread halves over 1.5 seconds, then return along the same path over 1.5 seconds.

**中文翻译：** 从第 42.0 秒开始，在 1.5 秒内将躯干朝两半面包倾斜二十厘米，然后用 1.5 秒沿原路径返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 1.5 秒内朝两半面包倾斜二十厘米？

2. 躯干是否随后在接下来的 1.5 秒内沿原路径返回？


## 270 — `embodied_180_E2B`

**原始英文指令：** At 34.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder while adding oil to the small frying pan.

**中文翻译：** 在第 34.0 秒，在向小平底锅中加油时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 油是否被加入小平底锅？

2. 在加油时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 271 — `embodied_181_E1`

**原始英文指令：** Starting at 15.0 seconds, accelerate steadily forward within the current track lane toward the dark race car directly ahead for 4 seconds.

**中文翻译：** 从第 15.0 秒开始，在当前赛道车道内朝正前方的深色赛车稳定加速四秒。

**状态：** 接受

**原子化判定句：**

1. 第一人称载具是否朝正前方的深色赛车稳定加速？

2. 载具是否在加速期间保持位于当前赛道车道内？

3. 加速是否持续 4 秒？


## 272 — `embodied_181_E2A`

**原始英文指令：** Starting at 21.5 seconds, make the visible braking-smoke plume directly ahead drift smoothly toward frame-right over 2 seconds.

**中文翻译：** 从第 21.5 秒开始，让正前方可见的刹车烟雾平稳地朝画面右侧飘移，并在两秒内完成。

**状态：** 接受

**原子化判定句：**

1. 正前方可见的刹车烟雾是否朝画面右侧飘移？

2. 烟雾是否平稳飘移？

3. 飘移是否在 2 秒内完成？


## 273 — `embodied_181_E2B`

**原始英文指令：** At 30.0 seconds, switch to a chase viewpoint three meters behind and one meter above the embodied vehicle while it moves through the contested bend.

**中文翻译：** 在第 30.0 秒，当第一人称载具驶过争夺激烈的弯道时，将视角切换为位于载具后方三米、上方一米的追逐视角。

**状态：** 接受

**原子化判定句：**

1. 第一人称载具是否驶过争夺激烈的弯道？

2. 载具驶过弯道时，视角是否切换为追逐视角？

3. 追逐视角是否位于载具后方三米、上方一米？


## 274 — `embodied_182_E1`

**原始英文指令：** At 7.0 seconds, rotate the small seasoning jar longitudinal axis thirty degrees toward frame-left within the countertop plane.

**中文翻译：** 在第 7.0 秒，在台面平面内将小调味罐的纵轴朝画面左侧旋转三十度。

**状态：** 接受

**原子化判定句：**

1. 小调味罐的纵轴是否朝画面左侧旋转三十度？

2. 该旋转是否保持在台面平面内？


## 275 — `embodied_182_E2A`

**原始英文指令：** At 27.0 seconds, change the non-text exterior surfaces of the purple cooking pot to brushed silver for the rest of the scene.

**中文翻译：** 在第 27.0 秒，将紫色烹饪锅外部不含文字的表面变为拉丝银色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 紫色烹饪锅外部不含文字的表面是否变为拉丝银色？

2. 拉丝银色外观是否保持至场景结束？


## 276 — `embodied_182_E2B`

**原始英文指令：** At 22.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder while finishing the transfer into the purple cooking pot.

**中文翻译：** 在第 22.0 秒，在完成向紫色烹饪锅中的转移动作时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 向紫色烹饪锅中的转移动作是否完成？

2. 在完成转移时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 277 — `embodied_183_E1`

**原始英文指令：** Starting at 19.0 seconds, make the live crab travel rightward in one smooth shallow arc over 4 seconds.

**中文翻译：** 从第 19.0 秒开始，让活螃蟹沿一条平滑的浅弧线向右移动，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 活螃蟹是否向右移动？

2. 螃蟹是否沿一条平滑的浅弧线移动？

3. 移动是否在 4 秒内完成？


## 278 — `embodied_183_E2A`

**原始英文指令：** At 30.0 seconds, change the non-text surfaces of the yellow-handled tool to warm ivory for the rest of the scene.

**中文翻译：** 在第 30.0 秒，将黄色手柄工具上不含文字的表面变为暖象牙色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 黄色手柄工具上不含文字的表面是否变为暖象牙色？

2. 暖象牙色外观是否保持至场景结束？


## 279 — `embodied_183_E2B`

**原始英文指令：** At 34.0 seconds, switch to a third-person viewpoint 1.5 meters behind the observer's right shoulder while guiding the crab.

**中文翻译：** 在第 34.0 秒，在引导螃蟹时，将视角切换为位于观察者右肩后方 1.5 米处的第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 螃蟹是否受到引导？

2. 在引导螃蟹时，视角是否切换为第三人称视角？

3. 第三人称视角是否位于观察者右肩后方 1.5 米处？


## 280 — `embodied_184_E1`

**原始英文指令：** Starting at 16.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the exposed RC-car chassis over 3 seconds.

**中文翻译：** 从第 16.0 秒开始，在三秒内将第一人称视点朝裸露的遥控车底盘方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 3 秒内向右移动半米？

2. 第一人称视点是否在同一段 3 秒内降低二十五厘米？

3. 视点是否朝裸露的遥控车底盘方向移动？


## 281 — `embodied_184_E2A`

**原始英文指令：** Starting at 31.0 seconds, lean the torso twenty centimeters toward the exposed chassis over 2 seconds, then return over 2 seconds.

**中文翻译：** 从第 31.0 秒开始，在两秒内将躯干朝裸露底盘倾斜二十厘米，然后用两秒返回。

**状态：** 接受

**原子化判定句：**

1. 躯干是否在 2 秒内朝裸露底盘倾斜二十厘米？

2. 躯干是否随后在接下来的 2 秒内回到原位？


## 282 — `embodied_184_E2B`

**原始英文指令：** At 31.0 seconds, render only the visible hands and forearms with cel-shaded game-character treatment while they point to the exposed chassis components.

**中文翻译：** 在第 31.0 秒，在可见双手和前臂指示裸露底盘部件时，仅将它们渲染为卡通渲染的游戏角色风格。

**状态：** 接受

**原子化判定句：**

1. 裸露的底盘部件是否被指示？

2. 在进行指示时，可见的双手和前臂是否被渲染为卡通渲染的游戏角色风格？

3. 卡通渲染效果是否仅作用于可见的双手和前臂？


## 283 — `embodied_186_E1`

**原始英文指令：** At 15.0 seconds, change only the outer rim of the transparent round bowl to matte cobalt blue for the rest of the scene.

**中文翻译：** 在第 15.0 秒，仅将透明圆碗的外缘变为哑光钴蓝色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 透明圆碗的外缘是否变为钴蓝色？

2. 变色后的外缘是否呈哑光质感？

3. 该变化是否仅作用于外缘？

4. 哑光钴蓝色外观是否保持至场景结束？


## 284 — `embodied_186_E2A`

**原始英文指令：** Starting at 30.0 seconds, make the green liquid inside the stationary bowl circulate clockwise in one visible current for 4 seconds.

**中文翻译：** 从第 30.0 秒开始，让静止碗中的绿色液体形成一股可见的顺时针水流并循环四秒。

**状态：** 接受

**原子化判定句：**

1. 静止碗中的绿色液体是否形成一股可见水流并循环？

2. 水流是否沿顺时针方向循环？

3. 循环是否持续 4 秒？


## 285 — `embodied_186_E2B`

**原始英文指令：** Starting at 30.0 seconds, make the green liquid inside the stationary bowl circulate counterclockwise in one visible current for 4 seconds.

**中文翻译：** 从第 30.0 秒开始，让静止碗中的绿色液体形成一股可见的逆时针水流并循环四秒。

**状态：** 接受

**原子化判定句：**

1. 静止碗中的绿色液体是否形成一股可见水流并循环？

2. 水流是否沿逆时针方向循环？

3. 循环是否持续 4 秒？


## 286 — `embodied_189_E1`

**原始英文指令：** At 19.0 seconds, change the non-text surfaces of the camera lens barrel to brushed silver.

**中文翻译：** 在第 19.0 秒，将相机镜头筒上不含文字的表面变为拉丝银色。

**状态：** 接受

**原子化判定句：**

1. 相机镜头筒的不含文字表面是否变为银色？

2. 银色表面是否呈现拉丝质感？


## 287 — `embodied_189_E2A`

**原始英文指令：** Starting at 33.0 seconds, lift and turn the camera lens along one smooth rising inspection arc while supporting its barrel over 4 seconds.

**中文翻译：** 从第 33.0 秒开始，在托住镜头筒的同时，沿一条平滑上升的观察弧线抬起并转动相机镜头，并在四秒内完成。

**状态：** 接受

**原子化判定句：**

1. 相机镜头筒是否被托住？

2. 在托住镜头筒时，相机镜头是否被抬起？

3. 镜头是否在被抬起的同时转动？

4. 抬起和转动是否沿一条平滑上升的观察弧线进行，并在 4 秒内完成？


## 288 — `embodied_189_E2B`

**原始英文指令：** At 34.0 seconds, render only the exposed rear metal lens mount with a hand-painted illustration treatment.

**中文翻译：** 在第 34.0 秒，仅将裸露的后部金属镜头卡口渲染为手绘插画风格。

**状态：** 接受

**原子化判定句：**

1. 裸露的后部金属镜头卡口是否被渲染为手绘插画风格？

2. 手绘效果是否仅作用于裸露的后部镜头卡口？


## 289 — `embodied_192_E1`

**原始英文指令：** At 15.0 seconds, render only the large white kit box with a hand-painted illustration treatment for the remaining footage.

**中文翻译：** 在第 15.0 秒，仅将白色大套件盒渲染为手绘插画风格，并保持至剩余视频结束。

**状态：** 接受

**原子化判定句：**

1. 白色大套件盒是否被渲染为手绘插画风格？

2. 手绘效果是否仅作用于该套件盒？

3. 该效果是否保持至剩余视频结束？


## 290 — `embodied_192_E2A`

**原始英文指令：** At 37.0 seconds, change the non-text surfaces of the twin-stick controller to soft coral red for the rest of the scene.

**中文翻译：** 在第 37.0 秒，将双摇杆控制器上不含文字的表面变为柔和的珊瑚红色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 双摇杆控制器上不含文字的表面是否变为柔和的珊瑚红色？

2. 柔和的珊瑚红色外观是否保持至场景结束？


## 291 — `embodied_192_E2B`

**原始英文指令：** At 30.0 seconds, replace the black soft-wrapped battery pack with a same-size hard-shell modular four-bay battery cassette with a matching plug.

**中文翻译：** 在第 30.0 秒，将黑色软包电池组替换为一个同样大小、带匹配插头的硬壳模块化四槽电池盒。

**状态：** 接受

**原子化判定句：**

1. 黑色软包电池组是否被替换为硬壳模块化电池盒？

2. 替换后的电池盒是否与原电池组大小相同？

3. 替换后的电池盒是否具有四个槽位？

4. 替换后的电池盒是否带有匹配插头？


## 292 — `embodied_193_E1`

**原始英文指令：** At 19.0 seconds, render only the suspended pink food piece with a hand-painted illustration treatment.

**中文翻译：** 在第 19.0 秒，仅将悬挂的粉色食物块渲染为手绘插画风格。

**状态：** 接受

**原子化判定句：**

1. 悬挂的粉色食物块是否被渲染为手绘插画风格？

2. 手绘效果是否仅作用于该悬挂食物块？


## 293 — `embodied_193_E2A`

**原始英文指令：** At 40.0 seconds, change the non-text surfaces of the pink food piece to brushed silver for the rest of the scene.

**中文翻译：** 在第 40.0 秒，将粉色食物块上不含文字的表面变为拉丝银色，并保持至场景结束。

**状态：** 接受

**原子化判定句：**

1. 粉色食物块上不含文字的表面是否变为拉丝银色？

2. 拉丝银色外观是否保持至场景结束？


## 294 — `embodied_193_E2B`

**原始英文指令：** At 34.0 seconds, replace the two small opossums with two similarly sized guinea pigs in the same task locations.

**中文翻译：** 在第 34.0 秒，将两只小负鼠替换为两只大小相近的豚鼠，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 两只小负鼠是否被替换为两只豚鼠？

2. 替换后的豚鼠是否与负鼠大小相近？

3. 豚鼠是否位于负鼠原本所在的任务位置？


## 295 — `embodied_195_E1`

**原始英文指令：** Starting at 8.0 seconds, slow the current protruding-layer turn so its visible quarter-turn completion moves from 12.0 seconds to 16.0 seconds.

**中文翻译：** 从第 8.0 秒开始，减慢当前突出层的转动，使其可见的四分之一圈完成时间从第 12.0 秒延后到第 16.0 秒。

**状态：** 接受

**原子化判定句：**

1. 当前突出层是否继续转动？

2. 突出层的转动是否被减慢？

3. 可见的四分之一圈是否改为在片段开始后 8 秒完成，而不是在 4 秒后完成？


## 296 — `embodied_195_E2A`

**原始英文指令：** Starting at 31.0 seconds, turn the protruding puzzle layer clockwise through a wider controlled arc over 3 seconds.

**中文翻译：** 从第 31.0 秒开始，让突出的拼图层沿一条更宽且受控的弧线顺时针转动，并在三秒内完成。

**状态：** 接受

**原子化判定句：**

1. 突出的拼图层是否顺时针转动？

2. 该拼图层是否沿一条更宽且受控的弧线转动？

3. 转动是否在 3 秒内完成？


## 297 — `embodied_195_E2B`

**原始英文指令：** At 23.0 seconds, position the held mirror puzzle in the left third of the frame at its current working depth.

**中文翻译：** 在第 23.0 秒，将手持镜面拼图放在画面左侧三分之一区域，并保持当前工作景深。

**状态：** 接受

**原子化判定句：**

1. 手持镜面拼图是否被放在画面左侧三分之一区域？

2. 该镜面拼图是否保持当前工作景深？


## 298 — `embodied_198_E1`

**原始英文指令：** Starting at 15.0 seconds, guide the patterned pencil left-to-right across both workbook diagrams in one pointing sweep over 4 seconds.

**中文翻译：** 从第 15.0 秒开始，用四秒完成一次从左向右的指示扫动，引导花纹铅笔划过练习册中的两幅图示。

**状态：** 接受

**原子化判定句：**

1. 花纹铅笔是否在 4 秒内完成一次从左向右的指示扫动？

2. 铅笔的指示扫动是否划过练习册中的两幅图示？


## 299 — `embodied_198_E2A`

**原始英文指令：** At 30.0 seconds, rotate the patterned pencil longitudinal axis thirty degrees counterclockwise within the page plane.

**中文翻译：** 在第 30.0 秒，在页面平面内将花纹铅笔的纵轴逆时针旋转三十度。

**状态：** 接受

**原子化判定句：**

1. 花纹铅笔的纵轴是否逆时针旋转三十度？

2. 该旋转是否保持在页面平面内？


## 300 — `embodied_198_E2B`

**原始英文指令：** Starting at 30.0 seconds, perform a two-second optical push-in to a stable close-up centered on the patterned pencil.

**中文翻译：** 从第 30.0 秒开始，进行一次持续两秒的光学推进，最终形成以花纹铅笔为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？

2. 光学推进结束后，画面是否成为以花纹铅笔为中心的稳定特写？
