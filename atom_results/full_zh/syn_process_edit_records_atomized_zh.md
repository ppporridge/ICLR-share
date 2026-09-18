# 全量编辑指令原子化结果——syn_process_edit_records.md——中文审阅版

- 源记录数：300

- 所有原子判定句均依据 `atom_results/README.md` 逐条人工审核。

- 原子判定句省略作为截取起点的绝对时间；后续时间点均已换算为片段内相对时间。


## 001 — `synthetic_process_001_E1`

**原始英文指令：** Starting at 12.5 seconds, slow the sunrise so the sun first clears the central mountain ridge at 20.5 seconds.

**中文翻译：** 从第 12.5 秒开始，减慢日出过程，使太阳在第 20.5 秒首次完全越过中央山脊。

**状态：** 接受

**原子化判定句：**

1. 日出过程是否减慢？

2. 太阳是否在 8 秒内首次完全越过中央山脊？


## 002 — `synthetic_process_001_E2A`

**原始英文指令：** Starting at 25.5 seconds, make the foreground grass bend rightward in three traveling wind waves over five seconds.

**中文翻译：** 从第 25.5 秒开始，让前景草地在五秒内随三道传播的风浪向右弯曲。

**状态：** 接受

**原子化判定句：**

1. 前景草地是否向右弯曲？

2. 是否恰好有三道传播的风浪掠过草地？

3. 三道风浪是否在 5 秒内完成？


## 003 — `synthetic_process_001_E2B`

**原始英文指令：** Starting at 27.0 seconds, render only the blue sky behind the mountain as a muted watercolor wash over two seconds.

**中文翻译：** 从第 27.0 秒开始，在两秒内仅将山后蓝天呈现为低饱和水彩晕染。

**状态：** 接受

**原子化判定句：**

1. 山后蓝天是否呈现为低饱和水彩晕染？

2. 风格变化是否仅限于该天空区域？

3. 风格变化是否在 2 秒内完成？


## 004 — `synthetic_process_002_E1`

**原始英文指令：** Starting at 15.5 seconds, smoothly zoom in until the low sun and central city skyline fill the middle half of the frame.

**中文翻译：** 从第 15.5 秒开始，平滑拉近镜头，直到低空太阳和中央城市天际线占据画面中间一半。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近，直至低空太阳和中央城市天际线占据画面中间一半？

2. 拉近过程是否平滑？


## 005 — `synthetic_process_002_E2A`

**原始英文指令：** Starting at 27.5 seconds, brighten the skyline and sky to a clear light-blue daytime illumination over four seconds.

**中文翻译：** 从第 27.5 秒开始，在四秒内将天际线和天空提亮为清澈浅蓝色日间照明。

**状态：** 接受

**原子化判定句：**

1. 天际线是否在 4 秒内提亮为清澈浅蓝色日间照明？

2. 天空是否在同一段 4 秒内提亮为清澈浅蓝色日间照明？


## 006 — `synthetic_process_002_E2B`

**原始英文指令：** Starting at 30.5 seconds, slow window-light activation so only one additional horizontal row is illuminated by 37.0 seconds.

**中文翻译：** 从第 30.5 秒开始，减慢窗灯点亮过程，使第 37.0 秒前仅新增一排水平灯光。

**状态：** 接受

**原子化判定句：**

1. 窗灯点亮过程是否减慢？

2. 是否在 6.5 秒内仅新增一排水平灯光？


## 007 — `synthetic_process_003_E1`

**原始英文指令：** Starting at 14.5 seconds, add a warm low sidelight across the left third of the grass field over two seconds.

**中文翻译：** 从第 14.5 秒开始，在两秒内为草地左侧三分之一区域添加温暖的低角度侧光。

**状态：** 接受

**原子化判定句：**

1. 草地上是否添加了温暖的低角度侧光？

2. 该侧光是否覆盖草地左侧三分之一区域？

3. 照明变化是否在 2 秒内完成？


## 008 — `synthetic_process_003_E2A`

**原始英文指令：** Starting at 27.5 seconds, accelerate puddle expansion until connected reflections occupy the lower third of the field by 32.5 seconds.

**中文翻译：** 从第 27.5 秒开始，加快水洼扩张，使相连的倒影在第 32.5 秒前占据田野下方三分之一区域。

**状态：** 接受

**原子化判定句：**

1. 水洼扩张过程是否加快？

2. 相连的倒影是否在 5 秒内占据田野下方三分之一区域？


## 009 — `synthetic_process_003_E2B`

**原始英文指令：** Starting at 29.0 seconds, pause further puddle-front expansion for five seconds, then resume from the held wet boundary.

**中文翻译：** 从第 29.0 秒开始，将水洼前沿的进一步扩张暂停五秒，然后从保持的湿润边界恢复扩张。

**状态：** 接受

**原子化判定句：**

1. 水洼前沿是否继续扩张？

2. 水洼前沿的进一步扩张是否暂停 5 秒？

3. 随后扩张是否从保持的湿润边界恢复？


## 010 — `synthetic_process_004_E1`

**原始英文指令：** Starting at 13.5 seconds, move the camera slowly right along a short arc around the central hill and river bend for five seconds.

**中文翻译：** 从第 13.5 秒开始，让镜头围绕中央山丘和河湾沿短弧线缓慢向右移动五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否缓慢向右移动？

2. 镜头是否沿围绕中央山丘和河湾的短弧线移动？

3. 镜头运动是否持续 5 秒？


## 011 — `synthetic_process_004_E2A`

**原始英文指令：** Starting at 26.0 seconds, advance the clearing until the full main river bend and most riverside buildings are visible by 29.5 seconds.

**中文翻译：** 从第 26.0 秒开始，推进雾气消散，使完整的主要河湾和大部分河岸建筑在第 29.5 秒前可见。

**状态：** 接受

**原子化判定句：**

1. 雾气消散过程是否推进？

2. 完整的主要河湾和大部分河岸建筑是否在 3.5 秒内可见？


## 012 — `synthetic_process_004_E2B`

**原始英文指令：** Starting at 28.0 seconds, accelerate the remaining fog dissipation until only narrow low valley bands remain by 33.5 seconds.

**中文翻译：** 从第 28.0 秒开始，加快剩余雾气消散，使第 33.5 秒前仅留下狭窄的低谷雾带。

**状态：** 接受

**原子化判定句：**

1. 剩余雾气是否更快消散？

2. 是否在 5.5 秒内仅留下狭窄的低谷雾带？


## 013 — `synthetic_process_005_E1`

**原始英文指令：** At 13.0 seconds, remove the vertical fence slat directly above the center of the bench backrest.

**中文翻译：** 在第 13.0 秒，移除长凳靠背中央正上方的竖直围栏板条。

**状态：** 接受

**原子化判定句：**

1. 长凳靠背中央正上方的竖直围栏板条是否被移除？


## 014 — `synthetic_process_005_E2A`

**原始英文指令：** At 25.5 seconds, position the bench half a meter closer to the fence, centered and parallel to it.

**中文翻译：** 在第 25.5 秒，将长凳放置得离围栏近半米，并与围栏居中且平行。

**状态：** 接受

**原子化判定句：**

1. 长凳是否被放置得离围栏近 0.5 米？

2. 长凳是否与围栏居中且平行？


## 015 — `synthetic_process_005_E2B`

**原始英文指令：** Starting at 28.0 seconds, accelerate snow accumulation until the seat layer reaches both armrest tops by 33.5 seconds.

**中文翻译：** 从第 28.0 秒开始，加快积雪累积，使座面雪层在第 33.5 秒前达到两侧扶手顶部。

**状态：** 接受

**原子化判定句：**

1. 积雪累积是否加快？

2. 座面雪层是否在 5.5 秒内达到两侧扶手顶部？


## 016 — `synthetic_process_006_E1`

**原始英文指令：** Starting at 12.5 seconds, make the central channel's surface ripples travel downstream at twice their original speed for five seconds.

**中文翻译：** 从第 12.5 秒开始，让中央河道表面波纹以原来两倍的速度向下游传播五秒。

**状态：** 接受

**原子化判定句：**

1. 中央河道表面波纹是否向下游传播？

2. 波纹是否以原来两倍的速度传播？

3. 加速后的传播是否持续 5 秒？


## 017 — `synthetic_process_006_E2A`

**原始英文指令：** Starting at 26.5 seconds, change the connected river water from muted blue-gray to clear pale turquoise over two seconds.

**中文翻译：** 从第 26.5 秒开始，在两秒内将相连河水从柔和蓝灰色改为清澈浅青绿色。

**状态：** 接受

**原子化判定句：**

1. 相连河水是否从柔和蓝灰色变为浅青绿色？

2. 变化后的河水是否显得清澈？

3. 这一变化是否在 2 秒内完成？


## 018 — `synthetic_process_006_E2B`

**原始英文指令：** Starting at 27.5 seconds, accelerate inundation until the right gravel bar is submerged while its higher grass bank remains dry by 32.0 seconds.

**中文翻译：** 从第 27.5 秒开始，加快淹没过程，使右侧砾石滩在第 32.0 秒前被淹没，同时其较高草岸保持干燥。

**状态：** 接受

**原子化判定句：**

1. 淹没过程是否加快？

2. 右侧砾石滩是否在 4.5 秒内被淹没？

3. 其较高草岸是否保持干燥？


## 019 — `synthetic_process_007_E1`

**原始英文指令：** Starting at 12.0 seconds, advance the rainbow until a continuous saturated arc spans the landscape by 16.5 seconds.

**中文翻译：** 从第 12.0 秒开始，推进彩虹形成，使一条连续饱和的弧线在第 16.5 秒前横跨景观。

**状态：** 接受

**原子化判定句：**

1. 彩虹是否发展为横跨景观的弧线？

2. 形成的弧线是否连续且色彩饱和？

3. 横跨景观的弧线是否在 4.5 秒内形成？


## 020 — `synthetic_process_007_E2A`

**原始英文指令：** Starting at 23.5 seconds, slow the rainbow's fading so the complete arc remains clearly visible through 30.0 seconds.

**中文翻译：** 从第 23.5 秒开始，减慢彩虹消退，使完整弧线持续清晰可见至第 30.0 秒。

**状态：** 接受

**原子化判定句：**

1. 彩虹消退是否减慢？

2. 完整弧线是否持续清晰可见 6.5 秒？


## 021 — `synthetic_process_007_E2B`

**原始英文指令：** Starting at 26.5 seconds, transform the entire rainbow landscape into a soft gouache painting over the next two seconds.

**中文翻译：** 从第 26.5 秒开始，在接下来的两秒内将整个彩虹景观转变为柔和的水粉画。

**状态：** 接受

**原子化判定句：**

1. 整个彩虹景观是否转变为柔和的水粉画？

2. 这一转变是否在 2 秒内完成？


## 022 — `synthetic_process_008_E1`

**原始英文指令：** Starting at 16.0 seconds, hold the intact pre-strike tree and storm stage for four seconds, then resume the lightning event.

**中文翻译：** 从第 16.0 秒开始，将完好的雷击前树木和风暴阶段保持四秒，然后恢复雷电事件。

**状态：** 接受

**原子化判定句：**

1. 完好的雷击前树木和风暴阶段是否保持不变 4 秒？

2. 随后雷电事件是否恢复？


## 023 — `synthetic_process_008_E2A`

**原始英文指令：** Starting at 22.5 seconds, make dense black smoke begin rising from the burning tree crown within one second.

**中文翻译：** 从第 22.5 秒开始，让浓密黑烟在一秒内开始从燃烧的树冠升起。

**状态：** 接受

**原子化判定句：**

1. 是否有浓密黑烟开始从燃烧的树冠升起？

2. 黑烟是否在 1 秒内开始升起？


## 024 — `synthetic_process_008_E2B`

**原始英文指令：** At 29.5 seconds, replace the burning broadleaf tree with one equally tall conifer at the same central location.

**中文翻译：** 在第 29.5 秒，将燃烧的阔叶树替换为位于同一中央位置、同等高度的一棵针叶树。

**状态：** 接受

**原子化判定句：**

1. 燃烧的阔叶树是否被替换为一棵针叶树？

2. 针叶树是否与原阔叶树同高？

3. 针叶树是否位于原阔叶树所在的中央位置？


## 025 — `synthetic_process_009_E1`

**原始英文指令：** At 13.5 seconds, shift the upper snow cornice right until its deepest overhang sits directly above the central dark rock band.

**中文翻译：** 在第 13.5 秒，将上部雪檐向右移动，直到其最深悬垂部分位于中央深色岩带正上方。

**状态：** 接受

**原子化判定句：**

1. 上部雪檐是否向右移动？

2. 其最深悬垂部分最终是否位于中央深色岩带正上方？


## 026 — `synthetic_process_009_E2A`

**原始英文指令：** At 26.0 seconds, replace the small dark rock outcrop left of the main slide track with a pale blue ice block.

**中文翻译：** 在第 26.0 秒，将主滑坡轨迹左侧的小型深色岩石露头替换为一块浅蓝色冰块。

**状态：** 接受

**原子化判定句：**

1. 主滑坡轨迹左侧的小型深色岩石露头是否被替换为一块浅蓝色冰块？


## 027 — `synthetic_process_009_E2B`

**原始英文指令：** Starting at 28.0 seconds, make the powder cloud below the cornice travel horizontally right for five seconds beside the descending slab.

**中文翻译：** 从第 28.0 秒开始，让雪檐下方的粉雪云在下落雪板旁水平向右移动五秒。

**状态：** 接受

**原子化判定句：**

1. 雪檐下方的粉雪云是否在下落雪板旁水平向右移动？

2. 这一移动是否持续 5 秒？


## 028 — `synthetic_process_010_E1`

**原始英文指令：** At 14.0 seconds, shift the narrow ice column half a meter right to widen its gap from the central blue fissure.

**中文翻译：** 在第 14.0 秒，将狭窄冰柱向右移动半米，以扩大其与中央蓝色裂隙之间的间距。

**状态：** 接受

**原子化判定句：**

1. 狭窄冰柱是否向右移动？

2. 移动距离是否为半米？

3. 冰柱与中央蓝色裂隙之间的间距是否增大？


## 029 — `synthetic_process_010_E2A`

**原始英文指令：** At 25.5 seconds, split the protruding right ice slab into two vertical slabs separated by one narrow gap.

**中文翻译：** 在第 25.5 秒，将右侧突出的冰板分成两块竖直冰板，两者之间留有一道狭窄间隙。

**状态：** 接受

**原子化判定句：**

1. 右侧突出的冰板是否被分成两块竖直冰板？

2. 两块竖直冰板之间是否留有一道狭窄间隙？


## 030 — `synthetic_process_010_E2B`

**原始英文指令：** Starting at 25.0 seconds, make the tipping ice slab separate into one small and one large fragment, with the small fragment falling first.

**中文翻译：** 从第 25.0 秒开始，让正在倾倒的冰板分裂为一小一大两块碎片，并让小碎片先下落。

**状态：** 接受

**原子化判定句：**

1. 正在倾倒的冰板是否分裂为一块小碎片和一块大碎片？

2. 小碎片是否先于大碎片下落？


## 031 — `synthetic_process_011_E1`

**原始英文指令：** Starting at 15.0 seconds, hold the dormant steaming vent stage for four seconds, then resume the geyser's rise.

**中文翻译：** 从第 15.0 秒开始，将喷口处于休眠冒汽的阶段保持四秒，然后恢复间歇泉的上升。

**状态：** 接受

**原子化判定句：**

1. 喷口处于休眠冒汽的阶段是否保持 4 秒？

2. 间歇泉是否在保持 4 秒后恢复上升？


## 032 — `synthetic_process_011_E2A`

**原始英文指令：** At 26.5 seconds, add one small rounded gray boulder on the stable ground just outside the geyser vent's right edge.

**中文翻译：** 在第 26.5 秒，在间歇泉喷口右侧边缘外紧邻的稳定地面上添加一块小型圆润灰色巨石。

**状态：** 接受

**原子化判定句：**

1. 是否添加了恰好一块小型圆润灰色巨石？

2. 该巨石是否位于间歇泉喷口右侧边缘外紧邻的稳定地面上？


## 033 — `synthetic_process_011_E2B`

**原始英文指令：** Starting at 29.0 seconds, change the main geyser water jet from white to translucent pale turquoise over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将间歇泉主水柱由白色变为半透明的浅青绿色。

**状态：** 接受

**原子化判定句：**

1. 间歇泉主水柱是否由白色变为浅青绿色？

2. 变化后的水柱是否呈半透明状态？

3. 这一变化是否在 2 秒内完成？


## 034 — `synthetic_process_012_E1`

**原始英文指令：** Starting at 13.5 seconds, make five visible stars above the mountains brighten and dim together five times over five seconds.

**中文翻译：** 从第 13.5 秒开始，让山脉上方五颗可见的星星在五秒内同步明暗变化五次。

**状态：** 接受

**原子化判定句：**

1. 山脉上方五颗可见星星是否共同变亮？

2. 五颗星星是否共同变暗？

3. 五颗星星是否在 5 秒内同步完成 5 次明暗变化？


## 035 — `synthetic_process_012_E2A`

**原始英文指令：** Starting at 27.0 seconds, accelerate nightfall until the remaining twilight band becomes deep navy by 32.0 seconds.

**中文翻译：** 从第 27.0 秒开始，加快夜幕降临，使残余的暮光带在第 32.0 秒前变为深海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 夜幕降临是否加快？

2. 残余的暮光带是否在 5 秒内变为深海军蓝色？


## 036 — `synthetic_process_012_E2B`

**原始英文指令：** Starting at 28.0 seconds, advance star-trail formation until the visible arcs reach twice their edit-point length by 34.0 seconds.

**中文翻译：** 从第 28.0 秒开始，推进星轨形成，使可见弧线在第 34.0 秒前达到编辑点时长度的两倍。

**状态：** 接受

**原子化判定句：**

1. 星轨形成是否得到推进？

2. 可见弧线是否在 6 秒内达到编辑点时长度的两倍？


## 037 — `synthetic_process_013_E1`

**原始英文指令：** Starting at 14.5 seconds, smoothly zoom in on the brightest central aurora band over five seconds.

**中文翻译：** 从第 14.5 秒开始，在五秒内平滑拉近镜头，聚焦于最明亮的中央极光带。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近并聚焦于最明亮的中央极光带？

2. 拉近过程是否平滑？

3. 镜头拉近是否在 5 秒内完成？


## 038 — `synthetic_process_013_E2A`

**原始英文指令：** Starting at 26.0 seconds, render only the dark sky behind the aurora with a fine charcoal-paper texture over two seconds.

**中文翻译：** 从第 26.0 秒开始，在两秒内仅将极光背后的暗色天空呈现为细腻的炭笔纸张纹理。

**状态：** 接受

**原子化判定句：**

1. 极光背后的暗色天空是否呈现为细腻的炭笔纸张纹理？

2. 纹理变化是否仅限于该天空区域？

3. 纹理变化是否在 2 秒内完成？


## 039 — `synthetic_process_013_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the visible aurora bands ripple upward in three successive waves over five seconds.

**中文翻译：** 从第 29.0 秒开始，让可见的极光带在五秒内分三道连续波浪向上起伏。

**状态：** 接受

**原子化判定句：**

1. 可见的极光带是否向上起伏？

2. 极光带是否形成恰好三道连续波浪？

3. 三道波浪是否在 5 秒内完成？


## 040 — `synthetic_process_014_E1`

**原始英文指令：** Starting at 13.0 seconds, render only the distant mountain ridges above the cloud sea in restrained monochrome ink-wash style.

**中文翻译：** 从第 13.0 秒开始，仅将云海上方的远处山脊呈现为克制的单色水墨风格。

**状态：** 接受

**原子化判定句：**

1. 云海上方的远处山脊是否呈现为克制的单色水墨风格？

2. 风格变化是否仅限于这些远处山脊？


## 041 — `synthetic_process_014_E2A`

**原始英文指令：** Starting at 25.0 seconds, smoothly zoom in until the central fog tongue and adjacent river bend occupy the middle half of the frame.

**中文翻译：** 从第 25.0 秒开始，平滑拉近镜头，直到中央雾舌及相邻河湾占据画面中间一半区域。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近，直至中央雾舌及相邻河湾占据画面中间一半区域？

2. 拉近过程是否平滑？


## 042 — `synthetic_process_014_E2B`

**原始英文指令：** Starting at 27.5 seconds, make the central fog tongue curl clockwise while continuing down the valley for five seconds.

**中文翻译：** 从第 27.5 秒开始，让中央雾舌顺时针卷曲，同时继续沿山谷向下移动五秒。

**状态：** 接受

**原子化判定句：**

1. 中央雾舌是否顺时针卷曲 5 秒？

2. 中央雾舌是否在同一段 5 秒内继续沿山谷向下移动？


## 043 — `synthetic_process_015_E1`

**原始英文指令：** Starting at 12.5 seconds, render only the exposed dry ground outside the water channels with fine charcoal hatching.

**中文翻译：** 从第 12.5 秒开始，仅将水道外露出的干燥地面呈现为细密的炭笔排线效果。

**状态：** 接受

**原子化判定句：**

1. 水道外露出的干燥地面是否呈现为细密的炭笔排线效果？

2. 风格变化是否仅限于该露出地面？


## 044 — `synthetic_process_015_E2A`

**原始英文指令：** Starting at 26.0 seconds, move the camera slowly forward toward the central retreating water channel for six seconds.

**中文翻译：** 从第 26.0 秒开始，让镜头朝中央正在退去的水道缓慢向前移动六秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否朝中央正在退去的水道向前移动？

2. 镜头移动是否缓慢？

3. 这一移动是否持续 6 秒？


## 045 — `synthetic_process_015_E2B`

**原始英文指令：** Starting at 27.0 seconds, rotate the main dark water channel clockwise until its long axis runs vertically toward the frame's top edge.

**中文翻译：** 从第 27.0 秒开始，将主要深色水道顺时针旋转，直到其长轴竖直指向画面顶边。

**状态：** 接受

**原子化判定句：**

1. 主要深色水道是否顺时针旋转？

2. 其长轴最终是否竖直并指向画面顶边？


## 046 — `synthetic_process_016_E1`

**原始英文指令：** At 13.5 seconds, shift the pale central patch upward until its upper gap to the dark rim is half its lower gap.

**中文翻译：** 在第 13.5 秒，将浅色中央斑块向上移动，直到它与深色边缘的上方间距为下方间距的一半。

**状态：** 接受

**原子化判定句：**

1. 浅色中央斑块是否向上移动？

2. 其与深色边缘的上方间距最终是否为下方间距的一半？


## 047 — `synthetic_process_016_E2A`

**原始英文指令：** At 33.0 seconds, remove the isolated pale granular mound on the lower inner rim of the dark cavity.

**中文翻译：** 在第 33.0 秒，移除深色凹坑下部内缘上孤立的浅色颗粒状小丘。

**状态：** 接受

**原子化判定句：**

1. 深色凹坑下部内缘上孤立的浅色颗粒状小丘是否被移除？


## 048 — `synthetic_process_016_E2B`

**原始英文指令：** Starting at 28.0 seconds, add a warm focused overhead light that highlights the circular depression's inner wall over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内添加一束暖色聚焦顶光，照亮圆形凹陷的内壁。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一束暖色聚焦顶光？

2. 该顶光是否照亮圆形凹陷的内壁？

3. 照明变化是否在 2 秒内完成？


## 049 — `synthetic_process_017_E1`

**原始英文指令：** Starting at 13.0 seconds, stop new waves from overtopping the coastal road until 21.0 seconds after the current sheet drains.

**中文翻译：** 从第 13.0 秒开始，在当前水层排空后的二十一秒内，阻止新的海浪漫过沿海道路。

**状态：** 接受

**原子化判定句：**

1. 当前水层是否排空？

2. 在当前水层排空后的 21 秒内，是否没有新的海浪漫过沿海道路？


## 050 — `synthetic_process_017_E2A`

**原始英文指令：** Starting at 27.0 seconds, pause the inland white-water front for five seconds, then resume its advance.

**中文翻译：** 从第 27.0 秒开始，让正在向内陆推进的白浪前沿暂停五秒，然后恢复推进。

**状态：** 接受

**原子化判定句：**

1. 正在向内陆推进的白浪前沿是否暂停 5 秒？

2. 白浪前沿是否在暂停 5 秒后恢复向内陆推进？


## 051 — `synthetic_process_017_E2B`

**原始英文指令：** At 28.0 seconds, replace the dark breakwater rocks along the road's left side with tan interlocking concrete wave blocks.

**中文翻译：** 在第 28.0 秒，将道路左侧沿线的深色防波堤岩石替换为棕褐色互锁混凝土消波块。

**状态：** 接受

**原子化判定句：**

1. 道路左侧沿线的深色防波堤岩石是否被替换为混凝土消波块？

2. 替换后的消波块是否为棕褐色且相互咬合？


## 052 — `synthetic_process_018_E1`

**原始英文指令：** Starting at 14.0 seconds, transform the full dust-storm scene into a cool steel-blue and neutral-gray duotone over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内将整个沙尘暴场景转换为冷调钢蓝色与中性灰色的双色效果。

**状态：** 接受

**原子化判定句：**

1. 整个沙尘暴场景是否转换为冷调钢蓝色与中性灰色的双色效果？

2. 这一转换是否在 2 秒内完成？


## 053 — `synthetic_process_018_E2A`

**原始英文指令：** Starting at 27.0 seconds, make the dust wall's upper edge curl upward in three rolling waves over five seconds.

**中文翻译：** 从第 27.0 秒开始，让沙尘墙的上缘在五秒内以三道翻滚波浪向上卷曲。

**状态：** 接受

**原子化判定句：**

1. 沙尘墙的上缘是否向上卷曲？

2. 是否形成恰好三道翻滚波浪？

3. 三道波浪是否在 5 秒内完成？


## 054 — `synthetic_process_018_E2B`

**原始英文指令：** Starting at 28.5 seconds, change only the advancing dust wall to muted rust red over the next two seconds.

**中文翻译：** 从第 28.5 秒开始，在接下来的两秒内仅将正在推进的沙尘墙变为低饱和铁锈红色。

**状态：** 接受

**原子化判定句：**

1. 正在推进的沙尘墙是否变为低饱和铁锈红色？

2. 颜色变化是否仅限于正在推进的沙尘墙？

3. 颜色变化是否在 2 秒内完成？


## 055 — `synthetic_process_019_E1`

**原始英文指令：** Starting at 13.5 seconds, pause shrinkage of the central Y-shaped snowfield for five seconds, then resume from the held boundary.

**中文翻译：** 从第 13.5 秒开始，让中央 Y 形雪地停止缩小五秒，然后从保持不变的边界处恢复缩小。

**状态：** 接受

**原子化判定句：**

1. 正在缩小的中央 Y 形雪地是否暂停缩小 5 秒？

2. 中央 Y 形雪地是否在暂停 5 秒后从保持不变的边界处恢复缩小？


## 056 — `synthetic_process_019_E2A`

**原始英文指令：** Starting at 26.0 seconds, transform the full mountain snowmelt scene into a transparent watercolor painting over two seconds.

**中文翻译：** 从第 26.0 秒开始，在两秒内将整个山地融雪场景转换为通透的水彩画。

**状态：** 接受

**原子化判定句：**

1. 整个山地融雪场景是否转换为通透的水彩画？

2. 这一转换是否在 2 秒内完成？


## 057 — `synthetic_process_019_E2B`

**原始英文指令：** Starting at 28.0 seconds, add a low warm sidelight from the right across the mountain slope and remaining snow over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内从右侧添加一道低角度暖色侧光，照过山坡和剩余积雪。

**状态：** 接受

**原子化判定句：**

1. 是否在 2 秒内从右侧添加低角度暖色侧光？

2. 暖色侧光是否照过山坡？

3. 暖色侧光是否照过剩余积雪？


## 058 — `synthetic_process_020_E1`

**原始英文指令：** At 14.0 seconds, move the right ice-shelf edge toward the left rock bank until the open-water gap is one third narrower.

**中文翻译：** 在第 14.0 秒，将右侧冰架边缘移向左侧岩岸，直到开放水面的间隙缩窄三分之一。

**状态：** 接受

**原子化判定句：**

1. 右侧冰架边缘是否移向左侧岩岸？

2. 开放水面的间隙是否缩窄三分之一？


## 059 — `synthetic_process_020_E2A`

**原始英文指令：** At 26.0 seconds, remove the small isolated tan rock from the lower-left bank beside the dark water channel.

**中文翻译：** 在第 26.0 秒，移除深色水道旁左下方岸边那块孤立的棕褐色小岩石。

**状态：** 接受

**原子化判定句：**

1. 深色水道旁左下方岸边那块孤立的棕褐色小岩石是否被移除？


## 060 — `synthetic_process_020_E2B`

**原始英文指令：** Starting at 28.0 seconds, pause both ice-shelf edges for five seconds, then resume expansion from their held positions.

**中文翻译：** 从第 28.0 秒开始，让冰架两侧边缘停止扩张五秒，然后从各自保持的位置恢复扩张。

**状态：** 接受

**原子化判定句：**

1. 正在扩张的冰架两侧边缘是否暂停 5 秒？

2. 冰架两侧边缘是否在暂停 5 秒后从各自保持的位置恢复扩张？


## 061 — `synthetic_process_021_E1`

**原始英文指令：** Starting at 14.5 seconds, delay the next central rain curtain so it does not form until 22.0 seconds.

**中文翻译：** 从第 14.5 秒开始，延迟下一道中央雨幕，使其直到第 22.0 秒才形成。

**状态：** 接受

**原子化判定句：**

1. 下一道中央雨幕是否在延迟 7.5 秒后形成？


## 062 — `synthetic_process_021_E2A`

**原始英文指令：** Starting at 30.0 seconds, advance the storm until three separated rain shafts span the central skyline by 34.5 seconds.

**中文翻译：** 从第 30.0 秒开始，推进风暴进程，使三道彼此分离的雨柱在第 34.5 秒前横跨中央天际线。

**状态：** 接受

**原子化判定句：**

1. 风暴进程是否得到推进？

2. 三道彼此分离的雨柱是否在 4.5 秒内横跨中央天际线？


## 063 — `synthetic_process_021_E2B`

**原始英文指令：** Starting at 28.5 seconds, make the dark cloud layer's lower edge send three ripples from right to left over five seconds.

**中文翻译：** 从第 28.5 秒开始，让暗色云层的下缘在五秒内由右向左传出三道波纹。

**状态：** 接受

**原子化判定句：**

1. 波纹是否沿暗色云层下缘由右向左传播？

2. 是否恰好产生三道波纹？

3. 三道波纹是否在 5 秒内完成？


## 064 — `synthetic_process_022_E1`

**原始英文指令：** Starting at 14.0 seconds, accelerate the harbor fog until the entire breakwater becomes only a faint outline by 20.0 seconds.

**中文翻译：** 从第 14.0 秒开始，加快港湾雾气的蔓延，使整条防波堤在第 20.0 秒前仅剩模糊轮廓。

**状态：** 接受

**原子化判定句：**

1. 港湾雾气的蔓延是否加快？

2. 整条防波堤是否在 6 秒内变得仅剩模糊轮廓？


## 065 — `synthetic_process_022_E2A`

**原始英文指令：** Starting at 30.5 seconds, render only the upper blue sky above the harbor fog as a soft chalk-pastel field over two seconds.

**中文翻译：** 从第 30.5 秒开始，在两秒内仅将港湾雾气上方的上部蓝天呈现为柔和的粉笔彩绘色块。

**状态：** 接受

**原子化判定句：**

1. 港湾雾气上方的上部蓝天是否呈现为柔和的粉笔彩绘色块？

2. 风格变化是否仅限于该上部天空？

3. 风格变化是否在 2 秒内完成？


## 066 — `synthetic_process_022_E2B`

**原始英文指令：** Starting at 28.5 seconds, add warm low sidelight to the left-shore building and nearest tree crowns over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内为左岸建筑和最近的树冠添加暖色低角度侧光。

**状态：** 接受

**原子化判定句：**

1. 左岸建筑是否添加了暖色低角度侧光？

2. 最近的树冠是否也添加了相同侧光？

3. 照明变化是否在 2 秒内完成？


## 067 — `synthetic_process_023_E1`

**原始英文指令：** At 15.0 seconds, add one short charred split log across the front-right gap of the burning wood pile.

**中文翻译：** 在第 15.0 秒，在燃烧木堆右前方的缺口上横放一根短小、烧焦且劈开的木柴。

**状态：** 接受

**原子化判定句：**

1. 是否添加了恰好一根短小、烧焦且劈开的木柴？

2. 该木柴是否横放在燃烧木堆右前方的缺口上？


## 068 — `synthetic_process_023_E2A`

**原始英文指令：** Starting at 28.0 seconds, accelerate flame decline until every visible flame remains below half the wood-pile height by 33.0 seconds.

**中文翻译：** 从第 28.0 秒开始，加快火焰衰减，使所有可见火焰在第 33.0 秒前都保持低于木堆高度的一半。

**状态：** 接受

**原子化判定句：**

1. 火焰衰减是否加快？

2. 所有可见火焰是否在 5 秒内都保持低于木堆高度的一半？


## 069 — `synthetic_process_023_E2B`

**原始英文指令：** Starting at 29.0 seconds, advance the burn stage until only two short flames and a low red ember bed remain by 33.5 seconds.

**中文翻译：** 从第 29.0 秒开始，推进燃烧阶段，使画面在第 33.5 秒前仅剩两簇短火焰和一层低矮的红色余烬。

**状态：** 接受

**原子化判定句：**

1. 燃烧阶段是否得到推进？

2. 是否在 4.5 秒内仅剩两簇短火焰？

3. 是否在同一段 4.5 秒内剩下一层低矮的红色余烬？


## 070 — `synthetic_process_024_E1`

**原始英文指令：** Starting at 14.5 seconds, hold the candle flame upright and completely still for five seconds, then let its natural flicker resume.

**中文翻译：** 从第 14.5 秒开始，让蜡烛火焰保持直立并完全静止五秒，然后恢复自然闪烁。

**状态：** 接受

**原子化判定句：**

1. 蜡烛火焰是否保持直立 5 秒？

2. 蜡烛火焰是否在同一段 5 秒内保持完全静止？

3. 蜡烛火焰是否在保持 5 秒后恢复自然闪烁？


## 071 — `synthetic_process_024_E2A`

**原始英文指令：** Starting at 27.0 seconds, accelerate flame weakening until the flame is no taller than the visible wick by 31.0 seconds.

**中文翻译：** 从第 27.0 秒开始，加快火焰减弱，使火焰在第 31.0 秒前不高于可见的烛芯。

**状态：** 接受

**原子化判定句：**

1. 火焰减弱是否加快？

2. 火焰是否在 4 秒内变得不高于可见的烛芯？


## 072 — `synthetic_process_024_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the single candle flame bend left and right twice over four seconds.

**中文翻译：** 从第 29.0 秒开始，让这一簇蜡烛火焰在四秒内左右弯曲两次。

**状态：** 接受

**原子化判定句：**

1. 单簇蜡烛火焰是否向左弯曲？

2. 单簇蜡烛火焰是否向右弯曲？

3. 火焰是否在 4 秒内完成 2 次左右弯曲？


## 073 — `synthetic_process_025_E1`

**原始英文指令：** Starting at 15.0 seconds, make the clear liquid visibly gelatinous with a rounded meniscus and slow surface deformation over two seconds.

**中文翻译：** 从第 15.0 秒开始，在两秒内让透明液体呈现明显的凝胶质感，并具有圆弧形弯月面和缓慢的表面形变。

**状态：** 接受

**原子化判定句：**

1. 透明液体是否在 2 秒内呈现明显的凝胶质感？

2. 透明液体是否在同一段 2 秒内形成圆弧形弯月面？

3. 透明液体是否在同一段 2 秒内呈现缓慢的表面形变？


## 074 — `synthetic_process_025_E2A`

**原始英文指令：** At 29.0 seconds, remove the dense small-bubble cluster attached to the lower-right wall of the transparent cylinder.

**中文翻译：** 在第 29.0 秒，移除附着在透明圆柱体右下方内壁上的密集小气泡簇。

**状态：** 接受

**原子化判定句：**

1. 附着在透明圆柱体右下方内壁上的密集小气泡簇是否被移除？


## 075 — `synthetic_process_025_E2B`

**原始英文指令：** Starting at 25.0 seconds, accelerate filling until the liquid surface reaches the bottom tip of the central glass rod by 30.0 seconds.

**中文翻译：** 从第 25.0 秒开始，加快注液速度，使液面在第 30.0 秒前到达中央玻璃棒的底端。

**状态：** 接受

**原子化判定句：**

1. 注液速度是否加快？

2. 液面是否在 5 秒内到达中央玻璃棒的底端？


## 076 — `synthetic_process_026_E1`

**原始英文指令：** Starting at 14.0 seconds, transform the entire blue-liquid dispersion scene into a layered wet-on-wet watercolor painting over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内将整个蓝色液体扩散场景转换为层次分明的湿画法水彩画。

**状态：** 接受

**原子化判定句：**

1. 整个蓝色液体扩散场景是否转换为层次分明的湿画法水彩画？

2. 这一转换是否在 2 秒内完成？


## 077 — `synthetic_process_026_E2A`

**原始英文指令：** Starting at 29.0 seconds, change only the remaining concentrated blue plumes to saturated violet over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内仅将剩余的浓缩蓝色羽流变为高饱和紫色。

**状态：** 接受

**原子化判定句：**

1. 剩余的浓缩蓝色羽流是否变为高饱和紫色？

2. 颜色变化是否仅限于这些羽流？

3. 颜色变化是否在 2 秒内完成？


## 078 — `synthetic_process_026_E2B`

**原始英文指令：** Starting at 28.5 seconds, pause dispersal of the remaining concentrated plume boundaries for five seconds, then resume.

**中文翻译：** 从第 28.5 秒开始，让剩余浓缩羽流边界的扩散暂停五秒，然后恢复扩散。

**状态：** 接受

**原子化判定句：**

1. 剩余浓缩羽流边界的扩散是否暂停 5 秒？

2. 这些边界是否在暂停 5 秒后恢复扩散？


## 079 — `synthetic_process_027_E1`

**原始英文指令：** Starting at 15.0 seconds, pause visible shrinkage of the white granular block for four seconds, then resume from its held size.

**中文翻译：** 从第 15.0 秒开始，让白色颗粒块可见的缩小过程暂停四秒，然后从保持的尺寸继续缩小。

**状态：** 接受

**原子化判定句：**

1. 白色颗粒块可见的缩小过程是否暂停 4 秒？

2. 白色颗粒块是否在暂停 4 秒后从保持的尺寸继续缩小？


## 080 — `synthetic_process_027_E2A`

**原始英文指令：** Starting at 29.0 seconds, change the remaining white block fragment to pale pink over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将剩余的白色块状碎片变为浅粉色。

**状态：** 接受

**原子化判定句：**

1. 剩余的块状碎片是否从白色变为浅粉色？

2. 颜色变化是否在 2 秒内完成？


## 081 — `synthetic_process_027_E2B`

**原始英文指令：** At 29.5 seconds, move the remaining main block fragment one fragment-width left across the glass bottom.

**中文翻译：** 在第 29.5 秒，将剩余的主要块状碎片沿玻璃底部向左移动一个碎片宽度。

**状态：** 接受

**原子化判定句：**

1. 剩余的主要块状碎片是否沿玻璃底部向左移动？

2. 移动距离是否为一个碎片宽度？


## 082 — `synthetic_process_028_E1`

**原始英文指令：** Starting at 14.0 seconds, transform the entire branching liquid-trace scene into a black-ink linocut print over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内将整个分支状液体痕迹场景转换为黑墨版画。

**状态：** 接受

**原子化判定句：**

1. 整个分支状液体痕迹场景是否转换为黑墨版画？

2. 这一转换是否在 2 秒内完成？


## 083 — `synthetic_process_028_E2A`

**原始英文指令：** Starting at 29.0 seconds, raise and tilt the camera into a stable overhead view of the fibrous sheet and round dish over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内抬高并倾斜镜头，形成对纤维薄片和圆形培养皿的稳定俯视视角。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 3 秒内升高？

2. 镜头是否在同一段 3 秒内倾斜至能够稳定俯视纤维薄片和圆形培养皿的视角？


## 084 — `synthetic_process_028_E2B`

**原始英文指令：** Starting at 28.5 seconds, smoothly zoom in until the highest black branch tips fill the middle third of the frame.

**中文翻译：** 从第 28.5 秒开始，平滑拉近镜头，直到最高的黑色分支尖端充满画面中间三分之一区域。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近，直至最高的黑色分支尖端充满画面中间三分之一区域？

2. 拉近过程是否平滑？


## 085 — `synthetic_process_029_E1`

**原始英文指令：** Starting at 15.0 seconds, pause the selected dark-green wave crest's approach and breaking for four seconds, then resume from the held stage.

**中文翻译：** 从第 15.0 秒开始，让选定深绿色浪峰的靠近和破碎过程暂停四秒，然后从保持的阶段恢复。

**状态：** 接受

**原子化判定句：**

1. 选定的深绿色浪峰是否暂停靠近 4 秒？

2. 选定浪峰的破碎过程是否在同一段 4 秒内暂停？

3. 其靠近和破碎过程是否在暂停 4 秒后从保持的阶段恢复？


## 086 — `synthetic_process_029_E2A`

**原始英文指令：** At 28.0 seconds, position the nearest continuous foam line parallel to the wet-dry sand boundary with one foam-band-width between them.

**中文翻译：** 在第 28.0 秒，将最近的连续泡沫线调整为与干湿沙地边界平行，并使两者间距为一条泡沫带的宽度。

**状态：** 接受

**原子化判定句：**

1. 最近的连续泡沫线是否与干湿沙地边界平行？

2. 泡沫线与干湿沙地边界之间的间距是否为一条泡沫带的宽度？


## 087 — `synthetic_process_029_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full shoreline scene into faded 1970s 16 mm film footage over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将整个海岸线场景转换为褪色的 20 世纪 70 年代 16 毫米胶片影像。

**状态：** 接受

**原子化判定句：**

1. 整个海岸线场景是否转换为褪色的 20 世纪 70 年代 16 毫米胶片影像？

2. 这一转换是否在 2 秒内完成？


## 088 — `synthetic_process_030_E1`

**原始英文指令：** Starting at 14.5 seconds, transform the full transparent-box fog scene into a cool steel-blue monochrome grade over two seconds.

**中文翻译：** 从第 14.5 秒开始，在两秒内将整个透明箱雾气场景转换为冷调钢蓝色单色调。

**状态：** 接受

**原子化判定句：**

1. 整个透明箱雾气场景是否转换为冷调钢蓝色单色调？

2. 这一转换是否在 2 秒内完成？


## 089 — `synthetic_process_030_E2A`

**原始英文指令：** Starting at 28.5 seconds, make three fog tendrils along the upper boundary curl upward one after another over five seconds.

**中文翻译：** 从第 28.5 秒开始，让上部边界沿线的三缕雾气在五秒内依次向上卷曲。

**状态：** 接受

**原子化判定句：**

1. 上部边界沿线是否恰好有三缕雾气向上卷曲？

2. 三缕雾气是否依次卷曲？

3. 这一过程是否在 5 秒内完成？


## 090 — `synthetic_process_030_E2B`

**原始英文指令：** Starting at 29.0 seconds, change only the dense accumulated fog to pale lavender over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内仅将浓密积聚的雾气变为浅薰衣草紫色。

**状态：** 接受

**原子化判定句：**

1. 浓密积聚的雾气是否变为浅薰衣草紫色？

2. 颜色变化是否仅限于该浓密积聚的雾气？

3. 颜色变化是否在 2 秒内完成？


## 091 — `synthetic_process_031_E1`

**原始英文指令：** Starting at 14.0 seconds, make grains on the left and right mound slopes cascade downward in three alternating waves over five seconds.

**中文翻译：** 从第 14.0 秒开始，让颗粒在土堆左右两侧斜坡上以三道交替波浪的形式向下倾泻，历时五秒。

**状态：** 接受

**原子化判定句：**

1. 左侧堆坡上的颗粒是否向下倾泻？

2. 右侧堆坡上的颗粒是否向下倾泻？

3. 两侧颗粒是否在 5 秒内形成 3 道交替波浪？


## 092 — `synthetic_process_031_E2A`

**原始英文指令：** Starting at 28.0 seconds, accelerate deposition until the particle mound apex rises directly beneath the outlet by 33.0 seconds.

**中文翻译：** 从第 28.0 秒开始，加快颗粒沉积，使颗粒堆顶点在第 33.0 秒前上升到出口正下方。

**状态：** 接受

**原子化判定句：**

1. 颗粒沉积是否加快？

2. 颗粒堆顶点是否在 5 秒内上升到出口正下方？


## 093 — `synthetic_process_031_E2B`

**原始英文指令：** Starting at 28.5 seconds, pause the falling-particle deposition and mound growth for five seconds, then resume from the held shape.

**中文翻译：** 从第 28.5 秒开始，让下落颗粒的沉积和颗粒堆生长暂停五秒，然后从保持的形状恢复。

**状态：** 接受

**原子化判定句：**

1. 下落颗粒的沉积是否暂停 5 秒？

2. 颗粒堆生长是否在同一段 5 秒内暂停？

3. 沉积和颗粒堆生长是否在暂停 5 秒后从保持的形状恢复？


## 094 — `synthetic_process_032_E1`

**原始英文指令：** Starting at 14.0 seconds, make the central transparent tube rise one centimeter and lower back twice over five seconds.

**中文翻译：** 从第 14.0 秒开始，让中央透明管在五秒内上升一厘米再下降复位，共完成两次。

**状态：** 接受

**原子化判定句：**

1. 中央透明管是否每次上升 1 厘米？

2. 中央透明管是否在每次上升后下降复位？

3. 透明管是否在 5 秒内完成 2 次升降？


## 095 — `synthetic_process_032_E2A`

**原始英文指令：** Starting at 27.5 seconds, pause the foam boundary's upward expansion for five seconds, then resume from the held height.

**中文翻译：** 从第 27.5 秒开始，让泡沫边界向上扩张的过程暂停五秒，然后从保持的高度恢复扩张。

**状态：** 接受

**原子化判定句：**

1. 泡沫边界向上扩张的过程是否暂停 5 秒？

2. 泡沫边界是否在暂停 5 秒后从保持的高度恢复向上扩张？


## 096 — `synthetic_process_032_E2B`

**原始英文指令：** Starting at 28.5 seconds, advance foam expansion until the dome sits just above the rim with three large clear bubbles by 33.0 seconds.

**中文翻译：** 从第 28.5 秒开始，推进泡沫扩张，使泡沫穹顶在第 33.0 秒前位于容器边缘略上方，并带有三个清晰的大气泡。

**状态：** 接受

**原子化判定句：**

1. 泡沫扩张是否得到推进？

2. 泡沫穹顶是否在 4.5 秒内位于容器边缘略上方？

3. 泡沫穹顶中是否在同一段 4.5 秒内出现三个清晰的大气泡？


## 097 — `synthetic_process_033_E1`

**原始英文指令：** Starting at 14.5 seconds, advance the pooling stage until the amber liquid reaches its source 22-second diameter by 19.5 seconds.

**中文翻译：** 从第 14.5 秒开始，推进汇聚阶段，使琥珀色液体在第 19.5 秒前达到源视频第 22 秒时的直径。

**状态：** 接受

**原子化判定句：**

1. 液体汇聚阶段是否得到推进？

2. 琥珀色液体是否在 5 秒内达到其在源视频第 22 秒时的直径？


## 098 — `synthetic_process_033_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the descending amber strand trace one small clockwise circle around the pool center over five seconds.

**中文翻译：** 从第 29.0 秒开始，让向下流动的琥珀色液柱在五秒内围绕液池中心顺时针画一个小圆圈。

**状态：** 接受

**原子化判定句：**

1. 向下流动的琥珀色液柱是否围绕液池中心顺时针画圆？

2. 是否恰好画出一个小圆圈？

3. 该圆圈是否在 5 秒内完成？


## 099 — `synthetic_process_033_E2B`

**原始英文指令：** Starting at 28.5 seconds, transform the entire amber-liquid pouring scene into an opaque gouache painting over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内将整个琥珀色液体倾倒场景转换为不透明的水粉画。

**状态：** 接受

**原子化判定句：**

1. 整个琥珀色液体倾倒场景是否转换为不透明的水粉画？

2. 这一转换是否在 2 秒内完成？


## 100 — `synthetic_process_034_E1`

**原始英文指令：** Starting at 14.0 seconds, advance bubbling until continuous bubble columns reach and ripple the full liquid surface by 19.0 seconds.

**中文翻译：** 从第 14.0 秒开始，推进冒泡过程，使连续的气泡柱在第 19.0 秒前到达整个液面并使其泛起波纹。

**状态：** 接受

**原子化判定句：**

1. 冒泡过程是否得到推进？

2. 连续的气泡柱是否在 5 秒内到达液面？

3. 气泡柱是否在同一段 5 秒内使整个液面泛起波纹？


## 101 — `synthetic_process_034_E2A`

**原始英文指令：** Starting at 28.0 seconds, make three central bubble columns spiral upward simultaneously for five seconds.

**中文翻译：** 从第 28.0 秒开始，让中央三道气泡柱同时螺旋上升五秒。

**状态：** 接受

**原子化判定句：**

1. 中央是否恰好有三道气泡柱螺旋上升？

2. 三道气泡柱是否同时螺旋上升？

3. 同时上升的运动是否持续 5 秒？


## 102 — `synthetic_process_034_E2B`

**原始英文指令：** Starting at 28.5 seconds, shift the entire bubbling-vessel scene to a cool cyan high-contrast grade over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内将整个冒泡容器场景转换为冷调青色高对比度色调。

**状态：** 接受

**原子化判定句：**

1. 整个冒泡容器场景是否转换为冷调青色色调？

2. 变化后的场景是否具有高对比度？

3. 这一变化是否在 2 秒内完成？


## 103 — `synthetic_process_035_E1`

**原始英文指令：** Starting at 14.5 seconds, make the white oblong tablet porous and brittle with three short surface cracks over two seconds.

**中文翻译：** 从第 14.5 秒开始，在两秒内让白色长椭圆形药片变得多孔而脆，并在表面出现三道短裂纹。

**状态：** 接受

**原子化判定句：**

1. 白色长椭圆形药片是否在 2 秒内变得多孔？

2. 药片是否在同一段 2 秒内变脆？

3. 药片表面是否在同一段 2 秒内出现三道短裂纹？


## 104 — `synthetic_process_035_E2A`

**原始英文指令：** At 29.0 seconds, reorient the thin white tablet remnant so its broad flat face points directly toward the camera.

**中文翻译：** 在第 29.0 秒，重新调整薄白色药片残片的方向，使其宽阔平面正对镜头。

**状态：** 接受

**原子化判定句：**

1. 薄白色药片残片是否被重新调整方向，使其宽阔平面正对镜头？


## 105 — `synthetic_process_035_E2B`

**原始英文指令：** At 28.5 seconds, remove the dense central bubble column rising directly above the white tablet remnant.

**中文翻译：** 在第 28.5 秒，移除从白色药片残片正上方升起的密集中央气泡柱。

**状态：** 接受

**原子化判定句：**

1. 从白色药片残片正上方升起的密集中央气泡柱是否被移除？


## 106 — `synthetic_process_036_E1`

**原始英文指令：** At 15.0 seconds, replace the round receiving bowl beneath the filter outlet with a square clear glass dish.

**中文翻译：** 在第 15.0 秒，将过滤器出口下方的圆形接收碗替换为方形透明玻璃皿。

**状态：** 接受

**原子化判定句：**

1. 过滤器出口下方的圆形接收碗是否被替换为玻璃皿？

2. 替换后的玻璃皿是否为方形？

3. 替换后的玻璃皿是否透明？


## 107 — `synthetic_process_036_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the collected filtrate visibly viscous so arriving drops form a rounded raised pool over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内让收集到的滤液呈现明显黏稠质感，使落下的液滴形成隆起的圆形液池。

**状态：** 接受

**原子化判定句：**

1. 收集到的滤液是否在 2 秒内呈现明显黏稠质感？

2. 落下的液滴是否在同一段 2 秒内形成隆起的圆形液池？


## 108 — `synthetic_process_036_E2B`

**原始英文指令：** Starting at 29.5 seconds, advance filtration until the upper free-liquid layer falls to one third of its current depth by 34.0 seconds.

**中文翻译：** 从第 29.5 秒开始，推进过滤过程，使上部自由液层在第 34.0 秒前降至当前深度的三分之一。

**状态：** 接受

**原子化判定句：**

1. 过滤过程是否得到推进？

2. 上部自由液层是否在 4.5 秒内降至编辑点时深度的三分之一？


## 109 — `synthetic_process_037_E1`

**原始英文指令：** Starting at 14.0 seconds, accelerate settling until the bottom sediment layer reaches twice its current thickness by 20.0 seconds.

**中文翻译：** 从第 14.0 秒开始，加快沉降，使底部沉积层在第 20.0 秒前达到当前厚度的两倍。

**状态：** 接受

**原子化判定句：**

1. 沉降是否加快？

2. 底部沉积层是否在 6 秒内达到编辑点时厚度的两倍？


## 110 — `synthetic_process_037_E2A`

**原始英文指令：** Starting at 28.5 seconds, change the clearer upper liquid from yellow-brown to pale turquoise over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内将较清澈的上层液体由黄褐色变为浅青绿色。

**状态：** 接受

**原子化判定句：**

1. 较清澈的上层液体是否由黄褐色变为浅青绿色？

2. 颜色变化是否在 2 秒内完成？


## 111 — `synthetic_process_037_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the full particle-settling scene into 1980s educational film footage over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将整个颗粒沉降场景转换为 20 世纪 80 年代教育影片影像。

**状态：** 接受

**原子化判定句：**

1. 整个颗粒沉降场景是否转换为 20 世纪 80 年代教育影片影像？

2. 这一转换是否在 2 秒内完成？


## 112 — `synthetic_process_038_E1`

**原始英文指令：** Starting at 14.0 seconds, make the single central fountain jet bend left and right twice over five seconds.

**中文翻译：** 从第 14.0 秒开始，让中央单股喷泉水柱在五秒内左右弯曲两次。

**状态：** 接受

**原子化判定句：**

1. 中央单股喷泉水柱是否左右弯曲？

2. 水柱是否恰好完成两次弯曲？

3. 两次弯曲是否在 5 秒内完成？


## 113 — `synthetic_process_038_E2A`

**原始英文指令：** Starting at 28.0 seconds, accelerate nozzle activation until every inner-ring nozzle produces a visible jet by 33.0 seconds.

**中文翻译：** 从第 28.0 秒开始，加快喷嘴启动，使内圈每个喷嘴在第 33.0 秒前都喷出可见水柱。

**状态：** 接受

**原子化判定句：**

1. 喷嘴启动是否加快？

2. 内圈每个喷嘴是否都在 5 秒内喷出可见水柱？


## 114 — `synthetic_process_038_E2B`

**原始英文指令：** Starting at 28.5 seconds, advance the fountain program until symmetric inward arcs rise from the full perimeter by 34.0 seconds.

**中文翻译：** 从第 28.5 秒开始，推进喷泉程序，使对称的向内弧形水柱在第 34.0 秒前从整个周边升起。

**状态：** 接受

**原子化判定句：**

1. 喷泉程序是否得到推进？

2. 对称的向内弧形水柱是否在 5.5 秒内从整个周边升起？


## 115 — `synthetic_process_039_E1`

**原始英文指令：** At 14.0 seconds, remove the isolated dark fuel block at the front-left rim of the white container.

**中文翻译：** 在第 14.0 秒，移除白色容器左前侧边缘处孤立的深色燃料块。

**状态：** 接受

**原子化判定句：**

1. 白色容器左前侧边缘处孤立的深色燃料块是否被移除？


## 116 — `synthetic_process_039_E2A`

**原始英文指令：** Starting at 29.0 seconds, pause decline of the remaining orange flames for five seconds, then resume from the held flame height.

**中文翻译：** 从第 29.0 秒开始，让剩余橙色火焰的衰减暂停五秒，然后从保持的火焰高度恢复衰减。

**状态：** 接受

**原子化判定句：**

1. 剩余橙色火焰的衰减是否暂停 5 秒？

2. 剩余橙色火焰是否在暂停 5 秒后从保持的火焰高度恢复衰减？


## 117 — `synthetic_process_039_E2B`

**原始英文指令：** Starting at 28.5 seconds, advance suppression until the last orange flame disappears and clear smoke wisps rise by 33.0 seconds.

**中文翻译：** 从第 28.5 秒开始，推进灭火过程，使最后一簇橙色火焰在第 33.0 秒前消失，并升起清晰的烟缕。

**状态：** 接受

**原子化判定句：**

1. 灭火过程是否得到推进？

2. 最后一簇橙色火焰是否在 4.5 秒内消失？

3. 清晰的烟缕是否在同一段 4.5 秒内升起？


## 118 — `synthetic_process_040_E1`

**原始英文指令：** Starting at 16.0 seconds, move the camera slowly right along a short arc around the covered candle for five seconds.

**中文翻译：** 从第 16.0 秒开始，让镜头围绕被罩住的蜡烛沿一小段弧线缓慢向右移动五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否围绕被罩住的蜡烛沿一小段弧线向右移动？

2. 镜头移动是否缓慢？

3. 这一移动是否持续 5 秒？


## 119 — `synthetic_process_040_E2A`

**原始英文指令：** At 29.0 seconds, position the inner candle cup two centimeters left of center inside the outer glass enclosure.

**中文翻译：** 在第 29.0 秒，将内层烛杯放置在外层玻璃罩中心左侧两厘米处。

**状态：** 接受

**原子化判定句：**

1. 内层烛杯是否位于外层玻璃罩中心左侧 2 厘米处？


## 120 — `synthetic_process_040_E2B`

**原始英文指令：** At 30.5 seconds, replace the smooth outer glass cylinder with a taller eight-sided clear glass enclosure around the candle.

**中文翻译：** 在第 30.5 秒，将光滑的外层玻璃圆筒替换为围绕蜡烛、更加高挑的八面透明玻璃罩。

**状态：** 接受

**原子化判定句：**

1. 光滑的外层玻璃圆筒是否被替换为围绕蜡烛的玻璃罩？

2. 替换后的玻璃罩是否比原圆筒更高？

3. 替换后的玻璃罩是否具有八个侧面？

4. 替换后的玻璃罩是否透明？


## 121 — `synthetic_process_041_E1`

**原始英文指令：** Starting at 11.5 seconds, advance foam growth until it reaches the bottle mouth and forms a rounded cap by 16.0 seconds.

**中文翻译：** 从第 11.5 秒开始，推进泡沫生长，使其在第 16.0 秒前到达瓶口并形成圆顶状泡沫帽。

**状态：** 接受

**原子化判定句：**

1. 泡沫生长是否得到推进？

2. 泡沫是否在 4.5 秒内到达瓶口？

3. 泡沫是否在同一段 4.5 秒内形成圆顶状泡沫帽？


## 122 — `synthetic_process_041_E2A`

**原始英文指令：** Starting at 28.0 seconds, delay visible thinning of the exterior foam lobes until 34.0 seconds.

**中文翻译：** 从第 28.0 秒开始，将外部泡沫瓣明显变薄的时间延迟到第 34.0 秒。

**状态：** 接受

**原子化判定句：**

1. 外部泡沫瓣是否在延迟 6 秒后明显变薄？


## 123 — `synthetic_process_041_E2B`

**原始英文指令：** Starting at 25.5 seconds, split the large front overflow foam lobe into two parallel descending lobes over 1.5 seconds.

**中文翻译：** 从第 25.5 秒开始，在一点五秒内将前方大型溢流泡沫瓣分成两个平行向下延伸的泡沫瓣。

**状态：** 接受

**原子化判定句：**

1. 前方大型溢流泡沫瓣是否在 1.5 秒内分成两个向下延伸的泡沫瓣？

2. 两个向下延伸的泡沫瓣是否相互平行？


## 124 — `synthetic_process_042_E1`

**原始英文指令：** Starting at 14.0 seconds, move the camera clockwise along a short arc above the red-blue liquid dish for five seconds.

**中文翻译：** 从第 14.0 秒开始，让镜头在红蓝液体培养皿上方沿一小段弧线顺时针移动五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在红蓝液体培养皿上方沿一小段弧线顺时针移动？

2. 这一移动是否持续 5 秒？


## 125 — `synthetic_process_042_E2A`

**原始英文指令：** Starting at 29.0 seconds, split the single red-blue interface spiral into two nested spiral arms over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将单条红蓝界面螺旋分成两条嵌套的螺旋臂。

**状态：** 接受

**原子化判定句：**

1. 单条红蓝界面螺旋是否分成恰好两条螺旋臂？

2. 两条螺旋臂是否相互嵌套？

3. 分裂过程是否在 2 秒内完成？


## 126 — `synthetic_process_042_E2B`

**原始英文指令：** Starting at 28.5 seconds, make both colored liquids gel-like with a shallow raised ridge along their spiral boundary over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内让两种彩色液体都呈凝胶状，并沿其螺旋边界形成一道浅而隆起的脊线。

**状态：** 接受

**原子化判定句：**

1. 两种彩色液体是否都在 2 秒内变为凝胶状？

2. 两种液体的螺旋边界沿线是否在同一段 2 秒内形成一道浅而隆起的脊线？


## 127 — `synthetic_process_043_E1`

**原始英文指令：** Starting at 14.0 seconds, transform the full spreading black-film scene into a monochrome aquatint print over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内将整个黑色薄膜扩散场景转换为单色飞尘腐蚀版画。

**状态：** 接受

**原子化判定句：**

1. 整个黑色薄膜扩散场景是否转换为单色飞尘腐蚀版画？

2. 这一转换是否在 2 秒内完成？


## 128 — `synthetic_process_043_E2A`

**原始英文指令：** At 29.0 seconds, reorient the asymmetric feathered liquid film 20 degrees clockwise within the round dish.

**中文翻译：** 在第 29.0 秒，将圆形培养皿内不对称的羽毛状液膜顺时针旋转二十度。

**状态：** 接受

**原子化判定句：**

1. 圆形培养皿内不对称的羽毛状液膜是否顺时针旋转？

2. 旋转角度是否为 20 度？


## 129 — `synthetic_process_043_E2B`

**原始英文指令：** Starting at 28.5 seconds, change the spread liquid film to deep emerald with copper iridescent lines over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内将铺展的液膜变为深祖母绿色，并呈现铜色虹彩线条。

**状态：** 接受

**原子化判定句：**

1. 铺展的液膜是否在 2 秒内变为深祖母绿色？

2. 液膜上是否在同一段 2 秒内出现铜色虹彩线条？


## 130 — `synthetic_process_044_E1`

**原始英文指令：** Starting at 6.5 seconds, delay vapor rising more than one bucket-rim height above the rim for five seconds.

**中文翻译：** 从第 6.5 秒开始，将蒸汽上升到桶沿上方超过一个桶沿高度的时间延迟五秒。

**状态：** 接受

**原子化判定句：**

1. 蒸汽是否在延迟 5 秒后上升到桶沿上方超过一个桶沿高度？


## 131 — `synthetic_process_044_E2A`

**原始英文指令：** Starting at 25.0 seconds, accelerate vapor dissipation until no continuous vapor crosses the bucket rim by 29.0 seconds.

**中文翻译：** 从第 25.0 秒开始，加快蒸汽消散，使连续蒸汽在第 29.0 秒前不再越过桶沿。

**状态：** 接受

**原子化判定句：**

1. 蒸汽消散是否加快？

2. 连续蒸汽是否在 4 秒内停止越过桶沿？


## 132 — `synthetic_process_044_E2B`

**原始英文指令：** Starting at 20.5 seconds, transform the full bucket-and-vapor scene into a soft pastel illustration over two seconds.

**中文翻译：** 从第 20.5 秒开始，在两秒内将整个桶与蒸汽场景转换为柔和的粉彩插画。

**状态：** 接受

**原子化判定句：**

1. 整个桶与蒸汽场景是否转换为柔和的粉彩插画？

2. 这一转换是否在 2 秒内完成？


## 133 — `synthetic_process_045_E1`

**原始英文指令：** Starting at 14.0 seconds, advance melting until the ice is half its original height and the puddle doubles in width by 19.0 seconds.

**中文翻译：** 从第 14.0 秒开始，推进融化过程，使冰块在第 19.0 秒前降至原高度的一半，并使水洼宽度增至两倍。

**状态：** 接受

**原子化判定句：**

1. 融化过程是否得到推进？

2. 冰块是否在 5 秒内降至原高度的一半？

3. 水洼是否在同一段 5 秒内达到编辑点时宽度的两倍？


## 134 — `synthetic_process_045_E2A`

**原始英文指令：** Starting at 29.0 seconds, shift the full melting-ice scene to a cool silver-blue duotone over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将整个融冰场景转换为冷调银蓝双色效果。

**状态：** 接受

**原子化判定句：**

1. 整个融冰场景是否转换为冷调银蓝双色效果？

2. 这一变化是否在 2 秒内完成？


## 135 — `synthetic_process_045_E2B`

**原始英文指令：** At 28.5 seconds, move the small residual ice piece to the left edge of its surrounding puddle.

**中文翻译：** 在第 28.5 秒，将残留的小冰块移至其周围水洼的左侧边缘。

**状态：** 接受

**原子化判定句：**

1. 残留的小冰块是否被移至其周围水洼的左侧边缘？


## 136 — `synthetic_process_046_E1`

**原始英文指令：** Starting at 14.0 seconds, advance softening until the block is half its initial height and fully surrounded by liquid by 19.0 seconds.

**中文翻译：** 从第 14.0 秒开始，推进软化过程，使块体在第 19.0 秒前降至初始高度的一半，并完全被液体包围。

**状态：** 接受

**原子化判定句：**

1. 软化过程是否得到推进？

2. 块体是否在 5 秒内降至初始高度的一半？

3. 块体是否在同一段 5 秒内完全被液体包围？


## 137 — `synthetic_process_046_E2A`

**原始英文指令：** Starting at 29.0 seconds, pause flattening of the thin brown remnant for five seconds, then resume from its held thickness.

**中文翻译：** 从第 29.0 秒开始，让薄棕色残留物的变平过程暂停五秒，然后从保持的厚度恢复。

**状态：** 接受

**原子化判定句：**

1. 薄棕色残留物的变平过程是否暂停 5 秒？

2. 棕色残留物是否在暂停 5 秒后从保持的厚度恢复变平？


## 138 — `synthetic_process_046_E2B`

**原始英文指令：** Starting at 28.5 seconds, make three concentric ripple rings travel outward across the brown liquid pool over five seconds.

**中文翻译：** 从第 28.5 秒开始，让三道同心波纹环在五秒内向外传播并越过棕色液池。

**状态：** 接受

**原子化判定句：**

1. 棕色液池上是否恰好出现三道同心波纹环？

2. 波纹环是否向外传播并越过液池？

3. 向外传播是否在 5 秒内完成？


## 139 — `synthetic_process_047_E1`

**原始英文指令：** Starting at 14.0 seconds, change the molten surface inside the round mold from orange to pale gold over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内将圆形模具内的熔融表面由橙色变为浅金色。

**状态：** 接受

**原子化判定句：**

1. 圆形模具内的熔融表面是否由橙色变为浅金色？

2. 颜色变化是否在 2 秒内完成？


## 140 — `synthetic_process_047_E2A`

**原始英文指令：** Starting at 29.0 seconds, make three surface ripple rings expand outward successively from the mold center over five seconds.

**中文翻译：** 从第 29.0 秒开始，让三道表面波纹环在五秒内依次从模具中心向外扩散。

**状态：** 接受

**原子化判定句：**

1. 是否恰好有三道表面波纹环从模具中心向外扩散？

2. 三道波纹环是否依次扩散？

3. 这一过程是否在 5 秒内完成？


## 141 — `synthetic_process_047_E2B`

**原始英文指令：** Starting at 29.0 seconds, delay the silver-gray cooling front across the pale-gold surface until 36.0 seconds.

**中文翻译：** 从第 29.0 秒开始，将银灰色冷却前沿掠过浅金色表面的时间延迟到第 36.0 秒。

**状态：** 接受

**原子化判定句：**

1. 银灰色冷却前沿是否在延迟 7 秒后掠过浅金色表面？


## 142 — `synthetic_process_048_E1`

**原始英文指令：** Starting at 14.5 seconds, pause visible changes in the blue coating edge and side drips for five seconds, then resume.

**中文翻译：** 从第 14.5 秒开始，让蓝色涂层边缘和侧面滴流的可见变化暂停五秒，然后恢复变化。

**状态：** 接受

**原子化判定句：**

1. 蓝色涂层边缘的可见变化是否暂停 5 秒？

2. 侧面滴流的可见变化是否在同一段 5 秒内暂停？

3. 涂层边缘和侧面滴流的变化是否在暂停 5 秒后恢复？


## 143 — `synthetic_process_048_E2A`

**原始英文指令：** At 29.0 seconds, add one small round blue paint bead beneath the center of the front coating edge.

**中文翻译：** 在第 29.0 秒，在前侧涂层边缘中央的下方添加一颗小型圆形蓝色漆珠。

**状态：** 接受

**原子化判定句：**

1. 是否添加了恰好一颗小型圆形蓝色漆珠？

2. 该漆珠是否位于前侧涂层边缘中央的下方？


## 144 — `synthetic_process_048_E2B`

**原始英文指令：** Starting at 29.0 seconds, slide the camera smoothly from right to left along the blue coating's front edge for four seconds.

**中文翻译：** 从第 29.0 秒开始，让镜头沿蓝色涂层的前缘从右向左平滑移动四秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿蓝色涂层的前缘从右向左移动？

2. 镜头移动是否平滑？

3. 这一移动是否持续 4 秒？


## 145 — `synthetic_process_049_E1`

**原始英文指令：** Starting at 14.0 seconds, accelerate the bowl's surface change until it becomes dry, matte, and pale tan-white-gray by 19.0 seconds.

**中文翻译：** 从第 14.0 秒开始，加快碗的表面变化，使其在第 19.0 秒前变得干燥、哑光，并呈浅棕白灰色。

**状态：** 接受

**原子化判定句：**

1. 碗的表面变化是否加快？

2. 碗的表面是否在 5 秒内变得干燥？

3. 碗的表面是否在同一段 5 秒内变为哑光？

4. 碗的表面是否在同一段 5 秒内变为浅棕白灰色？


## 146 — `synthetic_process_049_E2A`

**原始英文指令：** Starting at 29.0 seconds, render only the visible bowl surface with fine incised ceramic hatching over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内仅将碗的可见表面呈现为精细的陶瓷刻划排线效果。

**状态：** 接受

**原子化判定句：**

1. 碗的可见表面是否呈现为精细的陶瓷刻划排线效果？

2. 风格变化是否仅限于碗的可见表面？

3. 风格变化是否在 2 秒内完成？


## 147 — `synthetic_process_049_E2B`

**原始英文指令：** At 28.0 seconds, add one small tan clay chip on the cloth directly beneath the bowl's front crack.

**中文翻译：** 在第 28.0 秒，在碗前侧裂缝正下方的布面上添加一块棕褐色小陶土碎片。

**状态：** 接受

**原子化判定句：**

1. 布面上是否添加了恰好一块棕褐色小陶土碎片？

2. 该碎片是否位于碗前侧裂缝的正下方？


## 148 — `synthetic_process_050_E1`

**原始英文指令：** Starting at 14.0 seconds, transform the full metal-sheet scene into a hand-colored scientific etching over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内将整个金属板场景转换为手工着色的科学蚀刻画。

**状态：** 接受

**原子化判定句：**

1. 整个金属板场景是否转换为手工着色的科学蚀刻画？

2. 这一转换是否在 2 秒内完成？


## 149 — `synthetic_process_050_E2A`

**原始英文指令：** Starting at 29.0 seconds, smoothly zoom in until the central connected dark band fills the middle half of the frame.

**中文翻译：** 从第 29.0 秒开始，平滑拉近镜头，直到中央相连的深色带填满画面中间一半区域。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近，直至中央相连的深色带填满画面中间一半区域？

2. 拉近过程是否平滑？


## 150 — `synthetic_process_050_E2B`

**原始英文指令：** At 28.5 seconds, replace the silver-gray metal sheet with a same-sized brushed copper sheet bearing the same surface-band layout.

**中文翻译：** 在第 28.5 秒，将银灰色金属板替换为尺寸相同、保留相同表面带状布局的拉丝铜板。

**状态：** 接受

**原子化判定句：**

1. 银灰色金属板是否被替换为拉丝铜板？

2. 替换后的铜板是否与原金属板尺寸相同？

3. 替换后的铜板是否保留相同的表面带状布局？


## 151 — `synthetic_process_051_E1`

**原始英文指令：** Starting at 14.0 seconds, advance the surface change until green speckles outline both long edges of the dark band by 19.0 seconds.

**中文翻译：** 从第 14.0 秒开始，推进表面变化，使绿色斑点在第 19.0 秒前勾勒出深色带的两条长边。

**状态：** 接受

**原子化判定句：**

1. 表面变化是否得到推进？

2. 绿色斑点是否在 5 秒内勾勒出深色带的两条长边？


## 152 — `synthetic_process_051_E2A`

**原始英文指令：** Starting at 29.0 seconds, shift the full copper-surface close-up to a cool cyan-gray duotone over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将整个铜表面特写转换为冷调青灰双色效果。

**状态：** 接受

**原子化判定句：**

1. 整个铜表面特写是否转换为冷调青灰双色效果？

2. 这一变化是否在 2 秒内完成？


## 153 — `synthetic_process_051_E2B`

**原始英文指令：** Starting at 28.5 seconds, slide the camera left across the curved metal surface for five seconds following the dark band.

**中文翻译：** 从第 28.5 秒开始，让镜头沿深色带在弯曲金属表面上向左滑动五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿深色带在弯曲金属表面上向左滑动？

2. 镜头移动是否持续 5 秒？


## 154 — `synthetic_process_052_E1`

**原始英文指令：** Starting at 14.0 seconds, accelerate oil heating until the visible liquid becomes clearly golden amber by 19.0 seconds.

**中文翻译：** 从第 14.0 秒开始，加快油的加热，使可见液体在第 19.0 秒前明显变为金琥珀色。

**状态：** 接受

**原子化判定句：**

1. 油的加热是否加快？

2. 可见液体是否在 5 秒内明显变为金琥珀色？


## 155 — `synthetic_process_052_E2A`

**原始英文指令：** Starting at 28.0 seconds, pause expansion of the central foam ring for five seconds, then resume from its held diameter.

**中文翻译：** 从第 28.0 秒开始，让中央泡沫环的扩张暂停五秒，然后从保持的直径恢复扩张。

**状态：** 接受

**原子化判定句：**

1. 中央泡沫环的扩张是否暂停 5 秒？

2. 中央泡沫环是否在暂停 5 秒后从保持的直径恢复扩张？


## 156 — `synthetic_process_052_E2B`

**原始英文指令：** Starting at 28.5 seconds, make the largest visible surface bubble complete one clockwise orbit around the pan center over five seconds.

**中文翻译：** 从第 28.5 秒开始，让可见的最大表面气泡在五秒内绕锅中心顺时针运行一周。

**状态：** 接受

**原子化判定句：**

1. 可见的最大表面气泡是否绕锅中心顺时针运行？

2. 气泡是否恰好完成一周？

3. 这一周运行是否在 5 秒内完成？


## 157 — `synthetic_process_053_E1`

**原始英文指令：** Starting at 6.0 seconds, make three leaf-surface droplets roll along separate veins toward the right tip over five seconds.

**中文翻译：** 从第 6.0 秒开始，让叶面上的三颗液滴分别沿不同叶脉朝右侧叶尖滚动五秒。

**状态：** 接受

**原子化判定句：**

1. 叶面上是否恰好有三颗液滴朝右侧叶尖滚动？

2. 每颗液滴是否分别沿不同叶脉滚动？

3. 滚动是否持续 5 秒？


## 158 — `synthetic_process_053_E2A`

**原始英文指令：** Starting at 29.0 seconds, delay detachment of the large droplet from the leaf tip until 36.0 seconds.

**中文翻译：** 从第 29.0 秒开始，将大液滴脱离叶尖的时间延迟到第 36.0 秒。

**状态：** 接受

**原子化判定句：**

1. 大液滴是否在延迟 7 秒后脱离叶尖？


## 159 — `synthetic_process_053_E2B`

**原始英文指令：** Starting at 20.5 seconds, advance the second droplet until it reaches and hangs beneath the leaf tip by 25.0 seconds.

**中文翻译：** 从第 20.5 秒开始，推进第二颗液滴的运动，使其在第 25.0 秒前到达叶尖并悬挂在叶尖下方。

**状态：** 接受

**原子化判定句：**

1. 第二颗液滴是否向前移动？

2. 第二颗液滴是否在 4.5 秒内到达叶尖？

3. 第二颗液滴是否在同一段 4.5 秒内悬挂在叶尖下方？


## 160 — `synthetic_process_054_E1`

**原始英文指令：** At 14.0 seconds, reorient the transparent tied membrane so its long axis sits 15 degrees clockwise from horizontal.

**中文翻译：** 在第 14.0 秒，重新调整透明扎结膜的方向，使其长轴相对水平方向顺时针偏转十五度。

**状态：** 接受

**原子化判定句：**

1. 透明扎结膜是否被重新调整方向，使其长轴相对水平方向顺时针偏转 15 度？


## 161 — `synthetic_process_054_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the expanded transparent membrane taut and evenly tensioned over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内让膨胀的透明膜变得绷紧且张力均匀。

**状态：** 接受

**原子化判定句：**

1. 膨胀的透明膜是否在 2 秒内变得绷紧？

2. 透明膜是否在同一段 2 秒内变得张力均匀？


## 162 — `synthetic_process_054_E2B`

**原始英文指令：** Starting at 28.5 seconds, render only the transparent membrane as frosted translucent latex with soft pearlescent highlights over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内仅将透明膜呈现为带磨砂质感的半透明乳胶，并带有柔和的珠光高光。

**状态：** 接受

**原子化判定句：**

1. 是否仅有透明膜在 2 秒内呈现为带磨砂质感的半透明乳胶？

2. 透明膜上是否在同一段 2 秒内出现柔和的珠光高光？


## 163 — `synthetic_process_055_E1`

**原始英文指令：** Starting at 14.0 seconds, make the pale liquid inside the star mold gel-like with a soft matte surface over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内让星形模具内的浅色液体变为凝胶状，并形成柔和的哑光表面。

**状态：** 接受

**原子化判定句：**

1. 星形模具内的浅色液体是否在 2 秒内变为凝胶状？

2. 液体是否在同一段 2 秒内形成柔和的哑光表面？


## 164 — `synthetic_process_055_E2A`

**原始英文指令：** At 29.0 seconds, move the entire star-shaped container into the open upper-left region of the frame.

**中文翻译：** 在第 29.0 秒，将整个星形容器移至画面左上方的空旷区域。

**状态：** 接受

**原子化判定句：**

1. 整个星形容器是否被移至画面左上方的空旷区域？


## 165 — `synthetic_process_055_E2B`

**原始英文指令：** Starting at 28.5 seconds, accelerate inward whitening until the clear star-shaped center shrinks to a pinprick by 34.0 seconds.

**中文翻译：** 从第 28.5 秒开始，加快由外向内的变白过程，使透明的星形中心在第 34.0 秒前缩小至针尖大小。

**状态：** 接受

**原子化判定句：**

1. 由外向内的变白过程是否加快？

2. 透明的星形中心是否在 5.5 秒内缩小至针尖大小？


## 166 — `synthetic_process_056_E1`

**原始英文指令：** Starting at 14.0 seconds, make the descending transparent sheet rigid with a perfectly straight front edge over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内让正在下降的透明薄片变得坚硬，并使其前缘完全笔直。

**状态：** 接受

**原子化判定句：**

1. 正在下降的透明薄片是否在 2 秒内变得坚硬？

2. 其前缘是否在同一段 2 秒内变得完全笔直？


## 167 — `synthetic_process_056_E2A`

**原始英文指令：** Starting at 28.5 seconds, accelerate the transparent sheet's descent until it reaches its lowest visible position by 33.0 seconds.

**中文翻译：** 从第 28.5 秒开始，加快透明薄片下降，使其在第 33.0 秒前到达画面中的最低位置。

**状态：** 接受

**原子化判定句：**

1. 透明薄片的下降是否加快？

2. 透明薄片是否在 4.5 秒内到达画面中的最低位置？


## 168 — `synthetic_process_056_E2B`

**原始英文指令：** Starting at 28.5 seconds, advance the sheet until no red glow remains and it reaches its lowest visible position by 33.0 seconds.

**中文翻译：** 从第 28.5 秒开始，推进薄片的变化，使红色辉光在第 33.0 秒前完全消失，并使薄片到达画面中的最低位置。

**状态：** 接受

**原子化判定句：**

1. 薄片的变化是否得到推进？

2. 红色辉光是否在 4.5 秒内完全消失？

3. 薄片是否在同一段 4.5 秒内到达画面中的最低位置？


## 169 — `synthetic_process_057_E1`

**原始英文指令：** Starting at 14.0 seconds, advance surface settling until the rings flatten and only two small bubble points remain by 18.5 seconds.

**中文翻译：** 从第 14.0 秒开始，推进表面沉降，使环状结构在第 18.5 秒前变平，并仅剩两个小气泡点。

**状态：** 接受

**原子化判定句：**

1. 表面沉降是否得到推进？

2. 环状结构是否在 4.5 秒内变平？

3. 是否在同一段 4.5 秒内仅剩两个小气泡点？


## 170 — `synthetic_process_057_E2A`

**原始英文指令：** Starting at 32.0 seconds, make the transparent container tilt faster to the right for 3.5 seconds, carrying the thick slurry with it.

**中文翻译：** 从第 32.0 秒开始，让透明容器更快地向右倾斜三点五秒，并带动浓稠浆液随之移动。

**状态：** 接受

**原子化判定句：**

1. 透明容器是否更快地向右倾斜 3.5 秒？

2. 浓稠浆液是否在同一段 3.5 秒内随倾斜的容器一起移动？


## 171 — `synthetic_process_057_E2B`

**原始英文指令：** Starting at 28.5 seconds, make the two central surface bubbles complete one clockwise orbit around their shared midpoint over five seconds.

**中文翻译：** 从第 28.5 秒开始，让中央两个表面气泡在五秒内围绕它们的共同中点顺时针运行一周。

**状态：** 接受

**原子化判定句：**

1. 中央两个表面气泡是否围绕它们的共同中点顺时针运行？

2. 两个气泡是否恰好完成一周？

3. 这一周运行是否在 5 秒内完成？


## 172 — `synthetic_process_058_E1`

**原始英文指令：** At 14.0 seconds, move the square sample two centimeters forward to double its gap from the rear rubble.

**中文翻译：** 在第 14.0 秒，将方形样品向前移动两厘米，使其与后方碎石的间距增至两倍。

**状态：** 接受

**原子化判定句：**

1. 方形样品是否向前移动 2 厘米？

2. 方形样品与后方碎石的间距是否增至两倍？


## 173 — `synthetic_process_058_E2A`

**原始英文指令：** Starting at 29.0 seconds, render only the square sample surface as coarse stippled plaster over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内仅将方形样品表面呈现为粗糙点刻灰泥质感。

**状态：** 接受

**原子化判定句：**

1. 方形样品表面是否呈现为粗糙点刻灰泥质感？

2. 纹理变化是否仅限于方形样品表面？

3. 纹理变化是否在 2 秒内完成？


## 174 — `synthetic_process_058_E2B`

**原始英文指令：** Starting at 28.5 seconds, pause recession of the central dark patch for five seconds, then resume from the held boundary.

**中文翻译：** 从第 28.5 秒开始，让中央深色斑块的退缩暂停五秒，然后从保持的边界恢复退缩。

**状态：** 接受

**原子化判定句：**

1. 中央深色斑块的退缩是否暂停 5 秒？

2. 中央深色斑块是否在暂停 5 秒后从保持的边界恢复退缩？


## 175 — `synthetic_process_059_E1`

**原始英文指令：** Starting at 14.0 seconds, advance the sheet until only a narrow gray ring remains and all four corners rise by 19.0 seconds.

**中文翻译：** 从第 14.0 秒开始，推进薄片变化，使其在第 19.0 秒前仅剩一圈狭窄灰色环带，并让四个角全部翘起。

**状态：** 接受

**原子化判定句：**

1. 薄片的变化是否得到推进？

2. 是否在 5 秒内仅剩一圈狭窄灰色环带？

3. 四个角是否在同一段 5 秒内全部翘起？


## 176 — `synthetic_process_059_E2A`

**原始英文指令：** Starting at 29.0 seconds, transform the full sheet-on-rack scene into 1960s industrial film footage over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将整个网架上薄片的场景转换为 20 世纪 60 年代工业胶片影像。

**状态：** 接受

**原子化判定句：**

1. 整个网架上薄片的场景是否转换为 20 世纪 60 年代工业胶片影像？

2. 这一转换是否在 2 秒内完成？


## 177 — `synthetic_process_059_E2B`

**原始英文指令：** Starting at 28.5 seconds, make the pale sheet rigid and fully flat on the wire rack over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内让浅色薄片变得坚硬，并完全平铺在金属网架上。

**状态：** 接受

**原子化判定句：**

1. 浅色薄片是否在 2 秒内变得坚硬？

2. 浅色薄片是否在同一段 2 秒内完全平铺在金属网架上？


## 178 — `synthetic_process_060_E1`

**原始英文指令：** Starting at 14.0 seconds, change the advancing brown stain to deep blue over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内将正在扩展的棕色污渍变为深蓝色。

**状态：** 接受

**原子化判定句：**

1. 正在扩展的污渍是否从棕色变为深蓝色？

2. 颜色变化是否在 2 秒内完成？


## 179 — `synthetic_process_060_E2A`

**原始英文指令：** At 29.0 seconds, replace the pale right vertical wood border with a same-width brushed aluminum strip.

**中文翻译：** 在第 29.0 秒，将右侧浅色竖直木质边框替换为等宽的拉丝铝条。

**状态：** 接受

**原子化判定句：**

1. 右侧浅色竖直木质边框是否被替换为拉丝铝条？

2. 拉丝铝条是否与原木质边框等宽？


## 180 — `synthetic_process_060_E2B`

**原始英文指令：** Starting at 28.5 seconds, pause the stain front's rightward advance for five seconds, then resume from the held boundary.

**中文翻译：** 从第 28.5 秒开始，让污渍前沿向右推进的过程暂停五秒，然后从保持的边界恢复推进。

**状态：** 接受

**原子化判定句：**

1. 污渍前沿向右推进的过程是否暂停 5 秒？

2. 污渍前沿是否在暂停 5 秒后从保持的边界恢复向右推进？


## 181 — `synthetic_process_061_E1`

**原始英文指令：** Starting at 15.5 seconds, advance contraction until the front and right overhangs fit tightly around the support by 20.0 seconds.

**中文翻译：** 从第 15.5 秒开始，推进收缩过程，使前侧和右侧的悬垂部分在第 20.0 秒前紧密贴合支撑体。

**状态：** 接受

**原子化判定句：**

1. 收缩过程是否得到推进？

2. 前侧悬垂部分是否在 4.5 秒内紧密贴合支撑体？

3. 右侧悬垂部分是否在同一段 4.5 秒内紧密贴合支撑体？


## 182 — `synthetic_process_061_E2A`

**原始英文指令：** Starting at 27.0 seconds, transform the entire wrapped-support scene into a detailed monochrome graphite product-study drawing over two seconds.

**中文翻译：** 从第 27.0 秒开始，在两秒内将整个包裹支撑体的场景转换为细致的单色石墨产品研究素描。

**状态：** 接受

**原子化判定句：**

1. 整个包裹支撑体的场景是否转换为细致的单色石墨产品研究素描？

2. 这一转换是否在 2 秒内完成？


## 183 — `synthetic_process_061_E2B`

**原始英文指令：** At 29.5 seconds, move the wrapped support right until the silver nozzle aligns above the left third of its top surface.

**中文翻译：** 在第 29.5 秒，将被包裹的支撑体向右移动，直到银色喷嘴对准其顶面左侧三分之一区域的上方。

**状态：** 接受

**原子化判定句：**

1. 被包裹的支撑体是否向右移动？

2. 银色喷嘴最终是否对准支撑体顶面左侧三分之一区域的上方？


## 184 — `synthetic_process_062_E1`

**原始英文指令：** At 18.0 seconds, remove the narrow transparent film crescent outside the white center's lower-left edge.

**中文翻译：** 在第 18.0 秒，移除白色中心左下边缘外侧的狭窄透明薄膜月牙形区域。

**状态：** 接受

**原子化判定句：**

1. 白色中心左下边缘外侧的狭窄透明薄膜月牙形区域是否被移除？


## 185 — `synthetic_process_062_E2A`

**原始英文指令：** Starting at 28.0 seconds, change the remaining opaque white central patch to pale cyan over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内将剩余的不透明白色中央斑块变为浅青色。

**状态：** 接受

**原子化判定句：**

1. 剩余的不透明中央斑块是否从白色变为浅青色？

2. 颜色变化是否在 2 秒内完成？


## 186 — `synthetic_process_062_E2B`

**原始英文指令：** Starting at 32.5 seconds, smoothly zoom in until the small residual central patch fills the middle quarter of the frame.

**中文翻译：** 从第 32.5 秒开始，平滑拉近镜头，直到残留的小型中央斑块填满画面中间四分之一区域。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近，直至残留的小型中央斑块填满画面中间四分之一区域？

2. 拉近过程是否平滑？


## 187 — `synthetic_process_063_E1`

**原始英文指令：** Starting at 13.0 seconds, make the lower blue region a firm translucent gel with glossy sealed pores over two seconds.

**中文翻译：** 从第 13.0 秒开始，在两秒内将下方蓝色区域变为坚实的半透明凝胶，并使封闭的孔隙呈现光泽。

**状态：** 接受

**原子化判定句：**

1. 下方蓝色区域是否在 2 秒内变为坚实凝胶？

2. 该凝胶是否在同一段 2 秒内变为半透明？

3. 其封闭的孔隙是否在同一段 2 秒内呈现光泽？


## 188 — `synthetic_process_063_E2A`

**原始英文指令：** At 27.0 seconds, add one small dry white porous cube on the tray to the right of the main block.

**中文翻译：** 在第 27.0 秒，在主块体右侧的托盘上添加一个干燥的白色多孔小立方体。

**状态：** 接受

**原子化判定句：**

1. 托盘上是否添加了恰好一个干燥的白色多孔小立方体？

2. 该立方体是否位于主块体右侧？


## 189 — `synthetic_process_063_E2B`

**原始英文指令：** Starting at 27.5 seconds, make dark-blue liquid flow simultaneously from multiple visible pores across the main porous block for five seconds.

**中文翻译：** 从第 27.5 秒开始，让深蓝色液体同时从主多孔块体上的多个可见孔隙中流出五秒。

**状态：** 接受

**原子化判定句：**

1. 深蓝色液体是否从主多孔块体上的多个可见孔隙中流出？

2. 这些孔隙是否同时开始流出液体？

3. 液体流出是否持续 5 秒？


## 190 — `synthetic_process_064_E1`

**原始英文指令：** Starting at 10.5 seconds, accelerate the black strands until their tips contact the silver block's left face by 15.0 seconds.

**中文翻译：** 从第 10.5 秒开始，加快黑色丝束的运动，使其尖端在第 15.0 秒前接触银色块体的左侧面。

**状态：** 接受

**原子化判定句：**

1. 黑色丝束的运动是否加快？

2. 其尖端是否在 4.5 秒内接触银色块体的左侧面？


## 191 — `synthetic_process_064_E2A`

**原始英文指令：** Starting at 29.0 seconds, split the black wrapping layer into separate upper and lower bands over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将黑色包裹层分成彼此分离的上、下两条带。

**状态：** 接受

**原子化判定句：**

1. 黑色包裹层是否分成上、下两条带？

2. 两条带是否彼此分离？

3. 分裂过程是否在 2 秒内完成？


## 192 — `synthetic_process_064_E2B`

**原始英文指令：** Starting at 25.0 seconds, move the upper black strands clockwise over the block and the lower strands counterclockwise beneath it for five seconds.

**中文翻译：** 从第 25.0 秒开始，让上方黑色丝束在块体上方顺时针移动，同时让下方丝束在块体下方逆时针移动五秒。

**状态：** 接受

**原子化判定句：**

1. 上方黑色丝束是否在块体上方顺时针移动 5 秒？

2. 下方黑色丝束是否在同一段 5 秒内在块体下方逆时针移动？


## 193 — `synthetic_process_065_E1`

**原始英文指令：** Starting at 13.0 seconds, pause widening of the rounded silver bead for five seconds, then resume from the held outline.

**中文翻译：** 从第 13.0 秒开始，让圆润银色液珠的变宽过程暂停五秒，然后从保持的轮廓恢复变宽。

**状态：** 接受

**原子化判定句：**

1. 圆润银色液珠的变宽过程是否暂停 5 秒？

2. 圆润银色液珠是否在暂停 5 秒后从保持的轮廓恢复变宽？


## 194 — `synthetic_process_065_E2A`

**原始英文指令：** Starting at 28.5 seconds, accelerate spreading until the silver object's visible footprint reaches twice its current area by 34.0 seconds.

**中文翻译：** 从第 28.5 秒开始，加快铺展，使银色物体的可见占地面积在第 34.0 秒前达到当前面积的两倍。

**状态：** 接受

**原子化判定句：**

1. 铺展是否加快？

2. 银色物体的可见占地面积是否在 5.5 秒内达到编辑点时面积的两倍？


## 195 — `synthetic_process_065_E2B`

**原始英文指令：** At 27.5 seconds, add one smaller round silver droplet on the palm above and right of the main object.

**中文翻译：** 在第 27.5 秒，在手掌上主物体右上方添加一颗较小的圆形银色液滴。

**状态：** 接受

**原子化判定句：**

1. 手掌上是否添加了恰好一颗较小的圆形银色液滴？

2. 该液滴是否位于主物体的右上方？


## 196 — `synthetic_process_066_E1`

**原始英文指令：** Starting at 13.5 seconds, advance germination until the white root extends one seed-width to the right by 18.5 seconds.

**中文翻译：** 从第 13.5 秒开始，推进发芽过程，使白色根在第 18.5 秒前向右延伸一个种子宽度。

**状态：** 接受

**原子化判定句：**

1. 发芽过程是否得到推进？

2. 白色根是否在 5 秒内向右延伸一个种子宽度？


## 197 — `synthetic_process_066_E2A`

**原始英文指令：** Starting at 29.0 seconds, pause extension of the connected white root for five seconds, then resume from its held length.

**中文翻译：** 从第 29.0 秒开始，让相连白色根的延伸暂停五秒，然后从保持的长度恢复延伸。

**状态：** 接受

**原子化判定句：**

1. 相连白色根的延伸是否暂停 5 秒？

2. 相连白色根是否在暂停 5 秒后从保持的长度恢复延伸？


## 198 — `synthetic_process_066_E2B`

**原始英文指令：** Starting at 28.0 seconds, transform the entire seed-germination scene into faded 1970s botanical film footage over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内将整个种子发芽场景转换为褪色的 20 世纪 70 年代植物学胶片影像。

**状态：** 接受

**原子化判定句：**

1. 整个种子发芽场景是否转换为褪色的 20 世纪 70 年代植物学胶片影像？

2. 这一转换是否在 2 秒内完成？


## 199 — `synthetic_process_067_E1`

**原始英文指令：** At 14.5 seconds, add one smaller pale mushroom with a short stem on the empty upper-right wood area.

**中文翻译：** 在第 14.5 秒，在右上方空置的木材区域添加一株颜色较浅、菌柄较短且体型较小的蘑菇。

**状态：** 接受

**原子化判定句：**

1. 是否添加了恰好一株颜色较浅、菌柄较短且体型较小的蘑菇？

2. 该蘑菇是否位于右上方空置的木材区域？


## 200 — `synthetic_process_067_E2A`

**原始英文指令：** Starting at 28.0 seconds, render only the supporting wood cross-section as a charred mosaic texture over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内仅将支撑木材的横截面呈现为炭化马赛克纹理。

**状态：** 接受

**原子化判定句：**

1. 支撑木材的横截面是否呈现为炭化马赛克纹理？

2. 纹理变化是否仅限于木材横截面？

3. 纹理变化是否在 2 秒内完成？


## 201 — `synthetic_process_067_E2B`

**原始英文指令：** At 29.0 seconds, move the original larger mushroom three centimeters toward the lower-left open wood area.

**中文翻译：** 在第 29.0 秒，将原有的较大蘑菇朝左下方空置的木材区域移动三厘米。

**状态：** 接受

**原子化判定句：**

1. 原有的较大蘑菇是否朝左下方空置的木材区域移动？

2. 移动距离是否为 3 厘米？


## 202 — `synthetic_process_068_E1`

**原始英文指令：** Starting at 15.0 seconds, rotate the four foreground fruits a quarter-turn in alternating directions over five seconds.

**中文翻译：** 从第 15.0 秒开始，在五秒内让前景中的四个果实以交替方向各旋转四分之一圈。

**状态：** 接受

**原子化判定句：**

1. 前景中的四个果实是否全部旋转？

2. 每个果实是否各旋转四分之一圈？

3. 相邻果实的旋转方向是否交替？

4. 这些旋转是否在 5 秒内完成？


## 203 — `synthetic_process_068_E2A`

**原始英文指令：** Starting at 31.0 seconds, change the front-left foreground fruit to deep purple over two seconds.

**中文翻译：** 从第 31.0 秒开始，在两秒内将前景左前方的果实变为深紫色。

**状态：** 接受

**原子化判定句：**

1. 前景左前方的果实是否变为深紫色？

2. 颜色变化是否在 2 秒内完成？


## 204 — `synthetic_process_068_E2B`

**原始英文指令：** Starting at 29.5 seconds, render only the visible fruit surfaces as glazed ceramic with fine painted striations over two seconds.

**中文翻译：** 从第 29.5 秒开始，在两秒内仅将可见的果实表面呈现为带釉陶瓷，并带有精细的彩绘条纹。

**状态：** 接受

**原子化判定句：**

1. 是否仅有可见的果实表面在 2 秒内呈现为带釉陶瓷？

2. 这些表面上是否在同一段 2 秒内出现精细的彩绘条纹？


## 205 — `synthetic_process_069_E1`

**原始英文指令：** Starting at 13.0 seconds, render only the main leaf as pressed handmade paper with embossed veins over two seconds.

**中文翻译：** 从第 13.0 秒开始，在两秒内仅将主叶片呈现为压制手工纸，并带有浮雕叶脉。

**状态：** 接受

**原子化判定句：**

1. 是否仅有主叶片在 2 秒内呈现为压制手工纸？

2. 主叶片上是否在同一段 2 秒内出现浮雕叶脉？


## 206 — `synthetic_process_069_E2A`

**原始英文指令：** Starting at 30.0 seconds, make the brown-edged leaf visibly brittle with sharper curls and shallow creases over two seconds.

**中文翻译：** 从第 30.0 秒开始，在两秒内让带棕色边缘的叶片变得明显脆化，并形成更尖锐的卷曲和浅折痕。

**状态：** 接受

**原子化判定句：**

1. 带棕色边缘的叶片是否在 2 秒内变得明显脆化？

2. 其卷曲是否在同一段 2 秒内变得更尖锐？

3. 叶片上是否在同一段 2 秒内出现浅折痕？


## 207 — `synthetic_process_069_E2B`

**原始英文指令：** At 27.5 seconds, add one small dry brown leaf fragment on the empty background above and right of the leaf.

**中文翻译：** 在第 27.5 秒，在叶片右上方的空白背景处添加一小片干燥的棕色叶片碎片。

**状态：** 接受

**原子化判定句：**

1. 是否添加了恰好一小片干燥的棕色叶片碎片？

2. 该碎片是否位于叶片右上方的空白背景处？


## 208 — `synthetic_process_070_E1`

**原始英文指令：** At 16.0 seconds, add one small round pale dough-like ball on the bowl bottom to the right of the main mound.

**中文翻译：** 在第 16.0 秒，在主面团堆右侧的碗底添加一个浅色、圆形且呈面团质感的小球。

**状态：** 接受

**原子化判定句：**

1. 碗底是否添加了恰好一个浅色、圆形且呈面团质感的小球？

2. 该小球是否位于主面团堆右侧？


## 209 — `synthetic_process_070_E2A`

**原始英文指令：** Starting at 31.0 seconds, move the camera right along a short arc around the transparent bowl for five seconds.

**中文翻译：** 从第 31.0 秒开始，让镜头围绕透明碗沿一小段弧线向右移动五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否围绕透明碗沿一小段弧线向右移动？

2. 这一移动是否持续 5 秒？


## 210 — `synthetic_process_070_E2B`

**原始英文指令：** At 30.0 seconds, move the original large mound into the left half of the transparent bowl.

**中文翻译：** 在第 30.0 秒，将原有的大面团堆移至透明碗的左半部。

**状态：** 接受

**原子化判定句：**

1. 原有的大面团堆是否被移至透明碗的左半部？


## 211 — `synthetic_process_071_E1`

**原始英文指令：** Starting at 14.0 seconds, make three large egg-white bubbles travel clockwise around the yolk for five seconds.

**中文翻译：** 从第 14.0 秒开始，让三个大蛋清气泡围绕蛋黄顺时针移动五秒。

**状态：** 接受

**原子化判定句：**

1. 是否恰好有三个大蛋清气泡围绕蛋黄移动？

2. 气泡是否顺时针移动？

3. 这一移动是否持续 5 秒？


## 212 — `synthetic_process_071_E2A`

**原始英文指令：** Starting at 26.0 seconds, advance yolk coagulation until its visible surface becomes opaque white by 31.0 seconds.

**中文翻译：** 从第 26.0 秒开始，推进蛋黄凝固，使其可见表面在第 31.0 秒前变为不透明白色。

**状态：** 接受

**原子化判定句：**

1. 蛋黄凝固是否得到推进？

2. 蛋黄的可见表面是否在 5 秒内变为不透明白色？


## 213 — `synthetic_process_071_E2B`

**原始英文指令：** Starting at 29.0 seconds, accelerate yolk paling until its visible surface becomes off-white by 34.0 seconds.

**中文翻译：** 从第 29.0 秒开始，加快蛋黄变浅，使其可见表面在第 34.0 秒前变为灰白色。

**状态：** 接受

**原子化判定句：**

1. 蛋黄变浅是否加快？

2. 蛋黄的可见表面是否在 5 秒内变为灰白色？


## 214 — `synthetic_process_072_E1`

**原始英文指令：** Starting at 15.5 seconds, bend three front pasta strands outward in alternating arcs and return them toward the bundle over five seconds.

**中文翻译：** 从第 15.5 秒开始，让前方三根意面以交替弧线向外弯曲，并在五秒内回到面束方向。

**状态：** 接受

**原子化判定句：**

1. 前方三根意面是否在 5 秒内以交替弧线向外弯曲？

2. 这三根意面是否在同一段 5 秒内回到面束方向？


## 215 — `synthetic_process_072_E2A`

**原始英文指令：** Starting at 29.5 seconds, advance submergence until the exposed pasta ends are half their current length by 34.0 seconds.

**中文翻译：** 从第 29.5 秒开始，推进意面浸没，使露出的意面末端在第 34.0 秒前缩短至当前长度的一半。

**状态：** 接受

**原子化判定句：**

1. 意面浸没是否得到推进？

2. 露出的意面末端是否在 4.5 秒内缩短至编辑点时长度的一半？


## 216 — `synthetic_process_072_E2B`

**原始英文指令：** Starting at 30.0 seconds, delay broad sideways bending of the pasta across the water surface until 37.0 seconds.

**中文翻译：** 从第 30.0 秒开始，将意面在水面上大幅横向弯曲的时间延迟到第 37.0 秒。

**状态：** 接受

**原子化判定句：**

1. 意面是否在延迟 7 秒后于水面上大幅横向弯曲？


## 217 — `synthetic_process_073_E1`

**原始英文指令：** At 12.5 seconds, add one small green bay leaf floating flat on the red liquid near the pot's upper-right side.

**中文翻译：** 在第 12.5 秒，在锅内右上方附近的红色液体表面添加一片平浮的小绿月桂叶。

**状态：** 接受

**原子化判定句：**

1. 是否添加了恰好一片小绿月桂叶？

2. 该月桂叶是否平浮在锅内右上方附近的红色液体表面？


## 218 — `synthetic_process_073_E2A`

**原始英文指令：** Starting at 29.5 seconds, advance the process until a second distinct red-brown residue band forms above the first by 34.0 seconds.

**中文翻译：** 从第 29.5 秒开始，推进这一过程，使第二条清晰的红棕色残留带在第 34.0 秒前形成于第一条上方。

**状态：** 接受

**原子化判定句：**

1. 这一过程是否得到推进？

2. 第二条清晰的红棕色残留带是否在 4.5 秒内形成于第一条上方？


## 219 — `synthetic_process_073_E2B`

**原始英文指令：** Starting at 27.0 seconds, accelerate liquid-level decline until the gap below the wall residue band doubles by 33.5 seconds.

**中文翻译：** 从第 27.0 秒开始，加快液面下降，使壁面残留带下方的间距在第 33.5 秒前增至两倍。

**状态：** 接受

**原子化判定句：**

1. 液面下降是否加快？

2. 壁面残留带下方的间距是否在 6.5 秒内增至编辑点时的两倍？


## 220 — `synthetic_process_074_E1`

**原始英文指令：** At 13.5 seconds, remove the pale cheese patch nearest the pizza's front-left crust edge.

**中文翻译：** 在第 13.5 秒，移除最靠近披萨左前方饼边的浅色奶酪斑块。

**状态：** 接受

**原子化判定句：**

1. 最靠近披萨左前方饼边的浅色奶酪斑块是否被移除？


## 221 — `synthetic_process_074_E2A`

**原始英文指令：** Starting at 28.0 seconds, delay the appearance of new brown spots on the melted cheese until 34.0 seconds.

**中文翻译：** 从第 28.0 秒开始，将融化奶酪上出现新棕色斑点的时间延迟到第 34.0 秒。

**状态：** 接受

**原子化判定句：**

1. 融化奶酪上是否在延迟 6 秒后出现新的棕色斑点？


## 222 — `synthetic_process_074_E2B`

**原始英文指令：** Starting at 26.0 seconds, pause pizza-crust expansion and visible bubble enlargement for five seconds, then resume from the held shapes.

**中文翻译：** 从第 26.0 秒开始，让披萨饼边扩张和可见气泡变大暂停五秒，然后从保持的形状恢复。

**状态：** 接受

**原子化判定句：**

1. 披萨饼边扩张是否暂停 5 秒？

2. 可见气泡变大是否在同一段 5 秒内暂停？

3. 饼边扩张和气泡变大是否在暂停 5 秒后从各自保持的形状恢复？


## 223 — `synthetic_process_075_E1`

**原始英文指令：** Starting at 18.5 seconds, change the rising batter surface to dark cocoa brown over 1.5 seconds.

**中文翻译：** 从第 18.5 秒开始，在一点五秒内将正在上升的面糊表面变为深可可棕色。

**状态：** 接受

**原子化判定句：**

1. 正在上升的面糊表面是否变为深可可棕色？

2. 颜色变化是否在 1.5 秒内完成？


## 224 — `synthetic_process_075_E2A`

**原始英文指令：** Starting at 30.5 seconds, advance the batter until the first forked surface crack becomes clearly visible by 34.5 seconds.

**中文翻译：** 从第 30.5 秒开始，推进面糊变化，使第一道分叉的表面裂纹在第 34.5 秒前清晰可见。

**状态：** 接受

**原子化判定句：**

1. 面糊变化是否得到推进？

2. 第一道分叉的表面裂纹是否在 4 秒内变得清晰可见？


## 225 — `synthetic_process_075_E2B`

**原始英文指令：** Starting at 33.0 seconds, delay the first visible surface crack for ten seconds, allowing cracking to begin only at 43.0 seconds.

**中文翻译：** 从第 33.0 秒开始，将第一道可见表面裂纹延迟十秒，使开裂仅在第 43.0 秒开始。

**状态：** 接受

**原子化判定句：**

1. 第一道可见表面裂纹是否在延迟 10 秒后出现？


## 226 — `synthetic_process_076_E1`

**原始英文指令：** Starting at 15.0 seconds, advance unfurling until five upper leaflets are individually separated by 19.5 seconds.

**中文翻译：** 从第 15.0 秒开始，推进叶片展开，使上方五片小叶在第 19.5 秒前彼此分离。

**状态：** 接受

**原子化判定句：**

1. 叶片展开是否得到推进？

2. 上方五片小叶是否在 4.5 秒内彼此分离？


## 227 — `synthetic_process_076_E2A`

**原始英文指令：** At 31.0 seconds, move the lower curled bud right until its tip is one bud-width from the main stem.

**中文翻译：** 在第 31.0 秒，将下方卷曲的芽向右移动，直到其尖端与主茎相距一个芽的宽度。

**状态：** 接受

**原子化判定句：**

1. 下方卷曲的芽是否向右移动？

2. 其尖端最终是否与主茎相距一个芽的宽度？


## 228 — `synthetic_process_076_E2B`

**原始英文指令：** Starting at 29.5 seconds, move the camera upward along the main stem while tracking the unfurling tip for five seconds.

**中文翻译：** 从第 29.5 秒开始，让镜头沿主茎向上移动五秒，同时跟踪正在展开的尖端。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿主茎向上移动 5 秒？

2. 镜头是否在同一段 5 秒内跟踪正在展开的尖端？


## 229 — `synthetic_process_077_E1`

**原始英文指令：** At 14.0 seconds, replace the right-rear spiny cactus column with a smooth dark basalt column of the same size.

**中文翻译：** 在第 14.0 秒，将右后方带刺的仙人掌柱替换为尺寸相同的光滑深色玄武岩柱。

**状态：** 接受

**原子化判定句：**

1. 右后方带刺的仙人掌柱是否被替换为光滑的深色玄武岩柱？

2. 玄武岩柱是否与原仙人掌柱尺寸相同？


## 230 — `synthetic_process_077_E2A`

**原始英文指令：** Starting at 30.5 seconds, render only the main flower petals as translucent rice paper with fine visible fibers over two seconds.

**中文翻译：** 从第 30.5 秒开始，在两秒内仅将主花朵的花瓣呈现为半透明宣纸，并带有清晰可见的细纤维。

**状态：** 接受

**原子化判定句：**

1. 是否仅有主花朵的花瓣在 2 秒内呈现为半透明宣纸？

2. 花瓣上是否在同一段 2 秒内出现清晰可见的细纤维？


## 231 — `synthetic_process_077_E2B`

**原始英文指令：** Starting at 28.5 seconds, make the opening flower petals rigid with crisp planar facets over two seconds.

**中文翻译：** 从第 28.5 秒开始，在两秒内让正在开放的花瓣变得坚硬，并形成轮廓分明的平面切面。

**状态：** 接受

**原子化判定句：**

1. 正在开放的花瓣是否在 2 秒内变得坚硬？

2. 花瓣上是否在同一段 2 秒内形成轮廓分明的平面切面？


## 232 — `synthetic_process_078_E1`

**原始英文指令：** Starting at 13.0 seconds, transform the full underwater root-growth scene into a subdued 1990s botanical documentary style over two seconds.

**中文翻译：** 从第 13.0 秒开始，在两秒内将整个水下根系生长场景转换为低调的 20 世纪 90 年代植物纪录片风格。

**状态：** 接受

**原子化判定句：**

1. 整个水下根系生长场景是否转换为低调的 20 世纪 90 年代植物纪录片风格？

2. 这一转换是否在 2 秒内完成？


## 233 — `synthetic_process_078_E2A`

**原始英文指令：** Starting at 30.0 seconds, make three visible lateral roots sway left and right in alternating sequence for five seconds.

**中文翻译：** 从第 30.0 秒开始，让三条可见侧根以交替顺序左右摆动五秒。

**状态：** 接受

**原子化判定句：**

1. 是否恰好有三条可见侧根左右摆动？

2. 三条侧根是否以交替顺序摆动？

3. 摆动是否持续 5 秒？


## 234 — `synthetic_process_078_E2B`

**原始英文指令：** Starting at 27.5 seconds, accelerate lateral-root extension until the three longest branches reach one-and-a-half times their current length by 34.0 seconds.

**中文翻译：** 从第 27.5 秒开始，加快侧根延伸，使最长的三条分支在第 34.0 秒前达到当前长度的一点五倍。

**状态：** 接受

**原子化判定句：**

1. 侧根延伸是否加快？

2. 最长的三条分支是否在 6.5 秒内达到编辑点时长度的 1.5 倍？


## 235 — `synthetic_process_079_E1`

**原始英文指令：** Starting at 14.5 seconds, change the visible moss-like patches to saturated blue-green over two seconds.

**中文翻译：** 从第 14.5 秒开始，在两秒内将可见的苔藓状斑块变为高饱和蓝绿色。

**状态：** 接受

**原子化判定句：**

1. 可见的苔藓状斑块是否变为高饱和蓝绿色？

2. 颜色变化是否在 2 秒内完成？


## 236 — `synthetic_process_079_E2A`

**原始英文指令：** Starting at 31.5 seconds, smoothly zoom in until the connected moss-like network fills the middle two-thirds of the frame.

**中文翻译：** 从第 31.5 秒开始，平滑拉近镜头，直到相连的苔藓状网络填满画面中间三分之二区域。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近，直至相连的苔藓状网络填满画面中间三分之二区域？

2. 拉近过程是否平滑？


## 237 — `synthetic_process_079_E2B`

**原始英文指令：** At 29.5 seconds, move the isolated upper-right moss-like patch into the open lower-right area of the stone surface.

**中文翻译：** 在第 29.5 秒，将右上方孤立的苔藓状斑块移至石面右下方的空旷区域。

**状态：** 接受

**原子化判定句：**

1. 右上方孤立的苔藓状斑块是否被移至石面右下方的空旷区域？


## 238 — `synthetic_process_080_E1`

**原始英文指令：** Starting at 15.5 seconds, render only the exposed apple flesh as layered stippled watercolor over two seconds.

**中文翻译：** 从第 15.5 秒开始，在两秒内仅将裸露的苹果果肉呈现为分层点彩水彩效果。

**状态：** 接受

**原子化判定句：**

1. 裸露的苹果果肉是否呈现为分层点彩水彩效果？

2. 风格变化是否仅限于裸露的苹果果肉？

3. 风格变化是否在 2 秒内完成？


## 239 — `synthetic_process_080_E2A`

**原始英文指令：** Starting at 31.0 seconds, make the browning apple flesh dry and leathery with shallow radial wrinkles over two seconds.

**中文翻译：** 从第 31.0 秒开始，在两秒内让正在褐变的苹果果肉变得干燥且呈皮革质感，并形成浅的放射状皱纹。

**状态：** 接受

**原子化判定句：**

1. 正在褐变的苹果果肉是否在 2 秒内变得干燥？

2. 苹果果肉是否在同一段 2 秒内呈现皮革质感？

3. 是否在同一段 2 秒内形成浅的放射状皱纹？


## 240 — `synthetic_process_080_E2B`

**原始英文指令：** At 30.0 seconds, remove the single dark seed from the apple's central cavity.

**中文翻译：** 在第 30.0 秒，移除苹果中央凹槽中的唯一一颗深色种子。

**状态：** 接受

**原子化判定句：**

1. 苹果中央凹槽中的唯一一颗深色种子是否被移除？


## 241 — `synthetic_process_081_E1`

**原始英文指令：** Starting at 13.5 seconds, accelerate shell opening until the hatchling's face extends beyond the front rim by 19.5 seconds.

**中文翻译：** 从第 13.5 秒开始，加快蛋壳打开，使幼鸟的脸在第 19.5 秒前伸出前侧边缘。

**状态：** 接受

**原子化判定句：**

1. 蛋壳打开是否加快？

2. 幼鸟的脸是否在 6 秒内伸出前侧边缘？


## 242 — `synthetic_process_081_E2A`

**原始英文指令：** Starting at 27.5 seconds, make the first left-front shell fragment begin detaching at 30.5 seconds and settle by 32.5 seconds.

**中文翻译：** 从第 27.5 秒开始，让左前方第一块蛋壳碎片在第 30.5 秒开始脱离，并在第 32.5 秒前落稳。

**状态：** 接受

**原子化判定句：**

1. 左前方第一块蛋壳碎片是否在 3 秒后开始脱离？

2. 该蛋壳碎片是否在 5 秒内落稳？


## 243 — `synthetic_process_081_E2B`

**原始英文指令：** At 28.0 seconds, replace the green moss patch at the nest's left front with a small cluster of pale down feathers.

**中文翻译：** 在第 28.0 秒，将巢穴左前方的绿色苔藓斑块替换为一小簇浅色绒羽。

**状态：** 接受

**原子化判定句：**

1. 巢穴左前方的绿色苔藓斑块是否被替换为一小簇浅色绒羽？


## 244 — `synthetic_process_082_E1`

**原始英文指令：** Starting at 14.0 seconds, accelerate limb development until both forelimbs are fully visible and braced on the rock by 20.0 seconds.

**中文翻译：** 从第 14.0 秒开始，加快肢体发育，使两条前肢在第 20.0 秒前完全可见并支撑在岩石上。

**状态：** 接受

**原子化判定句：**

1. 肢体发育是否加快？

2. 两条前肢是否在 6 秒内变得完全可见？

3. 两条前肢是否在同一段 6 秒内支撑在岩石上？


## 245 — `synthetic_process_082_E2A`

**原始英文指令：** Starting at 27.0 seconds, pause the juvenile's visible tail shortening for five seconds, then resume from the held length.

**中文翻译：** 从第 27.0 秒开始，让幼体尾巴可见的缩短过程暂停五秒，然后从保持的长度恢复缩短。

**状态：** 接受

**原子化判定句：**

1. 幼体尾巴可见的缩短过程是否暂停 5 秒？

2. 尾巴是否在暂停 5 秒后从保持的长度恢复缩短？


## 246 — `synthetic_process_082_E2B`

**原始英文指令：** Starting at 28.0 seconds, smoothly zoom out until the full juvenile, remaining tail, and supporting rock fill the middle half of the frame.

**中文翻译：** 从第 28.0 秒开始，平滑拉远镜头，直到完整幼体、剩余尾巴和支撑岩石填满画面中间一半区域。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉远，直至完整幼体、剩余尾巴和支撑岩石填满画面中间一半区域？

2. 拉远过程是否平滑？


## 247 — `synthetic_process_083_E1`

**原始英文指令：** Starting at 13.0 seconds, make the five largest surface clusters drift clockwise around the vessel center for five seconds.

**中文翻译：** 从第 13.0 秒开始，让表面最大的五个团簇围绕容器中心顺时针漂移五秒。

**状态：** 接受

**原子化判定句：**

1. 是否恰好由表面最大的五个团簇围绕容器中心漂移？

2. 这些团簇是否顺时针漂移？

3. 漂移是否持续 5 秒？


## 248 — `synthetic_process_083_E2A`

**原始英文指令：** Starting at 27.0 seconds, pause further aggregation of the pale clusters for five seconds, then resume from their held boundaries.

**中文翻译：** 从第 27.0 秒开始，让浅色团簇的进一步聚集暂停五秒，然后从保持的边界恢复聚集。

**状态：** 接受

**原子化判定句：**

1. 浅色团簇的进一步聚集是否暂停 5 秒？

2. 浅色团簇是否在暂停 5 秒后从保持的边界恢复聚集？


## 249 — `synthetic_process_083_E2B`

**原始英文指令：** Starting at 27.5 seconds, accelerate cluster coalescence until the three largest surface clusters double their visible area by 34.5 seconds.

**中文翻译：** 从第 27.5 秒开始，加快团簇合并，使表面最大的三个团簇在第 34.5 秒前将可见面积扩大至两倍。

**状态：** 接受

**原子化判定句：**

1. 团簇合并是否加快？

2. 表面最大的三个团簇是否在 7 秒内达到编辑点时可见面积的两倍？


## 250 — `synthetic_process_084_E1`

**原始英文指令：** Starting at 14.5 seconds, make the upper visible rice grains rigid and glasslike with crisp outlines over two seconds.

**中文翻译：** 从第 14.5 秒开始，在两秒内让上方可见的米粒变得坚硬且呈玻璃质感，并具有清晰轮廓。

**状态：** 接受

**原子化判定句：**

1. 上方可见的米粒是否在 2 秒内变得坚硬？

2. 这些米粒是否在同一段 2 秒内呈现玻璃质感？

3. 这些米粒是否在同一段 2 秒内形成清晰轮廓？


## 251 — `synthetic_process_084_E2A`

**原始英文指令：** Starting at 28.0 seconds, make three visible edge bubbles bob up and down in alternating sequence for five seconds.

**中文翻译：** 从第 28.0 秒开始，让边缘处三个可见气泡以交替顺序上下浮动五秒。

**状态：** 接受

**原子化判定句：**

1. 边缘处是否恰好有三个可见气泡上下浮动？

2. 三个气泡是否以交替顺序浮动？

3. 上下浮动是否持续 5 秒？


## 252 — `synthetic_process_084_E2B`

**原始英文指令：** Starting at 29.0 seconds, transform the entire rice-soaking scene into a graphite-and-watercolor illustration over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将整个泡米场景转换为石墨与水彩结合的插画。

**状态：** 接受

**原子化判定句：**

1. 整个泡米场景是否转换为石墨与水彩结合的插画？

2. 这一转换是否在 2 秒内完成？


## 253 — `synthetic_process_085_E1`

**原始英文指令：** Starting at 13.0 seconds, accelerate foam growth until the white layer reaches half the visible bowl height by 19.5 seconds.

**中文翻译：** 从第 13.0 秒开始，加快泡沫生长，使白色泡沫层在第 19.5 秒前达到碗可见高度的一半。

**状态：** 接受

**原子化判定句：**

1. 泡沫生长是否加快？

2. 白色泡沫层是否在 6.5 秒内达到碗可见高度的一半？


## 254 — `synthetic_process_085_E2A`

**原始英文指令：** Starting at 27.0 seconds, advance the foam until broad whisk tracks remain visible for at least two seconds by 32.5 seconds.

**中文翻译：** 从第 27.0 秒开始，推进泡沫变化，使宽阔的打蛋器轨迹在第 32.5 秒前变得可见并至少保持两秒。

**状态：** 接受

**原子化判定句：**

1. 泡沫变化是否得到推进？

2. 宽阔的打蛋器轨迹是否在 5.5 秒内变得可见，并至少保持可见 2 秒？


## 255 — `synthetic_process_085_E2B`

**原始英文指令：** Starting at 27.5 seconds, make two broad foam waves travel clockwise around the whisk over five seconds.

**中文翻译：** 从第 27.5 秒开始，让两道宽阔泡沫波在五秒内围绕打蛋器顺时针传播。

**状态：** 接受

**原子化判定句：**

1. 是否恰好出现两道宽阔泡沫波？

2. 泡沫波是否围绕打蛋器顺时针传播？

3. 传播是否在 5 秒内完成？


## 256 — `synthetic_process_086_E1`

**原始英文指令：** At 13.5 seconds, move the largest central onion ring left until its edge is one ring-width from the nearer pan rivet.

**中文翻译：** 在第 13.5 秒，将中央最大的洋葱圈向左移动，直到其边缘与较近的锅铆钉相距一个洋葱圈宽度。

**状态：** 接受

**原子化判定句：**

1. 中央最大的洋葱圈是否向左移动？

2. 其边缘最终是否与较近的锅铆钉相距一个洋葱圈宽度？


## 257 — `synthetic_process_086_E2A`

**原始英文指令：** Starting at 27.5 seconds, make three foreground onion rings rotate in alternating directions for five seconds without overlapping.

**中文翻译：** 从第 27.5 秒开始，让前景中的三个洋葱圈以交替方向旋转五秒，且彼此不重叠。

**状态：** 接受

**原子化判定句：**

1. 前景中的三个洋葱圈是否以交替方向旋转 5 秒？

2. 这三个洋葱圈是否在同一段 5 秒内保持彼此不重叠？


## 258 — `synthetic_process_086_E2B`

**原始英文指令：** Starting at 28.0 seconds, make the visible onion rings crisp and brittle with lifted curled edges over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内让可见的洋葱圈变得酥脆且易碎，并形成翘起卷曲的边缘。

**状态：** 接受

**原子化判定句：**

1. 可见的洋葱圈是否在 2 秒内变得酥脆？

2. 这些洋葱圈是否在同一段 2 秒内变得易碎？

3. 其边缘是否在同一段 2 秒内变得翘起并卷曲？


## 259 — `synthetic_process_087_E1`

**原始英文指令：** Starting at 18.5 seconds, make the worker move the metal trowel through three left-to-right spreading passes over five seconds.

**中文翻译：** 从第 18.5 秒开始，让工人在五秒内使用金属抹子完成三次从左向右的铺抹动作。

**状态：** 接受

**原子化判定句：**

1. 工人是否使用金属抹子从左向右进行铺抹？

2. 工人是否恰好完成三次铺抹？

3. 三次铺抹是否在 5 秒内完成？


## 260 — `synthetic_process_087_E2A`

**原始英文指令：** Starting at 28.0 seconds, reorder construction so the worker builds one higher right-side row before placing the current row's leftmost brick.

**中文翻译：** 从第 28.0 秒开始，调整施工顺序，使工人在放置当前这一排最左侧砖块之前，先砌好右侧更高的一排。

**状态：** 接受

**原子化判定句：**

1. 工人是否在右侧砌好一排更高的砖？

2. 这排更高的砖是否在当前这一排最左侧砖块放置前完成？


## 261 — `synthetic_process_087_E2B`

**原始英文指令：** Starting at 33.5 seconds, accelerate mortar spreading until a level strip covers three adjacent top bricks by 38.0 seconds.

**中文翻译：** 从第 33.5 秒开始，加快砂浆铺抹，使一条平整砂浆带在第 38.0 秒前覆盖顶部相邻的三块砖。

**状态：** 接受

**原子化判定句：**

1. 砂浆铺抹是否加快？

2. 一条平整砂浆带是否在 4.5 秒内覆盖顶部相邻的三块砖？


## 262 — `synthetic_process_088_E1`

**原始英文指令：** Starting at 14.0 seconds, render only the gray tabletop around the puzzle as dark cork with fine pores over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内仅将拼图周围的灰色桌面呈现为带细小孔隙的深色软木。

**状态：** 接受

**原子化判定句：**

1. 是否仅有拼图周围的灰色桌面在 2 秒内呈现为深色软木？

2. 深色软木表面是否在同一段 2 秒内出现细小孔隙？


## 263 — `synthetic_process_088_E2A`

**原始英文指令：** At 28.0 seconds, replace the loose blue puzzle piece at the upper right with a solid yellow piece of the same shape.

**中文翻译：** 在第 28.0 秒，将右上方松散的蓝色拼图块替换为形状相同的纯黄色拼图块。

**状态：** 接受

**原子化判定句：**

1. 右上方松散的蓝色拼图块是否被替换为纯黄色拼图块？

2. 替换后的拼图块是否与原蓝色拼图块形状相同？


## 264 — `synthetic_process_088_E2B`

**原始英文指令：** Starting at 28.5 seconds, make the right hand circle twice above the central puzzle gap over four seconds.

**中文翻译：** 从第 28.5 秒开始，让右手在四秒内于中央拼图缺口上方绕圈两次。

**状态：** 接受

**原子化判定句：**

1. 右手是否在中央拼图缺口上方绕圈？

2. 右手是否恰好绕圈两次？

3. 两次绕圈是否在 4 秒内完成？


## 265 — `synthetic_process_089_E1`

**原始英文指令：** Starting at 13.0 seconds, pause extraction of the lower wooden block for five seconds, then resume from the held overlap position.

**中文翻译：** 从第 13.0 秒开始，让下方木块的抽出过程暂停五秒，然后从保持的重叠位置恢复抽出。

**状态：** 接受

**原子化判定句：**

1. 下方木块的抽出过程是否暂停 5 秒？

2. 下方木块是否在暂停 5 秒后从保持的重叠位置恢复抽出？


## 266 — `synthetic_process_089_E2A`

**原始英文指令：** Starting at 27.0 seconds, advance the tower's tilt until its top shifts left by one block width while standing at 31.5 seconds.

**中文翻译：** 从第 27.0 秒开始，推进塔体倾斜，使塔顶在第 31.5 秒前向左移动一个木块宽度，同时塔体仍保持直立未倒。

**状态：** 接受

**原子化判定句：**

1. 塔体倾斜是否得到推进？

2. 塔顶是否在 4.5 秒内向左移动一个木块宽度？

3. 塔体是否在这一移动过程中仍保持直立未倒？


## 267 — `synthetic_process_089_E2B`

**原始英文指令：** Starting at 28.0 seconds, make the central support block above the base compliant rubber that visibly compresses over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内将底座上方的中央支撑块变为柔顺橡胶，并使其产生可见压缩。

**状态：** 接受

**原子化判定句：**

1. 底座上方的中央支撑块是否在 2 秒内变为柔顺橡胶？

2. 该支撑块是否在同一段 2 秒内产生可见压缩？


## 268 — `synthetic_process_090_E1`

**原始英文指令：** Starting at 13.0 seconds, accelerate compression until the silver container reaches half its initial visible height by 19.5 seconds.

**中文翻译：** 从第 13.0 秒开始，加快压缩，使银色容器在第 19.5 秒前降至初始可见高度的一半。

**状态：** 接受

**原子化判定句：**

1. 压缩是否加快？

2. 银色容器是否在 6.5 秒内降至初始可见高度的一半？


## 269 — `synthetic_process_090_E2A`

**原始英文指令：** Starting at 27.0 seconds, render only the upper and lower press platens as hammered bronze over two seconds.

**中文翻译：** 从第 27.0 秒开始，在两秒内仅将上下压板呈现为锤纹青铜材质。

**状态：** 接受

**原子化判定句：**

1. 上、下压板是否都呈现为锤纹青铜材质？

2. 材质变化是否仅限于这两块压板？

3. 材质变化是否在 2 秒内完成？


## 270 — `synthetic_process_090_E2B`

**原始英文指令：** Starting at 28.0 seconds, make the compressed silver container highly elastic so its sharp folds round outward over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内让被压缩的银色容器变得高度有弹性，使其尖锐褶皱向外变圆。

**状态：** 接受

**原子化判定句：**

1. 被压缩的银色容器是否在 2 秒内变得高度有弹性？

2. 其尖锐褶皱是否在同一段 2 秒内向外变圆？


## 271 — `synthetic_process_091_E1`

**原始英文指令：** Starting at 13.0 seconds, make the upper tower masonry dry and brittle with granular chipped seam edges over two seconds.

**中文翻译：** 从第 13.0 秒开始，在两秒内让塔体上部砌体变得干燥且脆，并使接缝边缘呈颗粒状崩缺。

**状态：** 接受

**原子化判定句：**

1. 塔体上部砌体是否在 2 秒内变得干燥？

2. 该砌体是否在同一段 2 秒内变脆？

3. 其接缝边缘是否在同一段 2 秒内变得呈颗粒状并出现崩缺？


## 272 — `synthetic_process_091_E2A`

**原始英文指令：** At 27.5 seconds, rotate the falling upper tower section until the narrow window on its shadowed face points directly toward the camera.

**中文翻译：** 在第 27.5 秒，旋转正在坠落的塔体上段，直到其阴影侧表面上的狭窄窗户正对镜头。

**状态：** 接受

**原子化判定句：**

1. 正在坠落的塔体上段是否被旋转，直到其阴影侧表面上的狭窄窗户正对镜头？


## 273 — `synthetic_process_091_E2B`

**原始英文指令：** Starting at 28.0 seconds, advance the tower's fall until the upper section first touches the right-side ground by 35.5 seconds.

**中文翻译：** 从第 28.0 秒开始，推进塔体坠落，使上段在第 35.5 秒前首次接触右侧地面。

**状态：** 接受

**原子化判定句：**

1. 塔体坠落是否得到推进？

2. 上段是否在 7.5 秒内首次接触右侧地面？


## 274 — `synthetic_process_092_E1`

**原始英文指令：** At 14.0 seconds, remove the single backmost upright basket rod at the top center of the basket.

**中文翻译：** 在第 14.0 秒，移除篮筐顶部中央最后方的那一根直立篮条。

**状态：** 接受

**原子化判定句：**

1. 篮筐顶部中央最后方的那一根直立篮条是否被移除？


## 275 — `synthetic_process_092_E2A`

**原始英文指令：** Starting at 28.0 seconds, make the right hand pull the active weaving strip outward in two steady tugs over five seconds.

**中文翻译：** 从第 28.0 秒开始，让右手在五秒内以两次平稳拉动将正在编织的条带向外拉。

**状态：** 接受

**原子化判定句：**

1. 右手是否将正在编织的条带向外拉？

2. 是否使用恰好两次平稳拉动？

3. 两次拉动是否在 5 秒内完成？


## 276 — `synthetic_process_092_E2B`

**原始英文指令：** Starting at 29.0 seconds, render only the gray tabletop beneath the basket as dark woven felt over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内仅将篮筐下方的灰色桌面呈现为深色编织毡。

**状态：** 接受

**原子化判定句：**

1. 篮筐下方的灰色桌面是否呈现为深色编织毡？

2. 材质变化是否仅限于该桌面？

3. 材质变化是否在 2 秒内完成？


## 277 — `synthetic_process_093_E1`

**原始英文指令：** Starting at 14.0 seconds, make the left bridge section rotate toward the river center at twice the right section's speed for five seconds.

**中文翻译：** 从第 14.0 秒开始，让左侧桥段朝河流中心旋转五秒，速度为右侧桥段的两倍。

**状态：** 接受

**原子化判定句：**

1. 左侧桥段是否朝河流中心旋转 5 秒？

2. 左侧桥段在同一段 5 秒内的旋转速度是否为右侧桥段的两倍？


## 278 — `synthetic_process_093_E2A`

**原始英文指令：** Starting at 27.5 seconds, change the right movable bridge truss to saturated cobalt blue over two seconds.

**中文翻译：** 从第 27.5 秒开始，在两秒内将右侧可动桥桁架变为高饱和钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 右侧可动桥桁架是否变为高饱和钴蓝色？

2. 颜色变化是否在 2 秒内完成？


## 279 — `synthetic_process_093_E2B`

**原始英文指令：** Starting at 28.0 seconds, advance bridge closing until the two inner ends first meet over the river by 34.5 seconds.

**中文翻译：** 从第 28.0 秒开始，推进桥梁闭合，使两个内侧端部在第 34.5 秒前于河面上方首次接合。

**状态：** 接受

**原子化判定句：**

1. 桥梁闭合是否得到推进？

2. 两个内侧端部是否在 6.5 秒内于河面上方首次接合？


## 280 — `synthetic_process_094_E1`

**原始英文指令：** Starting at 16.0 seconds, accelerate the current upward zipper pass until the slider exits the upper frame edge by 20.0 seconds.

**中文翻译：** 从第 16.0 秒开始，加快当前向上的拉链闭合过程，使拉头在第 20.0 秒前移出画面上边缘。

**状态：** 接受

**原子化判定句：**

1. 当前向上的拉链闭合过程是否加快？

2. 拉头是否在 4 秒内移出画面上边缘？


## 281 — `synthetic_process_094_E2A`

**原始英文指令：** Starting at 28.0 seconds, advance zipper closure until the right fabric edge is joined across the middle half by 32.5 seconds.

**中文翻译：** 从第 28.0 秒开始，推进拉链闭合，使右侧布料边缘在第 32.5 秒前于中间一半区域完成连接。

**状态：** 接受

**原子化判定句：**

1. 拉链闭合是否得到推进？

2. 右侧布料边缘是否在 4.5 秒内于中间一半区域完成连接？


## 282 — `synthetic_process_094_E2B`

**原始英文指令：** At 29.0 seconds, move the left hand directly above the right hand with a small visible gap between them.

**中文翻译：** 在第 29.0 秒，将左手移至右手正上方，并在两手之间保留一个清晰可见的小间隙。

**状态：** 接受

**原子化判定句：**

1. 左手是否被移至右手正上方？

2. 两手之间是否保留一个清晰可见的小间隙？


## 283 — `synthetic_process_095_E1`

**原始英文指令：** At 12.5 seconds, split the intact right-side neck mass into two large fragments along a new diagonal seam.

**中文翻译：** 在第 12.5 秒，沿一道新的斜向接缝将右侧完整的颈部块体分成两个大碎块。

**状态：** 接受

**原子化判定句：**

1. 右侧完整的颈部块体是否分成恰好两个大碎块？

2. 分裂是否沿一道新的斜向接缝发生？


## 284 — `synthetic_process_095_E2A`

**原始英文指令：** Starting at 27.0 seconds, accelerate widening of the main neck crack until its central gap doubles by 33.5 seconds.

**中文翻译：** 从第 27.0 秒开始，加快主颈部裂缝变宽，使其中央间隙在第 33.5 秒前扩大至两倍。

**状态：** 接受

**原子化判定句：**

1. 主颈部裂缝变宽是否加快？

2. 其中央间隙是否在 6.5 秒内扩大至编辑点时宽度的两倍？


## 285 — `synthetic_process_095_E2B`

**原始英文指令：** Starting at 27.5 seconds, make the right fragment group begin detaching at 33.5 seconds and settle separately by 36.0 seconds.

**中文翻译：** 从第 27.5 秒开始，让右侧碎块组在第 33.5 秒开始脱离，并在第 36.0 秒前单独落稳。

**状态：** 接受

**原子化判定句：**

1. 右侧碎块组是否在 6 秒后开始脱离？

2. 右侧碎块组是否在 8.5 秒内单独落稳？


## 286 — `synthetic_process_096_E1`

**原始英文指令：** At 13.0 seconds, move the purple color dish beside the blue dish until their outer rims are one centimeter apart.

**中文翻译：** 在第 13.0 秒，将紫色颜料皿移至蓝色颜料皿旁边，直到两者外缘相距一厘米。

**状态：** 接受

**原子化判定句：**

1. 紫色颜料皿是否被移至蓝色颜料皿旁边？

2. 两者外缘最终是否相距 1 厘米？


## 287 — `synthetic_process_096_E2A`

**原始英文指令：** Starting at 27.0 seconds, make the gloved hand trace two complete clockwise circles around the central yellow disc over five seconds.

**中文翻译：** 从第 27.0 秒开始，让戴手套的手在五秒内围绕中央黄色圆盘顺时针完整画两圈。

**状态：** 接受

**原子化判定句：**

1. 戴手套的手是否围绕中央黄色圆盘顺时针画圈？

2. 是否恰好完成两个完整圆圈？

3. 两个圆圈是否在 5 秒内完成？


## 288 — `synthetic_process_096_E2B`

**原始英文指令：** Starting at 27.5 seconds, smoothly zoom out until the full pattern and all six color dishes fill the middle two-thirds of the frame.

**中文翻译：** 从第 27.5 秒开始，平滑拉远镜头，直到完整图案和全部六个颜料皿填满画面中间三分之二区域。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉远，直至完整图案和全部六个颜料皿填满画面中间三分之二区域？

2. 拉远过程是否平滑？


## 289 — `synthetic_process_097_E1`

**原始英文指令：** Starting at 13.5 seconds, move the camera through a shallow rightward arc around the wheel for five seconds.

**中文翻译：** 从第 13.5 秒开始，让镜头围绕车轮沿一段平缓的右向弧线移动五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否围绕车轮沿一段平缓的右向弧线移动？

2. 这一移动是否持续 5 秒？


## 290 — `synthetic_process_097_E2A`

**原始英文指令：** At 28.0 seconds, merge the two parallel loose spokes on the lower-left tabletop into one straight double-width spoke.

**中文翻译：** 在第 28.0 秒，将桌面左下方两根平行的松散辐条合并为一根笔直的双倍宽度辐条。

**状态：** 接受

**原子化判定句：**

1. 桌面左下方两根平行的松散辐条是否合并为一根笔直辐条？

2. 合并后的辐条宽度是否为单根原辐条的两倍？


## 291 — `synthetic_process_097_E2B`

**原始英文指令：** Starting at 28.5 seconds, accelerate spoke installation until no visible rim sector wider than thirty degrees remains empty by 35.5 seconds.

**中文翻译：** 从第 28.5 秒开始，加快辐条安装，使轮缘在第 35.5 秒前不再存在宽度超过三十度的可见空缺扇区。

**状态：** 接受

**原子化判定句：**

1. 辐条安装是否加快？

2. 所有可见的轮缘空缺扇区是否在 7 秒内都变得不超过 30 度宽？


## 292 — `synthetic_process_098_E1`

**原始英文指令：** Starting at 14.0 seconds, smoothly zoom out until the entire bowl and four nearest loose fragments fill the middle half of the frame.

**中文翻译：** 从第 14.0 秒开始，平滑拉远镜头，直到整个碗和最近的四块松散碎片填满画面中间一半区域。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉远，直至整个碗和最近的四块松散碎片填满画面中间一半区域？

2. 拉远过程是否平滑？


## 293 — `synthetic_process_098_E2A`

**原始英文指令：** Starting at 27.5 seconds, render only the wooden tabletop beneath the bowl as dark slate over two seconds.

**中文翻译：** 从第 27.5 秒开始，在两秒内仅将碗下方的木质桌面呈现为深色石板。

**状态：** 接受

**原子化判定句：**

1. 碗下方的木质桌面是否呈现为深色石板？

2. 材质变化是否仅限于该桌面？

3. 材质变化是否在 2 秒内完成？


## 294 — `synthetic_process_098_E2B`

**原始英文指令：** At 28.5 seconds, split the large loose curved ceramic shard on the right into two smaller curved pieces.

**中文翻译：** 在第 28.5 秒，将右侧松散的大型弯曲陶瓷碎片分成两块较小的弯曲碎片。

**状态：** 接受

**原子化判定句：**

1. 右侧松散的大型弯曲陶瓷碎片是否分成恰好两块？

2. 分成的两块是否都更小且保持弯曲形状？


## 295 — `synthetic_process_099_E1`

**原始英文指令：** Starting at 13.5 seconds, accelerate flame propagation until two additional match heads have ignited by 19.5 seconds.

**中文翻译：** 从第 13.5 秒开始，加快火焰传播，使另外两个火柴头在第 19.5 秒前点燃。

**状态：** 接受

**原子化判定句：**

1. 火焰传播是否加快？

2. 是否有另外两个火柴头在 6 秒内点燃？


## 296 — `synthetic_process_099_E2A`

**原始英文指令：** Starting at 27.5 seconds, advance the burn-and-fall process until only two upright red-headed matches remain by 32.5 seconds.

**中文翻译：** 从第 27.5 秒开始，推进燃烧和倒落过程，使画面在第 32.5 秒前仅剩两根直立的红头火柴。

**状态：** 接受

**原子化判定句：**

1. 燃烧和倒落过程是否得到推进？

2. 是否在 5 秒内仅剩两根直立的红头火柴？


## 297 — `synthetic_process_099_E2B`

**原始英文指令：** At 28.0 seconds, move the rightmost remaining upright match one match-width farther right along the black base.

**中文翻译：** 在第 28.0 秒，将最右侧剩余的直立火柴沿黑色底座再向右移动一个火柴宽度。

**状态：** 接受

**原子化判定句：**

1. 最右侧剩余的直立火柴是否沿黑色底座进一步向右移动？

2. 移动距离是否为一个火柴宽度？


## 298 — `synthetic_process_100_E1`

**原始英文指令：** Starting at 14.0 seconds, make the black bladder shell thicker and more elastic with shallow longitudinal ribs over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内使黑色囊状外壳变得更厚、更有弹性，并出现浅的纵向棱纹。

**状态：** 接受

**原子化判定句：**

1. 黑色囊状外壳是否在 2 秒内变得更厚？

2. 黑色囊状外壳是否在同一段 2 秒内变得更有弹性？

3. 黑色囊状外壳是否在同一段 2 秒内出现浅的纵向棱纹？


## 299 — `synthetic_process_100_E2A`

**原始英文指令：** Starting at 28.0 seconds, make the left-side black pump rock gently forward and backward twice over five seconds.

**中文翻译：** 从第 28.0 秒开始，让左侧黑色泵在五秒内轻柔地前后摇动两次。

**状态：** 接受

**原子化判定句：**

1. 左侧黑色泵是否轻柔地前后摇动？

2. 黑色泵是否恰好完成两次摇动？

3. 两次摇动是否在 5 秒内完成？


## 300 — `synthetic_process_100_E2B`

**原始英文指令：** Starting at 29.0 seconds, advance bladder inflation until the gray beam's upper edge aligns with the red wall marker by 35.5 seconds.

**中文翻译：** 从第 29.0 秒开始，推进囊体充气，使灰色横梁的上边缘在第 35.5 秒前与墙上的红色标记对齐。

**状态：** 接受

**原子化判定句：**

1. 囊体充气是否得到推进？

2. 灰色横梁的上边缘是否在 6.5 秒内与墙上的红色标记对齐？
