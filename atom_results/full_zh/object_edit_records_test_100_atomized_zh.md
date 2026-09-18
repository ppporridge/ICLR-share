# 全量编辑指令原子化结果——object_edit_records_test_100.md——中文审阅版

- 源记录数：300

- 所有原子判定句均依据 `atom_results/README.md` 逐条人工审核。

- 原子判定句省略作为截取起点的绝对时间；后续时间点均已换算为片段内相对时间。


## 001 — `object_001_E1`

**原始英文指令：** Starting at 14.0 seconds, change the adult rabbit's fur from mottled gray-brown to pale cream over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将成年兔子的灰棕杂色皮毛变为浅奶油色。

**状态：** 接受

**原子化判定句：**

1. 成年兔子的皮毛是否从灰棕杂色变为浅奶油色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 002 — `object_001_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the adult rabbit lower its head and gently nuzzle the visible kits twice.

**中文翻译：** 从第 29.0 秒开始，让成年兔子低下头，轻轻蹭可见的幼兔两次。

**状态：** 接受

**原子化判定句：**

1. 成年兔子是否朝可见的幼兔低下头？

2. 低头后，成年兔子是否轻轻蹭可见的幼兔恰好两次？


## 003 — `object_001_E2B`

**原始英文指令：** At 29.0 seconds, add one light-brown rabbit kit at the outer right edge of the nursing cluster.

**中文翻译：** 在第 29.0 秒，在哺乳兔群的最右侧边缘添加一只浅棕色幼兔。

**状态：** 接受

**原子化判定句：**

1. 哺乳兔群中是否添加了一只幼兔？

2. 是否恰好添加了一只幼兔？

3. 新增幼兔是否为浅棕色？

4. 新增幼兔是否位于兔群的最右侧边缘？


## 004 — `object_004_E1`

**原始英文指令：** Starting at 14.0 seconds, change the peacock's neck plumage from vivid blue to emerald green over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将孔雀颈部的鲜蓝色羽毛变为祖母绿色。

**状态：** 接受

**原子化判定句：**

1. 孔雀颈部的羽毛是否从鲜蓝色变为祖母绿色？

2. 羽毛颜色变化是否在 2 秒内完成？


## 005 — `object_004_E2A`

**原始英文指令：** At 29.0 seconds, reposition the peacock and the nearest dark guinea fowl side by side on the path.

**中文翻译：** 在第 29.0 秒，将孔雀和最近的深色珍珠鸡并排移到小路上。

**状态：** 接受

**原子化判定句：**

1. 孔雀和最近的深色珍珠鸡是否都被移到小路上？

2. 两只鸟是否并排放置？


## 006 — `object_004_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the peacock fan its tail and shake the feathers twice.

**中文翻译：** 从第 29.0 秒开始，让孔雀展开尾羽并抖动羽毛两次。

**状态：** 接受

**原子化判定句：**

1. 孔雀是否展开尾羽？

2. 展开尾羽后，孔雀是否将尾羽恰好抖动两次？


## 007 — `object_008_E1`

**原始英文指令：** Starting at 14.0 seconds, change the larger boar's mottled brown coat to dark charcoal over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将较大野猪的棕色杂斑皮毛变为深炭灰色。

**状态：** 接受

**原子化判定句：**

1. 较大野猪的皮毛是否从棕色杂斑变为深炭灰色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 008 — `object_008_E2A`

**原始英文指令：** At 29.0 seconds, reposition the two boars side by side with one body width between them.

**中文翻译：** 在第 29.0 秒，将两头野猪并排放置，彼此相隔一个身宽。

**状态：** 接受

**原子化判定句：**

1. 两头野猪是否被并排放置？

2. 两头野猪之间是否相隔一个身宽？


## 009 — `object_008_E2B`

**原始英文指令：** At 29.0 seconds, remove the smaller boar positioned uphill from the larger boar.

**中文翻译：** 在第 29.0 秒，移除位于较大野猪上坡方向的较小野猪。

**状态：** 接受

**原子化判定句：**

1. 位于较大野猪上坡方向的较小野猪是否被移除？


## 010 — `object_011_E1`

**原始英文指令：** Starting at 14.0 seconds, change the dry pale-brown training-ground surface to damp dark brown over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将干燥的浅棕色训练场地面变为潮湿的深棕色。

**状态：** 接受

**原子化判定句：**

1. 训练场地面是否从干燥变为潮湿？

2. 地面是否从浅棕色变为深棕色？

3. 这些地面变化是否在 2 秒内完成？


## 011 — `object_011_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the foremost tracked vehicle execute a wide right turn while advancing for five seconds.

**中文翻译：** 从第 29.0 秒开始，让最前方的履带车辆在前进的同时进行大幅度右转，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 最前方的履带车辆是否持续前进 5 秒？

2. 前进时，该车辆是否进行大幅度右转？


## 012 — `object_011_E2B`

**原始英文指令：** At 29.0 seconds, remove the smaller box-shaped support vehicle from the formation.

**中文翻译：** 在第 29.0 秒，从编队中移除较小的箱形支援车辆。

**状态：** 接受

**原子化判定句：**

1. 较小的箱形支援车辆是否从编队中被移除？


## 013 — `object_013_E1`

**原始英文指令：** Starting at 14.0 seconds, make the flag ripple with half its original amplitude for five seconds.

**中文翻译：** 从第 14.0 秒开始，让旗帜以原来一半的振幅飘动五秒。

**状态：** 接受

**原子化判定句：**

1. 旗帜飘动的振幅是否减为原来的一半？

2. 半振幅飘动是否持续 5 秒？


## 014 — `object_013_E2A`

**原始英文指令：** Starting at 29.0 seconds, zoom out smoothly to include the full flagpole and more surrounding sky over four seconds.

**中文翻译：** 从第 29.0 秒开始，在四秒内平稳拉远镜头，以纳入完整旗杆和更多周围天空。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 4 秒内平稳拉远？

2. 拉远结束时，完整旗杆和更多周围天空是否可见？


## 015 — `object_013_E2B`

**原始英文指令：** At 29.0 seconds, add a small plain blue pennant on a separate pole to the right of the existing flag.

**中文翻译：** 在第 29.0 秒，在现有旗帜右侧的一根独立旗杆上添加一面纯蓝色小三角旗。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一面小三角旗？

2. 新增三角旗是否为纯蓝色？

3. 三角旗是否安装在一根独立旗杆上？

4. 该旗杆是否位于现有旗帜右侧？


## 016 — `object_014_E1`

**原始英文指令：** Starting at 14.0 seconds, make the water bottle follow a wide S-shaped rolling path for six seconds.

**中文翻译：** 从第 14.0 秒开始，让水瓶沿宽幅 S 形轨迹滚动六秒。

**状态：** 接受

**原子化判定句：**

1. 水瓶是否滚动？

2. 水瓶滚动时是否沿 S 形轨迹移动？

3. 该 S 形轨迹是否宽幅？

4. 滚动是否持续 6 秒？


## 017 — `object_014_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the rolling water bottle smoothly from directly overhead for five seconds.

**中文翻译：** 从第 29.0 秒开始，从正上方平稳跟拍正在滚动的水瓶五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟拍正在滚动的水瓶？

2. 跟拍视角是否位于正上方？

3. 跟拍移动是否平稳？

4. 跟拍是否持续 5 秒？


## 018 — `object_014_E2B`

**原始英文指令：** Starting at 29.0 seconds, apply a crisp high-contrast monochrome grade to the full frame over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内为整个画面应用清晰的高对比度单色调。

**状态：** 接受

**原子化判定句：**

1. 整个画面是否应用了单色调？

2. 该单色调是否具有高对比度？

3. 处理后的画面是否显得清晰锐利？

4. 调色是否在 2 秒内完成？


## 019 — `object_015_E1`

**原始英文指令：** Starting at 20.0 seconds, change the central tree trunk's bark from medium brown to pale gray over the next two seconds.

**中文翻译：** 从第 20.0 秒开始，在接下来的两秒内将中央树干的树皮从中棕色变为浅灰色。

**状态：** 接受

**原子化判定句：**

1. 中央树干的树皮是否从中棕色变为浅灰色？

2. 树皮颜色变化是否在 2 秒内完成？


## 020 — `object_015_E2A`

**原始英文指令：** Starting at 34.0 seconds, pause the lower panda's second climb for three seconds before it resumes.

**中文翻译：** 从第 34.0 秒开始，让下方熊猫的第二次攀爬暂停三秒，然后恢复。

**状态：** 接受

**原子化判定句：**

1. 下方熊猫是否开始第二次攀爬？

2. 在第二次攀爬过程中，下方熊猫是否暂停 3 秒？

3. 暂停 3 秒后，下方熊猫是否恢复攀爬？


## 021 — `object_015_E2B`

**原始英文指令：** Starting at 35.0 seconds, make the lower panda reach one forepaw toward the upper panda twice.

**中文翻译：** 从第 35.0 秒开始，让下方熊猫将一只前爪朝上方熊猫伸出两次。

**状态：** 接受

**原子化判定句：**

1. 下方熊猫是否将前爪伸向上方熊猫？

2. 下方熊猫是否使用一只前爪完成伸爪动作？

3. 伸爪动作是否恰好进行两次？


## 022 — `object_017_E1`

**原始英文指令：** Starting at 14.0 seconds, change the spotted cat's base coat from golden-tan to cool pale gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将斑点猫的底色皮毛从金棕色变为冷调浅灰色。

**状态：** 接受

**原子化判定句：**

1. 斑点猫的底色皮毛是否从金棕色变为灰色？

2. 变化后的灰色皮毛是否较浅？

3. 变化后的灰色皮毛是否呈冷色调？

4. 皮毛颜色变化是否在 2 秒内完成？


## 023 — `object_017_E2A`

**原始英文指令：** At 29.0 seconds, reposition the spotted cat at the waterline along the muddy bank.

**中文翻译：** 在第 29.0 秒，将斑点猫移到泥泞河岸的水边线上。

**状态：** 接受

**原子化判定句：**

1. 斑点猫是否被移到泥泞河岸的水边线上？


## 024 — `object_017_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the shallow water lap against the bank in larger repeated ripples for five seconds.

**中文翻译：** 从第 29.0 秒开始，让浅水以更大的重复波纹拍打河岸五秒。

**状态：** 接受

**原子化判定句：**

1. 浅水是否拍打河岸？

2. 形成的波纹是否比原来更大？

3. 波纹是否反复出现？

4. 拍打河岸是否持续 5 秒？


## 025 — `object_019_E1`

**原始英文指令：** Starting at 16.0 seconds, change the cloudy blue-gray sky to clear blue with sparse clouds over the next three seconds.

**中文翻译：** 从第 16.0 秒开始，在接下来的三秒内将多云的蓝灰色天空变为只有稀疏云朵的晴朗蓝天。

**状态：** 接受

**原子化判定句：**

1. 蓝灰色多云天空是否在 3 秒内变为晴朗蓝天？

2. 天空中是否只保留稀疏云朵？


## 026 — `object_019_E2A`

**原始英文指令：** At 29.0 seconds, reorient the jet so its wings are level while it continues away from the camera.

**中文翻译：** 在第 29.0 秒，重新调整喷气式飞机的姿态，使其在继续远离镜头时保持机翼水平。

**状态：** 接受

**原子化判定句：**

1. 喷气式飞机是否继续远离镜头？

2. 远离镜头时，喷气式飞机的机翼是否被调整为水平姿态？


## 027 — `object_019_E2B`

**原始英文指令：** Starting at 31.0 seconds, make the departing jet perform two shallow wing rocks.

**中文翻译：** 从第 31.0 秒开始，让正在远离的喷气式飞机进行两次轻微的左右摇翼。

**状态：** 接受

**原子化判定句：**

1. 喷气式飞机是否继续远离？

2. 远离时，喷气式飞机是否恰好进行两次轻微的左右摇翼？


## 028 — `object_020_E1`

**原始英文指令：** Starting at 14.0 seconds, change the dry exposed soil beneath the deer to visibly wet dark-brown soil over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将鹿下方干燥裸露的土壤变为明显湿润的深棕色土壤。

**状态：** 接受

**原子化判定句：**

1. 鹿下方裸露的土壤是否从干燥变为明显湿润？

2. 土壤是否变为深棕色？

3. 这些土壤变化是否在 2 秒内完成？


## 029 — `object_020_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the antlered deer stamp one front hoof twice.

**中文翻译：** 从第 29.0 秒开始，让有角的鹿用一只前蹄跺地两次。

**状态：** 接受

**原子化判定句：**

1. 有角的鹿是否用前蹄跺地？

2. 跺地动作是否使用一只前蹄？

3. 跺地动作是否恰好进行两次？


## 030 — `object_020_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the dog complete one full circle around the antlered deer.

**中文翻译：** 从第 29.0 秒开始，让狗围绕有角的鹿完整绕行一圈。

**状态：** 接受

**原子化判定句：**

1. 狗是否围绕有角的鹿移动？

2. 狗的移动轨迹是否围绕鹿形成完整的一圈？

3. 狗是否恰好绕行一圈？


## 031 — `object_022_E1`

**原始英文指令：** Starting at 14.0 seconds, make the white rabbit push the soccer ball through one tight clockwise circle.

**中文翻译：** 从第 14.0 秒开始，让白兔推着足球沿紧凑的顺时针圆形轨迹绕行一圈。

**状态：** 接受

**原子化判定句：**

1. 白兔是否推着足球移动？

2. 足球是否沿紧凑的圆形轨迹移动？

3. 足球是否沿顺时针方向移动？

4. 足球是否恰好绕行一圈？


## 032 — `object_022_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the soccer ball roll along a clear zigzag path after the rabbit nudges it.

**中文翻译：** 从第 29.0 秒开始，让兔子先轻推足球，随后使足球沿清晰的之字形轨迹滚动。

**状态：** 接受

**原子化判定句：**

1. 兔子是否轻推足球？

2. 兔子轻推后，足球是否沿清晰的之字形轨迹滚动？


## 033 — `object_022_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the garden background as a colored-pencil illustration over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将花园背景呈现为彩色铅笔插画。

**状态：** 接受

**原子化判定句：**

1. 花园背景是否被呈现为插画？

2. 该插画是否采用彩色铅笔风格？

3. 渲染变化是否在 2 秒内完成？


## 034 — `object_023_E1`

**原始英文指令：** At 14.0 seconds, remove the round silver fuel-tank cap from the top of the red tank.

**中文翻译：** 在第 14.0 秒，移除红色油箱顶部的圆形银色油箱盖。

**状态：** 接受

**原子化判定句：**

1. 红色油箱顶部的圆形银色油箱盖是否被移除？


## 035 — `object_023_E2A`

**原始英文指令：** Starting at 29.0 seconds, orbit clockwise around the motorcycle at wheel height for five seconds.

**中文翻译：** 从第 29.0 秒开始，让镜头在车轮高度围绕摩托车顺时针环绕五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否围绕摩托车环绕？

2. 镜头是否沿顺时针方向环绕？

3. 环绕视角是否保持在车轮高度？

4. 环绕是否持续 5 秒？


## 036 — `object_023_E2B`

**原始英文指令：** At 29.0 seconds, remove the red sedan parked behind the motorcycle.

**中文翻译：** 在第 29.0 秒，移除停在摩托车后方的红色轿车。

**状态：** 接受

**原子化判定句：**

1. 停在摩托车后方的红色轿车是否被移除？


## 037 — `object_024_E1`

**原始英文指令：** Starting at 20.0 seconds, change the dry pale-brown dirt road to damp dark brown over the next two seconds.

**中文翻译：** 从第 20.0 秒开始，在接下来的两秒内将干燥的浅棕色土路变为潮湿的深棕色。

**状态：** 接受

**原子化判定句：**

1. 土路是否从干燥变为潮湿？

2. 土路是否从浅棕色变为深棕色？

3. 这些变化是否在 2 秒内完成？


## 038 — `object_024_E2A`

**原始英文指令：** Starting at 31.0 seconds, make the main tank's remaining corridor-entry process progress at twice its original speed.

**中文翻译：** 从第 31.0 秒开始，让主坦克剩余的进入通道过程以原速度的两倍推进。

**状态：** 接受

**原子化判定句：**

1. 主坦克剩余的进入通道过程是否以原速度的两倍推进？


## 039 — `object_024_E2B`

**原始英文指令：** At 35.0 seconds, make the dust behind the distant tank rise into a higher rolling plume when that tank appears at 39.0 seconds.

**中文翻译：** 在第 35.0 秒，当远处坦克于第 39.0 秒出现时，让其后方的尘土升成更高的翻滚尘柱。

**状态：** 接受

**原子化判定句：**

1. 远处坦克是否在 4 秒内出现？

2. 远处坦克出现时，其后方的尘土是否升成更高的翻滚尘柱？


## 040 — `object_026_E1`

**原始英文指令：** Starting at 14.0 seconds, change the horned chameleon's yellow-green side region to vivid golden yellow over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将有角变色龙侧面的黄绿色区域变为鲜艳的金黄色。

**状态：** 接受

**原子化判定句：**

1. 有角变色龙侧面的黄绿色区域是否变为金黄色？

2. 形成的金黄色是否鲜艳？

3. 颜色变化是否在 2 秒内完成？


## 041 — `object_026_E2A`

**原始英文指令：** At 29.0 seconds, reorient both chameleons to face the left end of the horizontal branch.

**中文翻译：** 在第 29.0 秒，重新调整两只变色龙的朝向，使它们面向水平树枝的左端。

**状态：** 接受

**原子化判定句：**

1. 两只变色龙是否都被重新调整为面向水平树枝的左端？


## 042 — `object_026_E2B`

**原始英文指令：** At 29.0 seconds, replace the horizontal branch with a thick cork perch of the same length.

**中文翻译：** 在第 29.0 秒，将水平树枝替换为一根等长的粗软木栖木。

**状态：** 接受

**原子化判定句：**

1. 水平树枝是否被替换为软木栖木？

2. 替换后的软木栖木是否粗厚？

3. 替换后的栖木是否与原树枝等长？


## 043 — `object_027_E1`

**原始英文指令：** Starting at 14.0 seconds, change the main bus's black body panels to deep navy blue over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将主公交车的黑色车身面板变为深海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 主公交车的车身面板是否从黑色变为深海军蓝色？

2. 面板颜色变化是否在 2 秒内完成？


## 044 — `object_027_E2A`

**原始英文指令：** Starting at 29.0 seconds, move the camera to a centered view directly behind the main bus over four seconds.

**中文翻译：** 从第 29.0 秒开始，在四秒内将镜头移到主公交车正后方的居中视角。

**状态：** 接受

**原子化判定句：**

1. 镜头是否移到主公交车正后方？

2. 形成的视图是否以主公交车为中心？

3. 镜头移动是否在 4 秒内完成？


## 045 — `object_027_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the main bus follow shallower curves at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让主公交车以原速度的一半沿更平缓的弯道行驶六秒。

**状态：** 接受

**原子化判定句：**

1. 主公交车是否沿比原先更平缓的弯道行驶？

2. 沿这些弯道行驶时，公交车是否以原速度的一半持续行驶 6 秒？


## 046 — `object_031_E1`

**原始英文指令：** Starting at 17.0 seconds, make the frog swim with slower and longer hind-leg strokes for five seconds.

**中文翻译：** 从第 17.0 秒开始，让青蛙以更慢、更长的后腿划水动作游泳五秒。

**状态：** 接受

**原子化判定句：**

1. 青蛙是否以比原先更慢的后腿划水动作继续游泳 5 秒？

2. 在同一段 5 秒内，青蛙的后腿划水动作是否比原先更长？


## 047 — `object_031_E2A`

**原始英文指令：** Starting at 32.0 seconds, track the frog smoothly from directly overhead for five seconds.

**中文翻译：** 从第 32.0 秒开始，从正上方平稳跟拍青蛙五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟拍青蛙？

2. 跟拍视角是否位于正上方？

3. 跟拍移动是否平稳？

4. 跟拍是否持续 5 秒？


## 048 — `object_031_E2B`

**原始英文指令：** Starting at 32.0 seconds, apply a vivid teal high-contrast grade to the full frame over the next two seconds.

**中文翻译：** 从第 32.0 秒开始，在接下来的两秒内为整个画面应用鲜艳的蓝绿色高对比度调色。

**状态：** 接受

**原子化判定句：**

1. 整个画面是否应用了调色？

2. 调色是否呈鲜艳的蓝绿色？

3. 调色是否具有高对比度？

4. 调色是否在 2 秒内完成？


## 049 — `object_032_E1`

**原始英文指令：** Starting at 14.0 seconds, change the main crab's blue-green shell to vivid red over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将主螃蟹的蓝绿色甲壳变为鲜红色。

**状态：** 接受

**原子化判定句：**

1. 主螃蟹的甲壳是否从蓝绿色变为红色？

2. 形成的红色是否鲜艳？

3. 甲壳颜色变化是否在 2 秒内完成？


## 050 — `object_032_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the main crab side-step at twice its original speed for five seconds.

**中文翻译：** 从第 29.0 秒开始，让主螃蟹以原速度的两倍横向移动五秒。

**状态：** 接受

**原子化判定句：**

1. 主螃蟹是否以原速度的两倍横向移动？

2. 两倍速横向移动是否持续 5 秒？


## 051 — `object_032_E2B`

**原始英文指令：** At 29.0 seconds, add one smaller blue-green crab behind the main crab.

**中文翻译：** 在第 29.0 秒，在主螃蟹后方添加一只较小的蓝绿色螃蟹。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一只螃蟹？

2. 新增螃蟹是否比主螃蟹小？

3. 新增螃蟹是否为蓝绿色？

4. 新增螃蟹是否位于主螃蟹后方？


## 052 — `object_033_E1`

**原始英文指令：** Starting at 14.0 seconds, change the diffuse blue underwater illumination to brighter cyan light with visible sun shafts over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将漫射的蓝色水下照明变为更明亮的青色光，并出现可见的阳光光束。

**状态：** 接受

**原子化判定句：**

1. 漫射的蓝色水下照明是否在 2 秒内变为更明亮的青色光？

2. 可见的阳光光束是否在同一段 2 秒内出现？


## 053 — `object_033_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the shark perform one gentle body roll while swimming forward.

**中文翻译：** 从第 29.0 秒开始，让鲨鱼在向前游动时进行一次轻柔的身体翻滚。

**状态：** 接受

**原子化判定句：**

1. 鲨鱼是否继续向前游动？

2. 向前游动时，鲨鱼是否恰好进行一次轻柔的身体翻滚？


## 054 — `object_033_E2B`

**原始英文指令：** At 29.0 seconds, replace the nearest dark reef formation with a pale sand mound of the same size.

**中文翻译：** 在第 29.0 秒，将最近的深色礁石结构替换为一个同样大小的浅色沙丘。

**状态：** 接受

**原子化判定句：**

1. 最近的深色礁石结构是否被替换为浅色沙丘？

2. 浅色沙丘是否与原礁石结构大小相同？


## 055 — `object_039_E1`

**原始英文指令：** Starting at 14.0 seconds, make the black cat and the orange-white cat touch noses twice.

**中文翻译：** 从第 14.0 秒开始，让黑猫和橙白猫碰鼻两次。

**状态：** 接受

**原子化判定句：**

1. 黑猫和橙白猫是否碰鼻？

2. 两只猫是否恰好碰鼻两次？


## 056 — `object_039_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the orange-and-white cat circle the black cat at half its original speed for five seconds.

**中文翻译：** 从第 29.0 秒开始，让橙白猫以原速度的一半围绕黑猫转圈五秒。

**状态：** 接受

**原子化判定句：**

1. 橙白猫是否围绕黑猫转圈？

2. 橙白猫是否以原速度的一半转圈？

3. 半速转圈是否持续 5 秒？


## 057 — `object_039_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full frame into a 1990s consumer-camcorder recording over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将整个画面转换为 20 世纪 90 年代家用摄像机录像风格。

**状态：** 接受

**原子化判定句：**

1. 整个画面是否呈现出家用摄像机录像的视觉效果？

2. 形成的摄像机录像风格是否具有 20 世纪 90 年代的视觉特征？

3. 风格转变是否在 2 秒内完成？


## 058 — `object_040_E1`

**原始英文指令：** At 14.0 seconds, change the foreground horizontal log from dry to visibly wet with a slightly darker surface.

**中文翻译：** 在第 14.0 秒，将前景中的水平原木从干燥状态变为明显湿润，并使其表面略微变暗。

**状态：** 接受

**原子化判定句：**

1. 前景中的水平原木是否从干燥状态变为明显湿润？

2. 原木表面是否略微变暗？


## 059 — `object_040_E2A`

**原始英文指令：** At 29.0 seconds, reposition the black cat's forepaws symmetrically on opposite sides of the tree fork.

**中文翻译：** 在第 29.0 秒，将黑猫的两只前爪对称地移到树杈两侧。

**状态：** 接受

**原子化判定句：**

1. 黑猫的两只前爪是否分别位于树杈两侧？

2. 两只前爪的位置是否对称？


## 060 — `object_040_E2B`

**原始英文指令：** At 29.0 seconds, remove the rear horizontal wooden pole from behind the black cat.

**中文翻译：** 在第 29.0 秒，移除黑猫后方的水平木杆。

**状态：** 接受

**原子化判定句：**

1. 黑猫后方的水平木杆是否被移除？


## 061 — `object_041_E1`

**原始英文指令：** Starting at 14.0 seconds, change the sunny outdoor weather to lightly overcast conditions over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将晴朗的室外天气变为轻微阴天。

**状态：** 接受

**原子化判定句：**

1. 晴朗的室外天气是否变为阴天？

2. 形成的阴天程度是否较轻？

3. 天气变化是否在 2 秒内完成？


## 062 — `object_041_E2A`

**原始英文指令：** At 29.0 seconds, reposition the two silverback gorillas side by side with one body width between them.

**中文翻译：** 在第 29.0 秒，将两只银背大猩猩并排放置，彼此相隔一个身宽。

**状态：** 接受

**原子化判定句：**

1. 两只银背大猩猩是否并排放置？

2. 两只银背大猩猩之间是否相隔一个身宽？


## 063 — `object_041_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the gorilla nearest the grass slope stand and beat its chest twice.

**中文翻译：** 从第 29.0 秒开始，让最靠近草坡的大猩猩站起来并拍打胸部两次。

**状态：** 接受

**原子化判定句：**

1. 最靠近草坡的大猩猩是否站起来？

2. 站起来后，这只大猩猩是否恰好拍打胸部两次？


## 064 — `object_042_E1`

**原始英文指令：** Starting at 14.0 seconds, make the black-white-and-brown puppy perform three consecutive play bows toward the mirror.

**中文翻译：** 从第 14.0 秒开始，让黑白棕相间的幼犬朝镜子连续做三次游戏鞠躬动作。

**状态：** 接受

**原子化判定句：**

1. 黑白棕相间的幼犬是否朝镜子做游戏鞠躬动作？

2. 幼犬是否恰好做三次游戏鞠躬？

3. 三次游戏鞠躬是否连续完成？


## 065 — `object_042_E2A`

**原始英文指令：** At 29.0 seconds, reposition the puppy at the center of the carpet one body length from the mirror.

**中文翻译：** 在第 29.0 秒，将幼犬移到地毯中央，与镜子相距一个身长。

**状态：** 接受

**原子化判定句：**

1. 幼犬是否被移到地毯中央？

2. 幼犬与镜子是否相距一个身长？


## 066 — `object_042_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full puppy-and-mirror scene into a layered paper-collage style over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将完整的幼犬与镜子场景转换为分层纸张拼贴风格。

**状态：** 接受

**原子化判定句：**

1. 完整的幼犬与镜子场景是否转换为纸张拼贴风格？

2. 纸张拼贴是否具有可见的分层结构？

3. 风格转变是否在 2 秒内完成？


## 067 — `object_045_E1`

**原始英文指令：** Starting at 14.0 seconds, change the larger ring-tailed animal's gray-black coat to warm brown over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将较大环尾动物的灰黑色皮毛变为暖棕色。

**状态：** 接受

**原子化判定句：**

1. 较大环尾动物的皮毛是否从灰黑色变为暖棕色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 068 — `object_045_E2A`

**原始英文指令：** Starting at 29.0 seconds, zoom out smoothly over four seconds to show both animals and the complete enclosure floor.

**中文翻译：** 从第 29.0 秒开始，在四秒内平稳拉远镜头，以显示两只动物和完整的围栏地面。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 4 秒内平稳拉远？

2. 拉远结束时，两只动物和完整的围栏地面是否都可见？


## 069 — `object_045_E2B`

**原始英文指令：** At 29.0 seconds, replace the protruding rock pillar on the left with a vertical weathered log of the same size.

**中文翻译：** 在第 29.0 秒，将左侧凸出的岩柱替换为一根同样大小的竖直风化原木。

**状态：** 接受

**原子化判定句：**

1. 左侧凸出的岩柱是否被替换为原木？

2. 替换后的原木是否竖直且呈风化状态？

3. 替换后的原木是否与原岩柱大小相同？


## 070 — `object_046_E1`

**原始英文指令：** Starting at 20.0 seconds, change the foreground polar bear's cream-white coat to pale golden beige over the next two seconds.

**中文翻译：** 从第 20.0 秒开始，在接下来的两秒内将前景北极熊的乳白色皮毛变为浅金米色。

**状态：** 接受

**原子化判定句：**

1. 前景北极熊的皮毛是否从乳白色变为浅金米色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 071 — `object_046_E2A`

**原始英文指令：** At 29.0 seconds, reposition the lying foreground polar bear on the right side of the same snow pit.

**中文翻译：** 在第 29.0 秒，将躺卧的前景北极熊移到同一雪坑的右侧。

**状态：** 接受

**原子化判定句：**

1. 躺卧的前景北极熊是否被移到同一雪坑的右侧？


## 072 — `object_046_E2B`

**原始英文指令：** At 35.0 seconds, remove the standing polar bear farthest behind the snow pit when it enters the view at 39.0 seconds.

**中文翻译：** 在第 35.0 秒，当雪坑后方最远处站立的北极熊于第 39.0 秒进入画面时，将其移除。

**状态：** 接受

**原子化判定句：**

1. 雪坑后方最远处站立的北极熊是否在 4 秒内进入画面？

2. 该北极熊进入画面时，是否被移除？


## 073 — `object_047_E1`

**原始英文指令：** Starting at 14.0 seconds, make the black rabbit push the rainbow-colored ball three times with its nose.

**中文翻译：** 从第 14.0 秒开始，让黑兔用鼻子推动彩虹色球三次。

**状态：** 接受

**原子化判定句：**

1. 黑兔是否推动彩虹色球？

2. 黑兔是否用鼻子推动球？

3. 黑兔是否恰好推动球三次？


## 074 — `object_047_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the rainbow-colored ball roll across the rug at half its original speed for five seconds.

**中文翻译：** 从第 29.0 秒开始，让彩虹色球以原速度的一半滚过地毯五秒。

**状态：** 接受

**原子化判定句：**

1. 彩虹色球是否滚过地毯？

2. 球是否以原速度的一半滚动？

3. 半速滚动是否持续 5 秒？


## 075 — `object_047_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the room background as a colored-pencil illustration over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将房间背景呈现为彩色铅笔插画。

**状态：** 接受

**原子化判定句：**

1. 房间背景是否被呈现为插画？

2. 该插画是否采用彩色铅笔风格？

3. 渲染变化是否在 2 秒内完成？


## 076 — `object_049_E1`

**原始英文指令：** At 14.0 seconds, change the golf cart's transparent windshield from upright to fully folded down.

**中文翻译：** 在第 14.0 秒，将高尔夫球车的透明挡风玻璃从竖直状态变为完全折下。

**状态：** 接受

**原子化判定句：**

1. 高尔夫球车的透明挡风玻璃是否从竖直状态向下折叠？

2. 挡风玻璃是否完全折下？


## 077 — `object_049_E2A`

**原始英文指令：** At 29.0 seconds, reposition the raccoon beside the golf cart's front wheel.

**中文翻译：** 在第 29.0 秒，将浣熊移到高尔夫球车前轮旁。

**状态：** 接受

**原子化判定句：**

1. 浣熊是否被移到高尔夫球车前轮旁？


## 078 — `object_049_E2B`

**原始英文指令：** At 29.0 seconds, replace the white cup mounted on the golf cart with a plain red thermos of the same size.

**中文翻译：** 在第 29.0 秒，将安装在高尔夫球车上的白色杯子替换为一个同样大小的纯红色保温杯。

**状态：** 接受

**原子化判定句：**

1. 高尔夫球车上的白色杯子是否被替换为红色保温杯？

2. 替换后的保温杯是否没有图案？

3. 替换后的保温杯是否与原杯子大小相同？


## 079 — `object_053_E1`

**原始英文指令：** Starting at 14.0 seconds, make the heron reposition the dark fish in its beak three times.

**中文翻译：** 从第 14.0 秒开始，让鹭将喙中的深色鱼调整位置三次。

**状态：** 接受

**原子化判定句：**

1. 鹭是否调整喙中深色鱼的位置？

2. 鹭是否恰好调整鱼的位置三次？


## 080 — `object_053_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the gray heron take four deliberate steps through the grass while holding the fish.

**中文翻译：** 从第 29.0 秒开始，让灰鹭在衔着鱼的同时穿过草地，缓慢而有意识地走四步。

**状态：** 接受

**原子化判定句：**

1. 灰鹭是否穿过草地行走？

2. 灰鹭是否恰好走四步？

3. 这四步是否缓慢而有意识？

4. 四步行走过程中，灰鹭是否始终衔着鱼？


## 081 — `object_053_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the gray heron as a monochrome ink-wash painting over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将灰鹭呈现为单色水墨画。

**状态：** 接受

**原子化判定句：**

1. 灰鹭是否被呈现为水墨画？

2. 该水墨画是否为单色？

3. 渲染变化是否在 2 秒内完成？


## 082 — `object_054_E1`

**原始英文指令：** Starting at 14.0 seconds, change the pale-brown climbing rock wall to dark slate gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将浅棕色攀爬岩壁变为深石板灰色。

**状态：** 接受

**原子化判定句：**

1. 攀爬岩壁是否从浅棕色变为深石板灰色？

2. 岩壁颜色变化是否在 2 秒内完成？


## 083 — `object_054_E2A`

**原始英文指令：** Starting at 29.0 seconds, accelerate the bear's climbing progress toward the upper ledge to twice its original rate for six seconds.

**中文翻译：** 从第 29.0 秒开始，将熊朝上方岩架攀爬的进度加快到原速的两倍，持续六秒。

**状态：** 接受

**原子化判定句：**

1. 熊是否继续朝上方岩架攀爬？

2. 攀爬进度是否达到原速的两倍？

3. 两倍速攀爬是否持续 6 秒？


## 084 — `object_054_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the black bear climb along a wider left-right zigzag route for six seconds.

**中文翻译：** 从第 29.0 秒开始，让黑熊沿更宽的左右之字形路线攀爬六秒。

**状态：** 接受

**原子化判定句：**

1. 黑熊是否沿左右之字形路线攀爬？

2. 之字形路线是否比原来更宽？

3. 沿该路线攀爬是否持续 6 秒？


## 085 — `object_056_E1`

**原始英文指令：** Starting at 14.0 seconds, make the opossum follow a wider arc at half its original speed for five seconds.

**中文翻译：** 从第 14.0 秒开始，让负鼠以原速度的一半沿更宽的弧线移动五秒。

**状态：** 接受

**原子化判定句：**

1. 负鼠是否沿弧线移动？

2. 该弧线是否比原来更宽？

3. 负鼠是否以原速度的一半移动？

4. 移动是否持续 5 秒？


## 086 — `object_056_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the opossum and the leashed dog circle each other once without contact.

**中文翻译：** 从第 29.0 秒开始，让负鼠和拴着牵引绳的狗互相绕行一圈，期间不发生接触。

**状态：** 接受

**原子化判定句：**

1. 负鼠和拴着牵引绳的狗是否互相绕行？

2. 它们是否恰好互相绕行一圈？

3. 绕行过程中它们是否始终没有接触？


## 087 — `object_056_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the dog's blue harness as a cel-shaded game asset over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将狗的蓝色胸背带呈现为赛璐珞着色的游戏资产。

**状态：** 接受

**原子化判定句：**

1. 狗的蓝色胸背带是否被呈现为游戏资产？

2. 该游戏资产是否采用赛璐珞着色？

3. 渲染变化是否在 2 秒内完成？


## 088 — `object_059_E1`

**原始英文指令：** Starting at 14.0 seconds, change the yellow-brown kelp bed to deep green over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将黄棕色海带床变为深绿色。

**状态：** 接受

**原子化判定句：**

1. 海带床是否从黄棕色变为深绿色？

2. 海带颜色变化是否在 2 秒内完成？


## 089 — `object_059_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the kelp fronds beneath the shark sway strongly toward the right for five seconds.

**中文翻译：** 从第 29.0 秒开始，让鲨鱼下方的海带叶片朝右侧强烈摆动五秒。

**状态：** 接受

**原子化判定句：**

1. 鲨鱼下方的海带叶片是否朝右侧摆动？

2. 摆动幅度是否强烈？

3. 摆动是否持续 5 秒？


## 090 — `object_059_E2B`

**原始英文指令：** At 29.0 seconds, remove the small companion fish swimming beneath the shark's belly.

**中文翻译：** 在第 29.0 秒，移除在鲨鱼腹部下方游动的小型伴生鱼。

**状态：** 接受

**原子化判定句：**

1. 在鲨鱼腹部下方游动的小型伴生鱼是否被移除？


## 091 — `object_062_E1`

**原始英文指令：** At 20.0 seconds, change the central large display box from closed to fully hinged open.

**中文翻译：** 在第 20.0 秒，将中央的大展示盒从关闭状态变为铰链完全打开。

**状态：** 接受

**原子化判定句：**

1. 中央的大展示盒是否从关闭状态沿铰链打开？

2. 展示盒是否完全打开？


## 092 — `object_062_E2A`

**原始英文指令：** At 29.0 seconds, reposition the three orange blister packs into one evenly spaced horizontal row.

**中文翻译：** 在第 29.0 秒，将三个橙色泡罩包装重新排列为间距均匀的一行。

**状态：** 接受

**原子化判定句：**

1. 三个橙色泡罩包装是否都排列在同一行？

2. 这一行是否为水平方向？

3. 三个包装之间的间距是否均匀？


## 093 — `object_062_E2B`

**原始英文指令：** At 35.0 seconds, remove the small silver package at the front-left edge of the display.

**中文翻译：** 在第 35.0 秒，移除展示区左前缘的小型银色包装。

**状态：** 接受

**原子化判定句：**

1. 展示区左前缘的小型银色包装是否被移除？


## 094 — `object_064_E1`

**原始英文指令：** Starting at 14.0 seconds, change the jumping spider's brown-orange abdomen to vivid turquoise over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将跳蛛的棕橙色腹部变为鲜艳的绿松石色。

**状态：** 接受

**原子化判定句：**

1. 跳蛛的腹部是否从棕橙色变为绿松石色？

2. 形成的绿松石色是否鲜艳？

3. 腹部颜色变化是否在 2 秒内完成？


## 095 — `object_064_E2A`

**原始英文指令：** At 29.0 seconds, reorient the jumping spider to face left along the top of the curved white rail.

**中文翻译：** 在第 29.0 秒，重新调整跳蛛的朝向，使其在弯曲白色栏杆顶部面向左侧。

**状态：** 接受

**原子化判定句：**

1. 跳蛛是否位于弯曲白色栏杆顶部？

2. 跳蛛是否被重新调整为沿栏杆面向左侧？


## 096 — `object_064_E2B`

**原始英文指令：** At 29.0 seconds, add one small green leaf on the curved white rail beside the jumping spider.

**中文翻译：** 在第 29.0 秒，在跳蛛旁边弯曲的白色栏杆上添加一片小绿叶。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一片叶子？

2. 新增叶子是否小且为绿色？

3. 叶子是否位于弯曲的白色栏杆上？

4. 叶子是否位于跳蛛旁边？


## 097 — `object_066_E1`

**原始英文指令：** Starting at 14.0 seconds, change the foreground giraffe's dark-brown patches to deep burgundy over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将前景长颈鹿的深棕色斑块变为深酒红色。

**状态：** 接受

**原子化判定句：**

1. 前景长颈鹿的斑块是否从深棕色变为深酒红色？

2. 斑块颜色变化是否在 2 秒内完成？


## 098 — `object_066_E2A`

**原始英文指令：** At 29.0 seconds, reposition the foreground giraffe and the spiral-horned antelope side by side with one body width between them.

**中文翻译：** 在第 29.0 秒，将前景长颈鹿和螺旋角羚羊并排放置，彼此相隔一个身宽。

**状态：** 接受

**原子化判定句：**

1. 前景长颈鹿和螺旋角羚羊是否并排放置？

2. 两只动物之间是否相隔一个身宽？


## 099 — `object_066_E2B`

**原始英文指令：** At 29.0 seconds, remove the background giraffe farthest from the foreground pair when it becomes isolated at 36.0 seconds.

**中文翻译：** 在第 29.0 秒，当距离前景动物对最远的背景长颈鹿于第 36.0 秒单独显现时，将其移除。

**状态：** 接受

**原子化判定句：**

1. 距离前景动物对最远的背景长颈鹿是否在 7 秒内单独显现？

2. 该长颈鹿单独显现时，是否被移除？


## 100 — `object_068_E1`

**原始英文指令：** Starting at 14.0 seconds, make the black hand brush touch the frog's back lightly three times.

**中文翻译：** 从第 14.0 秒开始，让黑色手刷轻触青蛙背部三次。

**状态：** 接受

**原子化判定句：**

1. 黑色手刷是否接触青蛙背部？

2. 每次接触是否轻柔？

3. 手刷是否恰好接触青蛙三次？


## 101 — `object_068_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the small yellow-brown frog perform two long forward jumps across the mat.

**中文翻译：** 从第 29.0 秒开始，让黄棕色小青蛙在垫子上向前长跳两次。

**状态：** 接受

**原子化判定句：**

1. 黄棕色小青蛙是否在垫子上跳跃？

2. 跳跃方向是否向前？

3. 跳跃距离是否较长？

4. 青蛙是否恰好跳两次？


## 102 — `object_068_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the black hand brush as a clay-animation prop over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将黑色手刷呈现为黏土动画道具。

**状态：** 接受

**原子化判定句：**

1. 黑色手刷是否被呈现为道具？

2. 该道具是否采用黏土动画风格？

3. 渲染变化是否在 2 秒内完成？


## 103 — `object_069_E1`

**原始英文指令：** Starting at 14.0 seconds, change the ferry's red upper panels to cobalt blue over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将渡轮的红色上部面板变为钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 渡轮的上部面板是否从红色变为钴蓝色？

2. 面板颜色变化是否在 2 秒内完成？


## 104 — `object_069_E2A`

**原始英文指令：** Starting at 29.0 seconds, zoom out smoothly over four seconds to show the entire ferry and its full V-shaped wake.

**中文翻译：** 从第 29.0 秒开始，在四秒内平稳拉远镜头，以显示整艘渡轮及其完整的 V 形尾流。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 4 秒内平稳拉远？

2. 拉远结束时，整艘渡轮及其完整的 V 形尾流是否可见？


## 105 — `object_069_E2B`

**原始英文指令：** At 29.0 seconds, add one small white sailboat on the water to the left of the approaching ferry.

**中文翻译：** 在第 29.0 秒，在驶近的渡轮左侧水面上添加一艘白色小帆船。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一艘帆船？

2. 新增帆船是否小且为白色？

3. 帆船是否位于水面上？

4. 帆船是否位于驶近的渡轮左侧？


## 106 — `object_070_E1`

**原始英文指令：** At 14.0 seconds, change the black laptop computer from partly open to fully closed.

**中文翻译：** 在第 14.0 秒，将黑色笔记本电脑从部分打开变为完全合上。

**状态：** 接受

**原子化判定句：**

1. 黑色笔记本电脑是否从部分打开状态合上？

2. 笔记本电脑是否完全合上？


## 107 — `object_070_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the upright laptop computer rock gently left and right while remaining supported on the table edges for five seconds.

**中文翻译：** 从第 29.0 秒开始，让竖立的笔记本电脑在左右轻轻摇摆的同时，保持由桌子边缘支撑五秒。

**状态：** 接受

**原子化判定句：**

1. 竖立的笔记本电脑是否左右轻轻摇摆并持续 5 秒？

2. 摇摆期间，笔记本电脑是否始终由桌子边缘支撑？


## 108 — `object_070_E2B`

**原始英文指令：** At 29.0 seconds, replace the multicolored bag below the table with a plain brown cardboard box of the same size.

**中文翻译：** 在第 29.0 秒，将桌子下方的多色袋子替换为一个同样大小的纯棕色纸箱。

**状态：** 接受

**原子化判定句：**

1. 桌子下方的多色袋子是否被替换为纸箱？

2. 替换后的纸箱是否为棕色？

3. 替换后的纸箱外观是否朴素？

4. 替换后的纸箱是否与原袋子大小相同？


## 109 — `object_071_E1`

**原始英文指令：** Starting at 19.0 seconds, change the white fawn's coat to pale silver gray over the next two seconds.

**中文翻译：** 从第 19.0 秒开始，在接下来的两秒内将白色幼鹿的皮毛变为浅银灰色。

**状态：** 接受

**原子化判定句：**

1. 白色幼鹿的皮毛是否变为浅银灰色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 110 — `object_071_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the spotted fawn complete its exit before the white fawn next lowers its head.

**中文翻译：** 从第 29.0 秒开始，让斑点幼鹿在白色幼鹿下一次低头之前完成离场。

**状态：** 接受

**原子化判定句：**

1. 白色幼鹿是否再次低头？

2. 斑点幼鹿是否在白色幼鹿再次低头之前完成离场？


## 111 — `object_071_E2B`

**原始英文指令：** Starting at 34.0 seconds, make the pale-silver-gray fawn and the spotted fawn outside touch noses twice.

**中文翻译：** 从第 34.0 秒开始，让浅银灰色幼鹿和外面的斑点幼鹿碰鼻两次。

**状态：** 接受

**原子化判定句：**

1. 浅银灰色幼鹿和外面的斑点幼鹿是否碰鼻？

2. 两只幼鹿是否恰好碰鼻两次？


## 112 — `object_072_E1`

**原始英文指令：** Starting at 14.0 seconds, change the blue character model from hard painted material to soft felt over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将蓝色角色模型的材质从硬质涂装材料变为柔软毛毡。

**状态：** 接受

**原子化判定句：**

1. 蓝色角色模型的材质是否变为毛毡？

2. 形成的毛毡材质是否显得柔软？

3. 材质变化是否在 2 秒内完成？


## 113 — `object_072_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the smaller gray-purple character wave one forelimb twice.

**中文翻译：** 从第 29.0 秒开始，让较小的灰紫色角色挥动一只前肢两次。

**状态：** 接受

**原子化判定句：**

1. 较小的灰紫色角色是否挥动一只前肢？

2. 该角色是否恰好挥动前肢两次？


## 114 — `object_072_E2B`

**原始英文指令：** At 29.0 seconds, remove the smaller gray-purple character facing the blue model.

**中文翻译：** 在第 29.0 秒，移除面向蓝色模型的较小灰紫色角色。

**状态：** 接受

**原子化判定句：**

1. 面向蓝色模型的较小灰紫色角色是否被移除？


## 115 — `object_074_E1`

**原始英文指令：** At 14.0 seconds, change the silver sedan's headlights from switched off to switched on.

**中文翻译：** 在第 14.0 秒，将银色轿车的前灯从关闭状态变为开启状态。

**状态：** 接受

**原子化判定句：**

1. 银色轿车的前灯是否从关闭状态变为开启状态？


## 116 — `object_074_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the silver sedan follow a tighter curve at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让银色轿车以原速度的一半沿更紧的弯道行驶六秒。

**状态：** 接受

**原子化判定句：**

1. 银色轿车是否沿比原来更紧的弯道行驶？

2. 轿车是否以原速度的一半行驶？

3. 这一行驶状态是否持续 6 秒？


## 117 — `object_074_E2B`

**原始英文指令：** At 29.0 seconds, replace the nearest orange traffic cone beside the sedan with a plain blue cone of the same size.

**中文翻译：** 在第 29.0 秒，将轿车旁最近的橙色交通锥替换为一个同样大小的纯蓝色交通锥。

**状态：** 接受

**原子化判定句：**

1. 轿车旁最近的橙色交通锥是否被替换为蓝色交通锥？

2. 替换后的交通锥外观是否朴素？

3. 替换后的交通锥是否与原交通锥大小相同？


## 118 — `object_076_E1`

**原始英文指令：** Starting at 12.0 seconds, make the monkey brush the small puppy's back with both hands four times.

**中文翻译：** 从第 12.0 秒开始，让猴子用双手梳理小狗的背部四次。

**状态：** 接受

**原子化判定句：**

1. 猴子是否梳理小狗的背部？

2. 猴子是否使用双手梳理小狗？

3. 梳理动作是否恰好进行四次？


## 119 — `object_076_E2A`

**原始英文指令：** At 36.0 seconds, pause the monkey's renewed grooming of the puppy for three seconds, then resume it.

**中文翻译：** 在第 36.0 秒，让猴子重新开始的幼犬梳理动作暂停三秒，然后恢复。

**状态：** 接受

**原子化判定句：**

1. 猴子是否重新开始梳理幼犬？

2. 重新开始梳理后，该动作是否暂停 3 秒？

3. 暂停 3 秒后，猴子是否恢复梳理幼犬？


## 120 — `object_076_E2B`

**原始英文指令：** Starting at 27.0 seconds, apply muted pastel colors and fine paper grain to the full monkey-and-puppy scene over the next two seconds.

**中文翻译：** 从第 27.0 秒开始，在接下来的两秒内为完整的猴子与幼犬场景应用柔和的粉彩色调和细腻纸张颗粒。

**状态：** 接受

**原子化判定句：**

1. 完整的猴子与幼犬场景是否在 2 秒内应用了柔和的粉彩色调？

2. 完整场景是否在同一段 2 秒内应用了细腻纸张颗粒？


## 121 — `object_083_E1`

**原始英文指令：** Starting at 14.0 seconds, change the deer's red-brown coat to cool gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将鹿的红棕色皮毛变为冷灰色。

**状态：** 接受

**原子化判定句：**

1. 鹿的皮毛是否从红棕色变为冷灰色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 122 — `object_083_E2A`

**原始英文指令：** At 29.0 seconds, reposition the deer at the center of the gravel shoulder beside the wooden fence.

**中文翻译：** 在第 29.0 秒，将鹿移到木栅栏旁碎石路肩的中央。

**状态：** 接受

**原子化判定句：**

1. 鹿是否被移到碎石路肩中央？

2. 鹿是否位于木栅栏旁？


## 123 — `object_083_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the deer perform two short backward hops away from the wooden fence.

**中文翻译：** 从第 29.0 秒开始，让鹿背离木栅栏向后短跳两次。

**状态：** 接受

**原子化判定句：**

1. 鹿是否向后跳？

2. 跳跃是否使鹿远离木栅栏？

3. 跳跃距离是否较短？

4. 鹿是否恰好跳两次？


## 124 — `object_084_E1`

**原始英文指令：** Starting at 14.0 seconds, change the medium-green lakeside grass to deep emerald green over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将湖边的中绿色草地变为深祖母绿色。

**状态：** 接受

**原子化判定句：**

1. 湖边草地是否从中绿色变为深祖母绿色？

2. 草地颜色变化是否在 2 秒内完成？


## 125 — `object_084_E2A`

**原始英文指令：** At 29.0 seconds, reposition the nearby gray cygnets into one evenly spaced row behind the foreground adult swan.

**中文翻译：** 在第 29.0 秒，将附近的灰色幼天鹅重新排列为前景成年天鹅后方间距均匀的一行。

**状态：** 接受

**原子化判定句：**

1. 附近的灰色幼天鹅是否排列成一行？

2. 这一行是否位于前景成年天鹅后方？

3. 幼天鹅在该行中的间距是否均匀？


## 126 — `object_084_E2B`

**原始英文指令：** At 29.0 seconds, remove the large gray stone nearest the pond edge behind the foreground swans.

**中文翻译：** 在第 29.0 秒，移除前景天鹅后方最靠近池塘边缘的大灰石。

**状态：** 接受

**原子化判定句：**

1. 前景天鹅后方最靠近池塘边缘的大灰石是否被移除？


## 127 — `object_085_E1`

**原始英文指令：** Starting at 12.0 seconds, make the active lion roll the small dark ball steadily forward with its nose for five seconds.

**中文翻译：** 从第 12.0 秒开始，让活跃的狮子用鼻子稳定地向前滚动小黑球五秒。

**状态：** 接受

**原子化判定句：**

1. 活跃的狮子是否用鼻子滚动小黑球？

2. 小球是否向前滚动？

3. 滚动是否稳定？

4. 滚动是否持续 5 秒？


## 128 — `object_085_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the lion resting beside the left wall stretch both forelegs forward twice.

**中文翻译：** 从第 29.0 秒开始，让在左墙旁休息的狮子向前伸展双前腿两次。

**状态：** 接受

**原子化判定句：**

1. 在左墙旁休息的狮子是否伸展双前腿？

2. 双前腿是否向前伸展？

3. 伸展动作是否恰好进行两次？


## 129 — `object_085_E2B`

**原始英文指令：** Starting at 27.0 seconds, render the lion resting beside the left wall as a charcoal sketch over the next two seconds.

**中文翻译：** 从第 27.0 秒开始，在接下来的两秒内将在左墙旁休息的狮子呈现为炭笔素描。

**状态：** 接受

**原子化判定句：**

1. 在左墙旁休息的狮子是否被呈现为炭笔素描？

2. 渲染变化是否在 2 秒内完成？


## 130 — `object_088_E1`

**原始英文指令：** Starting at 14.0 seconds, change the black-and-white cat's black fur to medium gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将黑白猫的黑色皮毛变为中灰色。

**状态：** 接受

**原子化判定句：**

1. 黑白猫的黑色皮毛是否变为中灰色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 131 — `object_088_E2A`

**原始英文指令：** At 29.0 seconds, reorient the black-and-white cat to face directly away from the white cat.

**中文翻译：** 在第 29.0 秒，重新调整黑白猫的朝向，使其正对着远离白猫的方向。

**状态：** 接受

**原子化判定句：**

1. 黑白猫是否被重新调整为正对着远离白猫的方向？


## 132 — `object_088_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the white cat turn in one complete circle on the ground.

**中文翻译：** 从第 29.0 秒开始，让白猫在地面上完整转一圈。

**状态：** 接受

**原子化判定句：**

1. 白猫是否完成一整圈转动？

2. 白猫是否恰好只转一圈？

3. 转圈过程中白猫是否保持在地面上？


## 133 — `object_090_E1`

**原始英文指令：** Starting at 14.0 seconds, change the shallow river water from muted gray-brown to clear blue-green over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将浅河水从暗淡的灰棕色变为清澈的蓝绿色。

**状态：** 接受

**原子化判定句：**

1. 浅河水是否从暗淡的灰棕色变为蓝绿色？

2. 变化后的河水是否显得清澈？

3. 河水变化是否在 2 秒内完成？


## 134 — `object_090_E2A`

**原始英文指令：** Starting at 23.0 seconds, accelerate the adult elephants' convergence to twice its original rate, forming a close group around the smaller elephant by 27.0 seconds.

**中文翻译：** 从第 23.0 秒开始，将成年大象聚拢的速度提高到原来的两倍，并在第 27.0 秒前于较小的大象周围形成紧密群组。

**状态：** 接受

**原子化判定句：**

1. 成年大象是否以原速度的两倍朝较小的大象聚拢？

2. 成年大象是否在 4 秒内于较小的大象周围形成紧密群组？


## 135 — `object_090_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the water splashes around the smaller elephant spread outward in three broad rings.

**中文翻译：** 从第 29.0 秒开始，让较小大象周围的水花以三个宽阔的环向外扩散。

**状态：** 接受

**原子化判定句：**

1. 较小大象周围的水花是否以环状向外扩散？

2. 是否恰好形成三个环？

3. 形成的环是否宽阔？


## 136 — `object_093_E1`

**原始英文指令：** Starting at 14.0 seconds, make the helicopter's landing skid lift the traffic cone twice in separate contacts.

**中文翻译：** 从第 14.0 秒开始，让直升机的起落架通过两次独立接触将交通锥提起两次。

**状态：** 接受

**原子化判定句：**

1. 直升机的起落架是否提起交通锥？

2. 起落架是否恰好提起交通锥两次？

3. 每次提起是否通过一次独立接触完成？


## 137 — `object_093_E2A`

**原始英文指令：** Starting at 29.0 seconds, accelerate the helicopter's remaining transport and release of the traffic cone to twice its original rate, returning it to the grass by 34.0 seconds.

**中文翻译：** 从第 29.0 秒开始，将直升机剩余的交通锥运输和释放过程加快到原速的两倍，并在第 34.0 秒前使其回到草地。

**状态：** 接受

**原子化判定句：**

1. 直升机剩余的交通锥运输过程是否以原速的两倍推进？

2. 直升机是否在加速后的过程中释放交通锥？

3. 交通锥是否在 5 秒内回到草地？


## 138 — `object_093_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full helicopter field scene into a 1960s color aviation film over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将完整的直升机与场地场景转换为 20 世纪 60 年代彩色航空电影风格。

**状态：** 接受

**原子化判定句：**

1. 完整的直升机与场地场景是否呈现出航空电影的视觉效果？

2. 形成的航空电影风格是否具有 20 世纪 60 年代的视觉特征？

3. 形成的电影画面是否为彩色？

4. 风格转变是否在 2 秒内完成？


## 139 — `object_094_E1`

**原始英文指令：** Starting at 14.0 seconds, change the helicopter's red fuselage panels to emerald green over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将直升机的红色机身面板变为祖母绿色。

**状态：** 接受

**原子化判定句：**

1. 直升机的机身面板是否从红色变为祖母绿色？

2. 面板颜色变化是否在 2 秒内完成？


## 140 — `object_094_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the aerobatic helicopter smoothly from a constant side angle for five seconds.

**中文翻译：** 从第 29.0 秒开始，以固定的侧面角度平稳跟拍特技飞行直升机五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟拍特技飞行直升机？

2. 跟拍是否保持固定的侧面角度？

3. 跟拍是否平稳？

4. 跟拍是否持续 5 秒？


## 141 — `object_094_E2B`

**原始英文指令：** At 29.0 seconds, replace the large dense cloud behind the helicopter with a thin elongated cloud.

**中文翻译：** 在第 29.0 秒，将直升机后方大片浓密的云替换为一条细长的云。

**状态：** 接受

**原子化判定句：**

1. 直升机后方大片浓密的云是否被替换？

2. 替换后的云是否较薄？

3. 替换后的云是否呈细长形？


## 142 — `object_095_E1`

**原始英文指令：** Starting at 14.0 seconds, change the long-haired dog's white coat to pale golden cream over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将长毛犬的白色皮毛变为浅金奶油色。

**状态：** 接受

**原子化判定句：**

1. 长毛犬的皮毛是否从白色变为浅金奶油色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 143 — `object_095_E2A`

**原始英文指令：** Starting at 42.0 seconds, make the dog's final run toward the snow edge progress at twice its original rate, reaching the edge by 44.0 seconds.

**中文翻译：** 从第 42.0 秒开始，让狗最后一次朝雪地边缘奔跑的过程以原速度的两倍推进，并在第 44.0 秒前到达边缘。

**状态：** 接受

**原子化判定句：**

1. 狗最后一次朝雪地边缘奔跑的过程是否以原速度的两倍推进？

2. 狗是否在 2 秒内到达雪地边缘？


## 144 — `object_095_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the leashed dog follow a wider zigzag route at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让拴着牵引绳的狗以原速度的一半沿更宽的之字形路线移动六秒。

**状态：** 接受

**原子化判定句：**

1. 拴着牵引绳的狗是否沿之字形路线移动？

2. 之字形路线是否比原来更宽？

3. 狗是否以原速度的一半移动？

4. 移动是否持续 6 秒？


## 145 — `object_096_E1`

**原始英文指令：** Starting at 14.0 seconds, change the capuchin monkey's dry fur to visibly wet fur with lightly clumped strands over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将卷尾猴干燥的皮毛变为明显湿润、毛束轻微结块的皮毛。

**状态：** 接受

**原子化判定句：**

1. 卷尾猴的皮毛是否在 2 秒内从干燥变为明显湿润？

2. 卷尾猴的毛束是否在同一段 2 秒内变得轻微结块？


## 146 — `object_096_E2A`

**原始英文指令：** At 29.0 seconds, reposition the seated monkey at the center of the wooden table.

**中文翻译：** 在第 29.0 秒，将坐着的猴子移到木桌中央。

**状态：** 接受

**原子化判定句：**

1. 坐着的猴子是否被移到木桌中央？


## 147 — `object_096_E2B`

**原始英文指令：** At 29.0 seconds, add one red apple beside the banana pieces on the wooden table.

**中文翻译：** 在第 29.0 秒，在木桌上的香蕉块旁添加一个红苹果。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个苹果？

2. 苹果是否为红色？

3. 苹果是否位于木桌上？

4. 苹果是否位于香蕉块旁？


## 148 — `object_099_E1`

**原始英文指令：** Starting at 20.0 seconds, change the adult tiger's black stripes to dark blue over the next two seconds.

**中文翻译：** 从第 20.0 秒开始，在接下来的两秒内将成年虎的黑色条纹变为深蓝色。

**状态：** 接受

**原子化判定句：**

1. 成年虎的条纹是否从黑色变为深蓝色？

2. 条纹颜色变化是否在 2 秒内完成？


## 149 — `object_099_E2A`

**原始英文指令：** Starting at 38.0 seconds, zoom out smoothly over four seconds to show the adult tiger, both cubs, and both waiting vehicles.

**中文翻译：** 从第 38.0 秒开始，在四秒内平稳拉远镜头，以显示成年虎、两只幼虎和两辆等候的车辆。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 4 秒内平稳拉远？

2. 拉远结束时，成年虎、两只幼虎和两辆等候的车辆是否都可见？


## 150 — `object_099_E2B`

**原始英文指令：** At 35.0 seconds, make the dry leaves behind the tiger family rise and swirl when the road crossing begins at 38.0 seconds.

**中文翻译：** 在第 35.0 秒，当虎群于第 38.0 秒开始过路时，让它们后方的干树叶扬起并旋转。

**状态：** 接受

**原子化判定句：**

1. 虎群是否在 3 秒内开始过路？

2. 开始过路时，虎群后方的干树叶是否扬起并旋转？


## 151 — `object_101_E1`

**原始英文指令：** At 14.0 seconds, change the all-terrain vehicle's headlights from switched off to switched on.

**中文翻译：** 在第 14.0 秒，将全地形车的前灯从关闭状态变为开启状态。

**状态：** 接受

**原子化判定句：**

1. 全地形车的前灯是否从关闭状态变为开启状态？


## 152 — `object_101_E2A`

**原始英文指令：** At 29.0 seconds, reposition the all-terrain vehicle directly before the central dirt ramp.

**中文翻译：** 在第 29.0 秒，将全地形车移到中央土坡正前方。

**状态：** 接受

**原子化判定句：**

1. 全地形车是否被移到中央土坡正前方？


## 153 — `object_101_E2B`

**原始英文指令：** At 29.0 seconds, add one plain blue traffic cone beside the central dirt ramp.

**中文翻译：** 在第 29.0 秒，在中央土坡旁添加一个纯蓝色交通锥。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个交通锥？

2. 交通锥是否为纯蓝色？

3. 交通锥是否位于中央土坡旁？


## 154 — `object_102_E1`

**原始英文指令：** Starting at 14.0 seconds, make the squirrel pat the long-haired cat's upper back four times with both forepaws.

**中文翻译：** 从第 14.0 秒开始，让松鼠用两只前爪拍打长毛猫的上背部四次。

**状态：** 接受

**原子化判定句：**

1. 松鼠是否拍打长毛猫的上背部？

2. 松鼠是否使用两只前爪？

3. 松鼠是否恰好拍打四次？


## 155 — `object_102_E2A`

**原始英文指令：** At 29.0 seconds, reposition the squirrel at the center of the long-haired cat's back.

**中文翻译：** 在第 29.0 秒，将松鼠移到长毛猫背部中央。

**状态：** 接受

**原子化判定句：**

1. 松鼠是否被移到长毛猫背部中央？


## 156 — `object_102_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the office background as a soft watercolor painting over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将办公室背景呈现为柔和的水彩画。

**状态：** 接受

**原子化判定句：**

1. 办公室背景是否被呈现为水彩画？

2. 形成的水彩画是否具有柔和的观感？

3. 渲染变化是否在 2 秒内完成？


## 157 — `object_104_E1`

**原始英文指令：** Starting at 14.0 seconds, change the buffalo's dark black-brown coat to pale ash gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将水牛深黑棕色的皮毛变为浅灰白色。

**状态：** 接受

**原子化判定句：**

1. 水牛的皮毛是否从深黑棕色变为浅灰白色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 158 — `object_104_E2A`

**原始英文指令：** At 29.0 seconds, reposition the two nearest lions side by side two body lengths behind the buffalo.

**中文翻译：** 在第 29.0 秒，将最近的两只狮子并排移到水牛后方两个身长处。

**状态：** 接受

**原子化判定句：**

1. 最近的两只狮子是否被并排放置？

2. 两只狮子是否位于水牛后方？

3. 它们与水牛是否相隔两个身长？


## 159 — `object_104_E2B`

**原始英文指令：** At 29.0 seconds, replace the palm-shaped shrub nearest the chase path with a gray boulder of similar size.

**中文翻译：** 在第 29.0 秒，将最靠近追逐路线的棕榈状灌木替换为一块大小相近的灰色巨石。

**状态：** 接受

**原子化判定句：**

1. 最靠近追逐路线的棕榈状灌木是否被替换为巨石？

2. 替换后的巨石是否为灰色？

3. 巨石是否与原灌木大小相近？


## 160 — `object_106_E1`

**原始英文指令：** Starting at 14.0 seconds, make the peacock and the brown-red chicken touch their extended wing tips three times.

**中文翻译：** 从第 14.0 秒开始，让孔雀和棕红色鸡用伸展的翼尖相触三次。

**状态：** 接受

**原子化判定句：**

1. 孔雀和棕红色鸡的翼尖是否相触？

2. 相触时它们的翅膀是否伸展？

3. 翼尖是否恰好相触三次？


## 161 — `object_106_E2A`

**原始英文指令：** At 29.0 seconds, reposition the peacock and the chicken side by side with two body lengths between them.

**中文翻译：** 在第 29.0 秒，将孔雀和鸡并排放置，彼此相隔两个身长。

**状态：** 接受

**原子化判定句：**

1. 孔雀和鸡是否被并排放置？

2. 它们之间是否相隔两个身长？


## 162 — `object_106_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full grassland bird scene into a textured oil-painting style over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将完整的草地鸟类场景转换为带纹理的油画风格。

**状态：** 接受

**原子化判定句：**

1. 完整的草地鸟类场景是否转换为油画风格？

2. 形成的油画风格是否具有可见纹理？

3. 风格转变是否在 2 秒内完成？


## 163 — `object_107_E1`

**原始英文指令：** Starting at 14.0 seconds, change the rhinoceros's gray-brown skin to cool slate gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将犀牛的灰棕色皮肤变为冷石板灰色。

**状态：** 接受

**原子化判定句：**

1. 犀牛的皮肤是否从灰棕色变为冷石板灰色？

2. 皮肤颜色变化是否在 2 秒内完成？


## 164 — `object_107_E2A`

**原始英文指令：** At 29.0 seconds, reorient the rhinoceros to face directly away from the camera.

**中文翻译：** 在第 29.0 秒，重新调整犀牛的朝向，使其正对着远离镜头的方向。

**状态：** 接受

**原子化判定句：**

1. 犀牛是否被重新调整为正对着远离镜头的方向？


## 165 — `object_107_E2B`

**原始英文指令：** At 29.0 seconds, remove the isolated tall grass clump directly before the rhinoceros.

**中文翻译：** 在第 29.0 秒，移除犀牛正前方孤立的高草丛。

**状态：** 接受

**原子化判定句：**

1. 犀牛正前方孤立的高草丛是否被移除？


## 166 — `object_110_E1`

**原始英文指令：** Starting at 14.0 seconds, change the muted green-brown seagrass to deep emerald green over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将暗淡的绿棕色海草变为深祖母绿色。

**状态：** 接受

**原子化判定句：**

1. 海草是否从暗淡的绿棕色变为深祖母绿色？

2. 海草颜色变化是否在 2 秒内完成？


## 167 — `object_110_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the submerged hippo turn at half its original rate for five seconds.

**中文翻译：** 从第 29.0 秒开始，让水下河马以原转向速度的一半转动五秒。

**状态：** 接受

**原子化判定句：**

1. 水下河马是否以原转向速度的一半转动？

2. 半速转动是否持续 5 秒？


## 168 — `object_110_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the submerged hippo follow a tighter clockwise arc above the seabed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让水下河马在海床上方沿更紧的顺时针弧线移动六秒。

**状态：** 接受

**原子化判定句：**

1. 水下河马是否沿更紧的弧线移动？

2. 河马是否沿顺时针方向移动？

3. 河马是否保持在海床上方？

4. 移动是否持续 6 秒？


## 169 — `object_112_E1`

**原始英文指令：** Starting at 14.0 seconds, make the tabby kitten bat the yellow feather four times with alternating forepaws.

**中文翻译：** 从第 14.0 秒开始，让虎斑幼猫交替使用前爪拍打黄色羽毛四次。

**状态：** 接受

**原子化判定句：**

1. 虎斑幼猫是否拍打黄色羽毛？

2. 幼猫是否恰好拍打四次？

3. 四次拍打是否交替使用前爪？


## 170 — `object_112_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the tabby kitten roll over twice beside the red flower-shaped toys.

**中文翻译：** 从第 29.0 秒开始，让虎斑幼猫在红色花形玩具旁翻滚两次。

**状态：** 接受

**原子化判定句：**

1. 虎斑幼猫是否翻滚？

2. 幼猫是否恰好翻滚两次？

3. 翻滚是否发生在红色花形玩具旁？


## 171 — `object_112_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the yellow feather toy as a clay-animation prop over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将黄色羽毛玩具呈现为黏土动画道具。

**状态：** 接受

**原子化判定句：**

1. 黄色羽毛玩具是否被呈现为道具？

2. 该道具是否采用黏土动画风格？

3. 渲染变化是否在 2 秒内完成？


## 172 — `object_113_E1`

**原始英文指令：** Starting at 14.0 seconds, change the stunt kite's yellow-green wing panels to bright cyan over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将特技风筝的黄绿色翼面变为亮青色。

**状态：** 接受

**原子化判定句：**

1. 特技风筝的翼面是否从黄绿色变为亮青色？

2. 翼面颜色变化是否在 2 秒内完成？


## 173 — `object_113_E2A`

**原始英文指令：** Starting at 29.0 seconds, move the camera smoothly to follow the stunt kite, keeping it within the central region of the frame for five seconds.

**中文翻译：** 从第 29.0 秒开始，让镜头平稳移动以跟随特技风筝，并使其在画面中央区域保持五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平稳移动并跟随特技风筝 5 秒？

2. 镜头移动期间，特技风筝是否保持在画面中央区域？


## 174 — `object_113_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the stunt kite follow four compact alternating zigzags over six seconds.

**中文翻译：** 从第 29.0 秒开始，让特技风筝在六秒内完成四次紧凑的交替之字形飞行。

**状态：** 接受

**原子化判定句：**

1. 特技风筝是否沿之字形轨迹飞行？

2. 风筝是否恰好完成四次之字形飞行？

3. 之字形轨迹是否紧凑且方向交替？

4. 四次之字形飞行是否在 6 秒内完成？


## 175 — `object_117_E1`

**原始英文指令：** At 14.0 seconds, change the robot toy's two back wing panels from folded to fully extended.

**中文翻译：** 在第 14.0 秒，将机器人玩具的两块背部翼板从折叠状态变为完全展开。

**状态：** 接受

**原子化判定句：**

1. 机器人玩具的两块背部翼板是否都从折叠状态展开？

2. 两块翼板是否都完全展开？


## 176 — `object_117_E2A`

**原始英文指令：** At 29.0 seconds, pause the expanded robot form's turntable rotation for three seconds, then resume it.

**中文翻译：** 在第 29.0 秒，让展开形态机器人的转台旋转暂停三秒，然后恢复。

**状态：** 接受

**原子化判定句：**

1. 展开形态的机器人是否正在转台上旋转？

2. 转台旋转是否暂停 3 秒？

3. 暂停 3 秒后，转台旋转是否恢复？


## 177 — `object_117_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the expanded robot toy swing both arms outward twice.

**中文翻译：** 从第 29.0 秒开始，让展开形态的机器人玩具将双臂向外摆动两次。

**状态：** 接受

**原子化判定句：**

1. 展开形态的机器人玩具是否摆动双臂？

2. 双臂是否向外摆动？

3. 向外摆动是否恰好进行两次？


## 178 — `object_120_E1`

**原始英文指令：** Starting at 14.0 seconds, change the flat cool marine light to warm low-angle illumination over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将平淡的冷调海上光线变为暖色低角度照明。

**状态：** 接受

**原子化判定句：**

1. 海上光线是否从冷调变为暖调？

2. 变化后的照明是否来自低角度？

3. 光线变化是否在 2 秒内完成？


## 179 — `object_120_E2A`

**原始英文指令：** Starting at 29.0 seconds, zoom out smoothly over four seconds to show the entire ship and both sides of its bow wake.

**中文翻译：** 从第 29.0 秒开始，在四秒内平稳拉远镜头，以显示整艘船及其船首尾流的两侧。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 4 秒内平稳拉远？

2. 拉远结束时，整艘船及其船首尾流的两侧是否都可见？


## 180 — `object_120_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the passenger ship pitch with half its original vertical amplitude for six seconds.

**中文翻译：** 从第 29.0 秒开始，让客船以原竖直振幅的一半俯仰六秒。

**状态：** 接受

**原子化判定句：**

1. 客船俯仰的竖直振幅是否减为原来的一半？

2. 半振幅俯仰是否持续 6 秒？


## 181 — `object_121_E1`

**原始英文指令：** Starting at 14.0 seconds, make the two adult tigers touch noses and alternately tap each other's foreleg three times.

**中文翻译：** 从第 14.0 秒开始，让两只成年虎碰鼻，并交替拍打对方的前腿三次。

**状态：** 接受

**原子化判定句：**

1. 两只成年虎是否碰鼻？

2. 两只成年虎是否交替拍打对方的前腿恰好三次？


## 182 — `object_121_E2A`

**原始英文指令：** At 29.0 seconds, reposition the two adult tigers side by side with one body width between them.

**中文翻译：** 在第 29.0 秒，将两只成年虎并排放置，彼此相隔一个身宽。

**状态：** 接受

**原子化判定句：**

1. 两只成年虎是否被并排放置？

2. 两只成年虎之间是否相隔一个身宽？


## 183 — `object_121_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the two adult tigers as detailed colored-pencil illustrations over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将两只成年虎呈现为细致的彩色铅笔插画。

**状态：** 接受

**原子化判定句：**

1. 两只成年虎是否都被呈现为插画？

2. 插画是否采用彩色铅笔风格？

3. 插画是否细致？

4. 渲染变化是否在 2 秒内完成？


## 184 — `object_122_E1`

**原始英文指令：** Starting at 14.0 seconds, change the small shark's light-gray dorsal skin to pale blue-gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将小鲨鱼背部的浅灰色皮肤变为浅蓝灰色。

**状态：** 接受

**原子化判定句：**

1. 小鲨鱼背部的皮肤是否从浅灰色变为浅蓝灰色？

2. 皮肤颜色变化是否在 2 秒内完成？


## 185 — `object_122_E2A`

**原始英文指令：** At 29.0 seconds, reposition the small shark at the center of the clear sandy channel.

**中文翻译：** 在第 29.0 秒，将小鲨鱼移到清澈沙质水道的中央。

**状态：** 接受

**原子化判定句：**

1. 小鲨鱼是否被移到清澈沙质水道的中央？


## 186 — `object_122_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the small shark follow a tighter clockwise arc through the shallow water for six seconds.

**中文翻译：** 从第 29.0 秒开始，让小鲨鱼在浅水中沿更紧的顺时针弧线游动六秒。

**状态：** 接受

**原子化判定句：**

1. 小鲨鱼是否沿更紧的弧线游动？

2. 鲨鱼是否沿顺时针方向游动？

3. 鲨鱼是否在浅水中移动？

4. 游动是否持续 6 秒？


## 187 — `object_123_E1`

**原始英文指令：** Starting at 13.0 seconds, make the two adult zebras rear together and place both forelegs across each other's shoulders twice.

**中文翻译：** 从第 13.0 秒开始，让两只成年斑马一起后腿站立，并将双前腿搭在对方肩上两次。

**状态：** 接受

**原子化判定句：**

1. 两只成年斑马是否一起后腿站立？

2. 后腿站立时，两只斑马是否将双前腿搭在对方肩上恰好两次？


## 188 — `object_123_E2A`

**原始英文指令：** At 29.0 seconds, reposition the two adult zebras facing each other with one body length between them.

**中文翻译：** 在第 29.0 秒，将两只成年斑马面对面放置，彼此相隔一个身长。

**状态：** 接受

**原子化判定句：**

1. 两只成年斑马是否面对彼此？

2. 两只成年斑马之间是否相隔一个身长？


## 189 — `object_123_E2B`

**原始英文指令：** Starting at 28.0 seconds, transform the full zebra enclosure scene into a textured oil-painting style over the next two seconds.

**中文翻译：** 从第 28.0 秒开始，在接下来的两秒内将完整的斑马围栏场景转换为带纹理的油画风格。

**状态：** 接受

**原子化判定句：**

1. 完整的斑马围栏场景是否转换为油画风格？

2. 形成的油画风格是否具有可见纹理？

3. 风格转变是否在 2 秒内完成？


## 190 — `object_125_E1`

**原始英文指令：** Starting at 14.0 seconds, change the squirrel's gray-brown dorsal fur to warm reddish brown over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将松鼠背部的灰棕色皮毛变为暖红棕色。

**状态：** 接受

**原子化判定句：**

1. 松鼠背部的皮毛是否从灰棕色变为暖红棕色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 191 — `object_125_E2A`

**原始英文指令：** At 29.0 seconds, reposition the squirrel beside the base of the black container near the wall.

**中文翻译：** 在第 29.0 秒，将松鼠移到墙边黑色容器的底部旁。

**状态：** 接受

**原子化判定句：**

1. 松鼠是否被移到墙边黑色容器的底部旁？


## 192 — `object_125_E2B`

**原始英文指令：** At 29.0 seconds, add one small plain pine cone on the exposed ground beside the squirrel.

**中文翻译：** 在第 29.0 秒，在松鼠旁裸露的地面上添加一个小型普通松果。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个松果？

2. 松果是否小且外观普通？

3. 松果是否位于裸露的地面上？

4. 松果是否位于松鼠旁？


## 193 — `object_127_E1`

**原始英文指令：** Starting at 14.0 seconds, make the active opossum gently touch the supine opossum's shoulder twice with its nose and forepaw.

**中文翻译：** 从第 14.0 秒开始，让活跃的负鼠用鼻子和前爪轻触仰卧负鼠的肩部两次。

**状态：** 接受

**原子化判定句：**

1. 活跃的负鼠是否轻触仰卧负鼠的肩部？

2. 它是否同时使用鼻子和前爪？

3. 它是否恰好接触肩部两次？


## 194 — `object_127_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the active opossum circle the supine opossum once over five seconds.

**中文翻译：** 从第 29.0 秒开始，让活跃的负鼠在五秒内围绕仰卧的负鼠绕行一圈。

**状态：** 接受

**原子化判定句：**

1. 活跃的负鼠是否围绕仰卧的负鼠绕行？

2. 它是否恰好绕行一圈？

3. 完整一圈是否在 5 秒内完成？


## 195 — `object_127_E2B`

**原始英文指令：** Starting at 29.0 seconds, change the dry pale grass around the two opossums to visibly wet, darker grass over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将两只负鼠周围干燥的浅色草地变为明显湿润、颜色更深的草地。

**状态：** 接受

**原子化判定句：**

1. 两只负鼠周围的草地是否在 2 秒内从干燥变为明显湿润？

2. 草地是否在同一段 2 秒内变得更暗？


## 196 — `object_128_E1`

**原始英文指令：** Starting at 20.0 seconds, change the curved transparent container wall to evenly frosted translucent plastic over the next two seconds.

**中文翻译：** 从第 20.0 秒开始，在接下来的两秒内将弯曲透明的容器壁变为均匀磨砂的半透明塑料。

**状态：** 接受

**原子化判定句：**

1. 弯曲的容器壁是否变为塑料材质？

2. 形成的塑料是否为半透明？

3. 塑料表面是否呈均匀磨砂状态？

4. 材质变化是否在 2 秒内完成？


## 197 — `object_128_E2A`

**原始英文指令：** At 35.0 seconds, reposition the tiny red-brown arachnid at the center of the white liner.

**中文翻译：** 在第 35.0 秒，将微小的红棕色蛛形动物移到白色衬垫中央。

**状态：** 接受

**原子化判定句：**

1. 微小的红棕色蛛形动物是否被移到白色衬垫中央？


## 198 — `object_128_E2B`

**原始英文指令：** Starting at 35.0 seconds, make the tiny red-brown arachnid raise its front pair of legs three times.

**中文翻译：** 从第 35.0 秒开始，让微小的红棕色蛛形动物将前面一对腿抬起三次。

**状态：** 接受

**原子化判定句：**

1. 微小的红棕色蛛形动物是否抬起前面一对腿？

2. 它是否恰好抬起三次？


## 199 — `object_130_E1`

**原始英文指令：** Starting at 14.0 seconds, change the shallow wetland channel from muted green-brown to clear turquoise over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将浅湿地水道从暗淡的绿棕色变为清澈的绿松石色。

**状态：** 接受

**原子化判定句：**

1. 浅湿地水道是否从暗淡的绿棕色变为绿松石色？

2. 变化后的水体是否显得清澈？

3. 水体变化是否在 2 秒内完成？


## 200 — `object_130_E2A`

**原始英文指令：** Starting at 29.0 seconds, accelerate the lions' separation into the water and grass routes to twice its original rate for six seconds.

**中文翻译：** 从第 29.0 秒开始，将狮子分开进入水路和草地路线的过程加快到原速的两倍，持续六秒。

**状态：** 接受

**原子化判定句：**

1. 狮子是否分开进入水路和草地路线？

2. 分开过程是否以原速的两倍推进？

3. 两倍速分开过程是否持续 6 秒？


## 201 — `object_130_E2B`

**原始英文指令：** At 29.0 seconds, replace the isolated tall grass clump nearest the water channel with a gray boulder of similar size.

**中文翻译：** 在第 29.0 秒，将最靠近水道的孤立高草丛替换为一块大小相近的灰色巨石。

**状态：** 接受

**原子化判定句：**

1. 最靠近水道的孤立高草丛是否被替换为巨石？

2. 替换后的巨石是否为灰色？

3. 巨石是否与原草丛大小相近？


## 202 — `object_135_E1`

**原始英文指令：** Starting at 14.0 seconds, change the monitor lizard's pale dorsal spots and bands to muted gold over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将巨蜥背部的浅色斑点和条带变为暗金色。

**状态：** 接受

**原子化判定句：**

1. 巨蜥背部的浅色斑点是否变为暗金色？

2. 巨蜥背部的浅色条带是否变为暗金色？

3. 两处颜色变化是否都在 2 秒内完成？


## 203 — `object_135_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the monitor lizard follow a wider curve at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让巨蜥以原速度的一半沿更宽的弧线移动六秒。

**状态：** 接受

**原子化判定句：**

1. 巨蜥是否沿比原来更宽的弧线移动？

2. 巨蜥是否以原速度的一半移动？

3. 移动是否持续 6 秒？


## 204 — `object_135_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the indoor background outside the monitor lizard as a soft charcoal sketch over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将巨蜥以外的室内背景呈现为柔和的炭笔素描。

**状态：** 接受

**原子化判定句：**

1. 巨蜥以外的室内背景是否被呈现为炭笔素描？

2. 形成的炭笔素描是否具有柔和的观感？

3. 渲染变化是否在 2 秒内完成？


## 205 — `object_138_E1`

**原始英文指令：** Starting at 14.0 seconds, make the two orange-white fish circle the fallen red container once in opposite directions.

**中文翻译：** 从第 14.0 秒开始，让两条橙白色鱼沿相反方向围绕倒下的红色容器各绕行一圈。

**状态：** 接受

**原子化判定句：**

1. 两条橙白色鱼是否都围绕倒下的红色容器游动？

2. 每条鱼是否都恰好完整绕行一圈？

3. 两条鱼的绕行方向是否相反？


## 206 — `object_138_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the white tubular tool trace three slow circles above the aquarium substrate.

**中文翻译：** 从第 29.0 秒开始，让白色管状工具在水族箱底床上方缓慢画三个圆圈。

**状态：** 接受

**原子化判定句：**

1. 白色管状工具是否画出圆圈？

2. 工具是否恰好画出三个圆圈？

3. 画圈动作是否缓慢？

4. 圆圈是否在水族箱底床上方画出？


## 207 — `object_138_E2B`

**原始英文指令：** At 29.0 seconds, remove the white tubular tool extending into the aquarium from outside the frame.

**中文翻译：** 在第 29.0 秒，移除从画面外伸入水族箱的白色管状工具。

**状态：** 接受

**原子化判定句：**

1. 从画面外伸入水族箱的白色管状工具是否被移除？


## 208 — `object_140_E1`

**原始英文指令：** At 14.0 seconds, change the nearest illuminated courtyard lamp from switched on to switched off.

**中文翻译：** 在第 14.0 秒，将最近的亮起庭院灯从开启状态变为关闭状态。

**状态：** 接受

**原子化判定句：**

1. 最近的亮起庭院灯是否从开启状态变为关闭状态？


## 209 — `object_140_E2A`

**原始英文指令：** Starting at 29.0 seconds, zoom out smoothly over four seconds to show the fox, paved path, low wall, and raised grass together.

**中文翻译：** 从第 29.0 秒开始，在四秒内平稳拉远镜头，以同时显示狐狸、铺装小路、矮墙和高起的草地。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 4 秒内平稳拉远？

2. 拉远结束时，狐狸、铺装小路、矮墙和高起的草地是否同时可见？


## 210 — `object_140_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the red fox walk along the low wall at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让红狐以原速度的一半沿矮墙行走六秒。

**状态：** 接受

**原子化判定句：**

1. 红狐是否沿矮墙行走？

2. 红狐是否以原速度的一半行走？

3. 行走是否持续 6 秒？


## 211 — `object_144_E1`

**原始英文指令：** Starting at 19.0 seconds, make the small puppy pin the pink plush toy with both forepaws and shake it from side to side three times.

**中文翻译：** 从第 19.0 秒开始，让小狗用两只前爪按住粉色毛绒玩具，并将其左右摇动三次。

**状态：** 接受

**原子化判定句：**

1. 小狗是否用两只前爪按住粉色毛绒玩具？

2. 按住玩具时，小狗是否将其恰好左右摇动三次？


## 212 — `object_144_E2A`

**原始英文指令：** At 29.0 seconds, reposition the pink plush toy between the small puppy's two forepaws.

**中文翻译：** 在第 29.0 秒，将粉色毛绒玩具移到小狗的两只前爪之间。

**状态：** 接受

**原子化判定句：**

1. 粉色毛绒玩具是否被移到小狗的两只前爪之间？


## 213 — `object_144_E2B`

**原始英文指令：** Starting at 29.0 seconds, render the small puppy as a handcrafted felt stop-motion character over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将小狗呈现为手工毛毡定格动画角色。

**状态：** 接受

**原子化判定句：**

1. 小狗是否被呈现为定格动画角色？

2. 该角色是否具有毛毡质感？

3. 该角色是否显得由手工制作？

4. 渲染变化是否在 2 秒内完成？


## 214 — `object_145_E1`

**原始英文指令：** Starting at 14.0 seconds, change the wet mud coating the elephant calf to dry lightly cracked mud over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将覆盖幼象的湿泥变为干燥、轻微开裂的泥层。

**状态：** 接受

**原子化判定句：**

1. 覆盖幼象的泥层是否在 2 秒内从湿润变为干燥？

2. 干燥的泥层是否在同一段 2 秒内变得轻微开裂？


## 215 — `object_145_E2A`

**原始英文指令：** At 29.0 seconds, reposition the elephant calf centrally between the three adult elephants with equal spacing to each adult.

**中文翻译：** 在第 29.0 秒，将幼象移到三头成年象之间的中央，并与每头成年象保持相等距离。

**状态：** 接受

**原子化判定句：**

1. 幼象是否位于三头成年象之间的中央？

2. 幼象与三头成年象中的每一头是否保持相等距离？


## 216 — `object_145_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the elephant calf lift and curl its trunk overhead three times.

**中文翻译：** 从第 29.0 秒开始，让幼象将鼻子举过头顶并卷曲三次。

**状态：** 接受

**原子化判定句：**

1. 幼象是否将鼻子举过头顶？

2. 鼻子举起时是否发生卷曲？

3. 举起并卷曲鼻子的动作是否恰好进行三次？


## 217 — `object_147_E1`

**原始英文指令：** Starting at 14.0 seconds, change the locomotive's unmarked black hood panels to deep forest green over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将机车无标记的黑色罩板变为深森林绿色。

**状态：** 接受

**原子化判定句：**

1. 机车的黑色罩板是否变为深森林绿色？

2. 罩板颜色变化是否在 2 秒内完成？


## 218 — `object_147_E2A`

**原始英文指令：** At 29.0 seconds, reorient the diesel locomotive to face directly right along the far parallel track.

**中文翻译：** 在第 29.0 秒，重新调整柴油机车的朝向，使其沿远处平行轨道正对右侧。

**状态：** 接受

**原子化判定句：**

1. 柴油机车是否被重新调整为沿远处平行轨道正对右侧？


## 219 — `object_147_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the foreground grass beside the parallel railway form two broad bending waves as the train passes.

**中文翻译：** 从第 29.0 秒开始，让列车经过时平行铁路旁的前景草地形成两道宽阔的弯曲波浪。

**状态：** 接受

**原子化判定句：**

1. 列车是否沿平行铁路经过？

2. 列车经过时，铁路旁的前景草地是否形成恰好两道宽阔的弯曲波浪？


## 220 — `object_148_E1`

**原始英文指令：** Starting at 14.0 seconds, change the orange cat's fur to pale cream over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将橙猫的皮毛变为浅奶油色。

**状态：** 接受

**原子化判定句：**

1. 橙猫的皮毛是否变为浅奶油色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 221 — `object_148_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the cat smoothly from a constant elevated side angle for five seconds.

**中文翻译：** 从第 29.0 秒开始，以固定的高位侧面角度平稳跟拍猫五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟拍猫？

2. 跟拍是否保持固定的高位侧面角度？

3. 跟拍是否平稳？

4. 跟拍是否持续 5 秒？


## 222 — `object_148_E2B`

**原始英文指令：** At 29.0 seconds, remove the isolated reddish-brown branch from the lower foreground of the grass scene.

**中文翻译：** 在第 29.0 秒，移除草地场景前景下方孤立的红棕色树枝。

**状态：** 接受

**原子化判定句：**

1. 草地场景前景下方孤立的红棕色树枝是否被移除？


## 223 — `object_153_E1`

**原始英文指令：** At 14.0 seconds, change the crocodile's jaws from closed to a half-open state.

**中文翻译：** 在第 14.0 秒，将鳄鱼的上下颌从闭合状态变为半张开状态。

**状态：** 接受

**原子化判定句：**

1. 鳄鱼的上下颌是否从闭合状态张开？

2. 上下颌是否停在半张开状态？


## 224 — `object_153_E2A`

**原始英文指令：** Starting at 29.0 seconds, reorder the actions so all three lionesses encircle the crocodile before its next defensive twist begins.

**中文翻译：** 从第 29.0 秒开始，重新安排动作顺序，使三只母狮在鳄鱼下一次防御性扭身开始之前将其包围。

**状态：** 接受

**原子化判定句：**

1. 鳄鱼是否开始下一次防御性扭身？

2. 在该防御性扭身开始之前，三只母狮是否已将鳄鱼包围？


## 225 — `object_153_E2B`

**原始英文指令：** At 29.0 seconds, replace the isolated gray riverbank rock nearest the crocodile with pale driftwood of similar size.

**中文翻译：** 在第 29.0 秒，将最靠近鳄鱼的孤立灰色河岸岩石替换为大小相近的浅色浮木。

**状态：** 接受

**原子化判定句：**

1. 最靠近鳄鱼的孤立灰色河岸岩石是否被替换为浮木？

2. 替换后的浮木是否为浅色？

3. 浮木是否与原岩石大小相近？


## 226 — `object_154_E1`

**原始英文指令：** Starting at 14.0 seconds, change the aircraft's unmarked white fuselage panels to bright silver over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将飞机无标记的白色机身面板变为亮银色。

**状态：** 接受

**原子化判定句：**

1. 飞机的白色机身面板是否变为亮银色？

2. 面板颜色变化是否在 2 秒内完成？


## 227 — `object_154_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the taxiing aircraft smoothly from a constant low side angle for five seconds.

**中文翻译：** 从第 29.0 秒开始，以固定的低位侧面角度平稳跟拍正在滑行的飞机五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟拍正在滑行的飞机？

2. 跟拍是否保持固定的低位侧面角度？

3. 跟拍是否平稳？

4. 跟拍是否持续 5 秒？


## 228 — `object_154_E2B`

**原始英文指令：** At 29.0 seconds, replace the isolated dry grass clump nearest the taxiway with a low gray boulder of similar size.

**中文翻译：** 在第 29.0 秒，将最靠近滑行道的孤立干草丛替换为一块大小相近的低矮灰色巨石。

**状态：** 接受

**原子化判定句：**

1. 最靠近滑行道的孤立干草丛是否被替换为巨石？

2. 替换后的巨石是否低矮？

3. 巨石是否为灰色？

4. 巨石是否与原草丛大小相近？


## 229 — `object_157_E1`

**原始英文指令：** Starting at 14.0 seconds, change the bright-green seedling leaves outside the railing to muted purple-red over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将栏杆外幼苗的亮绿色叶片变为暗紫红色。

**状态：** 接受

**原子化判定句：**

1. 栏杆外幼苗的叶片是否从亮绿色变为暗紫红色？

2. 叶片颜色变化是否在 2 秒内完成？


## 230 — `object_157_E2A`

**原始英文指令：** Starting at 29.0 seconds, reorder the actions so the approaching monkey reaches the seated monkey before the seated monkey touches the green leaves.

**中文翻译：** 从第 29.0 秒开始，重新安排动作顺序，使走近的猴子在坐着的猴子触碰绿叶之前到达其身边。

**状态：** 接受

**原子化判定句：**

1. 坐着的猴子是否触碰绿叶？

2. 走近的猴子是否在该触叶动作发生之前到达坐着的猴子身边？


## 231 — `object_157_E2B`

**原始英文指令：** At 29.0 seconds, add one small plain red ball on the soil beside the muted purple-red seedlings.

**中文翻译：** 在第 29.0 秒，在暗紫红色幼苗旁的土壤上添加一个小型纯红色球。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个球？

2. 球是否小且为纯红色？

3. 球是否位于土壤上？

4. 球是否位于暗紫红色幼苗旁？


## 232 — `object_158_E1`

**原始英文指令：** Starting at 14.0 seconds, change the rosetted jaguar's golden-tan base coat to pale silver over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将玫瑰斑美洲豹的金棕色底毛变为浅银色。

**状态：** 接受

**原子化判定句：**

1. 玫瑰斑美洲豹的底毛是否从金棕色变为浅银色？

2. 底毛颜色变化是否在 2 秒内完成？


## 233 — `object_158_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the adult jaguar walk toward the vegetation at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让成年美洲豹以原速度的一半朝植被行走六秒。

**状态：** 接受

**原子化判定句：**

1. 成年美洲豹是否朝植被行走？

2. 美洲豹是否以原速度的一半行走？

3. 行走是否持续 6 秒？


## 234 — `object_158_E2B`

**原始英文指令：** At 29.0 seconds, add one small green shrub on the open sand near the forest edge behind the jaguar.

**中文翻译：** 在第 29.0 秒，在美洲豹后方靠近森林边缘的开阔沙地上添加一丛绿色小灌木。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一丛灌木？

2. 灌木是否小且为绿色？

3. 灌木是否位于靠近森林边缘的开阔沙地上？

4. 灌木是否位于美洲豹后方？


## 235 — `object_159_E1`

**原始英文指令：** Starting at 14.0 seconds, change the slightly cloudy aquarium water to fully clear water over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将略显浑浊的水族箱水变为完全清澈。

**状态：** 接受

**原子化判定句：**

1. 水族箱水是否从浑浊变为清澈？

2. 水体是否达到完全清澈？

3. 水体变化是否在 2 秒内完成？


## 236 — `object_159_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the central green aquatic plant sway left and right three times.

**中文翻译：** 从第 29.0 秒开始，让中央的绿色水生植物左右摆动三次。

**状态：** 接受

**原子化判定句：**

1. 中央的绿色水生植物是否左右摆动？

2. 水生植物是否恰好完成三次左右摆动？


## 237 — `object_159_E2B`

**原始英文指令：** At 29.0 seconds, replace the largest flat gray stone beside the aquatic plant with a plain white shell of similar size.

**中文翻译：** 在第 29.0 秒，将水生植物旁最大的扁平灰石替换为一个大小相近的纯白色贝壳。

**状态：** 接受

**原子化判定句：**

1. 水生植物旁最大的扁平灰石是否被替换为贝壳？

2. 替换后的贝壳是否为白色？

3. 贝壳的外观是否朴素？

4. 贝壳是否与原石头大小相近？


## 238 — `object_160_E1`

**原始英文指令：** Starting at 14.0 seconds, change the hard direct sunlight on the toad and asphalt to soft diffuse daylight over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将照在蟾蜍和沥青上的强烈直射阳光变为柔和的漫射日光。

**状态：** 接受

**原子化判定句：**

1. 照在蟾蜍和沥青上的光线是否都变为日光？

2. 变化后的日光是否柔和且为漫射光？

3. 光线变化是否在 2 秒内完成？


## 239 — `object_160_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the brown toad lift its front body with both forelegs twice over five seconds.

**中文翻译：** 从第 29.0 秒开始，让棕色蟾蜍在五秒内用两条前腿抬起前半身两次。

**状态：** 接受

**原子化判定句：**

1. 棕色蟾蜍是否抬起前半身？

2. 蟾蜍是否使用两条前腿抬起？

3. 抬起动作是否恰好进行两次？

4. 两次抬起是否在 5 秒内完成？


## 240 — `object_160_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the brown toad crawl forward at twice its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让棕色蟾蜍以原速度的两倍向前爬行六秒。

**状态：** 接受

**原子化判定句：**

1. 棕色蟾蜍是否向前爬行？

2. 蟾蜍是否以原速度的两倍爬行？

3. 两倍速爬行是否持续 6 秒？


## 241 — `object_161_E1`

**原始英文指令：** At 14.0 seconds, change the robot vacuum's raised top sensor to a flush position within the surrounding housing.

**中文翻译：** 在第 14.0 秒，将扫地机器人的凸起顶部传感器变为与周围外壳齐平的位置。

**状态：** 接受

**原子化判定句：**

1. 扫地机器人的凸起顶部传感器是否变为与周围外壳齐平的位置？


## 242 — `object_161_E2A`

**原始英文指令：** At 29.0 seconds, reposition the robot vacuum at the center of the dark floor area.

**中文翻译：** 在第 29.0 秒，将扫地机器人移到深色地面区域的中央。

**状态：** 接受

**原子化判定句：**

1. 扫地机器人是否被移到深色地面区域的中央？


## 243 — `object_161_E2B`

**原始英文指令：** At 29.0 seconds, add one small plain orange traffic cone beside the white cabinet near the robot vacuum.

**中文翻译：** 在第 29.0 秒，在扫地机器人附近的白色柜子旁添加一个小型纯橙色交通锥。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个交通锥？

2. 交通锥是否小且为纯橙色？

3. 交通锥是否位于白色柜子旁？

4. 交通锥是否靠近扫地机器人？


## 244 — `object_162_E1`

**原始英文指令：** Starting at 14.0 seconds, change the fox's red-brown dorsal fur to pale silver-gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将狐狸背部的红棕色皮毛变为浅银灰色。

**状态：** 接受

**原子化判定句：**

1. 狐狸背部的皮毛是否从红棕色变为浅银灰色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 245 — `object_162_E2A`

**原始英文指令：** At 29.0 seconds, reposition the fox one meter directly in front of the standing adult beside the parked vehicle.

**中文翻译：** 在第 29.0 秒，将狐狸移到停放车辆旁站立成人正前方一米处。

**状态：** 接受

**原子化判定句：**

1. 狐狸是否被移到停放车辆旁站立成人的正前方？

2. 狐狸与该成人是否相距一米？


## 246 — `object_162_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the pale-silver-gray fox sit and raise one forepaw twice over five seconds.

**中文翻译：** 从第 29.0 秒开始，让浅银灰色狐狸在五秒内坐下并抬起一只前爪两次。

**状态：** 接受

**原子化判定句：**

1. 浅银灰色狐狸是否在 5 秒内坐下？

2. 坐下后，狐狸是否在同一段 5 秒内恰好抬起一只前爪两次？


## 247 — `object_165_E1`

**原始英文指令：** Starting at 14.0 seconds, change the cool blue-green underwater light to warm neutral illumination over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将冷调蓝绿色水下光线变为暖中性照明。

**状态：** 接受

**原子化判定句：**

1. 水下光线是否变为中性照明？

2. 变化后的中性照明是否带有暖色调？

3. 光线变化是否在 2 秒内完成？


## 248 — `object_165_E2A`

**原始英文指令：** At 29.0 seconds, reposition the cephalopod above the center of the pale rippled sand patch.

**中文翻译：** 在第 29.0 秒，将头足类动物移到浅色波纹沙地区域中央上方。

**状态：** 接受

**原子化判定句：**

1. 头足类动物是否被移到浅色波纹沙地区域上方？

2. 头足类动物是否位于该沙地区域中央的正上方？


## 249 — `object_165_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the cephalopod follow a tighter clockwise arc above the seabed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让头足类动物在海床上方沿更紧的顺时针弧线移动六秒。

**状态：** 接受

**原子化判定句：**

1. 头足类动物是否沿更紧的弧线移动？

2. 它是否沿顺时针方向移动？

3. 它是否保持在海床上方？

4. 移动是否持续 6 秒？


## 250 — `object_168_E1`

**原始英文指令：** Starting at 14.0 seconds, change the opossum-like animal's gray-white dorsal fur to warm reddish brown over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将负鼠状动物背部的灰白色皮毛变为暖红棕色。

**状态：** 接受

**原子化判定句：**

1. 负鼠状动物背部的皮毛是否从灰白色变为暖红棕色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 251 — `object_168_E2A`

**原始英文指令：** At 29.0 seconds, reorient the opossum-like animal to face directly toward the camera.

**中文翻译：** 在第 29.0 秒，重新调整负鼠状动物的朝向，使其正对镜头。

**状态：** 接受

**原子化判定句：**

1. 负鼠状动物是否被重新调整为正对镜头？


## 252 — `object_168_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the opossum-like animal raise both forepaws together twice over five seconds.

**中文翻译：** 从第 29.0 秒开始，让负鼠状动物在五秒内同时抬起两只前爪两次。

**状态：** 接受

**原子化判定句：**

1. 负鼠状动物是否抬起两只前爪？

2. 两只前爪是否同时抬起？

3. 它是否恰好抬起两次？

4. 两次抬爪是否在 5 秒内完成？


## 253 — `object_169_E1`

**原始英文指令：** Starting at 14.0 seconds, make the black and gray-brown jumping spiders touch their raised front legs three times.

**中文翻译：** 从第 14.0 秒开始，让黑色和灰棕色跳蛛用抬起的前腿相触三次。

**状态：** 接受

**原子化判定句：**

1. 黑色和灰棕色跳蛛的前腿是否相触？

2. 相触的前腿是否处于抬起状态？

3. 两只跳蛛是否恰好相触三次？


## 254 — `object_169_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the two jumping spiders smoothly from a constant overhead distance for five seconds.

**中文翻译：** 从第 29.0 秒开始，以固定的俯视距离平稳跟拍两只跳蛛五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟拍两只跳蛛？

2. 跟拍是否保持固定的俯视距离？

3. 跟拍是否平稳？

4. 跟拍是否持续 5 秒？


## 255 — `object_169_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full jumping-spider scene into a detailed ink-wash illustration over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将完整的跳蛛场景转换为细致的水墨插画。

**状态：** 接受

**原子化判定句：**

1. 完整的跳蛛场景是否转换为插画？

2. 插画是否采用水墨风格？

3. 插画是否细致？

4. 这一转变是否在 2 秒内完成？


## 256 — `object_170_E1`

**原始英文指令：** Starting at 14.0 seconds, change the surrounding green grass blades to pale blue-green over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将周围的绿色草叶变为浅蓝绿色。

**状态：** 接受

**原子化判定句：**

1. 周围的草叶是否从绿色变为浅蓝绿色？

2. 草叶颜色变化是否在 2 秒内完成？


## 257 — `object_170_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the four flower and seed-head stems sway together in three synchronized waves.

**中文翻译：** 从第 29.0 秒开始，让四根花朵和种子头茎秆一起同步摆动三轮。

**状态：** 接受

**原子化判定句：**

1. 四根花朵和种子头茎秆是否都发生摆动？

2. 四根茎秆是否同步摆动？

3. 它们是否恰好完成三轮同步摆动？


## 258 — `object_170_E2B`

**原始英文指令：** At 29.0 seconds, add one smaller white seed head behind the central brown flower head.

**中文翻译：** 在第 29.0 秒，在中央棕色花头后方添加一个较小的白色种子头。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个种子头？

2. 新增种子头是否比中央花头小？

3. 种子头是否为白色？

4. 种子头是否位于中央棕色花头后方？


## 259 — `object_171_E1`

**原始英文指令：** Starting at 14.0 seconds, change the tree frog's bright-green dorsal skin to deep turquoise over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将树蛙背部的亮绿色皮肤变为深绿松石色。

**状态：** 接受

**原子化判定句：**

1. 树蛙背部的皮肤是否从亮绿色变为深绿松石色？

2. 皮肤颜色变化是否在 2 秒内完成？


## 260 — `object_171_E2A`

**原始英文指令：** Starting at 29.0 seconds, zoom out smoothly over four seconds to include the full tree frog, supporting leaf, and adjacent trunk.

**中文翻译：** 从第 29.0 秒开始，在四秒内平稳拉远镜头，以纳入完整的树蛙、支撑叶片和相邻树干。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 4 秒内平稳拉远？

2. 拉远结束时，完整的树蛙、支撑叶片和相邻树干是否可见？


## 261 — `object_171_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the tree frog climb toward the adjacent trunk at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让树蛙以原速度的一半朝相邻树干攀爬六秒。

**状态：** 接受

**原子化判定句：**

1. 树蛙是否朝相邻树干攀爬？

2. 树蛙是否以原速度的一半攀爬？

3. 攀爬是否持续 6 秒？


## 262 — `object_173_E1`

**原始英文指令：** Starting at 14.0 seconds, change the juvenile rhinoceros's gray skin to cool blue-gray over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将幼年犀牛的灰色皮肤变为冷蓝灰色。

**状态：** 接受

**原子化判定句：**

1. 幼年犀牛的皮肤是否从灰色变为冷蓝灰色？

2. 皮肤颜色变化是否在 2 秒内完成？


## 263 — `object_173_E2A`

**原始英文指令：** Starting at 29.0 seconds, accelerate the juvenile rhinoceros's approach-touch-depart interaction cycle to twice its original rate for six seconds.

**中文翻译：** 从第 29.0 秒开始，将幼年犀牛的接近、接触、离开互动循环加快到原速的两倍，持续六秒。

**状态：** 接受

**原子化判定句：**

1. 幼年犀牛是否完成接近、接触、离开的互动循环？

2. 完整循环是否以原速的两倍推进？

3. 两倍速循环是否持续 6 秒？


## 264 — `object_173_E2B`

**原始英文指令：** At 29.0 seconds, add one small plain blue rubber ball on the concrete floor inside the red railing.

**中文翻译：** 在第 29.0 秒，在红色栏杆内的混凝土地面上添加一个小型纯蓝色橡胶球。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型橡胶球？

2. 球是否为纯蓝色？

3. 球是否位于混凝土地面上？

4. 球是否位于红色栏杆内？


## 265 — `object_174_E1`

**原始英文指令：** Starting at 14.0 seconds, change the stag's yellow-brown coat to deep chestnut brown over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将雄鹿的黄棕色皮毛变为深栗棕色。

**状态：** 接受

**原子化判定句：**

1. 雄鹿的皮毛是否从黄棕色变为深栗棕色？

2. 皮毛颜色变化是否在 2 秒内完成？


## 266 — `object_174_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the small gray-brown dog follow a wider arc around the stag at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让灰棕色小狗以原速度的一半沿更宽的弧线围绕雄鹿移动六秒。

**状态：** 接受

**原子化判定句：**

1. 灰棕色小狗是否沿弧线围绕雄鹿移动？

2. 弧线是否比原来更宽？

3. 小狗是否以原速度的一半移动？

4. 移动是否持续 6 秒？


## 267 — `object_174_E2B`

**原始英文指令：** At 29.0 seconds, replace the circular ground facility cover with a flat gray stone of similar size.

**中文翻译：** 在第 29.0 秒，将圆形地面设施盖替换为一块大小相近的扁平灰石。

**状态：** 接受

**原子化判定句：**

1. 圆形地面设施盖是否被替换为石头？

2. 替换后的石头是否扁平？

3. 石头是否为灰色？

4. 石头是否与原设施盖大小相近？


## 268 — `object_175_E1`

**原始英文指令：** Starting at 14.0 seconds, make the dark horse and zebra raise their forequarters and press their forelegs together twice.

**中文翻译：** 从第 14.0 秒开始，让深色马和斑马抬起前半身，并将前腿相互抵住两次。

**状态：** 接受

**原子化判定句：**

1. 深色马和斑马是否抬起前半身？

2. 抬起前半身后，它们是否将前腿恰好相互抵住两次？


## 269 — `object_175_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the dark horse and zebra smoothly from a constant side angle for five seconds.

**中文翻译：** 从第 29.0 秒开始，以固定的侧面角度平稳跟拍深色马和斑马五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否同时跟拍深色马和斑马？

2. 跟拍是否保持固定的侧面角度？

3. 跟拍是否平稳？

4. 跟拍是否持续 5 秒？


## 270 — `object_175_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full horse-and-zebra pasture scene into a 1970s color nature documentary over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将完整的马与斑马牧场场景转换为 20 世纪 70 年代彩色自然纪录片风格。

**状态：** 接受

**原子化判定句：**

1. 完整的马与斑马牧场场景是否呈现出自然纪录片的视觉效果？

2. 形成的自然纪录片风格是否具有 20 世纪 70 年代的视觉特征？

3. 形成的纪录片画面是否为彩色？

4. 风格转变是否在 2 秒内完成？


## 271 — `object_181_E1`

**原始英文指令：** Starting at 14.0 seconds, change the micro drone's unmarked dark frame arms to bright silver over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将微型无人机无标记的深色机架臂变为亮银色。

**状态：** 接受

**原子化判定句：**

1. 微型无人机的深色机架臂是否变为亮银色？

2. 机架臂颜色变化是否在 2 秒内完成？


## 272 — `object_181_E2A`

**原始英文指令：** At 29.0 seconds, reposition the micro quadrotor directly below the spherical chandelier in the entrance hall.

**中文翻译：** 在第 29.0 秒，将微型四旋翼无人机移到入口大厅球形吊灯的正下方。

**状态：** 接受

**原子化判定句：**

1. 微型四旋翼无人机是否被移到入口大厅球形吊灯的正下方？


## 273 — `object_181_E2B`

**原始英文指令：** At 29.0 seconds, add one small plain blue landing pad on the entrance-hall floor beneath the drone.

**中文翻译：** 在第 29.0 秒，在无人机下方的入口大厅地面上添加一个小型纯蓝色着陆垫。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型着陆垫？

2. 着陆垫是否为纯蓝色？

3. 着陆垫是否位于入口大厅地面上？

4. 着陆垫是否位于无人机下方？


## 274 — `object_185_E1`

**原始英文指令：** Starting at 14.0 seconds, make the brown bear press the fish with one forepaw and pull it upward with its mouth three times.

**中文翻译：** 从第 14.0 秒开始，让棕熊用一只前爪按住鱼，并用嘴将鱼向上拉三次。

**状态：** 接受

**原子化判定句：**

1. 棕熊是否用一只前爪按住鱼？

2. 按住鱼时，棕熊是否用嘴将鱼恰好向上拉三次？


## 275 — `object_185_E2A`

**原始英文指令：** At 29.0 seconds, reposition the fish centrally between the brown bear's two forepaws on the mossy rock.

**中文翻译：** 在第 29.0 秒，将鱼移到苔藓岩石上棕熊两只前爪之间的中央。

**状态：** 接受

**原子化判定句：**

1. 鱼是否被移到苔藓岩石上？

2. 鱼是否位于棕熊两只前爪之间的中央？


## 276 — `object_185_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full bear-and-river scene into a 1970s color nature documentary over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内将完整的熊与河流场景转换为 20 世纪 70 年代彩色自然纪录片风格。

**状态：** 接受

**原子化判定句：**

1. 完整的熊与河流场景是否呈现出自然纪录片的视觉效果？

2. 形成的自然纪录片风格是否具有 20 世纪 70 年代的视觉特征？

3. 形成的纪录片画面是否为彩色？

4. 风格转变是否在 2 秒内完成？


## 277 — `object_187_E1`

**原始英文指令：** Starting at 14.0 seconds, change the monitor lizard's pale body spots and bands to muted gold over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将巨蜥身上的浅色斑点和条带变为暗金色。

**状态：** 接受

**原子化判定句：**

1. 巨蜥身上的浅色斑点是否变为暗金色？

2. 巨蜥身上的浅色条带是否变为暗金色？

3. 两处颜色变化是否都在 2 秒内完成？


## 278 — `object_187_E2A`

**原始英文指令：** At 29.0 seconds, reorient the monitor lizard to face directly toward the far bathtub rim.

**中文翻译：** 在第 29.0 秒，重新调整巨蜥的朝向，使其正对远端浴缸边缘。

**状态：** 接受

**原子化判定句：**

1. 巨蜥是否被重新调整为正对远端浴缸边缘？


## 279 — `object_187_E2B`

**原始英文指令：** At 29.0 seconds, replace the metal bathtub faucet with a matte-black faucet of the same size.

**中文翻译：** 在第 29.0 秒，将金属浴缸水龙头替换为一个同样大小的哑光黑色水龙头。

**状态：** 接受

**原子化判定句：**

1. 金属浴缸水龙头是否被替换为黑色水龙头？

2. 替换后的水龙头是否为哑光表面？

3. 替换后的水龙头是否与原水龙头大小相同？


## 280 — `object_188_E1`

**原始英文指令：** Starting at 14.0 seconds, change the dented front panel of the red race car in the lower-left area with yellow-and-green graphics to a smooth undented state over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将左下区域带黄绿色图案的红色赛车凹陷前面板变为平滑无凹痕状态。

**状态：** 接受

**原子化判定句：**

1. 赛车凹陷的前面板是否变得平滑？

2. 前面板上的凹痕是否消失？

3. 这些面板变化是否在 2 秒内完成？


## 281 — `object_188_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the leading visible moving race car smoothly from directly above for five seconds.

**中文翻译：** 从第 29.0 秒开始，从正上方平稳跟拍画面中领先的行驶赛车五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟拍画面中领先的行驶赛车？

2. 跟拍视角是否位于正上方？

3. 跟拍是否平稳？

4. 跟拍是否持续 5 秒？


## 282 — `object_188_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the dust plume behind the moving race cars drift strongly toward the inside of the track for five seconds.

**中文翻译：** 从第 29.0 秒开始，让行驶赛车后方的尘柱朝赛道内侧强烈飘移五秒。

**状态：** 接受

**原子化判定句：**

1. 行驶赛车后方的尘柱是否朝赛道内侧飘移？

2. 飘移是否强烈？

3. 飘移是否持续 5 秒？


## 283 — `object_190_E1`

**原始英文指令：** Starting at 14.0 seconds, change the robot's unmarked yellow body panels to bright red over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将机器人无标记的黄色机身面板变为亮红色。

**状态：** 接受

**原子化判定句：**

1. 机器人的黄色机身面板是否变为亮红色？

2. 面板颜色变化是否在 2 秒内完成？


## 284 — `object_190_E2A`

**原始英文指令：** At 29.0 seconds, pause the tracked robot's combined turning and arm-motion sequence for three seconds, then resume it.

**中文翻译：** 在第 29.0 秒，让履带式机器人的转向与手臂运动组合序列暂停三秒，然后恢复。

**状态：** 接受

**原子化判定句：**

1. 履带式机器人是否正在执行转向与手臂运动组合序列？

2. 该组合序列是否暂停 3 秒？

3. 暂停 3 秒后，该组合序列是否恢复？


## 285 — `object_190_E2B`

**原始英文指令：** At 29.0 seconds, add one small plain blue cube on the wooden floor beside the tracked robot.

**中文翻译：** 在第 29.0 秒，在履带式机器人旁的木地板上添加一个小型纯蓝色立方体。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型立方体？

2. 立方体是否为纯蓝色？

3. 立方体是否位于木地板上？

4. 立方体是否位于履带式机器人旁？


## 286 — `object_194_E1`

**原始英文指令：** Starting at 14.0 seconds, change the pale tan-gray gravel forest road to deep reddish brown over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将浅棕灰色的森林碎石路变为深红棕色。

**状态：** 接受

**原子化判定句：**

1. 森林碎石路是否从浅棕灰色变为深红棕色？

2. 道路颜色变化是否在 2 秒内完成？


## 287 — `object_194_E2A`

**原始英文指令：** Starting at 29.0 seconds, reorder the crossings so the adult boar finishes first, followed by the first smaller boar and then the second.

**中文翻译：** 从第 29.0 秒开始，重新安排过路顺序，使成年野猪先完成，随后是第一只较小野猪，最后是第二只。

**状态：** 接受

**原子化判定句：**

1. 成年野猪是否最先完成过路？

2. 第一只较小野猪是否在成年野猪之后完成过路？

3. 第二只较小野猪是否在第一只较小野猪之后完成过路？


## 288 — `object_194_E2B`

**原始英文指令：** Starting at 29.0 seconds, make each of the two smaller boars hop once over the forest-road edge.

**中文翻译：** 从第 29.0 秒开始，让两只较小野猪各自跳过森林道路边缘一次。

**状态：** 接受

**原子化判定句：**

1. 两只较小野猪是否都跳过森林道路边缘？

2. 每只野猪是否都恰好跳过一次？


## 289 — `object_195_E1`

**原始英文指令：** Starting at 14.0 seconds, change the weather above the railway to a light rain shower over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将铁路上方的天气变为小阵雨。

**状态：** 接受

**原子化判定句：**

1. 铁路上方是否开始下雨？

2. 形成的雨势是否为小阵雨？

3. 天气变化是否在 2 秒内完成？


## 290 — `object_195_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the passenger locomotive smoothly from a constant parallel side distance for five seconds.

**中文翻译：** 从第 29.0 秒开始，以固定的平行侧向距离平稳跟拍客运机车五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟拍客运机车？

2. 跟拍是否保持固定的平行侧向距离？

3. 跟拍是否平稳？

4. 跟拍是否持续 5 秒？


## 291 — `object_195_E2B`

**原始英文指令：** At 29.0 seconds, remove the blue striped emblem from the side panel of the passing locomotive.

**中文翻译：** 在第 29.0 秒，移除驶过机车侧面板上的蓝色条纹徽记。

**状态：** 接受

**原子化判定句：**

1. 驶过机车侧面板上的蓝色条纹徽记是否被移除？


## 292 — `object_198_E1`

**原始英文指令：** Starting at 14.0 seconds, make the juvenile hippo gently touch each larger hippo's muzzle twice.

**中文翻译：** 从第 14.0 秒开始，让幼年河马轻触每只较大河马的口鼻部两次。

**状态：** 接受

**原子化判定句：**

1. 幼年河马是否接触每只较大河马的口鼻部？

2. 每次接触是否轻柔？

3. 幼年河马是否恰好接触每只较大河马两次？


## 293 — `object_198_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the juvenile hippo surface twice beside the two larger hippos.

**中文翻译：** 从第 29.0 秒开始，让幼年河马在两只较大河马旁浮出水面两次。

**状态：** 接受

**原子化判定句：**

1. 幼年河马是否在两只较大河马旁浮出水面？

2. 幼年河马是否恰好浮出水面两次？


## 294 — `object_198_E2B`

**原始英文指令：** Starting at 29.0 seconds, apply a cool natural-film color grade and fine grain to the full three-hippo pool scene over the next two seconds.

**中文翻译：** 从第 29.0 秒开始，在接下来的两秒内为完整的三只河马水池场景应用冷调自然胶片色彩分级和细腻颗粒。

**状态：** 接受

**原子化判定句：**

1. 完整的三只河马水池场景是否在 2 秒内应用了冷调自然胶片色彩分级？

2. 完整场景是否在同一段 2 秒内应用了细腻颗粒？


## 295 — `object_199_E1`

**原始英文指令：** Starting at 14.0 seconds, change the gecko's pale cream base skin to muted turquoise over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将壁虎的浅奶油色底色皮肤变为暗绿松石色。

**状态：** 接受

**原子化判定句：**

1. 壁虎的底色皮肤是否从浅奶油色变为暗绿松石色？

2. 皮肤颜色变化是否在 2 秒内完成？


## 296 — `object_199_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the leopard gecko wave its thick tail from side to side three times.

**中文翻译：** 从第 29.0 秒开始，让豹纹壁虎将粗尾巴左右摆动三次。

**状态：** 接受

**原子化判定句：**

1. 豹纹壁虎是否将粗尾巴左右摆动？

2. 壁虎是否恰好完成三次左右摆动？


## 297 — `object_199_E2B`

**原始英文指令：** At 29.0 seconds, replace the plain pink circular dish beside the gecko with a plain blue dish of the same size.

**中文翻译：** 在第 29.0 秒，将壁虎旁的纯粉色圆盘替换为一个同样大小的纯蓝色盘子。

**状态：** 接受

**原子化判定句：**

1. 壁虎旁的纯粉色圆盘是否被替换为蓝色盘子？

2. 替换后的盘子外观是否朴素？

3. 替换后的盘子是否与原盘子大小相同？


## 298 — `object_200_E1`

**原始英文指令：** Starting at 14.0 seconds, change the hard direct sunlight on the alligator-like animal and fairway to soft diffuse overcast illumination over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将照在鳄鱼状动物和球道上的强烈直射阳光变为柔和漫射的阴天照明。

**状态：** 接受

**原子化判定句：**

1. 照在鳄鱼状动物和球道上的光线是否都变为阴天照明？

2. 变化后的照明是否柔和且为漫射光？

3. 光线变化是否在 2 秒内完成？


## 299 — `object_200_E2A`

**原始英文指令：** Starting at 29.0 seconds, zoom out smoothly over four seconds to show the full alligator-like animal, distant adult, and sand bunker together.

**中文翻译：** 从第 29.0 秒开始，在四秒内平稳拉远镜头，以同时显示完整的鳄鱼状动物、远处成人和沙坑。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 4 秒内平稳拉远？

2. 拉远结束时，完整的鳄鱼状动物、远处成人和沙坑是否同时可见？


## 300 — `object_200_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the alligator-like animal walk across the fairway at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让鳄鱼状动物以原速度的一半穿过球道行走六秒。

**状态：** 接受

**原子化判定句：**

1. 鳄鱼状动物是否穿过球道行走？

2. 它是否以原速度的一半行走？

3. 行走是否持续 6 秒？
