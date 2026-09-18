# 全量编辑指令原子化结果——syn_embodied_edit_records.md——中文审阅版

- 源记录数：300

- 所有原子判定句均依据 `atom_results/README.md` 逐条人工审核。

- 原子判定句省略作为截取起点的绝对时间；后续时间点均已换算为片段内相对时间。


## 001 — `synthetic_embodied_001_E1`

**原始英文指令：** At 10.5 seconds, recolor the blue sofa's visible seat and back upholstery to burnt orange.

**中文翻译：** 在第 10.5 秒，将蓝色沙发可见的座面和靠背面料改为焦橙色。

**状态：** 接受

**原子化判定句：**

1. 蓝色沙发可见的座面面料是否改为焦橙色？

2. 蓝色沙发可见的靠背面料是否改为焦橙色？


## 002 — `synthetic_embodied_001_E2A`

**原始英文指令：** At 22.5 seconds, remove the red toy car resting beside the colored blocks on the yellow rug.

**中文翻译：** 在第 22.5 秒，移除黄色地毯上彩色积木旁的红色玩具车。

**状态：** 接受

**原子化判定句：**

1. 黄色地毯上彩色积木旁的红色玩具车是否被移除？


## 003 — `synthetic_embodied_001_E2B`

**原始英文指令：** At 24.5 seconds, pause the observer's forward locomotion toward the window for three seconds, then resume it.

**中文翻译：** 在第 24.5 秒，将观察者朝窗户向前移动的过程暂停三秒，然后恢复移动。

**状态：** 接受

**原子化判定句：**

1. 观察者是否朝窗户向前移动？

2. 观察者向前移动的过程是否暂停 3 秒？

3. 随后观察者是否恢复朝窗户向前移动？


## 004 — `synthetic_embodied_002_E1`

**原始英文指令：** At 14 seconds, halve the observer's forward locomotion speed along the corridor for four seconds.

**中文翻译：** 在第 14 秒，将观察者沿走廊向前移动的速度减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 观察者是否继续沿走廊向前移动？

2. 观察者的前进速度是否减半？

3. 减半后的速度是否持续 4 秒？


## 005 — `synthetic_embodied_002_E2A`

**原始英文指令：** At 22.5 seconds, replace the potted tree at the corridor end with a tall cactus in a square planter.

**中文翻译：** 在第 22.5 秒，将走廊尽头的盆栽树替换为种在方形花盆中的高大仙人掌。

**状态：** 接受

**原子化判定句：**

1. 走廊尽头的盆栽树是否被替换为仙人掌？

2. 替换后的仙人掌是否高大？

3. 仙人掌是否种在方形花盆中？


## 006 — `synthetic_embodied_002_E2B`

**原始英文指令：** At 26.5 seconds, recolor the black square tree pot at the corridor end to terracotta red.

**中文翻译：** 在第 26.5 秒，将走廊尽头黑色方形树盆改为赤陶红色。

**状态：** 接受

**原子化判定句：**

1. 走廊尽头的黑色方形树盆是否被改为赤陶红色？


## 007 — `synthetic_embodied_003_E1`

**原始英文指令：** At 12 seconds, add one plain orange rubber ball inside the empty main shopping-cart basket.

**中文翻译：** 在第 12 秒，在空的主购物车篮筐内添加一个无图案的橙色橡胶球。

**状态：** 接受

**原子化判定句：**

1. 空的主购物车篮筐内是否添加了恰好一个球？

2. 新增的球是否为橙色？

3. 新增的球是否为橡胶材质？

4. 新增的球是否无图案？


## 008 — `synthetic_embodied_003_E2A`

**原始英文指令：** At 24.5 seconds, stop the shopping-cart pusher's forward walking for three seconds before continuing down the aisle.

**中文翻译：** 在第 24.5 秒，让推购物车者停止向前行走三秒，然后继续沿过道前进。

**状态：** 接受

**原子化判定句：**

1. 推购物车者是否沿过道向前行走？

2. 推购物车者是否停止向前行走 3 秒？

3. 随后推购物车者是否继续沿过道前进？


## 009 — `synthetic_embodied_003_E2B`

**原始英文指令：** At 25.5 seconds, make the shopping-cart basket wires visibly corroded with rough orange rust.

**中文翻译：** 在第 25.5 秒，让购物车篮筐的金属丝明显腐蚀，并带有粗糙的橙色锈迹。

**状态：** 接受

**原子化判定句：**

1. 购物车篮筐的金属丝是否明显腐蚀？

2. 金属丝上的锈迹是否呈粗糙的橙色？


## 010 — `synthetic_embodied_004_E1`

**原始英文指令：** At 12.5 seconds, widen the gallery framing until both sides of the central doorway have more surrounding wall visible.

**中文翻译：** 在第 12.5 秒，扩大画廊的取景范围，直到中央门口两侧都显示出更多周围墙面。

**状态：** 接受

**原子化判定句：**

1. 画廊的取景范围是否扩大？

2. 中央门口左侧是否显示出更多周围墙面？

3. 中央门口右侧是否显示出更多周围墙面？


## 011 — `synthetic_embodied_004_E2A`

**原始英文指令：** At 24 seconds, remove the long dark bench positioned against the right wall of the picture gallery.

**中文翻译：** 在第 24 秒，移除靠在画廊右墙边的深色长凳。

**状态：** 接受

**原子化判定句：**

1. 靠在画廊右墙边的深色长凳是否被移除？


## 012 — `synthetic_embodied_004_E2B`

**原始英文指令：** At 25.5 seconds, make the long bench beside the gallery's right wall rock gently twice over four seconds.

**中文翻译：** 在第 25.5 秒，让画廊右墙旁的长凳在四秒内轻轻摇晃两次。

**状态：** 接受

**原子化判定句：**

1. 画廊右墙旁的长凳是否轻轻摇晃？

2. 长凳是否恰好摇晃两次？

3. 两次摇晃是否在 4 秒内完成？


## 013 — `synthetic_embodied_005_E1`

**原始英文指令：** At 15 seconds, halve the umbrella-carrying walker's forward speed for four seconds.

**中文翻译：** 在第 15 秒，将撑伞行人的前进速度减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 撑伞行人是否继续向前移动？

2. 行人的前进速度是否减半？

3. 减半后的速度是否持续 4 秒？


## 014 — `synthetic_embodied_005_E2A`

**原始英文指令：** At 25.5 seconds, change the black curved umbrella handle to a polished ivory-colored handle.

**中文翻译：** 在第 25.5 秒，将黑色弯曲伞柄改为抛光的象牙色伞柄。

**状态：** 接受

**原子化判定句：**

1. 弯曲伞柄是否从黑色变为象牙色？

2. 伞柄是否呈抛光表面？


## 015 — `synthetic_embodied_005_E2B`

**原始英文指令：** At 27.5 seconds, render the entire umbrella-and-street scene as a hand-painted watercolor animation.

**中文翻译：** 在第 27.5 秒，将整个雨伞与街道场景呈现为手绘水彩动画。

**状态：** 接受

**原子化判定句：**

1. 整个雨伞与街道场景是否被呈现为水彩动画？

2. 该动画是否具有手绘外观？


## 016 — `synthetic_embodied_006_E1`

**原始英文指令：** At 16 seconds, switch to a rear three-quarter third-person view showing the blue-jacketed walker and both poles.

**中文翻译：** 在第 16 秒，切换为后侧四分之三第三人称视角，画面中显示穿蓝色夹克的行人和两根手杖。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为后侧四分之三第三人称视角？

2. 该视角中是否能看到穿蓝色夹克的行人和两根手杖？


## 017 — `synthetic_embodied_006_E2A`

**原始英文指令：** At 28.5 seconds, make the walker perform two exaggerated high-knee steps along the existing snow track.

**中文翻译：** 在第 28.5 秒，让行人沿现有雪地足迹做两个夸张的高抬腿步。

**状态：** 接受

**原子化判定句：**

1. 行人是否沿现有雪地足迹做高抬腿步？

2. 高抬腿动作是否夸张？

3. 行人是否恰好完成两个这样的步子？


## 018 — `synthetic_embodied_006_E2B`

**原始英文指令：** At 29.5 seconds, replace both walking poles with matching wooden hiking staffs fitted with plain rubber tips.

**中文翻译：** 在第 29.5 秒，将两根行走杖都替换为相互匹配、装有无图案橡胶杖尖的木质徒步杖。

**状态：** 接受

**原子化判定句：**

1. 两根行走杖是否都被替换为木质徒步杖？

2. 两根木质徒步杖是否相互匹配？

3. 两根徒步杖是否都装有无图案橡胶杖尖？


## 019 — `synthetic_embodied_007_E1`

**原始英文指令：** At 12.5 seconds, set both sandaled feet parallel and one foot-width apart on the current rock for three seconds.

**中文翻译：** 在第 12.5 秒，让穿凉鞋的双脚在当前岩石上保持平行并相距一个脚宽，持续三秒。

**状态：** 接受

**原子化判定句：**

1. 穿凉鞋的双脚是否在当前岩石上保持平行并持续 3 秒？

2. 双脚是否在同一段 3 秒内保持相距一个脚宽？


## 020 — `synthetic_embodied_007_E2A`

**原始英文指令：** At 24 seconds, make the observer open and close both empty hands twice over four seconds.

**中文翻译：** 在第 24 秒，让观察者在四秒内将两只空手张开并合拢两次。

**状态：** 接受

**原子化判定句：**

1. 观察者是否将两只空手张开并合拢？

2. 观察者是否恰好完成两次张开—合拢循环？

3. 两次循环是否在 4 秒内完成？


## 021 — `synthetic_embodied_007_E2B`

**原始英文指令：** At 26.5 seconds, switch to a raised rear third-person view showing the observer's feet and the surrounding rocks.

**中文翻译：** 在第 26.5 秒，切换为抬高的后方第三人称视角，显示观察者的双脚和周围岩石。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为抬高的后方第三人称视角？

2. 该视角中是否能看到观察者的双脚和周围岩石？


## 022 — `synthetic_embodied_008_E1`

**原始英文指令：** At 12 seconds, make the main tent's khaki outer flysheet visibly wet with dark damp patches.

**中文翻译：** 在第 12 秒，让主帐篷的卡其色外帐明显变湿，并出现深色湿斑。

**状态：** 接受

**原子化判定句：**

1. 主帐篷的卡其色外帐是否明显变湿？

2. 外帐上是否出现深色湿斑？


## 023 — `synthetic_embodied_008_E2A`

**原始英文指令：** At 21 seconds, place the background green tent one tent-width farther to the right on the grass.

**中文翻译：** 在第 21 秒，将背景中的绿色帐篷在草地上向右移动一个帐篷宽度。

**状态：** 接受

**原子化判定句：**

1. 背景中的绿色帐篷是否向右移动？

2. 移动距离是否为一个帐篷宽度？

3. 移动后帐篷是否仍位于草地上？


## 024 — `synthetic_embodied_008_E2B`

**原始英文指令：** At 23.5 seconds, make the main tent's loose gray inner flap flutter twice over three seconds.

**中文翻译：** 在第 23.5 秒，让主帐篷松散的灰色内帘在三秒内飘动两次。

**状态：** 接受

**原子化判定句：**

1. 主帐篷松散的灰色内帘是否飘动？

2. 内帘是否恰好飘动两次？

3. 两次飘动是否在 3 秒内完成？


## 025 — `synthetic_embodied_009_E1`

**原始英文指令：** At 11 seconds, replace the visible plain metal bookends with small elephant-shaped wooden bookends.

**中文翻译：** 在第 11 秒，将可见的普通金属书挡替换为小型木质大象造型书挡。

**状态：** 接受

**原子化判定句：**

1. 可见的普通金属书挡是否被替换？

2. 替换后的书挡是否为大象造型？

3. 替换后的书挡是否为木质？

4. 替换后的书挡是否小型？


## 026 — `synthetic_embodied_009_E2A`

**原始英文指令：** At 21 seconds, turn the visible plain bookends a quarter-turn around their vertical axes.

**中文翻译：** 在第 21 秒，将可见的普通书挡绕各自竖直轴旋转四分之一圈。

**状态：** 接受

**原子化判定句：**

1. 可见的普通书挡是否分别绕各自竖直轴旋转？

2. 每个书挡的旋转幅度是否为四分之一圈？


## 027 — `synthetic_embodied_009_E2B`

**原始英文指令：** At 24 seconds, give the library aisle the soft grain and muted colors of an old sixteen-millimeter film.

**中文翻译：** 在第 24 秒，为图书馆过道赋予老式 16 毫米胶片的柔和颗粒感和低饱和色彩。

**状态：** 接受

**原子化判定句：**

1. 图书馆过道是否呈现老式 16 毫米胶片的柔和颗粒感？

2. 画面是否也呈现老式 16 毫米胶片的低饱和色彩？


## 028 — `synthetic_embodied_010_E1`

**原始英文指令：** At 12.5 seconds, pause the flashlight-carrying observer's forward locomotion for three seconds, then continue through the passage.

**中文翻译：** 在第 12.5 秒，将携带手电筒的观察者向前移动的过程暂停三秒，然后继续穿过通道。

**状态：** 接受

**原子化判定句：**

1. 携带手电筒的观察者是否向前穿过通道？

2. 观察者向前移动的过程是否暂停 3 秒？

3. 随后观察者是否继续穿过通道？


## 029 — `synthetic_embodied_010_E2A`

**原始英文指令：** At 23 seconds, switch to a close over-the-shoulder third-person view behind the flashlight carrier.

**中文翻译：** 在第 23 秒，切换为手电筒携带者身后的近距离越肩第三人称视角。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为手电筒携带者身后的越肩构图？

2. 新视角是否为近距离？

3. 新视角是否为第三人称？


## 030 — `synthetic_embodied_010_E2B`

**原始英文指令：** At 25.5 seconds, make the floor directly ahead within the flashlight beam visibly wet and reflective.

**中文翻译：** 在第 25.5 秒，让手电筒光束内正前方的地面明显变湿并具有反光效果。

**状态：** 接受

**原子化判定句：**

1. 手电筒光束内正前方的地面是否明显变湿？

2. 该地面是否产生反光效果？


## 031 — `synthetic_embodied_011_E1`

**原始英文指令：** At 13 seconds, switch to a rear-right third-person view framing the suitcase carrier's right arm and luggage.

**中文翻译：** 在第 13 秒，切换为右后方第三人称视角，将行李箱携带者的右臂和行李纳入画面。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为右后方第三人称视角？

2. 该视角是否将行李箱携带者的右臂和行李纳入画面？


## 032 — `synthetic_embodied_011_E2A`

**原始英文指令：** At 24 seconds, make the suitcase carrier take two short backward steps away from the chairs.

**中文翻译：** 在第 24 秒，让行李箱携带者迈两个短小的后退步，远离椅子。

**状态：** 接受

**原子化判定句：**

1. 行李箱携带者是否后退并远离椅子？

2. 后退步是否短小？

3. 携带者是否恰好迈出两个后退步？


## 033 — `synthetic_embodied_011_E2B`

**原始英文指令：** At 26.5 seconds, place the right palm beneath and around the suitcase handle in an underhand grip for three seconds.

**中文翻译：** 在第 26.5 秒，将右手掌置于行李箱把手下方并环握把手，以反手握法保持三秒。

**状态：** 接受

**原子化判定句：**

1. 右手掌是否置于行李箱把手下方并环握把手？

2. 右手是否形成反手握法？

3. 反手握持是否保持 3 秒？


## 034 — `synthetic_embodied_012_E1`

**原始英文指令：** At 14.5 seconds, place the low front-left aquarium rock closer to the tall central rock, leaving a narrow sand gap.

**中文翻译：** 在第 14.5 秒，将水族箱左前方的低矮岩石移近中央高岩石，并在两者之间留下一条狭窄沙隙。

**状态：** 接受

**原子化判定句：**

1. 水族箱左前方的低矮岩石是否被移近中央高岩石？

2. 两块岩石之间是否留有一条狭窄沙隙？


## 035 — `synthetic_embodied_012_E2A`

**原始英文指令：** At 25 seconds, make the visible aquarium fish circle clockwise around the main rock group for four seconds.

**中文翻译：** 在第 25 秒，让可见的水族箱鱼围绕主岩石群顺时针游动，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 可见的水族箱鱼是否围绕主岩石群游动？

2. 鱼群是否沿顺时针方向绕行？

3. 顺时针绕行是否持续 4 秒？


## 036 — `synthetic_embodied_012_E2B`

**原始英文指令：** At 28.5 seconds, change the tall central aquarium rock to a pale turquoise color.

**中文翻译：** 在第 28.5 秒，将水族箱中央的高岩石改为淡青绿色。

**状态：** 接受

**原子化判定句：**

1. 水族箱中央的高岩石是否被改为淡青绿色？


## 037 — `synthetic_embodied_013_E1`

**原始英文指令：** At 16 seconds, make the observer descend the next two stair treads with a sideways stepping gait.

**中文翻译：** 在第 16 秒，让观察者以侧向步态走下接下来的两级楼梯。

**状态：** 接受

**原子化判定句：**

1. 观察者是否走下接下来的两级楼梯？

2. 观察者下楼时是否采用侧向步态？


## 038 — `synthetic_embodied_013_E2A`

**原始英文指令：** At 28.5 seconds, place the left palm beneath the rope handrail in an underhand grip for three seconds.

**中文翻译：** 在第 28.5 秒，将左手掌置于绳索扶手下方，以反手握法保持三秒。

**状态：** 接受

**原子化判定句：**

1. 左手掌是否置于绳索扶手下方？

2. 左手是否以反手方式握住扶手？

3. 该握持是否保持 3 秒？


## 039 — `synthetic_embodied_013_E2B`

**原始英文指令：** At 29 seconds, switch to a rear-left third-person view showing the stair walker's feet and rope-holding hand.

**中文翻译：** 在第 29 秒，切换为左后方第三人称视角，显示楼梯行走者的双脚和握绳的手。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为左后方第三人称视角？

2. 该视角中是否能看到楼梯行走者的双脚和握绳的手？


## 040 — `synthetic_embodied_014_E1`

**原始英文指令：** At 14 seconds, make the empty seat pans just beyond the central divider flip up and down once.

**中文翻译：** 在第 14 秒，让中央隔板后方不远处的空座椅坐板向上翻起再落下一次。

**状态：** 接受

**原子化判定句：**

1. 中央隔板后方不远处的空座椅坐板是否向上翻起？

2. 坐板是否随后向下落回一次？


## 041 — `synthetic_embodied_014_E2A`

**原始英文指令：** At 25.5 seconds, remove the nearest empty seat below the concrete divider on the left side of the aisle.

**中文翻译：** 在第 25.5 秒，移除过道左侧混凝土隔板下方最近的空座椅。

**状态：** 接受

**原子化判定句：**

1. 过道左侧混凝土隔板下方最近的空座椅是否被移除？


## 042 — `synthetic_embodied_014_E2B`

**原始英文指令：** At 27 seconds, switch to a rear third-person view showing the observer and the separate blue-jacketed spectator ahead.

**中文翻译：** 在第 27 秒，切换为后方第三人称视角，显示观察者以及前方另一名穿蓝色夹克的观众。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为后方第三人称视角？

2. 该视角中是否能同时看到观察者和前方另一名穿蓝色夹克的观众？


## 043 — `synthetic_embodied_015_E1`

**原始英文指令：** At 12.5 seconds, recolor the two white benches on the covered deck to pale yellow.

**中文翻译：** 在第 12.5 秒，将有顶甲板上的两张白色长凳改为淡黄色。

**状态：** 接受

**原子化判定句：**

1. 有顶甲板上的第一张白色长凳是否改为淡黄色？

2. 有顶甲板上的第二张白色长凳是否改为淡黄色？


## 044 — `synthetic_embodied_015_E2A`

**原始英文指令：** At 25 seconds, replace the right-hand deck bench with a low wicker storage chest.

**中文翻译：** 在第 25 秒，将甲板右侧长凳替换为一个低矮的柳条储物箱。

**状态：** 接受

**原子化判定句：**

1. 甲板右侧长凳是否被替换为储物箱？

2. 替换后的储物箱是否低矮？

3. 替换后的储物箱是否为柳条材质？


## 045 — `synthetic_embodied_015_E2B`

**原始英文指令：** At 27.5 seconds, make the sea beyond the deck railings develop brisk rolling waves with small whitecaps.

**中文翻译：** 在第 27.5 秒，让甲板栏杆外的海面出现快速翻滚的波浪和小型白色浪花。

**状态：** 接受

**原子化判定句：**

1. 甲板栏杆外的海面是否出现翻滚的波浪？

2. 波浪是否快速翻滚？

3. 波浪上是否出现小型白色浪花？


## 046 — `synthetic_embodied_016_E1`

**原始英文指令：** At 9 seconds, halve the helmet-carrying observer's forward walking speed for four seconds.

**中文翻译：** 在第 9 秒，将携带头盔的观察者向前行走的速度减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 携带头盔的观察者是否继续向前行走？

2. 观察者向前行走的速度是否减半？

3. 减半后的速度是否持续 4 秒？


## 047 — `synthetic_embodied_016_E2A`

**原始英文指令：** At 20.5 seconds, give the parking-garage image a cool cyan shadow tone with softly desaturated highlights.

**中文翻译：** 在第 20.5 秒，为停车库画面添加冷青色阴影色调，并使高光呈柔和的低饱和效果。

**状态：** 接受

**原子化判定句：**

1. 停车库画面是否具有冷青色阴影色调？

2. 画面的高光是否也呈现柔和的低饱和效果？


## 048 — `synthetic_embodied_016_E2B`

**原始英文指令：** At 22.5 seconds, make the carried helmet's plain white shell visibly splattered with dark mud.

**中文翻译：** 在第 22.5 秒，让携带的头盔无图案白色外壳明显溅上深色泥浆。

**状态：** 接受

**原子化判定句：**

1. 携带的头盔无图案白色外壳是否明显溅有深色泥浆？


## 049 — `synthetic_embodied_017_E1`

**原始英文指令：** At 15.5 seconds, pause the observer's forward walking along the wooden boardwalk for three seconds, then resume it.

**中文翻译：** 在第 15.5 秒，将观察者沿木栈道向前行走的过程暂停三秒，然后恢复行走。

**状态：** 接受

**原子化判定句：**

1. 观察者是否沿木栈道向前行走？

2. 观察者向前行走的过程是否暂停 3 秒？

3. 随后观察者是否恢复沿木栈道向前行走？


## 050 — `synthetic_embodied_017_E2A`

**原始英文指令：** At 24.5 seconds, set the two guardrails flanking the pavilion exit farther apart by one railing-post width.

**中文翻译：** 在第 24.5 秒，将凉亭出口两侧的两道护栏拉开一个栏杆柱宽度的额外距离。

**状态：** 接受

**原子化判定句：**

1. 凉亭出口两侧的两道护栏是否被拉得更开？

2. 增加的间距是否等于一个栏杆柱宽度？


## 051 — `synthetic_embodied_017_E2B`

**原始英文指令：** At 28.5 seconds, widen the framing around the pavilion to include more of the surrounding rice field.

**中文翻译：** 在第 28.5 秒，扩大凉亭周围的取景范围，将更多周边稻田纳入画面。

**状态：** 接受

**原子化判定句：**

1. 凉亭周围的取景范围是否扩大？

2. 扩大后的画面是否纳入更多周边稻田？


## 052 — `synthetic_embodied_018_E1`

**原始英文指令：** At 17 seconds, widen the lighthouse framing to include its full top and more sea on both sides.

**中文翻译：** 在第 17 秒，扩大灯塔的取景范围，使画面包含完整的灯塔顶部以及两侧更多海面。

**状态：** 接受

**原子化判定句：**

1. 灯塔的取景范围是否扩大并包含完整的灯塔顶部？

2. 扩大后的画面是否包含灯塔两侧更多海面？


## 053 — `synthetic_embodied_018_E2A`

**原始英文指令：** At 28.5 seconds, make the wet concrete stair treads below the lighthouse platform dry and matte.

**中文翻译：** 在第 28.5 秒，让灯塔平台下方湿润的混凝土楼梯踏步变得干燥且呈哑光。

**状态：** 接受

**原子化判定句：**

1. 灯塔平台下方湿润的混凝土楼梯踏步是否变得干燥？

2. 楼梯踏步是否呈哑光？


## 054 — `synthetic_embodied_018_E2B`

**原始英文指令：** At 31 seconds, pause the observer's stair-climbing locomotion for three seconds, then resume climbing toward the lighthouse.

**中文翻译：** 在第 31 秒，将观察者爬楼梯的移动过程暂停三秒，然后恢复朝灯塔攀登。

**状态：** 接受

**原子化判定句：**

1. 观察者是否爬楼梯朝灯塔前进？

2. 观察者爬楼梯的移动过程是否暂停 3 秒？

3. 随后观察者是否恢复朝灯塔攀登？


## 055 — `synthetic_embodied_019_E1`

**原始英文指令：** At 13.5 seconds, make the red fabric valance above the ornate doorway flutter gently for two seconds.

**中文翻译：** 在第 13.5 秒，让华丽门口上方的红色布帘轻轻飘动两秒。

**状态：** 接受

**原子化判定句：**

1. 华丽门口上方的红色布帘是否轻轻飘动？

2. 轻柔飘动是否持续 2 秒？


## 056 — `synthetic_embodied_019_E2A`

**原始英文指令：** At 23 seconds, recolor the braided companion's plain red vest to deep teal.

**中文翻译：** 在第 23 秒，将扎辫同伴的无图案红色背心改为深蓝绿色。

**状态：** 接受

**原子化判定句：**

1. 扎辫同伴的无图案红色背心是否被改为深蓝绿色？


## 057 — `synthetic_embodied_019_E2B`

**原始英文指令：** At 26.5 seconds, widen the framing around the braided companion to show more of the passage beside both shoulders.

**中文翻译：** 在第 26.5 秒，扩大扎辫同伴周围的取景范围，显示其双肩两侧更多通道。

**状态：** 接受

**原子化判定句：**

1. 扎辫同伴周围的取景范围是否扩大？

2. 同伴左肩一侧是否显示出更多通道？

3. 同伴右肩一侧是否显示出更多通道？


## 058 — `synthetic_embodied_020_E1`

**原始英文指令：** At 14.5 seconds, halve the tray carrier's forward walking speed for four seconds.

**中文翻译：** 在第 14.5 秒，将托盘携带者向前行走的速度减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 托盘携带者是否继续向前行走？

2. 托盘携带者向前行走的速度是否减半？

3. 减半后的速度是否持续 4 秒？


## 059 — `synthetic_embodied_020_E2A`

**原始英文指令：** At 28 seconds, render the white tiled wall behind the worktable as a charcoal drawing.

**中文翻译：** 在第 28 秒，将工作台后方的白色瓷砖墙呈现为炭笔画风格。

**状态：** 接受

**原子化判定句：**

1. 工作台后方的白色瓷砖墙是否呈现为炭笔画风格？


## 060 — `synthetic_embodied_020_E2B`

**原始英文指令：** At 27.5 seconds, split the single empty rectangular metal tray into two separate smaller metal trays.

**中文翻译：** 在第 27.5 秒，将一个空的矩形金属托盘拆分为两个彼此分离的较小金属托盘。

**状态：** 接受

**原子化判定句：**

1. 一个空的矩形托盘是否被拆分为恰好两个彼此分离的托盘？

2. 拆分后的每个托盘是否都比原托盘更小？

3. 拆分后的两个托盘是否仍为金属材质？

4. 拆分后的两个托盘是否仍为空？


## 061 — `synthetic_embodied_021_E1`

**原始英文指令：** At 10.5 seconds, compress the remaining glass-filling process so the water reaches just below the rim by 15.5 seconds.

**中文翻译：** 在第 10.5 秒，加快剩余的玻璃杯注水过程，使水面在第 15.5 秒前达到杯沿下方不远处。

**状态：** 接受

**原子化判定句：**

1. 剩余的玻璃杯注水过程是否以更快的速度继续？

2. 水面是否在 5 秒内达到杯沿下方不远处？


## 062 — `synthetic_embodied_021_E2A`

**原始英文指令：** At 22.5 seconds, make the right hand wave twice beside the faucet over four seconds.

**中文翻译：** 在第 22.5 秒，让右手在水龙头旁于四秒内挥动两次。

**状态：** 接受

**原子化判定句：**

1. 右手是否在水龙头旁挥动？

2. 右手是否恰好挥动两次？

3. 两次挥动是否在 4 秒内完成？


## 063 — `synthetic_embodied_021_E2B`

**原始英文指令：** At 24.5 seconds, lower the viewpoint smoothly toward the filled glass's rim over three seconds.

**中文翻译：** 在第 24.5 秒，在三秒内将视点平滑降低至盛满水的玻璃杯杯沿附近。

**状态：** 接受

**原子化判定句：**

1. 视点是否降低至盛满水的玻璃杯杯沿附近？

2. 视点移动是否平滑？

3. 视点是否在 3 秒内到达杯沿附近？


## 064 — `synthetic_embodied_022_E1`

**原始英文指令：** At 13 seconds, make the held apple's skin wet with visible water droplets.

**中文翻译：** 在第 13 秒，让手中苹果的表皮变湿并带有可见水滴。

**状态：** 接受

**原子化判定句：**

1. 手中苹果的表皮是否变湿？

2. 苹果表皮上是否出现可见水滴？


## 065 — `synthetic_embodied_022_E2A`

**原始英文指令：** At 24.5 seconds, split the single apple into two separate halves with their cut faces visible.

**中文翻译：** 在第 24.5 秒，将一个苹果分成彼此分离的两半，并让切面可见。

**状态：** 接受

**原子化判定句：**

1. 一个苹果是否被分成彼此分离的两半？

2. 两半苹果的切面是否都清晰可见？


## 066 — `synthetic_embodied_022_E2B`

**原始英文指令：** At 26.5 seconds, set the right hand into a flat, fingers-together pose for three seconds.

**中文翻译：** 在第 26.5 秒，让右手保持平展、手指并拢的姿势三秒。

**状态：** 接受

**原子化判定句：**

1. 右手是否保持平展？

2. 右手手指是否并拢？

3. 这一姿势是否保持 3 秒？


## 067 — `synthetic_embodied_023_E1`

**原始英文指令：** At 16.5 seconds, make both hands alternately lift the brown duvet's near corners twice over four seconds.

**中文翻译：** 在第 16.5 秒，让双手在四秒内交替抬起棕色羽绒被的近侧两角两次。

**状态：** 接受

**原子化判定句：**

1. 双手是否抬起棕色羽绒被的近侧两角？

2. 双手是否交替抬起两角？

3. 是否恰好完成两次交替抬起？

4. 两次抬起是否在 4 秒内完成？


## 068 — `synthetic_embodied_023_E2A`

**原始英文指令：** At 26.5 seconds, replace the brown duvet beneath the hands with a thick rectangular foam cushion.

**中文翻译：** 在第 26.5 秒，将双手下方的棕色羽绒被替换为厚实的矩形泡沫垫。

**状态：** 接受

**原子化判定句：**

1. 双手下方的棕色羽绒被是否被替换为泡沫垫？

2. 替换后的泡沫垫是否厚实？

3. 替换后的泡沫垫是否为矩形？


## 069 — `synthetic_embodied_023_E2B`

**原始英文指令：** At 29.5 seconds, set both hands side by side, one palm-width apart, above the duvet for three seconds.

**中文翻译：** 在第 29.5 秒，让双手在羽绒被上方并排放置，相距一个手掌宽度，持续三秒。

**状态：** 接受

**原子化判定句：**

1. 双手是否在羽绒被上方并排保持 3 秒？

2. 双手是否在同一段 3 秒内保持相距一个手掌宽度？


## 070 — `synthetic_embodied_024_E1`

**原始英文指令：** At 19.5 seconds, position the visible right hand palm-down in the lower-center work area for three seconds.

**中文翻译：** 在第 19.5 秒，将可见的右手掌心向下放置在工作区下方中央，持续三秒。

**状态：** 接受

**原子化判定句：**

1. 可见的右手是否掌心向下放置在工作区下方中央？

2. 这一位置是否保持 3 秒？


## 071 — `synthetic_embodied_024_E2A`

**原始英文指令：** At 25.5 seconds, recolor the folded white cloth beneath the right hand to lavender purple.

**中文翻译：** 在第 25.5 秒，将右手下方折叠的白布改为薰衣草紫色。

**状态：** 接受

**原子化判定句：**

1. 右手下方折叠的白布是否被改为薰衣草紫色？


## 072 — `synthetic_embodied_024_E2B`

**原始英文指令：** At 28.5 seconds, make the right hand trace two small clockwise circles across the folded cloth over four seconds.

**中文翻译：** 在第 28.5 秒，让右手在四秒内沿折叠布料画两个小型顺时针圆圈。

**状态：** 接受

**原子化判定句：**

1. 右手是否在折叠布料上画小型圆圈？

2. 圆圈是否沿顺时针方向画出？

3. 右手是否恰好画两个圆圈？

4. 两个圆圈是否在 4 秒内完成？


## 073 — `synthetic_embodied_025_E1`

**原始英文指令：** At 13.5 seconds, give the windowsill watering scene warm amber highlights and softly muted shadows.

**中文翻译：** 在第 13.5 秒，为窗台浇水场景添加温暖的琥珀色高光和柔和低饱和的阴影。

**状态：** 接受

**原子化判定句：**

1. 窗台浇水场景是否具有温暖的琥珀色高光？

2. 该场景是否也具有柔和低饱和的阴影？


## 074 — `synthetic_embodied_025_E2A`

**原始英文指令：** At 23.5 seconds, recolor the dark green watering can in the right hand to bright yellow.

**中文翻译：** 在第 23.5 秒，将右手中的深绿色浇水壶改为亮黄色。

**状态：** 接受

**原子化判定句：**

1. 右手中的深绿色浇水壶是否被改为亮黄色？


## 075 — `synthetic_embodied_025_E2B`

**原始英文指令：** At 27.5 seconds, fuse the terracotta pot and its saucer into one continuous pedestal planter.

**中文翻译：** 在第 27.5 秒，将赤陶花盆及其托盘融合为一个连续一体的基座式花盆。

**状态：** 接受

**原子化判定句：**

1. 赤陶花盆及其托盘是否融合为一个花盆？

2. 融合后的花盆是否形成连续一体的结构？

3. 融合后的花盆是否呈基座式造型？


## 076 — `synthetic_embodied_026_E1`

**原始英文指令：** At 18.5 seconds, set the right hand into an open palm-up pose beside the art book for three seconds.

**中文翻译：** 在第 18.5 秒，让右手在画册旁保持张开且掌心向上的姿势三秒。

**状态：** 接受

**原子化判定句：**

1. 右手是否在画册旁保持张开且掌心向上？

2. 这一姿势是否保持 3 秒？


## 077 — `synthetic_embodied_026_E2A`

**原始英文指令：** At 22.5 seconds, change the brown wooden tabletop around the open book to a pale gray wood finish.

**中文翻译：** 在第 22.5 秒，将打开书本周围的棕色木桌面改为浅灰色木质饰面。

**状态：** 接受

**原子化判定句：**

1. 打开书本周围的棕色木桌面是否被改为浅灰色木质饰面？


## 078 — `synthetic_embodied_026_E2B`

**原始英文指令：** At 28 seconds, make the upper corners of the open art book's pages flutter gently for four seconds.

**中文翻译：** 在第 28 秒，让打开画册的书页上角轻轻翻动四秒。

**状态：** 接受

**原子化判定句：**

1. 打开画册的书页上角是否轻轻翻动？

2. 轻柔翻动是否持续 4 秒？


## 079 — `synthetic_embodied_027_E1`

**原始英文指令：** At 16.5 seconds, recolor the brown fabric bag resting on the lap to forest green.

**中文翻译：** 在第 16.5 秒，将放在腿上的棕色布袋改为森林绿色。

**状态：** 接受

**原子化判定句：**

1. 放在腿上的棕色布袋是否被改为森林绿色？


## 080 — `synthetic_embodied_027_E2A`

**原始英文指令：** At 25.5 seconds, replace the held black-framed eyeglasses with a plain folding magnifying glass.

**中文翻译：** 在第 25.5 秒，将手持的黑框眼镜替换为无图案的折叠式放大镜。

**状态：** 接受

**原子化判定句：**

1. 手持的黑框眼镜是否被替换为放大镜？

2. 替换后的放大镜是否可折叠？

3. 替换后的放大镜是否具有无图案的普通外观？


## 081 — `synthetic_embodied_027_E2B`

**原始英文指令：** At 29.5 seconds, make the right hand tap the open bag's near rim three times over four seconds.

**中文翻译：** 在第 29.5 秒，让右手在四秒内轻敲打开袋子的近侧边缘三次。

**状态：** 接受

**原子化判定句：**

1. 右手是否轻敲打开袋子的近侧边缘？

2. 右手是否恰好轻敲三次？

3. 三次轻敲是否在 4 秒内完成？


## 082 — `synthetic_embodied_028_E1`

**原始英文指令：** At 13 seconds, remove the perforated metal strainer insert from the left sink drain.

**中文翻译：** 在第 13 秒，从左侧水槽排水口移除带孔的金属滤网内件。

**状态：** 接受

**原子化判定句：**

1. 左侧水槽排水口中的带孔金属滤网内件是否被移除？


## 083 — `synthetic_embodied_028_E2A`

**原始英文指令：** At 24.5 seconds, set the faucet above the strawberry colander to its fully closed, non-flowing state.

**中文翻译：** 在第 24.5 秒，将草莓滤篮上方的水龙头设为完全关闭且不出水的状态。

**状态：** 接受

**原子化判定句：**

1. 草莓滤篮上方的水龙头是否完全关闭且没有水流出？


## 084 — `synthetic_embodied_028_E2B`

**原始英文指令：** At 27.5 seconds, orient the strawberry colander so its two blue handles point toward and away from the observer.

**中文翻译：** 在第 27.5 秒，调整草莓滤篮的方向，使两个蓝色把手分别朝向观察者和背离观察者。

**状态：** 接受

**原子化判定句：**

1. 草莓滤篮的一个蓝色把手是否朝向观察者？

2. 另一个蓝色把手是否背离观察者？


## 085 — `synthetic_embodied_029_E1`

**原始英文指令：** At 14 seconds, change the carried tray's silver metal finish to brushed copper.

**中文翻译：** 在第 14 秒，将携带托盘的银色金属饰面改为拉丝铜。

**状态：** 接受

**原子化判定句：**

1. 携带托盘的饰面是否从银色金属变为铜质外观？

2. 铜质饰面是否具有拉丝纹理？


## 086 — `synthetic_embodied_029_E2A`

**原始英文指令：** At 24.5 seconds, make the tray carrier walk with short shuffling steps for four seconds.

**中文翻译：** 在第 24.5 秒，让托盘携带者以短促拖步行走四秒。

**状态：** 接受

**原子化判定句：**

1. 托盘携带者是否以拖步行走？

2. 拖步是否短促？

3. 这种步态是否持续 4 秒？


## 087 — `synthetic_embodied_029_E2B`

**原始英文指令：** At 28.5 seconds, support both side edges of the brushed-copper tray from below with both palms for three seconds.

**中文翻译：** 在第 28.5 秒，用双手掌从下方托住拉丝铜托盘的两侧边缘，持续三秒。

**状态：** 接受

**原子化判定句：**

1. 左手掌是否从下方托住托盘的左侧边缘？

2. 右手掌是否从下方托住托盘的右侧边缘？

3. 这一托举状态是否保持 3 秒？


## 088 — `synthetic_embodied_030_E1`

**原始英文指令：** At 14.5 seconds, grip the two separated curtain edges from below with both hands for three seconds.

**中文翻译：** 在第 14.5 秒，用双手从下方握住分开的两侧窗帘边缘，持续三秒。

**状态：** 接受

**原子化判定句：**

1. 左手是否从下方握住分开的左侧窗帘边缘？

2. 右手是否从下方握住分开的右侧窗帘边缘？

3. 双手握持是否保持 3 秒？


## 089 — `synthetic_embodied_030_E2A`

**原始英文指令：** At 24.5 seconds, switch to a rear third-person view showing the observer between the two opened curtains.

**中文翻译：** 在第 24.5 秒，切换为后方第三人称视角，显示观察者位于两侧打开的窗帘之间。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为后方第三人称视角？

2. 该视角中是否能看到观察者位于两侧打开的窗帘之间？


## 090 — `synthetic_embodied_030_E2B`

**原始英文指令：** At 28 seconds, recolor the white painted window frame to dark navy blue.

**中文翻译：** 在第 28 秒，将白色涂漆窗框改为深海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 白色涂漆窗框是否被改为深海军蓝色？


## 091 — `synthetic_embodied_031_E1`

**原始英文指令：** At 14 seconds, switch to a rear-left over-the-shoulder view that includes both hands and the drawer front.

**中文翻译：** 在第 14 秒，切换为左后方越肩视角，将双手和抽屉正面纳入画面。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为左后方越肩视角？

2. 该视角是否将双手和抽屉正面纳入画面？


## 092 — `synthetic_embodied_031_E2A`

**原始英文指令：** At 21 seconds, make the left hand pull the drawer outward again over three seconds.

**中文翻译：** 在第 21 秒，让左手在三秒内再次将抽屉向外拉出。

**状态：** 接受

**原子化判定句：**

1. 左手是否再次将抽屉向外拉出？

2. 向外拉出的动作是否在 3 秒内完成？


## 093 — `synthetic_embodied_031_E2B`

**原始英文指令：** At 27.5 seconds, orient the curved silver drawer handle with its arch pointing upward.

**中文翻译：** 在第 27.5 秒，调整弯曲银色抽屉把手的方向，使其弧形部分朝上。

**状态：** 接受

**原子化判定句：**

1. 弯曲银色抽屉把手是否被调整为弧形部分朝上？


## 094 — `synthetic_embodied_032_E1`

**原始英文指令：** At 8 seconds, compress the current liquid-transfer process so the pour finishes at 12 seconds.

**中文翻译：** 在第 8 秒，加快当前液体转移过程，使倾倒在第 12 秒结束。

**状态：** 接受

**原子化判定句：**

1. 当前液体转移的倾倒过程是否以更快的速度继续？

2. 倾倒是否在 4 秒内结束？


## 095 — `synthetic_embodied_032_E2A`

**原始英文指令：** At 21.5 seconds, merge the two liquid-filled bottles into one wider bottle with a single opening.

**中文翻译：** 在第 21.5 秒，将两个装有液体的瓶子合并为一个具有单一开口的较宽瓶子。

**状态：** 接受

**原子化判定句：**

1. 两个装有液体的瓶子是否合并为一个瓶子？

2. 合并后的瓶子是否比原瓶子更宽？

3. 合并后的瓶子是否只有一个开口？


## 096 — `synthetic_embodied_032_E2B`

**原始英文指令：** At 22.5 seconds, orient the white dispenser pump on the left saucer with its nozzle pointing toward the observer.

**中文翻译：** 在第 22.5 秒，调整左侧托碟上白色分配泵的方向，使喷嘴朝向观察者。

**状态：** 接受

**原子化判定句：**

1. 左侧托碟上的白色分配泵是否被调整为喷嘴朝向观察者？


## 097 — `synthetic_embodied_033_E1`

**原始英文指令：** At 10.5 seconds, make the right hand pull the loose mandarin peel with three short tugs over four seconds.

**中文翻译：** 在第 10.5 秒，让右手在四秒内以三次短促拉动扯动松散的橘皮。

**状态：** 接受

**原子化判定句：**

1. 右手是否反复拉扯松散的橘皮？

2. 每次拉动是否短促？

3. 右手是否恰好拉动三次？

4. 三次拉动是否在 4 秒内完成？


## 098 — `synthetic_embodied_033_E2A`

**原始英文指令：** At 23 seconds, make the loose orange peel pieces on the plate dry, curled and brittle.

**中文翻译：** 在第 23 秒，让盘中的松散橙皮碎片变得干燥、卷曲且易碎。

**状态：** 接受

**原子化判定句：**

1. 盘中的松散橙皮碎片是否变得干燥？

2. 橙皮碎片是否卷曲？

3. 橙皮碎片是否呈现易碎状态？


## 099 — `synthetic_embodied_033_E2B`

**原始英文指令：** At 24.5 seconds, separate the mandarin on the white plate into two clusters of connected segments.

**中文翻译：** 在第 24.5 秒，将白盘中的橘子分成两簇，每簇内部的橘瓣仍相连。

**状态：** 接受

**原子化判定句：**

1. 白盘中的橘子是否被分成恰好两簇？

2. 每簇内部的橘瓣是否仍保持相连？


## 100 — `synthetic_embodied_034_E1`

**原始英文指令：** At 16 seconds, make both hands slide the lower dishwasher rack halfway inward and back out over four seconds.

**中文翻译：** 在第 16 秒，让双手在四秒内将洗碗机下层碗篮向内推至一半，再拉回外侧。

**状态：** 接受

**原子化判定句：**

1. 双手是否将洗碗机下层碗篮向内推至一半？

2. 随后双手是否将碗篮拉回外侧，并在 4 秒内完成这一往返动作？


## 101 — `synthetic_embodied_034_E2A`

**原始英文指令：** At 26 seconds, switch to a rear-right third-person view showing the operator, lower rack and countertop plate.

**中文翻译：** 在第 26 秒，切换为右后方第三人称视角，显示操作员、下层碗篮和台面上的盘子。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为右后方第三人称视角？

2. 该视角中是否能同时看到操作员、下层碗篮和台面上的盘子？


## 102 — `synthetic_embodied_034_E2B`

**原始英文指令：** At 29.5 seconds, fuse the two upright white plates in the lower rack into one oval serving platter.

**中文翻译：** 在第 29.5 秒，将下层碗篮中两个直立的白色盘子融合为一个椭圆形大餐盘。

**状态：** 接受

**原子化判定句：**

1. 下层碗篮中两个直立的白色盘子是否融合为一个大餐盘？

2. 融合后的大餐盘是否为椭圆形？


## 103 — `synthetic_embodied_035_E1`

**原始英文指令：** At 14.5 seconds, render the exposed white tabletop around the phone as a pale ink-wash painting.

**中文翻译：** 在第 14.5 秒，将手机周围露出的白色桌面呈现为浅色水墨画风格。

**状态：** 接受

**原子化判定句：**

1. 手机周围露出的白色桌面是否被呈现为水墨画风格？

2. 水墨画效果是否呈浅色？


## 104 — `synthetic_embodied_035_E2A`

**原始英文指令：** At 24.5 seconds, place the left thumb against the phone's upper-left corner for three seconds.

**中文翻译：** 在第 24.5 秒，将左手拇指贴在手机左上角并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 左手拇指是否贴在手机左上角？

2. 这一接触是否保持 3 秒？


## 105 — `synthetic_embodied_035_E2B`

**原始英文指令：** At 28 seconds, switch to a close rear-right over-the-shoulder view showing the phone and blue cloth.

**中文翻译：** 在第 28 秒，切换为近距离右后方越肩视角，显示手机和蓝色布料。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为近距离右后方越肩视角？

2. 该视角中是否能看到手机和蓝色布料？


## 106 — `synthetic_embodied_036_E1`

**原始英文指令：** At 15.5 seconds, place both palms on top of the mat roll near its center for three seconds.

**中文翻译：** 在第 15.5 秒，将双手掌放在垫卷顶部靠近中央的位置并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 双手掌是否放在垫卷顶部靠近中央的位置？

2. 双手掌是否在该处保持 3 秒？


## 107 — `synthetic_embodied_036_E2A`

**原始英文指令：** At 20 seconds, compress the remaining mat-rolling process so the entire mat is rolled by 22 seconds.

**中文翻译：** 在第 20 秒，加快剩余的卷垫过程，使整张垫子在第 22 秒前卷完。

**状态：** 接受

**原子化判定句：**

1. 剩余的卷垫过程是否以更快的速度继续？

2. 整张垫子是否在 2 秒内卷完？


## 108 — `synthetic_embodied_036_E2B`

**原始英文指令：** Starting at 28.5 seconds, make both hands pull the partially rolled blue mat once toward the observer over four seconds.

**中文翻译：** 从第 28.5 秒开始，让双手在四秒内将部分卷起的蓝色垫子朝观察者方向拉动一次。

**状态：** 接受

**原子化判定句：**

1. 双手是否将部分卷起的蓝色垫子朝观察者方向拉动？

2. 垫子是否恰好被拉动一次？

3. 拉动是否在 4 秒内完成？


## 109 — `synthetic_embodied_037_E1`

**原始英文指令：** At 14 seconds, add one plain wooden teaspoon on the tabletop immediately left of the lunchbox.

**中文翻译：** 在第 14 秒，在午餐盒紧邻左侧的桌面上添加一把无图案的木质茶匙。

**状态：** 接受

**原子化判定句：**

1. 午餐盒紧邻左侧的桌面上是否添加了恰好一把茶匙？

2. 新增茶匙是否为木质？

3. 新增茶匙是否无图案、外观普通？


## 110 — `synthetic_embodied_037_E2A`

**原始英文指令：** At 26.5 seconds, widen the framing to include the entire lunchbox, open lid and surrounding tabletop.

**中文翻译：** 在第 26.5 秒，扩大取景范围，将整个午餐盒、打开的盒盖和周围桌面纳入画面。

**状态：** 接受

**原子化判定句：**

1. 取景范围是否扩大？

2. 整个午餐盒是否被纳入扩大后的画面？

3. 打开的盒盖是否被纳入扩大后的画面？

4. 更多周围桌面是否被纳入扩大后的画面？


## 111 — `synthetic_embodied_037_E2B`

**原始英文指令：** At 26.5 seconds, make the right hand tap the lunchbox's front rim twice over three seconds.

**中文翻译：** 在第 26.5 秒，让右手在三秒内轻敲午餐盒前缘两次。

**状态：** 接受

**原子化判定句：**

1. 右手是否轻敲午餐盒前缘？

2. 右手是否恰好轻敲两次？

3. 两次轻敲是否在 3 秒内完成？


## 112 — `synthetic_embodied_038_E1`

**原始英文指令：** At 15 seconds, make the right hand wipe the right eyeglass lens with two vertical strokes over four seconds.

**中文翻译：** 在第 15 秒，让右手在四秒内用两次竖直擦拭动作清洁右侧眼镜镜片。

**状态：** 接受

**原子化判定句：**

1. 右手是否擦拭右侧眼镜镜片？

2. 擦拭轨迹是否为竖直方向？

3. 是否恰好完成两次擦拭？

4. 两次擦拭是否在 4 秒内完成？


## 113 — `synthetic_embodied_038_E2A`

**原始英文指令：** At 21 seconds, place the open glasses case directly behind the eyeglass bridge instead of to its right.

**中文翻译：** 在第 21 秒，将打开的眼镜盒放到眼镜鼻梁架正后方，而不是其右侧。

**状态：** 接受

**原子化判定句：**

1. 打开的眼镜盒是否被放到眼镜鼻梁架正后方而非其右侧？


## 114 — `synthetic_embodied_038_E2B`

**原始英文指令：** At 27.5 seconds, make both eyeglass lenses foggy with fine surface condensation.

**中文翻译：** 在第 27.5 秒，让两片眼镜镜片都因表面细小凝露而变得模糊。

**状态：** 接受

**原子化判定句：**

1. 第一片眼镜镜片是否因细小表面凝露而变得模糊？

2. 第二片眼镜镜片是否因细小表面凝露而变得模糊？


## 115 — `synthetic_embodied_039_E1`

**原始英文指令：** At 18.5 seconds, make the tied black refuse bag visibly dusty with pale gray powder.

**中文翻译：** 在第 18.5 秒，让扎紧的黑色垃圾袋明显沾有浅灰色粉尘。

**状态：** 接受

**原子化判定句：**

1. 扎紧的黑色垃圾袋是否明显沾有粉尘？

2. 粉尘是否为浅灰色？


## 116 — `synthetic_embodied_039_E2A`

**原始英文指令：** At 23 seconds, add one crumpled plain white paper ball inside the empty black bin.

**中文翻译：** 在第 23 秒，在空的黑色垃圾桶内添加一个揉皱的无图案白纸团。

**状态：** 接受

**原子化判定句：**

1. 空的黑色垃圾桶内是否添加了恰好一个白色纸团？

2. 纸团是否被揉皱？

3. 纸团是否无图案？


## 117 — `synthetic_embodied_039_E2B`

**原始英文指令：** At 32 seconds, make the left hand pat the empty bin's front rim twice over three seconds.

**中文翻译：** 在第 32 秒，让左手在三秒内轻拍空垃圾桶的前缘两次。

**状态：** 接受

**原子化判定句：**

1. 左手是否轻拍空垃圾桶的前缘？

2. 左手是否恰好轻拍两次？

3. 两次轻拍是否在 3 秒内完成？


## 118 — `synthetic_embodied_040_E1`

**原始英文指令：** At 15.5 seconds, remove the empty removable metal inner pot from inside the open cooker.

**中文翻译：** 在第 15.5 秒，从打开的电饭煲中移除空的可拆卸金属内锅。

**状态：** 接受

**原子化判定句：**

1. 打开的电饭煲中的空可拆卸金属内锅是否被移除？


## 119 — `synthetic_embodied_040_E2A`

**原始英文指令：** At 23.5 seconds, make the right hand lift the cooker lid back to its fully open position over three seconds.

**中文翻译：** 在第 23.5 秒，让右手在三秒内将电饭煲盖重新抬到完全打开的位置。

**状态：** 接受

**原子化判定句：**

1. 右手是否将电饭煲盖重新抬到完全打开的位置？

2. 锅盖是否在 3 秒内完全打开？


## 120 — `synthetic_embodied_040_E2B`

**原始英文指令：** At 28.5 seconds, make the exterior of the closed cooker lid wet with visible water beads.

**中文翻译：** 在第 28.5 秒，让关闭的电饭煲盖外表面变湿并带有可见水珠。

**状态：** 接受

**原子化判定句：**

1. 关闭的电饭煲盖外表面是否变湿？

2. 锅盖外表面是否出现可见水珠？


## 121 — `synthetic_embodied_041_E1`

**原始英文指令：** At 16 seconds, change the right hand to a three-finger precision grip around the black screwdriver handle for three seconds.

**中文翻译：** 在第 16 秒，让右手以三指精确握法握住黑色螺丝刀柄并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 右手是否以三指精确握法握住黑色螺丝刀柄？

2. 这一握法是否保持 3 秒？


## 122 — `synthetic_embodied_041_E2A`

**原始英文指令：** At 25.5 seconds, switch to a close over-the-shoulder view showing both hands and the lamp head.

**中文翻译：** 在第 25.5 秒，切换为近距离越肩视角，显示双手和灯头。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为近距离越肩视角？

2. 该视角中是否能看到双手和灯头？


## 123 — `synthetic_embodied_041_E2B`

**原始英文指令：** At 29 seconds, make the right hand twist the fitted light bulb a half-turn counterclockwise over three seconds.

**中文翻译：** 在第 29 秒，让右手在三秒内将已装入的灯泡逆时针旋转半圈。

**状态：** 接受

**原子化判定句：**

1. 右手是否旋转已装入的灯泡？

2. 灯泡是否沿逆时针方向旋转？

3. 旋转幅度是否为半圈？

4. 旋转是否在 3 秒内完成？


## 124 — `synthetic_embodied_042_E1`

**原始英文指令：** At 19.5 seconds, make the right hand rehearse one hammer stroke beside the nail without contact over two seconds.

**中文翻译：** 在第 19.5 秒，让右手在两秒内于钉子旁预演一次锤击动作，但不接触钉子。

**状态：** 接受

**原子化判定句：**

1. 右手是否在钉子旁预演锤击动作？

2. 是否恰好预演一次锤击？

3. 锤子是否未接触钉子？

4. 预演是否在 2 秒内完成？


## 125 — `synthetic_embodied_042_E2A`

**原始英文指令：** At 29.5 seconds, move the visible hammer from the right side into the upper-left frame quadrant for three seconds.

**中文翻译：** 在第 29.5 秒，将可见锤子从右侧移动到画面左上象限并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 可见锤子是否从右侧移动到画面左上象限？

2. 锤子是否在该处保持 3 秒？


## 126 — `synthetic_embodied_042_E2B`

**原始英文指令：** At 34.5 seconds, pause the nail-driving process at its current penetration depth for four seconds, then resume it.

**中文翻译：** 在第 34.5 秒，将钉钉过程停在当前钉入深度四秒，然后恢复。

**状态：** 接受

**原子化判定句：**

1. 钉钉过程是否将钉子继续钉入表面？

2. 钉钉过程是否在当前钉入深度暂停 4 秒？

3. 随后钉钉过程是否恢复？


## 127 — `synthetic_embodied_043_E1`

**原始英文指令：** At 15.5 seconds, position the existing screw at the center of the wooden board's right half.

**中文翻译：** 在第 15.5 秒，将现有螺钉放置在木板右半部分的中心。

**状态：** 接受

**原子化判定句：**

1. 现有螺钉是否被放置在木板右半部分的中心？


## 128 — `synthetic_embodied_043_E2A`

**原始英文指令：** At 25 seconds, make the wooden board beneath the screwdriver visibly damp with dark wet patches.

**中文翻译：** 在第 25 秒，让螺丝刀下方的木板明显变湿，并出现深色湿斑。

**状态：** 接受

**原子化判定句：**

1. 螺丝刀下方的木板是否明显变湿？

2. 木板上是否出现深色湿斑？


## 129 — `synthetic_embodied_043_E2B`

**原始英文指令：** At 29.5 seconds, make the right hand alternate clockwise and counterclockwise quarter-turns of the screwdriver for four seconds.

**中文翻译：** 在第 29.5 秒，让右手交替将螺丝刀顺时针和逆时针旋转四分之一圈，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 右手是否交替顺时针和逆时针旋转螺丝刀？

2. 每次旋转是否为四分之一圈？

3. 这一交替动作是否持续 4 秒？


## 130 — `synthetic_embodied_044_E1`

**原始英文指令：** At 13 seconds, add one small empty wooden shelf on the gray wall left of the blue paint strip.

**中文翻译：** 在第 13 秒，在蓝色涂漆条左侧的灰墙上添加一个小型空木架。

**状态：** 接受

**原子化判定句：**

1. 蓝色涂漆条左侧的灰墙上是否添加了恰好一个架子？

2. 新增架子是否小型？

3. 新增架子是否为木质？

4. 新增架子是否为空？


## 131 — `synthetic_embodied_044_E2A`

**原始英文指令：** At 23.5 seconds, make the gray wall left of the blue paint strip damp with irregular dark patches.

**中文翻译：** 在第 23.5 秒，让蓝色涂漆条左侧的灰墙变湿，并出现不规则深色斑块。

**状态：** 接受

**原子化判定句：**

1. 蓝色涂漆条左侧的灰墙是否变湿？

2. 墙上是否出现不规则深色斑块？


## 132 — `synthetic_embodied_044_E2B`

**原始英文指令：** At 26.5 seconds, make the green plant leaves at the right edge sway gently for four seconds.

**中文翻译：** 在第 26.5 秒，让右侧边缘的绿色植物叶片轻轻摆动四秒。

**状态：** 接受

**原子化判定句：**

1. 右侧边缘的绿色植物叶片是否轻轻摆动？

2. 轻柔摆动是否持续 4 秒？


## 133 — `synthetic_embodied_045_E1`

**原始英文指令：** At 14.5 seconds, make the central tree's lower branches sway broadly from side to side for four seconds.

**中文翻译：** 在第 14.5 秒，让中央树木的下部枝条大幅左右摆动四秒。

**状态：** 接受

**原子化判定句：**

1. 中央树木的下部枝条是否左右摆动？

2. 摆动幅度是否较大？

3. 摆动是否持续 4 秒？


## 134 — `synthetic_embodied_045_E2A`

**原始英文指令：** At 20 seconds, recolor the visible bark of the central tree trunk to pale cream.

**中文翻译：** 在第 20 秒，将中央树干的可见树皮改为浅奶油色。

**状态：** 接受

**原子化判定句：**

1. 中央树干的可见树皮是否被改为浅奶油色？


## 135 — `synthetic_embodied_045_E2B`

**原始英文指令：** At 27.5 seconds, tilt the viewpoint downward from the canopy toward the tree trunk over three seconds.

**中文翻译：** 在第 27.5 秒，在三秒内将视点从树冠向下倾斜至树干。

**状态：** 接受

**原子化判定句：**

1. 视点是否从树冠向下倾斜至树干？

2. 视点是否在 3 秒内到达树干视角？


## 136 — `synthetic_embodied_046_E1`

**原始英文指令：** At 16.5 seconds, make the right hand pull the tape-measure housing one palm-width farther right over three seconds.

**中文翻译：** 在第 16.5 秒，让右手在三秒内将卷尺外壳向右再拉一个手掌宽度。

**状态：** 接受

**原子化判定句：**

1. 右手是否将卷尺外壳向右再拉动？

2. 拉动距离是否为一个手掌宽度？

3. 拉动是否在 3 秒内完成？


## 137 — `synthetic_embodied_046_E2A`

**原始英文指令：** At 24.5 seconds, place the left index fingertip on top of the tape hook for three seconds.

**中文翻译：** 在第 24.5 秒，将左手食指指尖放在卷尺钩顶部并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 左手食指指尖是否放在卷尺钩顶部？

2. 这一接触是否保持 3 秒？


## 138 — `synthetic_embodied_046_E2B`

**原始英文指令：** At 29.5 seconds, pan the viewpoint gently rightward along the measuring tape over three seconds.

**中文翻译：** 在第 29.5 秒，在三秒内沿卷尺将视点轻柔地向右平移。

**状态：** 接受

**原子化判定句：**

1. 视点是否沿卷尺向右平移？

2. 平移动作是否轻柔？

3. 平移是否在 3 秒内完成？


## 139 — `synthetic_embodied_047_E1`

**原始英文指令：** At 14 seconds, move the visible soldering iron into the upper-right work area while retaining its angle for three seconds.

**中文翻译：** 在第 14 秒，将可见的烙铁移动到工作区右上方，同时保持其角度三秒。

**状态：** 接受

**原子化判定句：**

1. 可见的烙铁是否被移动到工作区右上方？

2. 烙铁是否保持原有角度并持续 3 秒？


## 140 — `synthetic_embodied_047_E2A`

**原始英文指令：** At 25.5 seconds, make the visible left hand draw the tweezers slightly leftward over three seconds.

**中文翻译：** 在第 25.5 秒，让可见的左手在三秒内将镊子稍微向左拉动。

**状态：** 接受

**原子化判定句：**

1. 可见的左手是否将镊子稍微向左拉动？

2. 拉动是否在 3 秒内完成？


## 141 — `synthetic_embodied_047_E2B`

**原始英文指令：** At 27.5 seconds, switch to a side third-person close-up of the operator's hands around the solder joint.

**中文翻译：** 在第 27.5 秒，切换为侧面第三人称特写，呈现焊点周围操作员的双手。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为侧面第三人称特写？

2. 该视角中是否呈现焊点周围操作员的双手？


## 142 — `synthetic_embodied_048_E1`

**原始英文指令：** At 15 seconds, make the right hand open and close the pliers twice over three seconds.

**中文翻译：** 在第 15 秒，让右手在三秒内将钳子张开并合拢两次。

**状态：** 接受

**原子化判定句：**

1. 右手是否将钳子张开并合拢？

2. 是否恰好完成两次张开—合拢循环？

3. 两次循环是否在 3 秒内完成？


## 143 — `synthetic_embodied_048_E2A`

**原始英文指令：** At 21 seconds, pause the wire-loop forming process at its current curvature for three seconds, then resume it.

**中文翻译：** 在第 21 秒，将金属线环成形过程停在当前曲率三秒，然后恢复。

**状态：** 接受

**原子化判定句：**

1. 金属线环成形过程是否继续改变金属线的形状？

2. 成形过程是否在当前曲率暂停 3 秒？

3. 随后金属线环成形过程是否恢复？


## 144 — `synthetic_embodied_048_E2B`

**原始英文指令：** At 27.5 seconds, place the held copper-colored wire one palm-width higher within the visible work area.

**中文翻译：** 在第 27.5 秒，将手持的铜色金属线在可见工作区内向上移动一个手掌宽度。

**状态：** 接受

**原子化判定句：**

1. 手持的铜色金属线是否向上移动？

2. 向上移动的距离是否为一个手掌宽度？

3. 移动后金属线是否仍位于可见工作区内？


## 145 — `synthetic_embodied_049_E1`

**原始英文指令：** At 13.5 seconds, set the left hand into a loose fist beside the mixing bowl for three seconds.

**中文翻译：** 在第 13.5 秒，让左手在搅拌碗旁保持松握拳姿势三秒。

**状态：** 接受

**原子化判定句：**

1. 左手是否在搅拌碗旁保持松握拳姿势？

2. 这一姿势是否保持 3 秒？


## 146 — `synthetic_embodied_049_E2A`

**原始英文指令：** At 24 seconds, make the right hand whisk the batter along a figure-eight path for four seconds.

**中文翻译：** 在第 24 秒，让右手沿八字形轨迹搅打面糊四秒。

**状态：** 接受

**原子化判定句：**

1. 右手是否沿八字形轨迹搅打面糊？

2. 这一搅打动作是否持续 4 秒？


## 147 — `synthetic_embodied_049_E2B`

**原始英文指令：** At 27.5 seconds, render the white mixing bowl as a clean black-outline cartoon object.

**中文翻译：** 在第 27.5 秒，将白色搅拌碗呈现为线条简洁的黑色轮廓卡通物体。

**状态：** 接受

**原子化判定句：**

1. 白色搅拌碗是否被呈现为黑色轮廓卡通物体？

2. 轮廓线条是否简洁清晰？


## 148 — `synthetic_embodied_050_E1`

**原始英文指令：** At 15.5 seconds, move the viewpoint through a short leftward arc around the plant's root ball over three seconds.

**中文翻译：** 在第 15.5 秒，在三秒内让视点绕植物根球沿短距离弧线向左移动。

**状态：** 接受

**原子化判定句：**

1. 视点是否绕植物根球沿弧线向左移动？

2. 移动弧线是否较短？

3. 移动是否在 3 秒内完成？


## 149 — `synthetic_embodied_050_E2A`

**原始英文指令：** At 26.5 seconds, make the loose soil around the root ball waterlogged with small reflective puddles.

**中文翻译：** 在第 26.5 秒，让根球周围的松散土壤积水饱和，并出现小型反光水洼。

**状态：** 接受

**原子化判定句：**

1. 根球周围的松散土壤是否呈积水饱和状态？

2. 土壤上是否出现水洼？

3. 水洼是否较小？

4. 水洼是否具有反光？


## 150 — `synthetic_embodied_050_E2B`

**原始英文指令：** At 29 seconds, render the observer's visible gardening hands in a cel-shaded animation style.

**中文翻译：** 在第 29 秒，将观察者可见的园艺双手呈现为赛璐璐着色动画风格。

**状态：** 接受

**原子化判定句：**

1. 观察者可见的园艺双手是否呈现为赛璐璐着色动画风格？


## 151 — `synthetic_embodied_051_E1`

**原始英文指令：** At 16 seconds, recolor the black metal crossbar and adjoining leg to cobalt blue.

**中文翻译：** 在第 16 秒，将黑色金属横杆及其相连支腿改为钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 黑色金属横杆是否改为钴蓝色？

2. 与横杆相连的黑色金属支腿是否改为钴蓝色？


## 152 — `synthetic_embodied_051_E2A`

**原始英文指令：** At 25.5 seconds, give the metal-frame assembly footage the soft scanlines and faded colors of a home videotape.

**中文翻译：** 在第 25.5 秒，为金属框架组装画面添加家庭录像带式的柔和扫描线和褪色色彩。

**状态：** 接受

**原子化判定句：**

1. 金属框架组装画面是否具有家庭录像带式的柔和扫描线？

2. 该画面是否也具有家庭录像带式的褪色色彩？


## 153 — `synthetic_embodied_051_E2B`

**原始英文指令：** At 29.5 seconds, add one loose silver washer on the gray work surface above the horizontal crossbar.

**中文翻译：** 在第 29.5 秒，在水平横杆上方的灰色工作面上添加一个散放的银色垫圈。

**状态：** 接受

**原子化判定句：**

1. 水平横杆上方的灰色工作面上是否添加了恰好一个垫圈？

2. 新增垫圈是否为银色？

3. 垫圈是否散放而未固定？


## 154 — `synthetic_embodied_052_E1`

**原始英文指令：** At 14.5 seconds, add one small round brass hook on the wall to the left of the picture frame.

**中文翻译：** 在第 14.5 秒，在画框左侧的墙上添加一个小型圆形黄铜挂钩。

**状态：** 接受

**原子化判定句：**

1. 画框左侧的墙上是否添加了恰好一个挂钩？

2. 新增挂钩是否小型？

3. 挂钩是否为圆形？

4. 挂钩是否为黄铜材质？


## 155 — `synthetic_embodied_052_E2A`

**原始英文指令：** At 23.5 seconds, make the left hand rock the picture frame clockwise and back once over four seconds.

**中文翻译：** 在第 23.5 秒，让左手在四秒内将画框顺时针摆动再摆回一次。

**状态：** 接受

**原子化判定句：**

1. 左手是否将画框顺时针摆动？

2. 画框是否随后摆回原方向一次？

3. 顺时针摆动并摆回的动作是否在 4 秒内完成？


## 156 — `synthetic_embodied_052_E2B`

**原始英文指令：** At 27.5 seconds, make the wooden picture-frame border dusty with a pale gray surface layer.

**中文翻译：** 在第 27.5 秒，让木质画框边框覆上一层浅灰色灰尘。

**状态：** 接受

**原子化判定句：**

1. 木质画框边框上是否出现灰尘表层？

2. 灰尘层是否为浅灰色？


## 157 — `synthetic_embodied_053_E1`

**原始英文指令：** At 14 seconds, make the loose curled wood shavings near the board's front edge tremble in place for four seconds.

**中文翻译：** 在第 14 秒，让木板前缘附近松散卷曲的木屑原地颤动四秒。

**状态：** 接受

**原子化判定句：**

1. 木板前缘附近松散卷曲的木屑是否原地颤动？

2. 颤动是否持续 4 秒？


## 158 — `synthetic_embodied_053_E2A`

**原始英文指令：** At 25.5 seconds, add one plain wooden pencil on the exposed workbench immediately left of the planed board.

**中文翻译：** 在第 25.5 秒，在刨光木板紧邻左侧的裸露工作台上添加一支无图案木铅笔。

**状态：** 接受

**原子化判定句：**

1. 刨光木板紧邻左侧的裸露工作台上是否添加了恰好一支铅笔？

2. 新增铅笔是否为木质？

3. 铅笔是否无图案？


## 159 — `synthetic_embodied_053_E2B`

**原始英文指令：** At 28.5 seconds, move the existing viewpoint slightly leftward along the workbench over three seconds.

**中文翻译：** 在第 28.5 秒，在三秒内将现有视点沿工作台稍微向左移动。

**状态：** 接受

**原子化判定句：**

1. 视点是否沿工作台稍微向左移动？

2. 移动是否在 3 秒内完成？


## 160 — `synthetic_embodied_054_E1`

**原始英文指令：** At 16 seconds, switch to a rear-left third-person view showing the operator's hands and the clamp jaws.

**中文翻译：** 在第 16 秒，切换为左后方第三人称视角，显示操作员的双手和夹具钳口。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为左后方第三人称视角？

2. 该视角中是否能看到操作员的双手和夹具钳口？


## 161 — `synthetic_embodied_054_E2A`

**原始英文指令：** At 24.5 seconds, make the exposed wooden board visibly wet with a darkened surface sheen.

**中文翻译：** 在第 24.5 秒，让裸露木板明显变湿，并带有变深的表面光泽。

**状态：** 接受

**原子化判定句：**

1. 裸露木板是否明显变湿？

2. 变湿后的木板是否带有变深的表面光泽？


## 162 — `synthetic_embodied_054_E2B`

**原始英文指令：** At 29 seconds, make the right hand squeeze and release the spring-clamp handles once over three seconds.

**中文翻译：** 在第 29 秒，让右手在三秒内挤压并松开弹簧夹手柄一次。

**状态：** 接受

**原子化判定句：**

1. 右手是否挤压弹簧夹手柄？

2. 右手是否随后松开手柄一次？

3. 挤压—松开循环是否在 3 秒内完成？


## 163 — `synthetic_embodied_055_E1`

**原始英文指令：** At 13.5 seconds, make the right hand lift the wrench off the nut and reseat it once over four seconds.

**中文翻译：** 在第 13.5 秒，让右手在四秒内将扳手从螺母上抬起，再重新套回一次。

**状态：** 接受

**原子化判定句：**

1. 右手是否将扳手从螺母上抬起？

2. 随后右手是否将扳手重新套回螺母，并在 4 秒内完成这一动作序列？


## 164 — `synthetic_embodied_055_E2A`

**原始英文指令：** At 23.5 seconds, orient the folded gray cloth at the back of the workbench with its long edge running front to back.

**中文翻译：** 在第 23.5 秒，调整工作台后部折叠灰布的方向，使其长边沿前后方向延伸。

**状态：** 接受

**原子化判定句：**

1. 工作台后部折叠的灰布是否被调整为长边沿前后方向延伸？


## 165 — `synthetic_embodied_055_E2B`

**原始英文指令：** At 27.5 seconds, remove the folded gray cloth from the workbench behind the brass pipe.

**中文翻译：** 在第 27.5 秒，从黄铜管后方的工作台上移除折叠灰布。

**状态：** 接受

**原子化判定句：**

1. 黄铜管后方工作台上的折叠灰布是否被移除？


## 166 — `synthetic_embodied_056_E1`

**原始英文指令：** At 15 seconds, place the upright floor pump one base-width farther left on the workshop floor.

**中文翻译：** 在第 15 秒，将直立式落地打气筒在工作间地面上向左移动一个底座宽度。

**状态：** 接受

**原子化判定句：**

1. 直立式落地打气筒是否在工作间地面上向左移动？

2. 移动距离是否为一个底座宽度？


## 167 — `synthetic_embodied_056_E2A`

**原始英文指令：** At 24.5 seconds, widen the framing to include both pumping hands and more of the bicycle wheel.

**中文翻译：** 在第 24.5 秒，扩大取景范围，将两只打气的手和更多自行车轮纳入画面。

**状态：** 接受

**原子化判定句：**

1. 取景范围是否扩大并将两只打气的手纳入画面？

2. 扩大后的画面是否也包含更多自行车轮？


## 168 — `synthetic_embodied_056_E2B`

**原始英文指令：** At 28 seconds, replace the rectangular black floor mat near the cabinets with a shallow wicker basket.

**中文翻译：** 在第 28 秒，将橱柜附近的黑色矩形地垫替换为一个浅口柳条篮。

**状态：** 接受

**原子化判定句：**

1. 橱柜附近的黑色矩形地垫是否被替换为篮子？

2. 替换后的篮子是否为浅口？

3. 替换后的篮子是否为柳条材质？


## 169 — `synthetic_embodied_057_E1`

**原始英文指令：** At 14.5 seconds, make the green crop leaves along the right bed edge sway together for four seconds.

**中文翻译：** 在第 14.5 秒，让右侧种植畦边缘的绿色作物叶片一起摆动四秒。

**状态：** 接受

**原子化判定句：**

1. 右侧种植畦边缘的绿色作物叶片是否一起摆动？

2. 共同摆动是否持续 4 秒？


## 170 — `synthetic_embodied_057_E2A`

**原始英文指令：** At 25 seconds, make the bare soil ahead of the rake dark and damp with visible clumps.

**中文翻译：** 在第 25 秒，让耙子前方的裸土变得深暗湿润，并带有可见土块。

**状态：** 接受

**原子化判定句：**

1. 耙子前方的裸土是否变暗？

2. 裸土是否变得湿润？

3. 裸土中是否出现可见土块？


## 171 — `synthetic_embodied_057_E2B`

**原始英文指令：** At 28.5 seconds, add one plain orange hand trowel on the soil beside the left wooden border.

**中文翻译：** 在第 28.5 秒，在左侧木质边框旁的土壤上添加一把无图案橙色手铲。

**状态：** 接受

**原子化判定句：**

1. 左侧木质边框旁的土壤上是否添加了恰好一把手铲？

2. 新增手铲是否为橙色？

3. 手铲是否无图案？


## 172 — `synthetic_embodied_058_E1`

**原始英文指令：** At 16 seconds, make the wall scraper's metal blade heavily oxidized with orange rust.

**中文翻译：** 在第 16 秒，让墙面刮刀的金属刀片严重氧化并布满橙色锈迹。

**状态：** 接受

**原子化判定句：**

1. 墙面刮刀的金属刀片是否呈严重氧化状态？

2. 刀片上是否布满橙色锈迹？


## 173 — `synthetic_embodied_058_E2A`

**原始英文指令：** At 26 seconds, make the right hand scrape the wall with two short horizontal strokes over four seconds.

**中文翻译：** 在第 26 秒，让右手在四秒内用两次短促的水平动作刮擦墙面。

**状态：** 接受

**原子化判定句：**

1. 右手是否刮擦墙面？

2. 刮擦动作是否短促且沿水平方向？

3. 是否恰好完成两次刮擦？

4. 两次刮擦是否在 4 秒内完成？


## 174 — `synthetic_embodied_058_E2B`

**原始英文指令：** At 29.5 seconds, move the rusted scraper into the upper-right frame region while retaining its angle for three seconds.

**中文翻译：** 在第 29.5 秒，将生锈的刮刀移动到画面右上区域，同时保持其角度三秒。

**状态：** 接受

**原子化判定句：**

1. 生锈的刮刀是否被移动到画面右上区域？

2. 刮刀是否保持原有角度并持续 3 秒？


## 175 — `synthetic_embodied_059_E1`

**原始英文指令：** At 12.5 seconds, replace the manual wire-stripping pliers with a self-adjusting automatic wire stripper.

**中文翻译：** 在第 12.5 秒，将手动剥线钳替换为自调节自动剥线器。

**状态：** 接受

**原子化判定句：**

1. 手动剥线钳是否被替换为自动剥线器？

2. 替换后的剥线器是否能够自调节？


## 176 — `synthetic_embodied_059_E2A`

**原始英文指令：** At 22.5 seconds, make the wire stripper's exposed metal jaws visibly corroded with orange rust.

**中文翻译：** 在第 22.5 秒，让剥线器裸露的金属钳口明显腐蚀并带有橙色锈迹。

**状态：** 接受

**原子化判定句：**

1. 剥线器裸露的金属钳口是否明显腐蚀？

2. 钳口上是否出现橙色锈迹？


## 177 — `synthetic_embodied_059_E2B`

**原始英文指令：** At 23.5 seconds, pause the red wire's insulation-stripping process at its current exposed length for three seconds, then resume it.

**中文翻译：** 在第 23.5 秒，将红色电线的绝缘层剥除过程停在当前裸露长度三秒，然后恢复。

**状态：** 接受

**原子化判定句：**

1. 绝缘层剥除过程是否使红色电线露出更多？

2. 剥除过程是否在当前裸露长度暂停 3 秒？

3. 随后绝缘层剥除过程是否恢复？


## 178 — `synthetic_embodied_060_E1`

**原始英文指令：** At 15 seconds, remove the uppermost silver lug nut from the exposed wheel hub.

**中文翻译：** 在第 15 秒，从裸露的轮毂上移除最上方的银色车轮螺母。

**状态：** 接受

**原子化判定句：**

1. 裸露轮毂上最上方的银色车轮螺母是否被移除？


## 179 — `synthetic_embodied_060_E2A`

**原始英文指令：** At 24.5 seconds, switch to a close over-the-shoulder view of the mechanic's hands at the exposed wheel hub.

**中文翻译：** 在第 24.5 秒，切换为近距离越肩视角，呈现裸露轮毂处机械师的双手。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为近距离越肩视角？

2. 该视角中是否呈现裸露轮毂处机械师的双手？


## 180 — `synthetic_embodied_060_E2B`

**原始英文指令：** At 28.5 seconds, increase the light illuminating the exposed brake assembly to a brighter neutral-white level.

**中文翻译：** 在第 28.5 秒，将照亮裸露制动组件的光线增强至更明亮的中性白色水平。

**状态：** 接受

**原子化判定句：**

1. 照亮裸露制动组件的光线是否变得更明亮？

2. 照明颜色是否变为中性白色？


## 181 — `synthetic_embodied_061_E1`

**原始英文指令：** At 14.5 seconds, change the forest trail's illumination to warm low-angle sunlight.

**中文翻译：** 在第 14.5 秒，将森林小径的照明改为温暖的低角度阳光。

**状态：** 接受

**原子化判定句：**

1. 森林小径是否由暖色阳光照亮？

2. 阳光是否以低角度照射？


## 182 — `synthetic_embodied_061_E2A`

**原始英文指令：** At 24 seconds, switch to a raised rear third-person view following the cyclist along the forest path.

**中文翻译：** 在第 24 秒，切换为抬高的后方第三人称视角，沿森林小径跟随骑行者。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为抬高的后方第三人称视角？

2. 该视角是否沿森林小径跟随骑行者？


## 183 — `synthetic_embodied_061_E2B`

**原始英文指令：** At 28.5 seconds, halve the cyclist's forward riding speed along the narrow path for four seconds.

**中文翻译：** 在第 28.5 秒，将骑行者沿狭窄小径向前骑行的速度减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 骑行者是否继续沿狭窄小径向前骑行？

2. 骑行者的前进速度是否减半？

3. 减半后的速度是否持续 4 秒？


## 184 — `synthetic_embodied_062_E1`

**原始英文指令：** At 15.5 seconds, tilt the viewpoint slightly downward toward the motorcycle handlebars over three seconds.

**中文翻译：** 在第 15.5 秒，在三秒内将视点稍微向下倾斜至摩托车车把。

**状态：** 接受

**原子化判定句：**

1. 视点是否稍微向下倾斜至摩托车车把？

2. 倾斜是否在 3 秒内完成？


## 185 — `synthetic_embodied_062_E2A`

**原始英文指令：** At 22.5 seconds, add one small round rear-view mirror above the left motorcycle handlebar.

**中文翻译：** 在第 22.5 秒，在摩托车左车把上方添加一个小型圆形后视镜。

**状态：** 接受

**原子化判定句：**

1. 摩托车左车把上方是否添加了恰好一个后视镜？

2. 新增后视镜是否小型？

3. 后视镜是否为圆形？


## 186 — `synthetic_embodied_062_E2B`

**原始英文指令：** At 29 seconds, set the rider's left thumb into an outward-pointing pose for three seconds.

**中文翻译：** 在第 29 秒，让骑行者左手拇指保持向外指的姿势三秒。

**状态：** 接受

**原子化判定句：**

1. 骑行者左手拇指是否向外指？

2. 这一姿势是否保持 3 秒？


## 187 — `synthetic_embodied_063_E1`

**原始英文指令：** At 14 seconds, switch to a raised rear-left over-the-shoulder view of the rider and road ahead.

**中文翻译：** 在第 14 秒，切换为抬高的左后方越肩视角，呈现骑行者和前方道路。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为抬高的左后方越肩视角？

2. 该视角中是否能看到骑行者和前方道路？


## 188 — `synthetic_embodied_063_E2A`

**原始英文指令：** At 22.5 seconds, halve the handlebar rider's forward travel speed along the riverside road for four seconds.

**中文翻译：** 在第 22.5 秒，将车把骑行者沿河滨道路向前行进的速度减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 车把骑行者是否继续沿河滨道路向前行进？

2. 骑行者的前进速度是否减半？

3. 减半后的速度是否持续 4 秒？


## 189 — `synthetic_embodied_063_E2B`

**原始英文指令：** At 27.5 seconds, make the road surface immediately ahead of the rider wet and reflective.

**中文翻译：** 在第 27.5 秒，让骑行者正前方的道路表面变湿并具有反光效果。

**状态：** 接受

**原子化判定句：**

1. 骑行者正前方的道路表面是否变湿？

2. 变湿后的道路表面是否具有反光效果？


## 190 — `synthetic_embodied_064_E1`

**原始英文指令：** At 14.5 seconds, render the forklift steering wheel in a bold comic-book ink style.

**中文翻译：** 在第 14.5 秒，将叉车方向盘呈现为粗犷的漫画墨线风格。

**状态：** 接受

**原子化判定句：**

1. 叉车方向盘是否被呈现为漫画墨线风格？

2. 该风格的线条是否粗犷醒目？


## 191 — `synthetic_embodied_064_E2A`

**原始英文指令：** At 21 seconds, recolor the yellow horizontal forklift cabin rail to orange-red.

**中文翻译：** 在第 21 秒，将黄色的叉车驾驶室水平栏杆改为橙红色。

**状态：** 接受

**原子化判定句：**

1. 黄色的叉车驾驶室水平栏杆是否被改为橙红色？


## 192 — `synthetic_embodied_064_E2B`

**原始英文指令：** At 28.5 seconds, change the driver's left hand to an underhand grip beneath the steering-wheel rim for three seconds.

**中文翻译：** 在第 28.5 秒，让驾驶员左手以反手握法握住方向盘轮缘下方并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 驾驶员左手是否在方向盘轮缘下方形成反手握法？

2. 这一握持是否保持 3 秒？


## 193 — `synthetic_embodied_065_E1`

**原始英文指令：** At 16 seconds, recolor the white boat console housing to pale mint green.

**中文翻译：** 在第 16 秒，将白色船舶控制台外壳改为浅薄荷绿色。

**状态：** 接受

**原子化判定句：**

1. 白色船舶控制台外壳是否被改为浅薄荷绿色？


## 194 — `synthetic_embodied_065_E2A`

**原始英文指令：** At 24.5 seconds, tighten the framing around the boat console to emphasize the steering wheel and three gauges.

**中文翻译：** 在第 24.5 秒，收紧船舶控制台周围的取景，突出方向盘和三个仪表。

**状态：** 接受

**原子化判定句：**

1. 船舶控制台周围的取景是否收紧？

2. 收紧后的画面是否突出方向盘和全部三个仪表？


## 195 — `synthetic_embodied_065_E2B`

**原始英文指令：** At 29.5 seconds, make the right hand tap the steering-wheel center twice over three seconds.

**中文翻译：** 在第 29.5 秒，让右手在三秒内轻敲方向盘中心两次。

**状态：** 接受

**原子化判定句：**

1. 右手是否轻敲方向盘中心？

2. 右手是否恰好轻敲两次？

3. 两次轻敲是否在 3 秒内完成？


## 196 — `synthetic_embodied_066_E1`

**原始英文指令：** At 14.5 seconds, lower the viewing angle slightly toward the blue kayak bow over three seconds.

**中文翻译：** 在第 14.5 秒，在三秒内将观看角度稍微向下移至蓝色皮划艇船首。

**状态：** 接受

**原子化判定句：**

1. 观看角度是否稍微向下移至蓝色皮划艇船首？

2. 向下移动是否在 3 秒内完成？


## 197 — `synthetic_embodied_066_E2A`

**原始英文指令：** At 24.5 seconds, change the kayak scene's illumination to cool diffuse overcast daylight.

**中文翻译：** 在第 24.5 秒，将皮划艇场景的照明改为冷色、漫射的阴天日光。

**状态：** 接受

**原子化判定句：**

1. 皮划艇场景是否由阴天日光照亮？

2. 日光色调是否偏冷？

3. 照明是否呈漫射状态？


## 198 — `synthetic_embodied_066_E2B`

**原始英文指令：** At 28.5 seconds, remove the black circular hatch cover from the kayak foredeck.

**中文翻译：** 在第 28.5 秒，从皮划艇前甲板移除黑色圆形舱盖。

**状态：** 接受

**原子化判定句：**

1. 皮划艇前甲板上的黑色圆形舱盖是否被移除？


## 199 — `synthetic_embodied_067_E1`

**原始英文指令：** At 13 seconds, make the large white sail visibly wet with irregular darker patches.

**中文翻译：** 在第 13 秒，让白色大帆明显变湿，并出现不规则深色斑块。

**状态：** 接受

**原子化判定句：**

1. 白色大帆是否明显变湿？

2. 帆面上是否出现深色斑块？

3. 深色斑块是否呈不规则形状？


## 200 — `synthetic_embodied_067_E2A`

**原始英文指令：** At 21.5 seconds, make both hands pull the sail-rope bundle with two short downward tugs over four seconds.

**中文翻译：** 在第 21.5 秒，让双手在四秒内用两次短促向下拉动牵拉帆绳束。

**状态：** 接受

**原子化判定句：**

1. 双手是否向下拉动帆绳束？

2. 向下拉动是否短促？

3. 是否恰好完成两次拉动？

4. 两次拉动是否在 4 秒内完成？


## 201 — `synthetic_embodied_067_E2B`

**原始英文指令：** At 26.5 seconds, replace the middle dark deck-hatch cover with a rectangular brass ventilation grille.

**中文翻译：** 在第 26.5 秒，将中间的深色甲板舱盖替换为矩形黄铜通风格栅。

**状态：** 接受

**原子化判定句：**

1. 中间的深色甲板舱盖是否被替换为通风格栅？

2. 替换后的格栅是否为矩形？

3. 替换后的格栅是否为黄铜材质？


## 202 — `synthetic_embodied_068_E1`

**原始英文指令：** At 15.5 seconds, set the two snowmobile handguards one glove-width farther apart.

**中文翻译：** 在第 15.5 秒，将雪地摩托的两个护手之间的距离再拉开一个手套宽度。

**状态：** 接受

**原子化判定句：**

1. 雪地摩托的两个护手是否被拉得更开？

2. 护手间距是否增加了一个手套宽度？


## 203 — `synthetic_embodied_068_E2A`

**原始英文指令：** At 24.5 seconds, halve the rider and snowmobile's forward travel speed for four seconds.

**中文翻译：** 在第 24.5 秒，将骑行者和雪地摩托向前行进的速度减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 骑行者和雪地摩托是否继续向前行进？

2. 其向前行进速度是否减半？

3. 减半后的速度是否持续 4 秒？


## 204 — `synthetic_embodied_068_E2B`

**原始英文指令：** At 29 seconds, change the snowy trail's illumination to warm sunlight with long soft shadows.

**中文翻译：** 在第 29 秒，将雪地小径的照明改为温暖阳光，并产生修长柔和的阴影。

**状态：** 接受

**原子化判定句：**

1. 雪地小径是否由温暖阳光照亮？

2. 这种照明是否产生修长柔和的阴影？


## 205 — `synthetic_embodied_069_E1`

**原始英文指令：** At 16.5 seconds, replace the ATV's black front luggage rack with a shallow wooden cargo tray.

**中文翻译：** 在第 16.5 秒，将全地形车的黑色前行李架替换为浅口木质载货托盘。

**状态：** 接受

**原子化判定句：**

1. 全地形车的黑色前行李架是否被替换为载货托盘？

2. 替换后的托盘是否为浅口？

3. 替换后的托盘是否为木质？


## 206 — `synthetic_embodied_069_E2A`

**原始英文指令：** At 25.5 seconds, position the rider's visible right hand palm-forward in the upper-center frame region for three seconds.

**中文翻译：** 在第 25.5 秒，将骑行者可见的右手以掌心朝前的姿势放在画面上方中央区域并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 骑行者可见的右手是否以掌心朝前的姿势放在画面上方中央区域？

2. 这一姿势是否保持 3 秒？


## 207 — `synthetic_embodied_069_E2B`

**原始英文指令：** At 30 seconds, make the wooden cargo tray on the ATV visibly wet with dark patches and a water sheen.

**中文翻译：** 在第 30 秒，让全地形车上的木质载货托盘明显变湿，并出现深色斑块和水光。

**状态：** 接受

**原子化判定句：**

1. 全地形车上的木质载货托盘是否明显变湿？

2. 托盘上是否出现深色湿斑？

3. 托盘表面是否出现水光？


## 208 — `synthetic_embodied_070_E1`

**原始英文指令：** At 15 seconds, raise the viewing angle slightly toward the field horizon over three seconds.

**中文翻译：** 在第 15 秒，在三秒内将观看角度稍微抬高至田野地平线。

**状态：** 接受

**原子化判定句：**

1. 观看角度是否稍微抬高至田野地平线？

2. 抬高是否在 3 秒内完成？


## 209 — `synthetic_embodied_070_E2A`

**原始英文指令：** At 25.5 seconds, make the driver's left hand tap the tractor steering-wheel center twice over three seconds.

**中文翻译：** 在第 25.5 秒，让驾驶员左手在三秒内轻敲拖拉机方向盘中心两次。

**状态：** 接受

**原子化判定句：**

1. 驾驶员左手是否轻敲拖拉机方向盘中心？

2. 左手是否恰好轻敲两次？

3. 两次轻敲是否在 3 秒内完成？


## 210 — `synthetic_embodied_070_E2B`

**原始英文指令：** At 28.5 seconds, make the tractor's front windshield wet with scattered transparent rain droplets.

**中文翻译：** 在第 28.5 秒，让拖拉机前挡风玻璃变湿，并散布透明雨滴。

**状态：** 接受

**原子化判定句：**

1. 拖拉机前挡风玻璃是否变湿？

2. 挡风玻璃上是否散布雨滴？

3. 雨滴是否透明？


## 211 — `synthetic_embodied_071_E1`

**原始英文指令：** At 14.5 seconds, halve the cyclist's pedaling cadence along the city road for four seconds.

**中文翻译：** 在第 14.5 秒，将骑行者沿城市道路骑行的踩踏频率减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 骑行者是否继续沿城市道路踩踏骑行？

2. 骑行者的踩踏频率是否减半？

3. 减半后的踩踏频率是否持续 4 秒？


## 212 — `synthetic_embodied_071_E2A`

**原始英文指令：** At 24 seconds, make the small front bicycle basket visibly rusted along its metal wires.

**中文翻译：** 在第 24 秒，让自行车前方小篮子的金属丝明显生锈。

**状态：** 接受

**原子化判定句：**

1. 自行车前方小篮子的金属丝是否明显生锈？


## 213 — `synthetic_embodied_071_E2B`

**原始英文指令：** At 28.5 seconds, set the front wire basket one palm-width farther forward from the bicycle handlebars.

**中文翻译：** 在第 28.5 秒，将前方金属丝篮从自行车车把向前再移动一个手掌宽度。

**状态：** 接受

**原子化判定句：**

1. 前方金属丝篮是否从自行车车把向前移动？

2. 向前移动的距离是否为一个手掌宽度？


## 214 — `synthetic_embodied_072_E1`

**原始英文指令：** At 13 seconds, make the train cab's two windshield wipers perform one synchronized sweep and return over three seconds.

**中文翻译：** 在第 13 秒，让列车驾驶室的两根雨刷在三秒内同步完成一次刮动并返回。

**状态：** 接受

**原子化判定句：**

1. 列车驾驶室的两根雨刷是否完成一次刮动并返回？

2. 两根雨刷是否同步运动？

3. 刮动并返回是否在 3 秒内完成？


## 215 — `synthetic_embodied_072_E2A`

**原始英文指令：** At 23.5 seconds, add one small plain suction-cup hook to the lower-right corner of the train cab windshield.

**中文翻译：** 在第 23.5 秒，在列车驾驶室挡风玻璃右下角添加一个小型无图案吸盘挂钩。

**状态：** 接受

**原子化判定句：**

1. 列车驾驶室挡风玻璃右下角是否添加了恰好一个吸盘挂钩？

2. 新增挂钩是否小型？

3. 挂钩是否外观普通、无图案？


## 216 — `synthetic_embodied_072_E2B`

**原始英文指令：** At 27.5 seconds, change the train cab scene's illumination to warm directional sunlight.

**中文翻译：** 在第 27.5 秒，将列车驾驶室场景的照明改为温暖的定向阳光。

**状态：** 接受

**原子化判定句：**

1. 列车驾驶室场景是否由暖色阳光照亮？

2. 阳光是否具有明确的照射方向？


## 217 — `synthetic_embodied_073_E1`

**原始英文指令：** At 16.5 seconds, recolor the snowblower's black engine housing to bright orange.

**中文翻译：** 在第 16.5 秒，将扫雪机的黑色发动机外壳改为亮橙色。

**状态：** 接受

**原子化判定句：**

1. 扫雪机的黑色发动机外壳是否被改为亮橙色？


## 218 — `synthetic_embodied_073_E2A`

**原始英文指令：** At 25 seconds, make the observer push the snowblower forward at half the walking pace for four seconds.

**中文翻译：** 在第 25 秒，让观察者以正常步行速度的一半向前推动扫雪机四秒。

**状态：** 接受

**原子化判定句：**

1. 观察者是否向前推动扫雪机？

2. 推动速度是否为正常步行速度的一半？

3. 这一速度是否持续 4 秒？


## 219 — `synthetic_embodied_073_E2B`

**原始英文指令：** At 29.5 seconds, set the snowblower's left and right wheels half a wheel-width farther apart.

**中文翻译：** 在第 29.5 秒，将扫雪机左右车轮之间的距离再拉开半个轮宽。

**状态：** 接受

**原子化判定句：**

1. 扫雪机左右车轮是否被拉得更开？

2. 车轮间距是否增加了半个轮宽？


## 220 — `synthetic_embodied_074_E1`

**原始英文指令：** At 15 seconds, give the lawn-mower footage the warm grain and gentle flicker of eight-millimeter home film.

**中文翻译：** 在第 15 秒，为割草机画面添加 8 毫米家庭胶片式的暖色颗粒和轻柔闪烁。

**状态：** 接受

**原子化判定句：**

1. 割草机画面是否具有 8 毫米家庭胶片式的暖色颗粒？

2. 该画面是否也具有 8 毫米家庭胶片式的轻柔闪烁？


## 221 — `synthetic_embodied_074_E2A`

**原始英文指令：** At 23.5 seconds, recolor the small red mower traveling ahead to bright turquoise.

**中文翻译：** 在第 23.5 秒，将前方行驶的小型红色割草机改为亮青绿色。

**状态：** 接受

**原子化判定句：**

1. 前方行驶的小型红色割草机是否被改为亮青绿色？


## 222 — `synthetic_embodied_074_E2B`

**原始英文指令：** At 28.5 seconds, place the driver's left hand at the top of the lawn-mower steering wheel for three seconds.

**中文翻译：** 在第 28.5 秒，将驾驶员左手放在割草机方向盘顶部并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 驾驶员左手是否放在割草机方向盘顶部？

2. 左手是否在该处保持 3 秒？


## 223 — `synthetic_embodied_075_E1`

**原始英文指令：** At 16 seconds, make the transport cart's black upright rails visibly corroded with patchy orange rust.

**中文翻译：** 在第 16 秒，让运输车的黑色直立栏杆明显腐蚀，并出现斑驳橙色锈迹。

**状态：** 接受

**原子化判定句：**

1. 运输车的黑色直立栏杆是否明显腐蚀？

2. 栏杆上是否出现斑驳橙色锈迹？


## 224 — `synthetic_embodied_075_E2A`

**原始英文指令：** At 25.5 seconds, widen the framing around the transport cart to include more floor beside both pushing hands.

**中文翻译：** 在第 25.5 秒，扩大运输车周围的取景范围，将两只推车手旁边更多地面纳入画面。

**状态：** 接受

**原子化判定句：**

1. 运输车周围的取景范围是否扩大？

2. 左侧推车手旁是否显示出更多地面？

3. 右侧推车手旁是否显示出更多地面？


## 225 — `synthetic_embodied_075_E2B`

**原始英文指令：** At 29.5 seconds, add one small blue mesh pouch hanging beneath the transport cart's right handle section.

**中文翻译：** 在第 29.5 秒，在运输车右侧把手区域下方添加一个悬挂的小型蓝色网袋。

**状态：** 接受

**原子化判定句：**

1. 运输车右侧把手区域下方是否添加了恰好一个袋子？

2. 袋子是否悬挂在该区域？

3. 袋子是否小型？

4. 袋子是否为蓝色网状材质？


## 226 — `synthetic_embodied_076_E1`

**原始英文指令：** At 13.5 seconds, remove the wooden bench along the courtyard wall left of the circular flower bed.

**中文翻译：** 在第 13.5 秒，移除圆形花坛左侧庭院墙边的木质长凳。

**状态：** 接受

**原子化判定句：**

1. 圆形花坛左侧庭院墙边的木质长凳是否被移除？


## 227 — `synthetic_embodied_076_E2A`

**原始英文指令：** At 24.5 seconds, make the rider and handlebar vehicle travel straight backward one meter over four seconds.

**中文翻译：** 在第 24.5 秒，让骑行者和车把式车辆在四秒内沿直线向后移动一米。

**状态：** 接受

**原子化判定句：**

1. 骑行者和车把式车辆是否沿直线向后移动？

2. 向后移动的距离是否为 1 米？

3. 移动是否在 4 秒内完成？


## 228 — `synthetic_embodied_076_E2B`

**原始英文指令：** At 27.5 seconds, change the courtyard's illumination to warm late-afternoon sunlight with longer tree shadows.

**中文翻译：** 在第 27.5 秒，将庭院照明改为温暖的傍晚阳光，并产生更长的树影。

**状态：** 接受

**原子化判定句：**

1. 庭院是否由温暖的傍晚阳光照亮？

2. 这种照明是否产生更长的树影？


## 229 — `synthetic_embodied_077_E1`

**原始英文指令：** At 15 seconds, recolor the floor cleaner's black console housing to light gray.

**中文翻译：** 在第 15 秒，将洗地机的黑色控制台外壳改为浅灰色。

**状态：** 接受

**原子化判定句：**

1. 洗地机的黑色控制台外壳是否被改为浅灰色？


## 230 — `synthetic_embodied_077_E2A`

**原始英文指令：** At 24.5 seconds, render the corridor wall and tiled floor as a soft watercolor background.

**中文翻译：** 在第 24.5 秒，将走廊墙面和瓷砖地面呈现为柔和的水彩背景。

**状态：** 接受

**原子化判定句：**

1. 走廊墙面是否被呈现为柔和的水彩背景？

2. 瓷砖地面是否被呈现为柔和的水彩背景？


## 231 — `synthetic_embodied_077_E2B`

**原始英文指令：** At 28 seconds, make the operator's right fingers drum three times on the cleaning machine's steering-wheel rim.

**中文翻译：** 在第 28 秒，让操作员右手手指在清洁机器方向盘轮缘上敲击三次。

**状态：** 接受

**原子化判定句：**

1. 操作员右手手指是否敲击清洁机器方向盘轮缘？

2. 右手手指是否恰好敲击三次？


## 232 — `synthetic_embodied_078_E1`

**原始英文指令：** At 15.5 seconds, render the entire loader-cab scene as a low-poly construction-simulator image.

**中文翻译：** 在第 15.5 秒，将整个装载机驾驶室场景呈现为低多边形工程模拟器画面。

**状态：** 接受

**原子化判定句：**

1. 整个装载机驾驶室场景是否被呈现为工程模拟器画面？

2. 画面是否采用低多边形视觉风格？


## 233 — `synthetic_embodied_078_E2A`

**原始英文指令：** At 23.5 seconds, position the operator's visible right hand palm-forward in the upper-right cabin area for three seconds.

**中文翻译：** 在第 23.5 秒，将操作员可见的右手以掌心朝前的姿势放在驾驶室右上区域并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 操作员可见的右手是否以掌心朝前的姿势放在驾驶室右上区域？

2. 这一姿势是否保持 3 秒？


## 234 — `synthetic_embodied_078_E2B`

**原始英文指令：** At 29 seconds, pan the viewpoint slightly rightward within the loader cab over three seconds.

**中文翻译：** 在第 29 秒，在三秒内将视点在装载机驾驶室内稍微向右平移。

**状态：** 接受

**原子化判定句：**

1. 视点是否在装载机驾驶室内稍微向右平移？

2. 平移是否在 3 秒内完成？


## 235 — `synthetic_embodied_079_E1`

**原始英文指令：** At 16 seconds, add one plain yellow cleaning cloth draped over the lift platform's left side rail.

**中文翻译：** 在第 16 秒，在升降平台左侧栏杆上添加一块搭挂着的无图案黄色清洁布。

**状态：** 接受

**原子化判定句：**

1. 升降平台左侧栏杆上是否添加了一块清洁布？

2. 清洁布是否搭挂在栏杆上？

3. 清洁布是否为黄色？

4. 清洁布是否无图案？


## 236 — `synthetic_embodied_079_E2A`

**原始英文指令：** At 25.5 seconds, give the elevated-platform footage the monochrome grain of an archival newsreel.

**中文翻译：** 在第 25.5 秒，为高空平台画面添加档案新闻纪录片式的单色颗粒感。

**状态：** 接受

**原子化判定句：**

1. 高空平台画面是否具有档案新闻纪录片风格？

2. 画面是否为单色？

3. 画面是否具有可见颗粒感？


## 237 — `synthetic_embodied_079_E2B`

**原始英文指令：** At 29.5 seconds, recolor the lift platform's orange tubular guardrails to bright white.

**中文翻译：** 在第 29.5 秒，将升降平台的橙色管状护栏改为亮白色。

**状态：** 接受

**原子化判定句：**

1. 升降平台的橙色管状护栏是否被改为亮白色？


## 238 — `synthetic_embodied_080_E1`

**原始英文指令：** At 14.5 seconds, switch to a rear-left third-person view following the dog walker and the leashed dog.

**中文翻译：** 在第 14.5 秒，切换为左后方第三人称视角，跟随遛狗者和被牵绳的狗。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为左后方第三人称视角？

2. 该视角是否同时跟随遛狗者和被牵绳的狗？


## 239 — `synthetic_embodied_080_E2A`

**原始英文指令：** At 24.5 seconds, make the dog walker take shorter forward steps for four seconds along the snowy path.

**中文翻译：** 在第 24.5 秒，让遛狗者沿雪地小径以更短的步幅向前行走四秒。

**状态：** 接受

**原子化判定句：**

1. 遛狗者是否继续沿雪地小径向前行走？

2. 遛狗者的前进步幅是否变短？

3. 较短步幅的行走是否持续 4 秒？


## 240 — `synthetic_embodied_080_E2B`

**原始英文指令：** At 28.5 seconds, recolor the leash connecting the dog walker and dog from blue to bright red.

**中文翻译：** 在第 28.5 秒，将连接遛狗者与狗的牵绳从蓝色改为亮红色。

**状态：** 接受

**原子化判定句：**

1. 连接遛狗者与狗的牵绳是否从蓝色改为亮红色？


## 241 — `synthetic_embodied_081_E1`

**原始英文指令：** At 15 seconds, render the kitchen drawer and bowl scene as a colored-pencil illustration.

**中文翻译：** 在第 15 秒，将厨房抽屉和碗的场景呈现为彩色铅笔插画。

**状态：** 接受

**原子化判定句：**

1. 厨房抽屉和碗的场景是否呈现为彩色铅笔插画？


## 242 — `synthetic_embodied_081_E2A`

**原始英文指令：** At 23.5 seconds, place the left palm directly beneath the lifted bowl's base for three seconds.

**中文翻译：** 在第 23.5 秒，将左手掌直接放在抬起碗的底部下方并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 左手掌是否直接放在抬起碗的底部下方？

2. 左手掌是否在该处保持 3 秒？


## 243 — `synthetic_embodied_081_E2B`

**原始英文指令：** At 28 seconds, switch to a close right-side third-person view of the person, countertop bowl and open drawer.

**中文翻译：** 在第 28 秒，切换为近距离右侧第三人称视角，呈现人物、台面上的碗和打开的抽屉。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为近距离右侧第三人称视角？

2. 该视角中是否能同时看到人物、台面上的碗和打开的抽屉？


## 244 — `synthetic_embodied_082_E1`

**原始英文指令：** At 14 seconds, switch to an over-the-shoulder view showing the sweeper's hands, broom and dustpan.

**中文翻译：** 在第 14 秒，切换为越肩视角，显示清扫者的双手、扫帚和簸箕。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为越肩视角？

2. 该视角中是否能同时看到清扫者的双手、扫帚和簸箕？


## 245 — `synthetic_embodied_082_E2A`

**原始英文指令：** At 23.5 seconds, change the floor's illumination around the dustpan to brighter cool-white overhead light.

**中文翻译：** 在第 23.5 秒，将簸箕周围地面的照明改为更明亮的冷白色顶光。

**状态：** 接受

**原子化判定句：**

1. 簸箕周围地面的照明是否变得更明亮？

2. 照明颜色是否变为冷白色？

3. 光线是否从上方照射？


## 246 — `synthetic_embodied_082_E2B`

**原始英文指令：** At 28.5 seconds, make the right hand arc the broom outward to the right and back once over three seconds.

**中文翻译：** 在第 28.5 秒，让右手在三秒内将扫帚沿弧线向右外侧移动再返回一次。

**状态：** 接受

**原子化判定句：**

1. 右手是否将扫帚沿弧线向右外侧移动？

2. 扫帚是否随后返回一次？

3. 向外移动并返回的动作是否在 3 秒内完成？


## 247 — `synthetic_embodied_083_E1`

**原始英文指令：** At 13 seconds, terminate watering the terracotta plant pot early at fifteen seconds, leaving the process unfinished.

**中文翻译：** 在第 13 秒开始编辑，于第 15 秒提前停止给赤陶花盆浇水，使浇水过程保持未完成。

**状态：** 接受

**原子化判定句：**

1. 是否正在给赤陶花盆浇水？

2. 浇水是否在 2 秒后停止？

3. 浇水停止时，该过程是否仍未完成？


## 248 — `synthetic_embodied_083_E2A`

**原始英文指令：** At 23 seconds, tighten the framing around the plant pot to emphasize the pooled water surface.

**中文翻译：** 在第 23 秒，收紧花盆周围的取景，以突出积水表面。

**状态：** 接受

**原子化判定句：**

1. 花盆周围的取景是否收紧？

2. 收紧后的画面是否突出积水表面？


## 249 — `synthetic_embodied_083_E2B`

**原始英文指令：** At 26.5 seconds, make the potted plant's leaves sway gently from side to side for four seconds.

**中文翻译：** 在第 26.5 秒，让盆栽植物的叶片轻轻左右摆动四秒。

**状态：** 接受

**原子化判定句：**

1. 盆栽植物的叶片是否轻轻左右摆动？

2. 摆动是否持续 4 秒？


## 250 — `synthetic_embodied_084_E1`

**原始英文指令：** At 16 seconds, switch to a raised rear third-person view following the person carrying the food tray.

**中文翻译：** 在第 16 秒，切换为抬高的后方第三人称视角，跟随携带食物托盘的人物。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为抬高的后方第三人称视角？

2. 该视角是否跟随携带食物托盘的人物？


## 251 — `synthetic_embodied_084_E2A`

**原始英文指令：** At 24.5 seconds, halve the tray carrier's walking pace through the cafe for four seconds.

**中文翻译：** 在第 24.5 秒，将托盘携带者穿过咖啡馆的步行速度减半，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 托盘携带者是否继续穿过咖啡馆行走？

2. 托盘携带者的步行速度是否减半？

3. 减半后的速度是否持续 4 秒？


## 252 — `synthetic_embodied_084_E2B`

**原始英文指令：** At 29.5 seconds, apply a cool desaturated color grade with lifted shadows to the cafe image.

**中文翻译：** 在第 29.5 秒，为咖啡馆画面应用冷色低饱和调色，并提亮阴影。

**状态：** 接受

**原子化判定句：**

1. 咖啡馆画面是否应用了冷色低饱和调色？

2. 咖啡馆画面的阴影是否被提亮？


## 253 — `synthetic_embodied_085_E1`

**原始英文指令：** At 13.5 seconds, replace the clamped wooden block with a short hollow square aluminum tube.

**中文翻译：** 在第 13.5 秒，将夹紧的木块替换为一根短的中空方形铝管。

**状态：** 接受

**原子化判定句：**

1. 夹紧的木块是否被替换为铝管？

2. 替换后的铝管是否较短？

3. 铝管是否中空？

4. 铝管的截面是否为方形？


## 254 — `synthetic_embodied_085_E2A`

**原始英文指令：** At 26 seconds, place the blue bench vise one base-width farther left along the workbench edge.

**中文翻译：** 在第 26 秒，将蓝色台虎钳沿工作台边缘向左再移动一个底座宽度。

**状态：** 接受

**原子化判定句：**

1. 蓝色台虎钳是否沿工作台边缘向左移动？

2. 移动距离是否为一个底座宽度？


## 255 — `synthetic_embodied_085_E2B`

**原始英文指令：** At 28.5 seconds, make the left hand trace one small circle above the clamped aluminum tube over three seconds.

**中文翻译：** 在第 28.5 秒，让左手在三秒内于夹紧的铝管上方画一个小圆圈。

**状态：** 接受

**原子化判定句：**

1. 左手是否在夹紧的铝管上方画圆圈？

2. 圆圈是否较小？

3. 是否恰好画一个圆圈？

4. 圆圈是否在 3 秒内完成？


## 256 — `synthetic_embodied_086_E1`

**原始英文指令：** At 15 seconds, grip the shopping-basket handle from below with the left hand for three seconds.

**中文翻译：** 在第 15 秒，用左手从下方握住购物篮把手并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 左手是否从下方握住购物篮把手？

2. 这一握持是否保持 3 秒？


## 257 — `synthetic_embodied_086_E2A`

**原始英文指令：** At 24.5 seconds, make the right fingers tap the red shopping-basket rim twice over three seconds.

**中文翻译：** 在第 24.5 秒，让右手手指在三秒内轻敲红色购物篮边缘两次。

**状态：** 接受

**原子化判定句：**

1. 右手手指是否轻敲红色购物篮边缘？

2. 右手手指是否恰好轻敲两次？

3. 两次轻敲是否在 3 秒内完成？


## 258 — `synthetic_embodied_086_E2B`

**原始英文指令：** At 28 seconds, apply a soft pastel color grade with reduced contrast to the shopping-aisle image.

**中文翻译：** 在第 28 秒，为购物过道画面应用柔和的粉彩调色并降低对比度。

**状态：** 接受

**原子化判定句：**

1. 购物过道画面是否应用了柔和的粉彩调色？

2. 画面对比度是否降低？


## 259 — `synthetic_embodied_087_E1`

**原始英文指令：** At 16.5 seconds, add one plain blue ribbon tied around the sealed cardboard parcel.

**中文翻译：** 在第 16.5 秒，在密封纸板包裹外添加一条系好的无图案蓝色丝带。

**状态：** 接受

**原子化判定句：**

1. 密封纸板包裹外是否添加了恰好一条丝带？

2. 丝带是否系在包裹外？

3. 丝带是否为蓝色？

4. 丝带是否无图案？


## 260 — `synthetic_embodied_087_E2A`

**原始英文指令：** At 25.5 seconds, set both index fingers into a downward-pointing pose above the delivered parcel for three seconds.

**中文翻译：** 在第 25.5 秒，让两根食指在已送达包裹上方保持向下指的姿势三秒。

**状态：** 接受

**原子化判定句：**

1. 左手食指是否在已送达包裹上方向下指？

2. 右手食指是否在包裹上方向下指？

3. 两根食指的姿势是否保持 3 秒？


## 261 — `synthetic_embodied_087_E2B`

**原始英文指令：** At 30 seconds, make the parcel carrier bend into a shallow squat and rise once over four seconds.

**中文翻译：** 在第 30 秒，让包裹携带者在四秒内屈身做一次浅蹲并站起。

**状态：** 接受

**原子化判定句：**

1. 包裹携带者是否屈身进入浅蹲姿势？

2. 包裹携带者是否随后站起复位？

3. 浅蹲并站起是否在 4 秒内完成一次？


## 262 — `synthetic_embodied_088_E1`

**原始英文指令：** At 14.5 seconds, render the entire plant-watering workstation scene in a clean cel-shaded animation style.

**中文翻译：** 在第 14.5 秒，将整个植物浇水工作台场景呈现为简洁的赛璐璐着色动画风格。

**状态：** 接受

**原子化判定句：**

1. 整个植物浇水工作台场景是否被呈现为赛璐璐着色动画风格？

2. 该风格是否呈现简洁清晰的观感？


## 263 — `synthetic_embodied_088_E2A`

**原始英文指令：** At 24.5 seconds, make the large green leaves above the black pot flutter gently for four seconds.

**中文翻译：** 在第 24.5 秒，让黑色花盆上方的绿色大叶片轻轻摆动四秒。

**状态：** 接受

**原子化判定句：**

1. 黑色花盆上方的绿色大叶片是否轻轻摆动？

2. 轻柔摆动是否持续 4 秒？


## 264 — `synthetic_embodied_088_E2B`

**原始英文指令：** At 28.5 seconds, remove the silver watering can behind the blue irrigation valve.

**中文翻译：** 在第 28.5 秒，移除蓝色灌溉阀后方的银色浇水壶。

**状态：** 接受

**原子化判定句：**

1. 蓝色灌溉阀后方的银色浇水壶是否被移除？


## 265 — `synthetic_embodied_089_E1`

**原始英文指令：** At 16 seconds, recolor the dark blue mug on the wooden counter to deep violet.

**中文翻译：** 在第 16 秒，将木质柜台上的深蓝色杯子改为深紫色。

**状态：** 接受

**原子化判定句：**

1. 木质柜台上的深蓝色杯子是否被改为深紫色？


## 266 — `synthetic_embodied_089_E2A`

**原始英文指令：** At 24.5 seconds, switch to a close left-side third-person view of the person loading the serving cart.

**中文翻译：** 在第 24.5 秒，切换为近距离左侧第三人称视角，呈现正在装载送餐车的人物。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为近距离左侧第三人称视角？

2. 该视角中是否呈现正在装载送餐车的人物？


## 267 — `synthetic_embodied_089_E2B`

**原始英文指令：** At 29.5 seconds, split the white plate into two separate semicircular pieces lying flat on the serving cart.

**中文翻译：** 在第 29.5 秒，将白色盘子分成两个彼此分离的半圆形部分，并使其平放在送餐车上。

**状态：** 接受

**原子化判定句：**

1. 白色盘子是否被分成两个彼此分离的半圆形部分？

2. 两个部分是否都平放在送餐车上？


## 268 — `synthetic_embodied_090_E1`

**原始英文指令：** At 13.5 seconds, make the right hand wave once from side to side above the traffic cone over three seconds.

**中文翻译：** 在第 13.5 秒，让右手在三秒内于交通锥上方左右挥动一次。

**状态：** 接受

**原子化判定句：**

1. 右手是否在交通锥上方左右挥动？

2. 右手是否恰好完成一次挥动循环？

3. 挥动循环是否在 3 秒内完成？


## 269 — `synthetic_embodied_090_E2A`

**原始英文指令：** At 23.5 seconds, remove the transparent windshield panel between the utility vehicle's front posts.

**中文翻译：** 在第 23.5 秒，移除多用途车前立柱之间的透明挡风玻璃面板。

**状态：** 接受

**原子化判定句：**

1. 多用途车前立柱之间的透明挡风玻璃面板是否被移除？


## 270 — `synthetic_embodied_090_E2B`

**原始英文指令：** At 28.5 seconds, place the utility vehicle's steering wheel one palm-width lower in front of the seated driver.

**中文翻译：** 在第 28.5 秒，将多用途车方向盘在坐着的驾驶员前方向下移动一个手掌宽度。

**状态：** 接受

**原子化判定句：**

1. 多用途车方向盘是否在坐着的驾驶员前方向下移动？

2. 向下移动的距离是否为一个手掌宽度？


## 271 — `synthetic_embodied_091_E1`

**原始英文指令：** At 16.5 seconds, tilt the viewing direction slightly upward toward the ceiling pipes over three seconds.

**中文翻译：** 在第 16.5 秒，在三秒内将观看方向稍微向上倾斜至天花板管道。

**状态：** 接受

**原子化判定句：**

1. 观看方向是否稍微向上倾斜至天花板管道？

2. 倾斜是否在 3 秒内完成？


## 272 — `synthetic_embodied_091_E2A`

**原始英文指令：** At 25.5 seconds, make the observer take one short backward step from the electrical cabinet over two seconds.

**中文翻译：** 在第 25.5 秒，让观察者在两秒内从电气柜前向后迈一个短步。

**状态：** 接受

**原子化判定句：**

1. 观察者是否从电气柜前向后迈一个短步？

2. 这一步是否在 2 秒内完成？


## 273 — `synthetic_embodied_091_E2B`

**原始英文指令：** At 29.5 seconds, make the open electrical-cabinet door dusty with a pale gray surface layer.

**中文翻译：** 在第 29.5 秒，让打开的电气柜门覆上一层浅灰色灰尘。

**状态：** 接受

**原子化判定句：**

1. 打开的电气柜门上是否出现灰尘表层？

2. 灰尘层是否为浅灰色？


## 274 — `synthetic_embodied_092_E1`

**原始英文指令：** At 17.5 seconds, make both gloved hands shift the level baking tray left and back once over three seconds.

**中文翻译：** 在第 17.5 秒，让戴手套的双手在三秒内将保持水平的烤盘向左移动再移回一次。

**状态：** 接受

**原子化判定句：**

1. 戴手套的双手是否在保持烤盘水平的同时将其向左移动？

2. 烤盘是否随后移回一次？

3. 烤盘移回时是否仍保持水平？

4. 向左移动并移回的动作是否在 3 秒内完成？


## 275 — `synthetic_embodied_092_E2A`

**原始英文指令：** At 23 seconds, recolor the metal baking tray carrying four dough pieces to deep cobalt blue.

**中文翻译：** 在第 23 秒，将承载四块面团的金属烤盘改为深钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 承载四块面团的金属烤盘是否被改为深钴蓝色？


## 276 — `synthetic_embodied_092_E2B`

**原始英文指令：** At 23.5 seconds, render the baker's visible oven mitts in a bold black-outline comic style.

**中文翻译：** 在第 23.5 秒，将烘焙者可见的隔热手套呈现为粗黑轮廓漫画风格。

**状态：** 接受

**原子化判定句：**

1. 烘焙者可见的隔热手套是否被呈现为漫画风格？

2. 该风格是否使用粗黑轮廓线？


## 277 — `synthetic_embodied_093_E1`

**原始英文指令：** At 14.5 seconds, give the held log a white bark pattern with dark horizontal flecks.

**中文翻译：** 在第 14.5 秒，为手持木柴添加带有深色水平斑点的白色树皮纹理。

**状态：** 接受

**原子化判定句：**

1. 手持木柴是否具有白色树皮纹理？

2. 树皮纹理中是否带有深色水平斑点？


## 278 — `synthetic_embodied_093_E2A`

**原始英文指令：** At 23.5 seconds, render the fire-ring stones in a crisp pencil-sketch style.

**中文翻译：** 在第 23.5 秒，将火圈石块呈现为清晰的铅笔素描风格。

**状态：** 接受

**原子化判定句：**

1. 火圈石块是否被呈现为铅笔素描风格？

2. 素描效果是否清晰利落？


## 279 — `synthetic_embodied_093_E2B`

**原始英文指令：** At 28.5 seconds, make the log outside the fire ring rock gently in place for four seconds.

**中文翻译：** 在第 28.5 秒，让火圈外的木柴原地轻轻摇动四秒。

**状态：** 接受

**原子化判定句：**

1. 火圈外的木柴是否原地轻轻摇动？

2. 摇动是否持续 4 秒？


## 280 — `synthetic_embodied_094_E1`

**原始英文指令：** At 16 seconds, recolor the wooden guardrails around the seaside viewing platform to muted teal.

**中文翻译：** 在第 16 秒，将海边观景平台周围的木质护栏改为柔和的蓝绿色。

**状态：** 接受

**原子化判定句：**

1. 海边观景平台周围的木质护栏是否被改为柔和的蓝绿色？


## 281 — `synthetic_embodied_094_E2A`

**原始英文指令：** At 25.5 seconds, render the entire seaside viewing-platform image as a pastel chalk illustration.

**中文翻译：** 在第 25.5 秒，将整个海边观景平台画面呈现为粉彩粉笔插画。

**状态：** 接受

**原子化判定句：**

1. 整个海边观景平台画面是否呈现为粉彩粉笔插画？


## 282 — `synthetic_embodied_094_E2B`

**原始英文指令：** At 29.5 seconds, make the observer take two short backward steps inside the viewing platform over four seconds.

**中文翻译：** 在第 29.5 秒，让观察者在四秒内于观景平台内向后迈两个短步。

**状态：** 接受

**原子化判定句：**

1. 观察者是否在观景平台内向后迈步？

2. 后退步是否短小？

3. 观察者是否恰好迈出两步？

4. 两步是否在 4 秒内完成？


## 283 — `synthetic_embodied_095_E1`

**原始英文指令：** At 15.5 seconds, make the green and orange fruit inside the cardboard box wet with visible water droplets.

**中文翻译：** 在第 15.5 秒，让纸板箱内的绿色和橙色水果变湿并带有可见水滴。

**状态：** 接受

**原子化判定句：**

1. 纸板箱内的绿色水果是否变湿并带有可见水滴？

2. 纸板箱内的橙色水果是否变湿并带有可见水滴？


## 284 — `synthetic_embodied_095_E2A`

**原始英文指令：** At 24.5 seconds, tighten the framing around the carried fruit box and both supporting hands.

**中文翻译：** 在第 24.5 秒，收紧携带水果箱及两只托举手周围的取景。

**状态：** 接受

**原子化判定句：**

1. 携带水果箱周围的取景是否收紧？

2. 收紧后的画面是否包含整个水果箱？

3. 画面是否包含左侧托举手？

4. 画面是否包含右侧托举手？


## 285 — `synthetic_embodied_095_E2B`

**原始英文指令：** At 28.5 seconds, render the produce carrier's visible hands and forearms in a charcoal-drawing style.

**中文翻译：** 在第 28.5 秒，将农产品携带者可见的双手和前臂呈现为炭笔画风格。

**状态：** 接受

**原子化判定句：**

1. 农产品携带者可见的双手是否被呈现为炭笔画风格？

2. 可见的前臂是否也被呈现为相同的炭笔画风格？


## 286 — `synthetic_embodied_096_E1`

**原始英文指令：** At 15 seconds, recolor the blue laboratory gloves on both visible hands to deep purple.

**中文翻译：** 在第 15 秒，将两只可见手上的蓝色实验室手套改为深紫色。

**状态：** 接受

**原子化判定句：**

1. 可见左手上的蓝色实验室手套是否改为深紫色？

2. 可见右手上的蓝色实验室手套是否改为深紫色？


## 287 — `synthetic_embodied_096_E2A`

**原始英文指令：** At 24.5 seconds, split the clear tube rack into two smaller racks standing side by side on the work mat.

**中文翻译：** 在第 24.5 秒，将透明试管架拆分为两个较小的试管架，并排立在工作垫上。

**状态：** 接受

**原子化判定句：**

1. 透明试管架是否被拆分为两个较小的试管架？

2. 两个较小试管架是否并排立在工作垫上？


## 288 — `synthetic_embodied_096_E2B`

**原始英文指令：** At 28 seconds, move the viewpoint through a short rightward arc around the held laboratory tube over three seconds.

**中文翻译：** 在第 28 秒，在三秒内让视点绕手持实验室试管沿短距离弧线向右移动。

**状态：** 接受

**原子化判定句：**

1. 视点是否绕手持实验室试管沿弧线向右移动？

2. 移动弧线是否较短？

3. 移动是否在 3 秒内完成？


## 289 — `synthetic_embodied_097_E1`

**原始英文指令：** At 12.5 seconds, remove the highest horizontal rung below the ladder's black top caps.

**中文翻译：** 在第 12.5 秒，移除梯子黑色顶盖下方最高的一根水平横档。

**状态：** 接受

**原子化判定句：**

1. 梯子黑色顶盖下方最高的一根水平横档是否被移除？


## 290 — `synthetic_embodied_097_E2A`

**原始英文指令：** At 23.5 seconds, switch to a rear third-person view showing the observer facing the leaning ladder.

**中文翻译：** 在第 23.5 秒，切换为后方第三人称视角，显示观察者面向倾斜靠放的梯子。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为后方第三人称视角？

2. 该视角中是否显示观察者面向倾斜靠放的梯子？


## 291 — `synthetic_embodied_097_E2B`

**原始英文指令：** At 26.5 seconds, change the ladder scene's illumination to warm side lighting with a stronger wall shadow.

**中文翻译：** 在第 26.5 秒，将梯子场景的照明改为温暖的侧光，并产生更明显的墙面阴影。

**状态：** 接受

**原子化判定句：**

1. 梯子场景是否由温暖的侧光照亮？

2. 这种照明是否产生更明显的墙面阴影？


## 292 — `synthetic_embodied_098_E1`

**原始英文指令：** At 16 seconds, place the loaded blue wheelbarrow half a wheel-width farther left inside the wooden bay.

**中文翻译：** 在第 16 秒，将装有物品的蓝色手推车在木质隔间内向左再移动半个轮宽。

**状态：** 接受

**原子化判定句：**

1. 装有物品的蓝色手推车是否在木质隔间内向左移动？

2. 移动距离是否为半个轮宽？

3. 移动后手推车是否仍位于木质隔间内？


## 293 — `synthetic_embodied_098_E2A`

**原始英文指令：** At 26.5 seconds, make both hands raise the wheelbarrow handles in two short upward pulses over three seconds.

**中文翻译：** 在第 26.5 秒，让双手在三秒内以两次短促向上动作抬起手推车把手。

**状态：** 接受

**原子化判定句：**

1. 双手是否以上推动作抬起手推车把手？

2. 上推动作是否短促？

3. 是否恰好完成两次上推？

4. 两次上推是否在 3 秒内完成？


## 294 — `synthetic_embodied_098_E2B`

**原始英文指令：** At 29.5 seconds, move the viewpoint slightly leftward past the raised wheelbarrow tray over three seconds.

**中文翻译：** 在第 29.5 秒，在三秒内将视点从抬起的手推车车斗旁稍微向左移动。

**状态：** 接受

**原子化判定句：**

1. 视点是否从抬起的手推车车斗旁稍微向左移动？

2. 移动是否在 3 秒内完成？


## 295 — `synthetic_embodied_099_E1`

**原始英文指令：** At 15.5 seconds, place the left palm beneath the round drinks tray's left underside for three seconds.

**中文翻译：** 在第 15.5 秒，将左手掌放在圆形饮料托盘左侧底部下方并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 左手掌是否放在圆形饮料托盘左侧底部下方？

2. 左手掌是否在该处保持 3 秒？


## 296 — `synthetic_embodied_099_E2A`

**原始英文指令：** At 25 seconds, switch to a raised rear-left third-person view following the person carrying the glasses.

**中文翻译：** 在第 25 秒，切换为抬高的左后方第三人称视角，跟随携带玻璃杯的人物。

**状态：** 接受

**原子化判定句：**

1. 画面是否切换为抬高的左后方第三人称视角？

2. 该视角是否跟随携带玻璃杯的人物？


## 297 — `synthetic_embodied_099_E2B`

**原始英文指令：** At 29.5 seconds, make the tray carrier take two short backward steps from the meeting table over four seconds.

**中文翻译：** 在第 29.5 秒，让托盘携带者在四秒内从会议桌旁向后迈两个短步。

**状态：** 接受

**原子化判定句：**

1. 托盘携带者是否从会议桌旁向后迈步？

2. 后退步是否短小？

3. 携带者是否恰好迈出两步？

4. 两步是否在 4 秒内完成？


## 298 — `synthetic_embodied_100_E1`

**原始英文指令：** At 16 seconds, make the right hand scrape the lower window frost with short vertical strokes for four seconds.

**中文翻译：** 在第 16 秒，让右手以短促的竖直动作刮除窗户下部的霜，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 右手是否刮除窗户下部的霜？

2. 刮擦轨迹是否为竖直方向？

3. 刮擦动作是否短促？

4. 刮霜动作是否持续 4 秒？


## 299 — `synthetic_embodied_100_E2A`

**原始英文指令：** At 24 seconds, terminate the window's frost-clearing process at 27 seconds with the remaining frost still in place.

**中文翻译：** 在第 24 秒开始编辑，于第 27 秒终止窗户除霜过程，同时保留尚未清除的霜。

**状态：** 接受

**原子化判定句：**

1. 窗户除霜过程是否进行？

2. 除霜过程是否在 3 秒后停止？

3. 过程停止时是否仍有部分霜留在原处？


## 300 — `synthetic_embodied_100_E2B`

**原始英文指令：** At 29.5 seconds, replace the blue flat scraping card with a short-handled metal ice scraper.

**中文翻译：** 在第 29.5 秒，将蓝色扁平刮卡替换为短柄金属除冰刮刀。

**状态：** 接受

**原子化判定句：**

1. 蓝色扁平刮卡是否被替换为除冰刮刀？

2. 替换后的刮刀是否为短柄？

3. 替换后的刮刀是否为金属材质？
