# 全量编辑指令原子化结果——syn_object_edit_records.md——中文审阅版

- 源记录数：300

- 所有原子判定句均依据 `atom_results/README.md` 逐条人工审核。

- 原子判定句省略作为截取起点的绝对时间；后续时间点均已换算为片段内相对时间。


## 001 — `synthetic_object_001_E1`

**原始英文指令：** Starting at 11.5 seconds, transform the full dog-and-frisbee scene into a colored-pencil animation over the next two seconds.

**中文翻译：** 从第 11.5 秒开始，在接下来的两秒内将整个狗与飞盘场景转变为彩色铅笔动画。

**状态：** 接受

**原子化判定句：**

1. 整个狗与飞盘场景是否转变为彩色铅笔动画？

2. 转变是否在 2 秒内完成？


## 002 — `synthetic_object_001_E2A`

**原始英文指令：** Starting at 33.5 seconds, make the dog carrying the red frisbee perform two high bounding strides along the curved paved path.

**中文翻译：** 从第 33.5 秒开始，让叼着红色飞盘的狗沿弯曲铺装小径做两个高幅度跃步。

**状态：** 接受

**原子化判定句：**

1. 叼着红色飞盘的狗是否沿弯曲铺装小径跃步？

2. 跃步幅度是否较高？

3. 狗是否恰好完成两个跃步？


## 003 — `synthetic_object_001_E2B`

**原始英文指令：** Starting at 24.5 seconds, accelerate the dog's ongoing leap and landing so all four paws return to the grass by 26.5 seconds.

**中文翻译：** 从第 24.5 秒开始，加快狗正在进行的跃起和落地动作，使四只爪在第 26.5 秒前全部回到草地。

**状态：** 接受

**原子化判定句：**

1. 狗正在进行的跃起和落地动作是否加快？

2. 四只爪是否在 2 秒内全部回到草地？


## 004 — `synthetic_object_002_E1`

**原始英文指令：** Starting at 8.5 seconds, change the fox's warm russet-brown dorsal coat to silver-gray over the next two seconds.

**中文翻译：** 从第 8.5 秒开始，在接下来的两秒内将狐狸背部温暖的赤褐色毛皮改为银灰色。

**状态：** 接受

**原子化判定句：**

1. 狐狸背部毛皮是否从温暖的赤褐色变为银灰色？

2. 颜色变化是否在 2 秒内完成？


## 005 — `synthetic_object_002_E2A`

**原始英文指令：** Starting at 32.5 seconds, move the camera in a low smooth clockwise arc around the fox for five seconds.

**中文翻译：** 从第 32.5 秒开始，让镜头以低机位沿顺时针平滑弧线环绕狐狸五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿顺时针弧线环绕狐狸？

2. 镜头是否保持低机位？

3. 镜头移动是否平滑？

4. 这一移动是否持续 5 秒？


## 006 — `synthetic_object_002_E2B`

**原始英文指令：** Starting at 22.0 seconds, make the fox scrape the snow twice with both forepaws directly beneath its chest.

**中文翻译：** 从第 22.0 秒开始，让狐狸用双前爪在胸部正下方刨雪两次。

**状态：** 接受

**原子化判定句：**

1. 狐狸是否用双前爪刨雪？

2. 刨雪位置是否在其胸部正下方？

3. 狐狸是否恰好刨雪两次？


## 007 — `synthetic_object_003_E1`

**原始英文指令：** Starting at 7.0 seconds, make the elephant sweep its trunk through the loose mound and fling soil over its left shoulder twice.

**中文翻译：** 从第 7.0 秒开始，让大象用象鼻扫过松散土堆，并将泥土越过左肩甩出两次。

**状态：** 接受

**原子化判定句：**

1. 大象是否用象鼻扫过松散土堆？

2. 它是否将泥土越过左肩甩出两次？


## 008 — `synthetic_object_003_E2A`

**原始英文指令：** Starting at 34.5 seconds, change the loose soil coating on the elephant's upper back into a thin crust of dried mud.

**中文翻译：** 从第 34.5 秒开始，将大象上背部覆盖的松散泥土变为一层薄薄的干泥壳。

**状态：** 接受

**原子化判定句：**

1. 大象上背部覆盖的松散泥土是否变为干泥壳？

2. 干泥壳是否较薄？


## 009 — `synthetic_object_003_E2B`

**原始英文指令：** At 21.0 seconds, place the loose soil mound half a trunk-length to the right of the elephant's right forefoot.

**中文翻译：** 在第 21.0 秒，将松散土堆放在大象右前脚右侧半个象鼻长度处。

**状态：** 接受

**原子化判定句：**

1. 松散土堆是否被放在大象右前脚右侧？

2. 土堆与右前脚的距离是否为半个象鼻长度？


## 010 — `synthetic_object_004_E1`

**原始英文指令：** Starting at 15.5 seconds, change the horse's relaxed walk into a steady trot along the beach for five seconds.

**中文翻译：** 从第 15.5 秒开始，将马沿海滩的轻松步行改为稳定小跑，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 马是否从步行改为沿海滩小跑？

2. 小跑是否稳定？

3. 小跑是否持续 5 秒？


## 011 — `synthetic_object_004_E2A`

**原始英文指令：** Starting at 28.0 seconds, add a warm golden rim light along the horse's visible outer silhouette over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内沿马可见的外轮廓添加温暖的金色轮廓光。

**状态：** 接受

**原子化判定句：**

1. 马可见的外轮廓是否添加了轮廓光？

2. 轮廓光是否为温暖的金色？

3. 照明变化是否在 2 秒内完成？


## 012 — `synthetic_object_004_E2B`

**原始英文指令：** Starting at 24.0 seconds, convert the full horse-on-beach video to a restrained 16 mm film look over two seconds.

**中文翻译：** 从第 24.0 秒开始，在两秒内将整个海滩马匹视频转变为克制的 16 毫米胶片风格。

**状态：** 接受

**原子化判定句：**

1. 整个海滩马匹视频是否呈现 16 毫米胶片风格？

2. 胶片处理是否呈现克制的观感？

3. 转变是否在 2 秒内完成？


## 013 — `synthetic_object_005_E1`

**原始英文指令：** Starting at 16.5 seconds, make the cat lift one front paw and tap the right shelf edge twice.

**中文翻译：** 从第 16.5 秒开始，让猫抬起一只前爪并轻拍右侧架子边缘两次。

**状态：** 接受

**原子化判定句：**

1. 猫是否抬起一只前爪？

2. 猫是否用该前爪轻拍右侧架子边缘两次？


## 014 — `synthetic_object_005_E2A`

**原始英文指令：** At 24.0 seconds, remove the horizontal stack of books from the top surface of the shelving unit.

**中文翻译：** 在第 24.0 秒，从置物架顶面移除横放的一摞书。

**状态：** 接受

**原子化判定句：**

1. 置物架顶面横放的一摞书是否被移除？


## 015 — `synthetic_object_005_E2B`

**原始英文指令：** At 29.5 seconds, move the walking orange cat onto the uncovered carpet in the left third of the frame.

**中文翻译：** 在第 29.5 秒，将行走的橙色猫移动到画面左侧三分之一区域露出的地毯上。

**状态：** 接受

**原子化判定句：**

1. 行走的橙色猫是否被移动到露出的地毯上？

2. 该地毯区域是否位于画面左侧三分之一？


## 016 — `synthetic_object_006_E1`

**原始英文指令：** Starting at 13.5 seconds, change the chameleon's cyan side band to amber-gold over the next two seconds.

**中文翻译：** 从第 13.5 秒开始，在接下来的两秒内将变色龙的青色侧带改为琥珀金色。

**状态：** 接受

**原子化判定句：**

1. 变色龙的青色侧带是否变为琥珀金色？

2. 颜色变化是否在 2 秒内完成？


## 017 — `synthetic_object_006_E2A`

**原始英文指令：** Starting at 34.5 seconds, pause the chameleon's forward step with its foot raised for three seconds, then resume placing it on the branch.

**中文翻译：** 从第 34.5 秒开始，将变色龙向前迈步的动作暂停三秒并保持脚抬起，然后恢复并将脚放到树枝上。

**状态：** 接受

**原子化判定句：**

1. 变色龙是否向前迈步？

2. 迈步动作是否在脚抬起的状态下暂停 3 秒？

3. 随后变色龙是否恢复迈步并将脚放到树枝上？


## 018 — `synthetic_object_006_E2B`

**原始英文指令：** At 27.0 seconds, replace the dark long-legged insect on the branch with one small brown moth.

**中文翻译：** 在第 27.0 秒，将树枝上的深色长腿昆虫替换为一只小型棕色飞蛾。

**状态：** 接受

**原子化判定句：**

1. 树枝上的深色长腿昆虫是否被替换为一只飞蛾？

2. 替换后的飞蛾是否小型？

3. 飞蛾是否为棕色？


## 019 — `synthetic_object_007_E1`

**原始英文指令：** Starting at 10.0 seconds, zoom in smoothly until the perched owl's spread wings nearly fill the frame.

**中文翻译：** 从第 10.0 秒开始，平滑拉近镜头，直到栖息猫头鹰展开的双翼几乎填满画面。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉近？

2. 拉近过程是否平滑？

3. 栖息猫头鹰展开的双翼最终是否几乎填满画面？


## 020 — `synthetic_object_007_E2A`

**原始英文指令：** Starting at 22.5 seconds, accelerate the owl's wingbeats during its flight toward the far post for three seconds.

**中文翻译：** 从第 22.5 秒开始，在猫头鹰飞向远处立柱的过程中加快其振翅频率，持续三秒。

**状态：** 接受

**原子化判定句：**

1. 猫头鹰是否继续飞向远处立柱？

2. 飞行过程中其振翅频率是否加快？

3. 加快后的振翅频率是否持续 3 秒？


## 021 — `synthetic_object_007_E2B`

**原始英文指令：** Starting at 24.5 seconds, change the owl's dark gray flight-feather markings to warm brown over two seconds.

**中文翻译：** 从第 24.5 秒开始，在两秒内将猫头鹰飞羽上的深灰色斑纹改为暖棕色。

**状态：** 接受

**原子化判定句：**

1. 猫头鹰飞羽上的斑纹是否从深灰色变为暖棕色？

2. 颜色变化是否在 2 秒内完成？


## 022 — `synthetic_object_008_E1`

**原始英文指令：** Starting at 12.5 seconds, slow the hummingbird's wingbeats enough to show distinct downstrokes for four seconds.

**中文翻译：** 从第 12.5 秒开始，将蜂鸟的振翅速度放慢到能够看清下拍动作，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 蜂鸟的振翅速度是否降低？

2. 下拍动作是否清晰可见？

3. 较慢的振翅速度是否持续 4 秒？


## 023 — `synthetic_object_008_E2A`

**原始英文指令：** At 31.0 seconds, position the hummingbird's beak tip one beak-length from the red flower opening.

**中文翻译：** 在第 31.0 秒，将蜂鸟的喙尖放置在距红花开口一个喙长的位置。

**状态：** 接受

**原子化判定句：**

1. 蜂鸟的喙尖是否被放置在红花开口附近？

2. 喙尖与花朵开口的距离是否恰好为一个喙长？


## 024 — `synthetic_object_008_E2B`

**原始英文指令：** Starting at 20.5 seconds, change the hummingbird's gray-white throat and chest to iridescent violet over two seconds.

**中文翻译：** 从第 20.5 秒开始，在两秒内将蜂鸟灰白色的喉部和胸部改为虹彩紫色。

**状态：** 接受

**原子化判定句：**

1. 蜂鸟的喉部是否变为虹彩紫色？

2. 蜂鸟的胸部是否变为虹彩紫色？

3. 两处颜色变化是否在 2 秒内完成？


## 025 — `synthetic_object_009_E1`

**原始英文指令：** Starting at 9.5 seconds, change the eagle's golden-brown head and neck feathers to pale silver over two seconds.

**中文翻译：** 从第 9.5 秒开始，在两秒内将鹰头部和颈部的金棕色羽毛改为浅银色。

**状态：** 接受

**原子化判定句：**

1. 鹰头部的羽毛是否变为浅银色？

2. 鹰颈部的羽毛是否变为浅银色？

3. 两处颜色变化是否在 2 秒内完成？


## 026 — `synthetic_object_009_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the perched eagle raise one foot and scratch the side of its neck twice.

**中文翻译：** 从第 29.0 秒开始，让栖息的鹰抬起一只脚，并抓挠颈侧两次。

**状态：** 接受

**原子化判定句：**

1. 栖息的鹰是否抬起一只脚？

2. 它是否用该脚抓挠颈侧两次？


## 027 — `synthetic_object_009_E2B`

**原始英文指令：** At 20.0 seconds, add one small weathered branch on the exposed rock immediately to the eagle's right.

**中文翻译：** 在第 20.0 秒，在鹰右侧紧邻的裸露岩石上添加一根小型风化树枝。

**状态：** 接受

**原子化判定句：**

1. 鹰右侧紧邻的裸露岩石上是否添加了一根树枝？

2. 树枝是否小型？

3. 树枝是否具有风化外观？


## 028 — `synthetic_object_010_E1`

**原始英文指令：** At 14.0 seconds, add one rounded pale-gray rock on the ice one body-length behind the penguin.

**中文翻译：** 在第 14.0 秒，在企鹅身后一个身长处的冰面上添加一块圆润的浅灰色岩石。

**状态：** 接受

**原子化判定句：**

1. 企鹅身后一个身长处的冰面上是否添加了一块岩石？

2. 岩石是否圆润？

3. 岩石是否为浅灰色？


## 029 — `synthetic_object_010_E2A`

**原始英文指令：** Starting at 33.0 seconds, move the camera smoothly to a higher three-quarter view of the penguin and ice edge.

**中文翻译：** 从第 33.0 秒开始，将镜头平滑移动到俯看企鹅和冰缘的较高四分之三视角。

**状态：** 接受

**原子化判定句：**

1. 镜头是否移动到俯看企鹅和冰缘的较高四分之三视角？

2. 镜头移动是否平滑？


## 030 — `synthetic_object_010_E2B`

**原始英文指令：** Starting at 26.5 seconds, make the penguin lower its head and tap the water surface twice with its beak tip.

**中文翻译：** 从第 26.5 秒开始，让企鹅低下头并用喙尖轻点水面两次。

**状态：** 接受

**原子化判定句：**

1. 企鹅是否低下头？

2. 它是否用喙尖轻点水面两次？


## 031 — `synthetic_object_011_E1`

**原始英文指令：** Starting at 16.5 seconds, turn the giraffe's head and upper neck to face the camera over the next 1.5 seconds.

**中文翻译：** 从第 16.5 秒开始，在接下来的 1.5 秒内将长颈鹿的头部和上颈转向镜头。

**状态：** 接受

**原子化判定句：**

1. 长颈鹿的头部是否转向镜头？

2. 其上颈是否随头部一同转动？

3. 两处转动是否在 1.5 秒内完成？


## 032 — `synthetic_object_011_E2A`

**原始英文指令：** Starting at 35.0 seconds, change the dry grass immediately around the giraffe to fresh green over two seconds.

**中文翻译：** 从第 35.0 秒开始，在两秒内将长颈鹿紧邻周围的干草改为鲜绿色。

**状态：** 接受

**原子化判定句：**

1. 长颈鹿紧邻周围的干草是否变为鲜绿色？

2. 变化是否在 2 秒内完成？


## 033 — `synthetic_object_011_E2B`

**原始英文指令：** At 22.0 seconds, remove the large fallen diagonal branch lying left of the giraffe and tree.

**中文翻译：** 在第 22.0 秒，移除位于长颈鹿和树木左侧的大型倒伏斜枝。

**状态：** 接受

**原子化判定句：**

1. 位于长颈鹿和树木左侧的大型倒伏斜枝是否被移除？


## 034 — `synthetic_object_012_E1`

**原始英文指令：** At 11.5 seconds, add one small blue rubber ball floating at the left edge of the puddle.

**中文翻译：** 在第 11.5 秒，在水洼左缘添加一个漂浮的小型蓝色橡胶球。

**状态：** 接受

**原子化判定句：**

1. 水洼左缘是否添加了一个漂浮的球？

2. 球是否小型？

3. 球是否为蓝色？

4. 球是否为橡胶材质？


## 035 — `synthetic_object_012_E2A`

**原始英文指令：** Starting at 35.5 seconds, make the dog scrape the grass twice with one visible forepaw.

**中文翻译：** 从第 35.5 秒开始，让狗用一只可见前爪刨草两次。

**状态：** 接受

**原子化判定句：**

1. 狗是否用一只可见前爪刨草？

2. 狗是否恰好刨草两次？


## 036 — `synthetic_object_012_E2B`

**原始英文指令：** Starting at 25.5 seconds, track alongside the walking dog from a low side angle for five seconds.

**中文翻译：** 从第 25.5 秒开始，以低侧视角沿行走的狗侧面跟拍五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿行走的狗侧面跟拍？

2. 跟拍视角是否为低侧视角？

3. 跟拍是否持续 5 秒？


## 037 — `synthetic_object_013_E1`

**原始英文指令：** Starting at 16.5 seconds, change the kangaroo's medium-brown body fur to sandy beige over two seconds.

**中文翻译：** 从第 16.5 秒开始，在两秒内将袋鼠的中棕色体毛改为沙米色。

**状态：** 接受

**原子化判定句：**

1. 袋鼠的体毛是否从中棕色变为沙米色？

2. 颜色变化是否在 2 秒内完成？


## 038 — `synthetic_object_013_E2A`

**原始英文指令：** Starting at 35.0 seconds, render only the kangaroo as a bronze sculpture over the next two seconds.

**中文翻译：** 从第 35.0 秒开始，在接下来的两秒内仅将袋鼠呈现为青铜雕塑。

**状态：** 接受

**原子化判定句：**

1. 袋鼠是否被呈现为青铜雕塑？

2. 该处理是否仅作用于袋鼠？

3. 渲染是否在 2 秒内完成？


## 039 — `synthetic_object_013_E2B`

**原始英文指令：** Starting at 30.0 seconds, accelerate the kangaroo's hopping cadence into faster bounds along the same route for five seconds.

**中文翻译：** 从第 30.0 秒开始，加快袋鼠的跳跃节奏，使其沿同一路线以更快的跃跳前进五秒。

**状态：** 接受

**原子化判定句：**

1. 袋鼠是否继续沿同一路线跃跳前进？

2. 袋鼠的跳跃节奏是否加快？

3. 加快后的节奏是否持续 5 秒？


## 040 — `synthetic_object_014_E1`

**原始英文指令：** Starting at 11.0 seconds, make the red panda hold position and swing its long tail through three broad side-to-side arcs.

**中文翻译：** 从第 11.0 秒开始，让小熊猫保持位置不动，并让长尾巴做三次大幅左右摆动。

**状态：** 接受

**原子化判定句：**

1. 小熊猫是否保持位置不动？

2. 它的长尾巴是否做三次大幅左右摆动？


## 041 — `synthetic_object_014_E2A`

**原始英文指令：** At 31.5 seconds, replace the thin leafless branch rising behind the red panda with a leafy green branch.

**中文翻译：** 在第 31.5 秒，将小熊猫后方竖起的细无叶树枝替换为一根绿色有叶树枝。

**状态：** 接受

**原子化判定句：**

1. 小熊猫后方竖起的细无叶树枝是否被替换？

2. 替换后的树枝是否有叶？

3. 替换后的树枝是否为绿色？


## 042 — `synthetic_object_014_E2B`

**原始英文指令：** Starting at 20.5 seconds, change the dry bark beneath the red panda to a freshly wet darker state over two seconds.

**中文翻译：** 从第 20.5 秒开始，在两秒内将小熊猫下方的干燥树皮改为刚被浸湿的深色状态。

**状态：** 接受

**原子化判定句：**

1. 小熊猫下方的干燥树皮是否变为刚被浸湿的状态？

2. 变湿后的树皮是否颜色变深？

3. 变化是否在 2 秒内完成？


## 043 — `synthetic_object_015_E1`

**原始英文指令：** At 12.0 seconds, move the floating otter to the right side of the flat pale rock, one body-length away.

**中文翻译：** 在第 12.0 秒，将漂浮的水獭移动到扁平浅色岩石右侧一个身长处。

**状态：** 接受

**原子化判定句：**

1. 漂浮的水獭是否被移动到扁平浅色岩石右侧？

2. 水獭与岩石的距离是否为一个身长？


## 044 — `synthetic_object_015_E2A`

**原始英文指令：** Starting at 36.5 seconds, change the pale rounded object held near the otter's mouth to deep coral red over two seconds.

**中文翻译：** 从第 36.5 秒开始，在两秒内将水獭嘴边拿着的浅色圆润物体改为深珊瑚红色。

**状态：** 接受

**原子化判定句：**

1. 水獭嘴边拿着的浅色圆润物体是否变为深珊瑚红色？

2. 颜色变化是否在 2 秒内完成？


## 045 — `synthetic_object_015_E2B`

**原始英文指令：** Starting at 24.0 seconds, make tight concentric ripples expand around the submerged otter for four seconds.

**中文翻译：** 从第 24.0 秒开始，让紧密的同心波纹围绕水下的水獭向外扩散四秒。

**状态：** 接受

**原子化判定句：**

1. 水下的水獭周围是否形成紧密的同心波纹？

2. 波纹是否向外扩散？

3. 扩散是否持续 4 秒？


## 046 — `synthetic_object_016_E1`

**原始英文指令：** At 13.5 seconds, remove the rounded ochre rock beside the animal's water entry point.

**中文翻译：** 在第 13.5 秒，移除动物入水点旁的圆润赭色岩石。

**状态：** 接受

**原子化判定句：**

1. 动物入水点旁的圆润赭色岩石是否被移除？


## 047 — `synthetic_object_016_E2A`

**原始英文指令：** Starting at 36.5 seconds, make the right-side seal-shaped animal swim one tight clockwise circle around the rounded ochre rock.

**中文翻译：** 从第 36.5 秒开始，让右侧海豹状动物围绕圆润赭色岩石沿紧密圆圈顺时针游一圈。

**状态：** 接受

**原子化判定句：**

1. 右侧海豹状动物是否围绕圆润赭色岩石游动？

2. 它是否沿顺时针方向游动？

3. 游动圆圈是否紧密？

4. 它是否恰好完成一圈？


## 048 — `synthetic_object_016_E2B`

**原始英文指令：** Starting at 24.0 seconds, create two broad trailing wakes behind the left-moving submerged animal for four seconds.

**中文翻译：** 从第 24.0 秒开始，在向左移动的水下动物身后形成两道宽阔尾流，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 水下动物是否继续向左移动？

2. 其身后是否恰好形成两道尾流？

3. 尾流是否宽阔？

4. 尾流是否持续 4 秒？


## 049 — `synthetic_object_017_E1`

**原始英文指令：** Starting at 17.0 seconds, change the goat's dry gray-brown coat to a visibly wet flattened state over two seconds.

**中文翻译：** 从第 17.0 秒开始，在两秒内将山羊干燥的灰棕色毛皮改为明显湿润贴伏的状态。

**状态：** 接受

**原子化判定句：**

1. 山羊干燥的毛皮是否变得明显湿润？

2. 湿润后的毛皮是否贴伏？

3. 变化是否在 2 秒内完成？


## 050 — `synthetic_object_017_E2A`

**原始英文指令：** Starting at 36.0 seconds, make the mountain goat rear once onto its hind legs and return to the rock ledge.

**中文翻译：** 从第 36.0 秒开始，让山羊用后腿直立一次，然后回到岩石台面。

**状态：** 接受

**原子化判定句：**

1. 山羊是否用后腿直立一次？

2. 随后它是否回到岩石台面？


## 051 — `synthetic_object_017_E2B`

**原始英文指令：** Starting at 22.5 seconds, change the goat's steady walk into a brisk trot along the same ledge for five seconds.

**中文翻译：** 从第 22.5 秒开始，将山羊的稳定步行改为沿同一岩石台面快步小跑，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 山羊是否从步行改为沿同一岩石台面小跑？

2. 小跑是否轻快？

3. 小跑是否持续 5 秒？


## 052 — `synthetic_object_018_E1`

**原始英文指令：** At 13.0 seconds, replace the oval gray stone behind the rabbit with a small red rubber ball.

**中文翻译：** 在第 13.0 秒，将兔子后方的椭圆形灰色石头替换为一个小型红色橡胶球。

**状态：** 接受

**原子化判定句：**

1. 兔子后方的椭圆形灰色石头是否被替换为一个球？

2. 替换后的球是否小型？

3. 球是否为红色？

4. 球是否为橡胶材质？


## 053 — `synthetic_object_018_E2A`

**原始英文指令：** At 33.0 seconds, move the white rabbit onto the open grass in the left third of the frame.

**中文翻译：** 在第 33.0 秒，将白兔移动到画面左侧三分之一区域的开阔草地上。

**状态：** 接受

**原子化判定句：**

1. 白兔是否被移动到开阔草地上？

2. 该草地区域是否位于画面左侧三分之一？


## 054 — `synthetic_object_018_E2B`

**原始英文指令：** Starting at 21.0 seconds, change both of the rabbit's pale pink inner ears to pale blue over two seconds.

**中文翻译：** 从第 21.0 秒开始，在两秒内将兔子两只浅粉色内耳都改为浅蓝色。

**状态：** 接受

**原子化判定句：**

1. 兔子的左侧内耳是否变为浅蓝色？

2. 兔子的右侧内耳是否变为浅蓝色？

3. 两处颜色变化是否在 2 秒内完成？


## 055 — `synthetic_object_019_E1`

**原始英文指令：** Starting at 18.5 seconds, delay the hedgehog's upcoming curl halfway through for three seconds, then resume the same curling process.

**中文翻译：** 从第 18.5 秒开始，让刺猬即将进行的卷曲动作在进行到一半时停顿三秒，然后恢复同一卷曲过程。

**状态：** 接受

**原子化判定句：**

1. 刺猬是否开始卷曲？

2. 卷曲过程是否在进行到一半时暂停 3 秒？

3. 随后同一卷曲过程是否恢复？


## 056 — `synthetic_object_019_E2A`

**原始英文指令：** At 36.5 seconds, move the thin foreground twig to the upper-left edge of the visible soil patch.

**中文翻译：** 在第 36.5 秒，将前景细树枝移动到可见土地区域的左上边缘。

**状态：** 接受

**原子化判定句：**

1. 前景细树枝是否被移动到可见土地区域的左上边缘？


## 057 — `synthetic_object_019_E2B`

**原始英文指令：** Starting at 31.5 seconds, change the curled hedgehog's brown spines to warm gray over two seconds.

**中文翻译：** 从第 31.5 秒开始，在两秒内将卷曲刺猬的棕色刺毛改为暖灰色。

**状态：** 接受

**原子化判定句：**

1. 卷曲刺猬的棕色刺毛是否变为暖灰色？

2. 颜色变化是否在 2 秒内完成？


## 058 — `synthetic_object_020_E1`

**原始英文指令：** Starting at 15.0 seconds, change the green-blue centers of the peacock's tail eyespots to copper-red over two seconds.

**中文翻译：** 从第 15.0 秒开始，在两秒内将孔雀尾羽眼斑的蓝绿色中心改为铜红色。

**状态：** 接受

**原子化判定句：**

1. 孔雀尾羽眼斑的中心是否从蓝绿色变为铜红色？

2. 颜色变化是否在 2 秒内完成？


## 059 — `synthetic_object_020_E2A`

**原始英文指令：** At 32.0 seconds, move the large gray rock to a position one peacock-width left of the tail fan.

**中文翻译：** 在第 32.0 秒，将大型灰色岩石移动到尾屏左侧一个孔雀宽度的位置。

**状态：** 接受

**原子化判定句：**

1. 大型灰色岩石是否被移动到尾屏左侧？

2. 岩石与尾屏的距离是否为一个孔雀宽度？


## 060 — `synthetic_object_020_E2B`

**原始英文指令：** Starting at 22.0 seconds, give the full peacock display scene a soft matte finish with gently reduced contrast over two seconds.

**中文翻译：** 从第 22.0 秒开始，在两秒内让整个孔雀开屏场景呈现柔和哑光质感，并轻微降低对比度。

**状态：** 接受

**原子化判定句：**

1. 整个孔雀开屏场景是否在 2 秒内呈现柔和哑光质感？

2. 整个场景的对比度是否在同一段 2 秒内轻微降低？


## 061 — `synthetic_object_021_E1`

**原始英文指令：** Starting at 11.5 seconds, make the red sports car perform one controlled fishtail through the wet bend before straightening.

**中文翻译：** 从第 11.5 秒开始，让红色跑车在湿滑弯道上完成一次受控甩尾，然后回正。

**状态：** 接受

**原子化判定句：**

1. 红色跑车是否在湿滑弯道上完成一次受控甩尾？

2. 随后跑车是否回正？


## 062 — `synthetic_object_021_E2A`

**原始英文指令：** Starting at 31 seconds, grade the full wet mountain-road scene with cool cyan-and-silver tones over the next two seconds.

**中文翻译：** 从第 31 秒开始，在接下来的两秒内为整个湿滑山路场景应用冷青色与银色调色。

**状态：** 接受

**原子化判定句：**

1. 整个湿滑山路场景是否呈现冷青色与银色调？

2. 调色是否在 2 秒内完成？


## 063 — `synthetic_object_021_E2B`

**原始英文指令：** Starting at 24.5 seconds, smoothly zoom out until the red sports car occupies roughly one fifth of the frame.

**中文翻译：** 从第 24.5 秒开始，平滑拉远镜头，直到红色跑车约占画面的五分之一。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉远？

2. 拉远过程是否平滑？

3. 红色跑车最终是否约占画面的五分之一？


## 064 — `synthetic_object_022_E1`

**原始英文指令：** Starting at 10.5 seconds, change the off-road vehicle's blue body panels to deep forest green over two seconds.

**中文翻译：** 从第 10.5 秒开始，在两秒内将越野车的蓝色车身面板改为深森林绿色。

**状态：** 接受

**原子化判定句：**

1. 越野车的车身面板是否从蓝色变为深森林绿色？

2. 颜色变化是否在 2 秒内完成？


## 065 — `synthetic_object_022_E2A`

**原始英文指令：** At 31.5 seconds, replace the rear-mounted spare wheel with a dark rectangular expedition fuel canister of comparable size.

**中文翻译：** 在第 31.5 秒，将后置备胎替换为尺寸相当的深色矩形探险燃油罐。

**状态：** 接受

**原子化判定句：**

1. 后置备胎是否被替换为探险燃油罐？

2. 燃油罐是否为深色？

3. 燃油罐是否为矩形？

4. 燃油罐是否与备胎尺寸相当？


## 066 — `synthetic_object_022_E2B`

**原始英文指令：** Starting at 23.5 seconds, make the off-road vehicle perform one short suspension bounce over the next dirt-track rise.

**中文翻译：** 从第 23.5 秒开始，让越野车在驶过下一个土路隆起处时完成一次短促悬挂弹跳。

**状态：** 接受

**原子化判定句：**

1. 越野车是否在驶过下一个土路隆起处时发生悬挂弹跳？

2. 弹跳是否短促？

3. 越野车是否恰好完成一次弹跳？


## 067 — `synthetic_object_023_E1`

**原始英文指令：** Starting at 14 seconds, make the two visible closed side doors on the bus swing fully open over the next two seconds.

**中文翻译：** 从第 14 秒开始，让公交车上两扇可见的关闭侧门在接下来的两秒内完全打开。

**状态：** 接受

**原子化判定句：**

1. 第一扇可见的关闭侧门是否完全打开？

2. 第二扇可见的关闭侧门是否完全打开？

3. 两扇门是否都在 2 秒内完全打开？


## 068 — `synthetic_object_023_E2A`

**原始英文指令：** At 21.5 seconds, move the yellow rear license plate upward to the vertical center of the black rear panel.

**中文翻译：** 在第 21.5 秒，将黄色后车牌向上移动到黑色后面板的垂直中心。

**状态：** 接受

**原子化判定句：**

1. 黄色后车牌是否向上移动？

2. 车牌最终是否位于黑色后面板的垂直中心？


## 069 — `synthetic_object_023_E2B`

**原始英文指令：** Starting at 27.5 seconds, move the camera smoothly from the bus's rear quarter toward its front doors for five seconds.

**中文翻译：** 从第 27.5 秒开始，让镜头从公交车后侧四分之三位置朝前门平滑移动五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否从公交车后侧四分之三位置朝前门移动？

2. 镜头移动是否平滑？

3. 移动是否持续 5 秒？


## 070 — `synthetic_object_024_E1`

**原始英文指令：** Starting at 12.5 seconds, change the motorcycle's glossy black fuel tank to metallic burgundy over the next two seconds.

**中文翻译：** 从第 12.5 秒开始，在接下来的两秒内将摩托车亮黑色油箱改为金属酒红色。

**状态：** 接受

**原子化判定句：**

1. 摩托车油箱是否从亮黑色变为酒红色？

2. 酒红色饰面是否具有金属质感？

3. 变化是否在 2 秒内完成？


## 071 — `synthetic_object_024_E2A`

**原始英文指令：** Starting at 30 seconds, make the loose yellow roadside dirt rise as dust and blow against the motorcycle's lower side for five seconds.

**中文翻译：** 从第 30 秒开始，让路边松散的黄色泥土扬起成尘，并吹向摩托车下侧，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 路边松散的黄色泥土是否扬起成尘？

2. 尘土是否吹向摩托车下侧并持续 5 秒？


## 072 — `synthetic_object_024_E2B`

**原始英文指令：** At 24.5 seconds, reposition the motorcycle into the inner half of its lane, one tire-width from the center line.

**中文翻译：** 在第 24.5 秒，将摩托车重新放置在所在车道的内侧一半，距中心线一个轮胎宽度。

**状态：** 接受

**原子化判定句：**

1. 摩托车是否被重新放置在所在车道的内侧一半？

2. 摩托车与中心线的距离是否为一个轮胎宽度？


## 073 — `synthetic_object_025_E1`

**原始英文指令：** At 13 seconds, shift the articulated tram one full car-length to the right along its current rails.

**中文翻译：** 在第 13 秒，将铰接式有轨电车沿当前轨道向右移动一整个车厢长度。

**状态：** 接受

**原子化判定句：**

1. 铰接式有轨电车是否向右移动？

2. 电车是否仍沿当前轨道移动？

3. 移动距离是否为一整个车厢长度？


## 074 — `synthetic_object_025_E2A`

**原始英文指令：** At 30 seconds, replace the old articulated tram with a brand-new single-car high-speed train in the same track position.

**中文翻译：** 在第 30 秒，将老旧铰接式有轨电车替换为位于同一轨道位置的全新单节高速列车。

**状态：** 接受

**原子化判定句：**

1. 老旧铰接式有轨电车是否被替换为全新单节高速列车？

2. 替换后的高速列车是否位于与原电车相同的轨道位置？


## 075 — `synthetic_object_025_E2B`

**原始英文指令：** Starting at 24.5 seconds, make the front pantograph flex downward and rebound against the overhead wire twice while moving.

**中文翻译：** 从第 24.5 秒开始，让前部受电弓在移动过程中向下弯曲并回弹接触架空线两次。

**状态：** 接受

**原子化判定句：**

1. 电车移动过程中，前部受电弓是否向下弯曲？

2. 受电弓是否随后回弹至架空线？

3. 每次回弹后受电弓是否接触架空线？

4. 受电弓是否恰好完成两次弯曲—回弹循环？


## 076 — `synthetic_object_026_E1`

**原始英文指令：** Starting at 14.5 seconds, make the freight train decelerate smoothly to a complete stop along the curved track over four seconds.

**中文翻译：** 从第 14.5 秒开始，让货运列车沿弯曲轨道平滑减速，并在四秒内完全停止。

**状态：** 接受

**原子化判定句：**

1. 货运列车是否沿弯曲轨道减速？

2. 减速过程是否平滑？

3. 列车是否完全停止？

4. 列车是否在 4 秒内停止？


## 077 — `synthetic_object_026_E2A`

**原始英文指令：** Starting at 34 seconds, transform the entire freight-train countryside scene into a warm Miyazaki-inspired hand-painted animation over two seconds.

**中文翻译：** 从第 34 秒开始，在两秒内将整个乡村货运列车场景转变为温暖的宫崎骏风格手绘动画。

**状态：** 接受

**原子化判定句：**

1. 整个乡村货运列车场景是否转变为手绘动画？

2. 动画是否呈现温暖的观感？

3. 动画是否具有宫崎骏风格的视觉特征？

4. 转变是否在 2 秒内完成？


## 078 — `synthetic_object_026_E2B`

**原始英文指令：** At 25.5 seconds, replace the first brown hopper wagon behind the locomotive with a silver cylindrical tanker wagon of equal length.

**中文翻译：** 在第 25.5 秒，将机车后方第一节棕色漏斗车替换为等长的银色圆柱形罐车。

**状态：** 接受

**原子化判定句：**

1. 机车后方第一节棕色漏斗车是否被替换为罐车？

2. 替换后的罐车是否为银色？

3. 罐车是否为圆柱形？

4. 罐车是否与原车厢等长？


## 079 — `synthetic_object_027_E1`

**原始英文指令：** At 12 seconds, shift the complete silver train forward by two car-lengths along the same elevated bridge track.

**中文翻译：** 在第 12 秒，将整列银色列车沿同一高架桥轨道向前移动两个车厢长度。

**状态：** 接受

**原子化判定句：**

1. 整列银色列车是否沿同一高架桥轨道向前移动？

2. 移动距离是否为两个车厢长度？


## 080 — `synthetic_object_027_E2A`

**原始英文指令：** Starting at 34 seconds, make two broad concentric ripple bands travel outward across the river beneath the bridge for five seconds.

**中文翻译：** 从第 34 秒开始，让两道宽阔的同心波纹带在桥下河面向外传播五秒。

**状态：** 接受

**原子化判定句：**

1. 桥下河面是否恰好出现两道同心波纹带？

2. 波纹带是否宽阔？

3. 波纹带是否向外传播？

4. 向外传播是否持续 5 秒？


## 081 — `synthetic_object_027_E2B`

**原始英文指令：** Starting at 24.5 seconds, change the passenger train's blue-gray side stripe to deep green over the next two seconds.

**中文翻译：** 从第 24.5 秒开始，在接下来的两秒内将客运列车的蓝灰色侧条纹改为深绿色。

**状态：** 接受

**原子化判定句：**

1. 客运列车的侧条纹是否从蓝灰色变为深绿色？

2. 颜色变化是否在 2 秒内完成？


## 082 — `synthetic_object_028_E1`

**原始英文指令：** At 14.5 seconds, remove the yellow safety line running along the visible edge of the station platform.

**中文翻译：** 在第 14.5 秒，移除沿车站站台可见边缘延伸的黄色安全线。

**状态：** 接受

**原子化判定句：**

1. 沿车站站台可见边缘延伸的黄色安全线是否被移除？


## 083 — `synthetic_object_028_E2A`

**原始英文指令：** Starting at 29.5 seconds, change the visible passenger doors from closed to fully open over the next two seconds.

**中文翻译：** 从第 29.5 秒开始，在接下来的两秒内将可见的乘客车门从关闭状态改为完全打开。

**状态：** 接受

**原子化判定句：**

1. 所有可见的乘客车门是否从关闭状态变为完全打开？

2. 所有车门是否都在 2 秒内完全打开？


## 084 — `synthetic_object_028_E2B`

**原始英文指令：** At 23 seconds, double the spacing between all visible ceiling lights along the left side of the platform.

**中文翻译：** 在第 23 秒，将站台左侧所有可见顶灯之间的间距扩大为原来的两倍。

**状态：** 接受

**原子化判定句：**

1. 站台左侧所有可见顶灯之间的间距是否增大？

2. 间距是否扩大为原来的两倍？


## 085 — `synthetic_object_029_E1`

**原始英文指令：** At 14 seconds, move the cream convertible half a lane-width closer to the right curb.

**中文翻译：** 在第 14 秒，将奶油色敞篷车朝右侧路缘移动半个车道宽度。

**状态：** 接受

**原子化判定句：**

1. 奶油色敞篷车是否朝右侧路缘靠近？

2. 移动距离是否为半个车道宽度？


## 086 — `synthetic_object_029_E2A`

**原始英文指令：** Starting at 31 seconds, reduce the cream convertible's forward speed to half its original rate for five seconds.

**中文翻译：** 从第 31 秒开始，将奶油色敞篷车的前进速度降低到原来的一半，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 奶油色敞篷车是否继续向前行驶？

2. 其前进速度是否降低到原来的一半？

3. 降低后的速度是否持续 5 秒？


## 087 — `synthetic_object_029_E2B`

**原始英文指令：** Starting at 25.5 seconds, change the weather across the residential street to steady rain under an overcast sky over two seconds.

**中文翻译：** 从第 25.5 秒开始，在两秒内将住宅街道的天气改为阴天下的持续降雨。

**状态：** 接受

**原子化判定句：**

1. 住宅街道是否开始持续降雨？

2. 天空是否变为阴天？

3. 天气变化是否在 2 秒内完成？


## 088 — `synthetic_object_030_E1`

**原始英文指令：** At 13 seconds, add one red compact car two car-lengths behind the yellow taxi in the same traffic lane.

**中文翻译：** 在第 13 秒，在黄色出租车后方两个车长、同一车道内添加一辆红色紧凑型汽车。

**状态：** 接受

**原子化判定句：**

1. 黄色出租车后方同一车道内是否添加了一辆汽车？

2. 新增汽车是否为红色？

3. 新增汽车是否为紧凑型？

4. 汽车是否位于出租车后方两个车长处？


## 089 — `synthetic_object_030_E2A`

**原始英文指令：** Starting at 31 seconds, increase the yellow taxi's forward speed by forty percent along the same lane for five seconds.

**中文翻译：** 从第 31 秒开始，将黄色出租车沿同一车道的前进速度提高百分之四十，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 黄色出租车是否继续沿同一车道向前行驶？

2. 其前进速度是否提高 40%？

3. 提高后的速度是否持续 5 秒？


## 090 — `synthetic_object_030_E2B`

**原始英文指令：** Starting at 24 seconds, render only the yellow taxi's roof sign as frosted translucent glass over two seconds.

**中文翻译：** 从第 24 秒开始，在两秒内仅将黄色出租车的车顶标志呈现为磨砂半透明玻璃。

**状态：** 接受

**原子化判定句：**

1. 黄色出租车的车顶标志是否被呈现为玻璃？

2. 玻璃是否呈磨砂半透明外观？

3. 该处理是否仅作用于车顶标志？

4. 渲染是否在 2 秒内完成？


## 091 — `synthetic_object_031_E1`

**原始英文指令：** At 15 seconds, rotate the ambulance ten degrees toward the right curb.

**中文翻译：** 在第 15 秒，将救护车朝右侧路缘旋转十度。

**状态：** 接受

**原子化判定句：**

1. 救护车是否朝右侧路缘旋转？

2. 旋转角度是否为 10 度？


## 092 — `synthetic_object_031_E2A`

**原始英文指令：** Starting at 32 seconds, make the visible roadside tree branches sway back and forth through two broad wind-driven arcs over five seconds.

**中文翻译：** 从第 32 秒开始，让可见的路边树枝在五秒内受风驱动大幅来回摆动两次。

**状态：** 接受

**原子化判定句：**

1. 可见的路边树枝是否受风驱动来回摆动？

2. 摆动弧度是否较大？

3. 树枝是否恰好完成两次摆动？

4. 两次摆动是否在 5 秒内完成？


## 093 — `synthetic_object_031_E2B`

**原始英文指令：** Starting at 27 seconds, make the ambulance exterior visibly old and dirty with weathered paint and road grime over two seconds.

**中文翻译：** 从第 27 秒开始，在两秒内让救护车外观明显变得老旧肮脏，并带有风化车漆和道路污垢。

**状态：** 接受

**原子化判定句：**

1. 救护车外观是否在 2 秒内明显变得老旧？

2. 救护车外观是否在同一段 2 秒内明显变脏？

3. 救护车车漆是否呈现风化状态？

4. 救护车外表是否出现道路污垢？


## 094 — `synthetic_object_032_E1`

**原始英文指令：** Starting at 11.5 seconds, smoothly zoom out until both vehicles and two empty lane-widths of roadway are visible.

**中文翻译：** 从第 11.5 秒开始，平滑拉远镜头，直到两辆车和两条车道宽的空路面都可见。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑拉远？

2. 拉远后，两辆车和两条车道宽的空路面是否都可见？


## 095 — `synthetic_object_032_E2A`

**原始英文指令：** Starting at 28.5 seconds, change the raised steel tow platform from dry and matte to rain-wet and reflective.

**中文翻译：** 从第 28.5 秒开始，将抬起的钢制拖车平台从干燥哑光改为被雨淋湿且具有反光效果。

**状态：** 接受

**原子化判定句：**

1. 抬起的钢制拖车平台是否从干燥状态变为被雨淋湿？

2. 拖车平台是否由哑光变为具有反光效果？


## 096 — `synthetic_object_032_E2B`

**原始英文指令：** Starting at 23.5 seconds, make the upright red bollard beside the wall sway left and right twice without leaving its base.

**中文翻译：** 从第 23.5 秒开始，让墙边直立的红色隔离柱左右摆动两次，同时底部不离开原位。

**状态：** 接受

**原子化判定句：**

1. 墙边直立的红色隔离柱是否左右摆动两次？

2. 摆动过程中，其底部是否始终保持在原位？


## 097 — `synthetic_object_033_E1`

**原始英文指令：** Starting at 9.5 seconds, change the street sweeper's bright blue body panels to vivid orange over the next two seconds.

**中文翻译：** 从第 9.5 秒开始，在接下来的两秒内将道路清扫车的亮蓝色车身面板改为鲜艳橙色。

**状态：** 接受

**原子化判定句：**

1. 道路清扫车的车身面板是否从亮蓝色变为鲜艳橙色？

2. 颜色变化是否在 2 秒内完成？


## 098 — `synthetic_object_033_E2A`

**原始英文指令：** At 28 seconds, gather the visible loose leaves into a narrow line directly ahead of the right circular brush.

**中文翻译：** 在第 28 秒，将可见的散落树叶聚拢成一道窄线，位于右侧圆形刷正前方。

**状态：** 接受

**原子化判定句：**

1. 可见的散落树叶是否被聚拢成一道线？

2. 这道线是否狭窄？

3. 这道线是否位于右侧圆形刷正前方？


## 099 — `synthetic_object_033_E2B`

**原始英文指令：** Starting at 21.5 seconds, lift the right circular street-sweeper brush completely clear of the pavement for four seconds.

**中文翻译：** 从第 21.5 秒开始，将道路清扫车右侧圆形刷完全抬离路面并保持四秒。

**状态：** 接受

**原子化判定句：**

1. 道路清扫车右侧圆形刷是否完全抬离路面？

2. 圆形刷是否保持离地 4 秒？


## 100 — `synthetic_object_034_E1`

**原始英文指令：** Starting at 14.5 seconds, make the rear discharge chute swing downward and pour one short stream of concrete onto the road.

**中文翻译：** 从第 14.5 秒开始，让后部卸料槽向下摆动，并向路面倾倒一股短暂的混凝土流。

**状态：** 接受

**原子化判定句：**

1. 后部卸料槽是否向下摆动？

2. 它是否向路面倾倒一股短暂的混凝土流？


## 101 — `synthetic_object_034_E2A`

**原始英文指令：** At 31 seconds, remove the long pale discharge chute projecting downward from the concrete mixer's rear assembly.

**中文翻译：** 在第 31 秒，移除从混凝土搅拌车后部组件向下伸出的浅色长卸料槽。

**状态：** 接受

**原子化判定句：**

1. 从混凝土搅拌车后部组件向下伸出的浅色长卸料槽是否被移除？


## 102 — `synthetic_object_034_E2B`

**原始英文指令：** Starting at 25.5 seconds, change the concrete mixer's large white drum to safety yellow over the next two seconds.

**中文翻译：** 从第 25.5 秒开始，在接下来的两秒内将混凝土搅拌车的大型白色搅拌筒改为安全黄色。

**状态：** 接受

**原子化判定句：**

1. 混凝土搅拌车的大型白色搅拌筒是否变为安全黄色？

2. 颜色变化是否在 2 秒内完成？


## 103 — `synthetic_object_035_E1`

**原始英文指令：** Starting at 17.5 seconds, make the dump-bed tailgate swing open and contact its lower stop once before remaining open.

**中文翻译：** 从第 17.5 秒开始，让自卸车厢尾门摆动打开，碰到下限位一次后保持打开。

**状态：** 接受

**原子化判定句：**

1. 自卸车厢尾门是否摆动打开？

2. 尾门是否碰到下限位一次？

3. 随后尾门是否保持打开？


## 104 — `synthetic_object_035_E2A`

**原始英文指令：** Starting at 29.5 seconds, change the raised dump bed from weathered beige to dark industrial green over two seconds.

**中文翻译：** 从第 29.5 秒开始，在两秒内将抬起的自卸车厢从风化米色改为深工业绿色。

**状态：** 接受

**原子化判定句：**

1. 抬起的自卸车厢是否从风化米色变为深工业绿色？

2. 颜色变化是否在 2 秒内完成？


## 105 — `synthetic_object_035_E2B`

**原始英文指令：** Starting at 28 seconds, transform the full dump-truck scene into a detailed charcoal-and-chalk drawing over two seconds.

**中文翻译：** 从第 28 秒开始，在两秒内将整个自卸卡车场景转变为细致的炭笔与粉笔画。

**状态：** 接受

**原子化判定句：**

1. 整个自卸卡车场景是否转变为炭笔与粉笔画？

2. 画面是否呈现细致的效果？

3. 转变是否在 2 秒内完成？


## 106 — `synthetic_object_036_E1`

**原始英文指令：** At 8.5 seconds, add one blue wheeled recycling bin against the left brick wall beside the van's route.

**中文翻译：** 在第 8.5 秒，在货车路线旁的左侧砖墙边添加一个蓝色带轮回收箱。

**状态：** 接受

**原子化判定句：**

1. 货车路线旁的左侧砖墙边是否添加了一个回收箱？

2. 回收箱是否为蓝色？

3. 回收箱是否带轮？


## 107 — `synthetic_object_036_E2A`

**原始英文指令：** Starting at 31 seconds, reduce the white van's forward speed to half its original rate for the next five seconds.

**中文翻译：** 从第 31 秒开始，将白色货车的前进速度降低到原来的一半，持续接下来的五秒。

**状态：** 接受

**原子化判定句：**

1. 白色货车是否继续向前行驶？

2. 其前进速度是否降低到原来的一半？

3. 降低后的速度是否持续 5 秒？


## 108 — `synthetic_object_036_E2B`

**原始英文指令：** Starting at 21.5 seconds, change the weather across the residential street to bright sunshine under a clear sky over two seconds.

**中文翻译：** 从第 21.5 秒开始，在两秒内将住宅街道的天气改为晴空下的明亮阳光。

**状态：** 接受

**原子化判定句：**

1. 住宅街道是否出现明亮阳光？

2. 天空是否变得晴朗？

3. 天气变化是否在 2 秒内完成？


## 109 — `synthetic_object_037_E1`

**原始英文指令：** Starting at 12.5 seconds, make two broad diagonal ripple fronts travel across the lake toward the shore over five seconds.

**中文翻译：** 从第 12.5 秒开始，让两道宽阔的斜向波纹前沿在五秒内横穿湖面并向岸边传播。

**状态：** 接受

**原子化判定句：**

1. 湖面上是否恰好出现两道波纹前沿？

2. 波纹前沿是否宽阔且呈斜向？

3. 波纹是否横穿湖面并向岸边传播？

4. 传播是否在 5 秒内完成？


## 110 — `synthetic_object_037_E2A`

**原始英文指令：** Starting at 35 seconds, transform the full lakeside motorhome scene into a muted 1970s color-film look over two seconds.

**中文翻译：** 从第 35 秒开始，在两秒内将整个湖畔房车场景转变为低饱和的 1970 年代彩色胶片风格。

**状态：** 接受

**原子化判定句：**

1. 整个湖畔房车场景是否呈现彩色胶片风格？

2. 画面是否具有 1970 年代的视觉特征？

3. 色彩处理是否低饱和、柔和？

4. 转变是否在 2 秒内完成？


## 111 — `synthetic_object_037_E2B`

**原始英文指令：** Starting at 25.5 seconds, change the motorhome's cream side panels to pale sage green over the next two seconds.

**中文翻译：** 从第 25.5 秒开始，在接下来的两秒内将房车的奶油色侧面板改为浅鼠尾草绿色。

**状态：** 接受

**原子化判定句：**

1. 房车的奶油色侧面板是否变为浅鼠尾草绿色？

2. 颜色变化是否在 2 秒内完成？


## 112 — `synthetic_object_038_E1`

**原始英文指令：** Starting at 13.5 seconds, increase the red van's reversing speed to one-and-a-half times its original rate for four seconds.

**中文翻译：** 从第 13.5 秒开始，将红色货车的倒车速度提高到原来的 1.5 倍，持续四秒。

**状态：** 接受

**原子化判定句：**

1. 红色货车是否继续倒车？

2. 倒车速度是否提高到原来的 1.5 倍？

3. 提高后的速度是否持续 4 秒？


## 113 — `synthetic_object_038_E2A`

**原始英文指令：** Starting at 31 seconds, change the visible white parking-bay lines to bright yellow over the next two seconds.

**中文翻译：** 从第 31 秒开始，在接下来的两秒内将可见的白色停车位线改为亮黄色。

**状态：** 接受

**原子化判定句：**

1. 可见的停车位线是否从白色变为亮黄色？

2. 颜色变化是否在 2 秒内完成？


## 114 — `synthetic_object_038_E2B`

**原始英文指令：** At 24.5 seconds, shift the red van forward by one full parking-bay length along its current heading.

**中文翻译：** 在第 24.5 秒，将红色货车沿当前朝向向前移动一个完整停车位长度。

**状态：** 接受

**原子化判定句：**

1. 红色货车是否沿当前朝向向前移动？

2. 移动距离是否为一个完整停车位长度？


## 115 — `synthetic_object_039_E1`

**原始英文指令：** Starting at 14.5 seconds, make the tanker truck wheels strike an uneven road section and produce one small hop before continuing forward.

**中文翻译：** 从第 14.5 秒开始，让罐式卡车车轮撞上不平路段，产生一次小幅跳起后继续前进。

**状态：** 接受

**原子化判定句：**

1. 罐式卡车车轮是否撞上不平路段？

2. 罐式卡车是否产生一次小幅跳起？

3. 随后罐式卡车是否继续前进？


## 116 — `synthetic_object_039_E2A`

**原始英文指令：** Starting at 31.5 seconds, change the roadside grassland from fresh green to dry golden yellow over two seconds.

**中文翻译：** 从第 31.5 秒开始，在两秒内将路边草地从鲜绿色改为干燥金黄色。

**状态：** 接受

**原子化判定句：**

1. 路边草地是否从鲜绿色变为金黄色？

2. 草地是否呈干燥状态？

3. 变化是否在 2 秒内完成？


## 117 — `synthetic_object_039_E2B`

**原始英文指令：** At 25.5 seconds, add a flock of twelve sheep across the open grassland well away from the highway.

**中文翻译：** 在第 25.5 秒，在远离公路的开阔草地上添加一群十二只羊。

**状态：** 接受

**原子化判定句：**

1. 开阔草地上是否添加了一群羊？

2. 羊群是否恰好包含 12 只羊？

3. 羊群是否远离公路？


## 118 — `synthetic_object_040_E1`

**原始英文指令：** At 16 seconds, rotate the glass transit shelter beside the trolleybus until its rear face points directly toward the camera.

**中文翻译：** 在第 16 秒，旋转无轨电车旁的玻璃公交候车亭，直到其后侧面正对镜头。

**状态：** 接受

**原子化判定句：**

1. 无轨电车旁的玻璃公交候车亭是否被旋转？

2. 候车亭的后侧面最终是否正对镜头？


## 119 — `synthetic_object_040_E2A`

**原始英文指令：** Starting at 34 seconds, change the unmarked road surface around the trolleybus from dark asphalt to pale concrete over two seconds.

**中文翻译：** 从第 34 秒开始，在两秒内将无轨电车周围无标线的路面从深色沥青改为浅色混凝土。

**状态：** 接受

**原子化判定句：**

1. 无轨电车周围无标线的路面是否从沥青变为混凝土？

2. 混凝土路面是否为浅色？

3. 变化是否在 2 秒内完成？


## 120 — `synthetic_object_040_E2B`

**原始英文指令：** Starting at 28 seconds, raise the camera smoothly into a high rear tracking view above the trolleybus over five seconds.

**中文翻译：** 从第 28 秒开始，在五秒内将镜头平滑抬高到无轨电车上方的高位后方跟拍视角。

**状态：** 接受

**原子化判定句：**

1. 镜头是否抬高到无轨电车上方？

2. 镜头移动是否平滑？

3. 镜头是否到达高位后方跟拍视角？

4. 镜头是否在 5 秒内到达该视角？


## 121 — `synthetic_object_041_E1`

**原始英文指令：** Starting at 12.5 seconds, render only the sailboat's forward triangular sail as translucent pale-blue and amber stained glass.

**中文翻译：** 从第 12.5 秒开始，仅将帆船前部三角帆呈现为浅蓝色与琥珀色的半透明彩绘玻璃。

**状态：** 接受

**原子化判定句：**

1. 帆船前部三角帆是否被呈现为彩绘玻璃？

2. 玻璃是否使用浅蓝色与琥珀色？

3. 玻璃是否半透明？

4. 该处理是否仅作用于这面帆？


## 122 — `synthetic_object_041_E2A`

**原始英文指令：** Starting at 31 seconds, make the sailboat's starboard wake push the nearby yellow buoy outward once before it settles.

**中文翻译：** 从第 31 秒开始，让帆船右舷尾流将附近的黄色浮标向外推开一次，然后使浮标稳定下来。

**状态：** 接受

**原子化判定句：**

1. 帆船右舷尾流是否将附近的黄色浮标向外推开一次？

2. 随后黄色浮标是否稳定下来？


## 123 — `synthetic_object_041_E2B`

**原始英文指令：** At 25 seconds, add one red spherical buoy two boat-lengths behind the sailboat's port hull in the open water.

**中文翻译：** 在第 25 秒，在帆船左舷船体后方两个船长的开阔水域添加一个红色球形浮标。

**状态：** 接受

**原子化判定句：**

1. 帆船左舷船体后方的开阔水域是否添加了一个浮标？

2. 浮标是否为红色？

3. 浮标是否为球形？

4. 浮标是否位于船体后方两个船长处？


## 124 — `synthetic_object_042_E1`

**原始英文指令：** Starting at 13 seconds, change the undisturbed water beyond the speedboat's wake from blue-gray to clear deep turquoise.

**中文翻译：** 从第 13 秒开始，将快艇尾流以外未受扰动的水面从蓝灰色改为清澈的深青绿色。

**状态：** 接受

**原子化判定句：**

1. 快艇尾流以外未受扰动的水面是否从蓝灰色变为深青绿色？

2. 水面是否显得清澈？


## 125 — `synthetic_object_042_E2A`

**原始英文指令：** At 36 seconds, remove the nearest orange conical buoy visible ahead and to the speedboat's right.

**中文翻译：** 在第 36 秒，移除快艇前方偏右最近的可见橙色锥形浮标。

**状态：** 接受

**原子化判定句：**

1. 快艇前方偏右最近的可见橙色锥形浮标是否被移除？


## 126 — `synthetic_object_042_E2B`

**原始英文指令：** Starting at 26.5 seconds, make the red-and-white speedboat perform two short alternating left-right turns before continuing forward.

**中文翻译：** 从第 26.5 秒开始，让红白快艇完成两次短促的左右交替转向，然后继续向前行驶。

**状态：** 接受

**原子化判定句：**

1. 红白快艇是否完成两次短促的左右交替转向？

2. 随后快艇是否继续向前行驶？


## 127 — `synthetic_object_043_E1`

**原始英文指令：** At 12 seconds, remove the yellow channel marker standing in the water to the approaching container ship's right.

**中文翻译：** 在第 12 秒，移除驶近集装箱船右侧水中竖立的黄色航道标志。

**状态：** 接受

**原子化判定句：**

1. 驶近集装箱船右侧水中竖立的黄色航道标志是否被移除？


## 128 — `synthetic_object_043_E2A`

**原始英文指令：** Starting at 35.5 seconds, make the dark harbor vessel cross the blue-and-white vessel's wake and roll gently once.

**中文翻译：** 从第 35.5 秒开始，让深色港口船穿过蓝白船只的尾流，并轻轻横摇一次。

**状态：** 接受

**原子化判定句：**

1. 深色港口船是否穿过蓝白船只的尾流？

2. 深色港口船是否轻轻横摇一次？


## 129 — `synthetic_object_043_E2B`

**原始英文指令：** Starting at 20 seconds, coat the uppermost visible blue container row with a thin layer of frost over two seconds.

**中文翻译：** 从第 20 秒开始，在两秒内为最上方可见的蓝色集装箱一排覆上一层薄霜。

**状态：** 接受

**原子化判定句：**

1. 最上方可见的蓝色集装箱一排是否覆有霜？

2. 霜层是否较薄？

3. 覆霜是否在 2 秒内完成？


## 130 — `synthetic_object_044_E1`

**原始英文指令：** Starting at 13.5 seconds, make the small tugboat reverse one tugboat-width away from the cargo ship and hold there.

**中文翻译：** 从第 13.5 秒开始，让小型拖船倒退一个拖船宽度以远离货船，并停留在该位置。

**状态：** 接受

**原子化判定句：**

1. 小型拖船是否倒退一个拖船宽度以远离货船？

2. 随后拖船是否停留在该位置？


## 131 — `synthetic_object_044_E2A`

**原始英文指令：** At 33 seconds, add one yellow spherical buoy two tugboat-lengths to the right of the small tugboat.

**中文翻译：** 在第 33 秒，在小型拖船右侧两个拖船长度处添加一个黄色球形浮标。

**状态：** 接受

**原子化判定句：**

1. 小型拖船右侧是否添加了一个浮标？

2. 浮标是否为黄色？

3. 浮标是否为球形？

4. 浮标与拖船的距离是否为两个拖船长度？


## 132 — `synthetic_object_044_E2B`

**原始英文指令：** Starting at 25.5 seconds, compress and flatten the front section of the tugboat's thick black bow fender over two seconds.

**中文翻译：** 从第 25.5 秒开始，在两秒内将拖船厚实黑色船首护舷的前段压缩并压平。

**状态：** 接受

**原子化判定句：**

1. 拖船船首护舷的前段是否被压缩？

2. 该部分是否被压平？

3. 两项变化是否在 2 秒内完成？


## 133 — `synthetic_object_045_E1`

**原始英文指令：** Starting at 12.5 seconds, make the catamaran's forward sail flap outward and return twice over four seconds.

**中文翻译：** 从第 12.5 秒开始，让双体船前帆在四秒内向外摆动并返回两次。

**状态：** 接受

**原子化判定句：**

1. 双体船前帆是否向外摆动？

2. 前帆是否在每次外摆后返回？

3. 前帆是否恰好完成两次外摆—返回循环？

4. 两次循环是否在 4 秒内完成？


## 134 — `synthetic_object_045_E2A`

**原始英文指令：** Starting at 31 seconds, change the catamaran's dark aft canopy from dry and matte to rain-wet and glossy.

**中文翻译：** 从第 31 秒开始，将双体船深色后部顶篷从干燥哑光改为被雨淋湿且有光泽。

**状态：** 接受

**原子化判定句：**

1. 双体船深色后部顶篷是否变为被雨淋湿的状态？

2. 变湿后的顶篷是否呈现光泽？


## 135 — `synthetic_object_045_E2B`

**原始英文指令：** Starting at 25.5 seconds, transform the full catamaran scene into a muted 1970s color-film look over two seconds.

**中文翻译：** 从第 25.5 秒开始，在两秒内将整个双体船场景转变为低饱和的 1970 年代彩色胶片风格。

**状态：** 接受

**原子化判定句：**

1. 整个双体船场景是否呈现彩色胶片风格？

2. 画面是否具有 1970 年代的视觉特征？

3. 色彩处理是否低饱和、柔和？

4. 转变是否在 2 秒内完成？


## 136 — `synthetic_object_046_E1`

**原始英文指令：** At 13 seconds, shift the complete yellow motorboat one boat-width toward the left side of the frame.

**中文翻译：** 在第 13 秒，将整艘黄色摩托艇向画面左侧移动一个船宽。

**状态：** 接受

**原子化判定句：**

1. 整艘黄色摩托艇是否向画面左侧移动？

2. 移动距离是否为一个船宽？


## 137 — `synthetic_object_046_E2A`

**原始英文指令：** Starting at 26 seconds, make the yellow motorboat's bow strike the approaching wave and throw one tall symmetrical spray fan.

**中文翻译：** 从第 26 秒开始，让黄色摩托艇船首撞上迎面波浪，并激起一道高而对称的扇形水花。

**状态：** 接受

**原子化判定句：**

1. 黄色摩托艇船首是否撞上迎面波浪？

2. 撞击是否激起一道高而对称的扇形水花？


## 138 — `synthetic_object_046_E2B`

**原始英文指令：** Starting at 24.5 seconds, smoothly zoom out until the yellow motorboat occupies about one fifth of the frame height.

**中文翻译：** 从第 24.5 秒开始，平滑拉远镜头，直到黄色摩托艇约占画面高度的五分之一。

**状态：** 接受

**原子化判定句：**

1. 镜头是否拉远？

2. 拉远过程是否平滑？

3. 黄色摩托艇最终是否约占画面高度的五分之一？


## 139 — `synthetic_object_047_E1`

**原始英文指令：** Starting at 12 seconds, increase the submarine's forward speed to twice its original rate along the same underwater path for five seconds.

**中文翻译：** 从第 12 秒开始，将潜艇沿同一水下路径的前进速度提高到原来的两倍，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 潜艇是否继续沿同一水下路径前进？

2. 其前进速度是否提高到原来的两倍？

3. 提高后的速度是否持续 5 秒？


## 140 — `synthetic_object_047_E2A`

**原始英文指令：** Starting at 30.5 seconds, arc the camera smoothly upward and inward to a near-overhead view of the submarine.

**中文翻译：** 从第 30.5 秒开始，让镜头沿弧线平滑向上并向内移动，到达近乎俯视潜艇的视角。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿弧线向上并向内移动？

2. 镜头移动是否平滑？

3. 镜头是否到达近乎俯视潜艇的视角？


## 141 — `synthetic_object_047_E2B`

**原始英文指令：** At 24.5 seconds, remove the large isolated boulder lying on the seabed below and ahead of the submarine.

**中文翻译：** 在第 24.5 秒，移除潜艇下方前方海床上的大型孤立巨石。

**状态：** 接受

**原子化判定句：**

1. 潜艇下方前方海床上的大型孤立巨石是否被移除？


## 142 — `synthetic_object_048_E1`

**原始英文指令：** Starting at 12.5 seconds, increase the hovercraft's forward speed to one-and-a-half times its original rate for five seconds.

**中文翻译：** 从第 12.5 秒开始，将气垫船的前进速度提高到原来的 1.5 倍，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 气垫船是否继续向前行驶？

2. 其前进速度是否提高到原来的 1.5 倍？

3. 提高后的速度是否持续 5 秒？


## 143 — `synthetic_object_048_E2A`

**原始英文指令：** At 31 seconds, move the hovercraft one body-length closer to the far shoreline along its existing forward heading.

**中文翻译：** 在第 31 秒，将气垫船沿现有前进方向向远岸再靠近一个船身长度。

**状态：** 接受

**原子化判定句：**

1. 气垫船是否向远岸靠近？

2. 气垫船是否沿现有前进方向移动？

3. 移动距离是否为一个船身长度？


## 144 — `synthetic_object_048_E2B`

**原始英文指令：** Starting at 25 seconds, fully inflate the hovercraft's black skirt and lift the rigid white body visibly higher above the water.

**中文翻译：** 从第 25 秒开始，将气垫船的黑色裙体完全充气，并使刚性白色船体明显升高到水面上方。

**状态：** 接受

**原子化判定句：**

1. 气垫船的黑色裙体是否完全充气？

2. 刚性白色船体是否明显升高到水面上方？


## 145 — `synthetic_object_049_E1`

**原始英文指令：** Starting at 14 seconds, change the undisturbed lake water beyond the floatplane's spray from gray-blue to clear emerald green.

**中文翻译：** 从第 14 秒开始，将水上飞机水花以外未受扰动的湖水从灰蓝色改为清澈的祖母绿色。

**状态：** 接受

**原子化判定句：**

1. 水上飞机水花以外未受扰动的湖水是否从灰蓝色变为祖母绿色？

2. 湖水是否显得清澈？


## 146 — `synthetic_object_049_E2A`

**原始英文指令：** At 30.5 seconds, add one yellow spherical marker buoy three wing-lengths ahead of the taxiing floatplane.

**中文翻译：** 在第 30.5 秒，在滑行水上飞机前方三个翼展长度处添加一个黄色球形标志浮标。

**状态：** 接受

**原子化判定句：**

1. 滑行水上飞机前方是否添加了一个标志浮标？

2. 浮标是否为黄色？

3. 浮标是否为球形？

4. 浮标是否位于飞机前方三个翼展长度处？


## 147 — `synthetic_object_049_E2B`

**原始英文指令：** Starting at 26 seconds, make the floatplane's twin floats bounce once together on the lake and settle into a steady skim.

**中文翻译：** 从第 26 秒开始，让水上飞机的双浮筒在湖面同步弹跳一次，然后稳定贴水滑行。

**状态：** 接受

**原子化判定句：**

1. 水上飞机的双浮筒是否在湖面同步弹跳一次？

2. 随后双浮筒是否稳定贴水滑行？


## 148 — `synthetic_object_050_E1`

**原始英文指令：** Starting at 12.5 seconds, make the helicopter's rotor wash press one circular patch of treetops downward before it rebounds.

**中文翻译：** 从第 12.5 秒开始，让直升机旋翼下洗气流将一块圆形树冠区域向下压，然后使其回弹。

**状态：** 接受

**原子化判定句：**

1. 直升机旋翼下洗气流是否将一块圆形树冠区域向下压？

2. 随后该树冠区域是否回弹？


## 149 — `synthetic_object_050_E2A`

**原始英文指令：** At 30.5 seconds, position the helicopter directly behind and two rotor-diameters above the prominent rock pinnacle below.

**中文翻译：** 在第 30.5 秒，将直升机放置在下方突出岩石尖峰的正后方、上方两个旋翼直径处。

**状态：** 接受

**原子化判定句：**

1. 直升机是否被放置在突出岩石尖峰的正后方？

2. 直升机是否位于岩石尖峰上方两个旋翼直径处？


## 150 — `synthetic_object_050_E2B`

**原始英文指令：** Starting at 20 seconds, open the helicopter's right-side cabin door fully and reveal the dark cabin opening over two seconds.

**中文翻译：** 从第 20 秒开始，在两秒内将直升机右侧舱门完全打开，并露出深色舱口。

**状态：** 接受

**原子化判定句：**

1. 直升机右侧舱门是否在 2 秒内完全打开？

2. 深色舱口是否露出？


## 151 — `synthetic_object_051_E1`

**原始英文指令：** At 14.5 seconds, replace the ferry's first red-and-black upper-deck housing with a silver cylindrical ventilation pod of comparable size.

**中文翻译：** 在第 14.5 秒，将渡轮第一个红黑色上层甲板舱体替换为尺寸相当的银色圆柱形通风舱。

**状态：** 接受

**原子化判定句：**

1. 渡轮第一个红黑色上层甲板舱体是否被替换为银色圆柱形通风舱？

2. 银色通风舱是否与原舱体尺寸相当？


## 152 — `synthetic_object_051_E2A`

**原始英文指令：** Starting at 32 seconds, raise the ferry's broad black dock ramp from the roadway to a fully upright closed position.

**中文翻译：** 从第 32 秒开始，将渡轮宽大的黑色码头坡道从路面抬起至完全直立关闭的位置。

**状态：** 接受

**原子化判定句：**

1. 渡轮宽大的黑色码头坡道是否从路面抬起？

2. 坡道是否达到完全直立关闭的位置？


## 153 — `synthetic_object_051_E2B`

**原始英文指令：** At 26 seconds, rotate the nearest dark car on the dock to face directly toward the center of the ferry ramp.

**中文翻译：** 在第 26 秒，旋转码头上最近的深色汽车，使其正对渡轮坡道中央。

**状态：** 接受

**原子化判定句：**

1. 码头上最近的深色汽车是否被旋转？

2. 汽车最终是否正对渡轮坡道中央？


## 154 — `synthetic_object_052_E1`

**原始英文指令：** Starting at 13 seconds, change the yacht's black side-window band to deep navy blue over the next two seconds.

**中文翻译：** 从第 13 秒开始，在接下来的两秒内将游艇黑色侧窗带改为深海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 游艇侧窗带是否从黑色变为深海军蓝色？

2. 颜色变化是否在 2 秒内完成？


## 155 — `synthetic_object_052_E2A`

**原始英文指令：** At 31 seconds, reposition the yacht so the nearest pale water marker remains two yacht-widths off its starboard side.

**中文翻译：** 在第 31 秒，重新放置游艇，使最近的浅色水面标志物保持在其右舷外两个游艇宽度处。

**状态：** 接受

**原子化判定句：**

1. 最近的浅色水面标志物是否位于游艇右舷外？

2. 标志物与游艇的间距是否为两个游艇宽度？


## 156 — `synthetic_object_052_E2B`

**原始英文指令：** Starting at 25.5 seconds, increase the yacht's forward speed to one-and-a-half times its original rate for five seconds.

**中文翻译：** 从第 25.5 秒开始，将游艇的前进速度提高到原来的 1.5 倍，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 游艇是否继续向前航行？

2. 其前进速度是否提高到原来的 1.5 倍？

3. 提高后的速度是否持续 5 秒？


## 157 — `synthetic_object_053_E1`

**原始英文指令：** Starting at 11.5 seconds, arc the camera smoothly from the trawler's port rear to a centered view behind the deployed net.

**中文翻译：** 从第 11.5 秒开始，让镜头沿弧线从拖网渔船左舷后方平滑移动到展开渔网后方的居中视角。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿弧线从拖网渔船左舷后方移动到展开渔网后方的居中视角？

2. 镜头移动是否平滑？


## 158 — `synthetic_object_053_E2A`

**原始英文指令：** Starting at 31 seconds, change the deployed fishing net's pale-gray mesh to bright orange over the next two seconds.

**中文翻译：** 从第 31 秒开始，在接下来的两秒内将展开渔网的浅灰色网眼改为亮橙色。

**状态：** 接受

**原子化判定句：**

1. 展开渔网的网眼是否从浅灰色变为亮橙色？

2. 颜色变化是否在 2 秒内完成？


## 159 — `synthetic_object_053_E2B`

**原始英文指令：** At 24 seconds, add one red spherical float beside the deployed net's left trailing corner and connect it to the edge line.

**中文翻译：** 在第 24 秒，在展开渔网左侧后角旁添加一个红色球形浮子，并将其连接到边缘绳。

**状态：** 接受

**原子化判定句：**

1. 展开渔网左侧后角旁是否添加了一个红色球形浮子？

2. 该浮子是否连接到渔网边缘绳？


## 160 — `synthetic_object_054_E1`

**原始英文指令：** At 13.5 seconds, shift the suspended red buoy two buoy-widths farther from the workboat's right side.

**中文翻译：** 在第 13.5 秒，将悬挂的红色浮标移动到离工作船右侧再远两个浮标宽度的位置。

**状态：** 接受

**原子化判定句：**

1. 悬挂的红色浮标是否被移得更远离工作船右侧？

2. 间距是否增加了两个浮标宽度？


## 161 — `synthetic_object_054_E2A`

**原始英文指令：** Starting at 20.5 seconds, make three broad circular ripple rings travel outward across the water beneath the suspended buoy.

**中文翻译：** 从第 20.5 秒开始，让三道宽阔圆形波纹环在悬挂浮标下方水面向外传播。

**状态：** 接受

**原子化判定句：**

1. 悬挂浮标下方水面是否恰好出现三道圆形波纹环？

2. 波纹环是否宽阔？

3. 波纹环是否向外传播？


## 162 — `synthetic_object_054_E2B`

**原始英文指令：** Starting at 25.5 seconds, change the suspended buoy from saturated red to bright safety yellow over two seconds.

**中文翻译：** 从第 25.5 秒开始，在两秒内将悬挂浮标从饱和红色改为明亮安全黄色。

**状态：** 接受

**原子化判定句：**

1. 悬挂浮标是否从饱和红色变为明亮安全黄色？

2. 颜色变化是否在 2 秒内完成？


## 163 — `synthetic_object_055_E1`

**原始英文指令：** At 11.5 seconds, remove the small light-gray landing platform projecting from the far riverbank above the cargo ship.

**中文翻译：** 在第 11.5 秒，移除货船上方远岸伸出的小型浅灰色登陆平台。

**状态：** 接受

**原子化判定句：**

1. 货船上方远岸伸出的小型浅灰色登陆平台是否被移除？


## 164 — `synthetic_object_055_E2A`

**原始英文指令：** Starting at 32 seconds, change the cargo ship's white-and-green exterior to a unified deep navy blue over two seconds.

**中文翻译：** 从第 32 秒开始，在两秒内将货船白绿相间的外观统一改为深海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 货船白绿相间的外观是否统一变为深海军蓝色？

2. 颜色变化是否在 2 秒内完成？


## 165 — `synthetic_object_055_E2B`

**原始英文指令：** Starting at 23.5 seconds, make the long cargo ship follow one shallow S-shaped path while remaining between the bridge supports.

**中文翻译：** 从第 23.5 秒开始，让长货船沿一条浅 S 形路径航行，同时保持位于桥墩之间。

**状态：** 接受

**原子化判定句：**

1. 长货船是否沿一条浅 S 形路径航行？

2. 航行过程中，货船是否始终保持位于桥墩之间？


## 166 — `synthetic_object_056_E1`

**原始英文指令：** Starting at 13.5 seconds, illuminate the full black gondola and standing paddler with a warm spotlight from above-left.

**中文翻译：** 从第 13.5 秒开始，用来自左上方的暖色聚光灯照亮整艘黑色贡多拉和站立的划船者。

**状态：** 接受

**原子化判定句：**

1. 整艘黑色贡多拉是否被聚光灯照亮？

2. 站立的划船者是否被同一聚光灯照亮？

3. 光线是否为暖色？

4. 光线是否来自左上方？


## 167 — `synthetic_object_056_E2A`

**原始英文指令：** At 31 seconds, replace the gondola's central red passenger seat with a blue upholstered bench of matching width.

**中文翻译：** 在第 31 秒，将贡多拉中央的红色乘客座椅替换为宽度匹配的蓝色软垫长凳。

**状态：** 接受

**原子化判定句：**

1. 贡多拉中央的红色乘客座椅是否被替换为长凳？

2. 替换后的长凳是否为蓝色？

3. 长凳是否带软垫？

4. 长凳宽度是否与原座椅匹配？


## 168 — `synthetic_object_056_E2B`

**原始英文指令：** Starting at 25.5 seconds, make the standing paddler lift the wooden oar, spin it once, and resume rowing.

**中文翻译：** 从第 25.5 秒开始，让站立的划船者抬起木桨、旋转一圈，然后恢复划船。

**状态：** 接受

**原子化判定句：**

1. 站立的划船者是否抬起木桨？

2. 划船者是否将木桨旋转一圈？

3. 随后划船者是否恢复划船？


## 169 — `synthetic_object_057_E1`

**原始英文指令：** Starting at 13 seconds, make the orange motorboat cross the cargo ship's wake, roll once to starboard, and level out.

**中文翻译：** 从第 13 秒开始，让橙色摩托艇穿过货船尾流、向右舷横摇一次，然后恢复水平。

**状态：** 接受

**原子化判定句：**

1. 橙色摩托艇是否穿过货船尾流？

2. 它是否向右舷横摇一次？

3. 随后摩托艇是否恢复水平？


## 170 — `synthetic_object_057_E2A`

**原始英文指令：** Starting at 31 seconds, open the orange motorboat's white roof hatch fully and leave it raised above the cabin.

**中文翻译：** 从第 31 秒开始，将橙色摩托艇的白色顶舱盖完全打开，并保持抬起在船舱上方。

**状态：** 接受

**原子化判定句：**

1. 橙色摩托艇的白色顶舱盖是否完全打开？

2. 舱盖是否保持抬起在船舱上方？


## 171 — `synthetic_object_057_E2B`

**原始英文指令：** At 25.5 seconds, remove the small white radar dome mounted above the orange motorboat's cabin.

**中文翻译：** 在第 25.5 秒，移除安装在橙色摩托艇船舱上方的小型白色雷达罩。

**状态：** 接受

**原子化判定句：**

1. 安装在橙色摩托艇船舱上方的小型白色雷达罩是否被移除？


## 172 — `synthetic_object_058_E1`

**原始英文指令：** Starting at 10.5 seconds, accelerate the buoy-lowering process so the red buoy first touches the water by 16 seconds.

**中文翻译：** 从第 10.5 秒开始，加快浮标下放过程，使红色浮标在第 16 秒前首次接触水面。

**状态：** 接受

**原子化判定句：**

1. 浮标下放过程是否以更快的速度继续？

2. 红色浮标是否在 5.5 秒内首次接触水面？


## 173 — `synthetic_object_058_E2A`

**原始英文指令：** Starting at 30 seconds, make the tethered red buoy perform three clear vertical bobs while remaining connected to the crane cable.

**中文翻译：** 从第 30 秒开始，让系住的红色浮标清晰地上下浮动三次，同时保持与起重机缆绳连接。

**状态：** 接受

**原子化判定句：**

1. 系住的红色浮标是否清晰地上下浮动三次？

2. 浮动过程中，浮标是否始终与起重机缆绳连接？


## 174 — `synthetic_object_058_E2B`

**原始英文指令：** Starting at 24 seconds, change the conical buoy from saturated red to vivid safety orange over the next two seconds.

**中文翻译：** 从第 24 秒开始，在接下来的两秒内将锥形浮标从饱和红色改为鲜艳安全橙色。

**状态：** 接受

**原子化判定句：**

1. 锥形浮标是否从饱和红色变为鲜艳安全橙色？

2. 颜色变化是否在 2 秒内完成？


## 175 — `synthetic_object_059_E1`

**原始英文指令：** Starting at 12.5 seconds, make the motorboat's trailing wake divide into three distinct parallel ripple bands for five seconds.

**中文翻译：** 从第 12.5 秒开始，让摩托艇的尾流分成三道清晰平行的波纹带，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 摩托艇的尾流是否分成恰好三道波纹带？

2. 三道波纹带是否清晰可分？

3. 波纹带是否彼此平行？

4. 波纹带是否持续 5 秒？


## 176 — `synthetic_object_059_E2A`

**原始英文指令：** Starting at 34 seconds, render only the stone breakwater behind the motorboat as a soft hand-painted watercolor band.

**中文翻译：** 从第 34 秒开始，仅将摩托艇后方的石质防波堤呈现为柔和的手绘水彩带。

**状态：** 接受

**原子化判定句：**

1. 摩托艇后方的石质防波堤是否被呈现为水彩带？

2. 水彩带是否具有手绘外观？

3. 水彩效果是否柔和？

4. 该处理是否仅作用于防波堤？


## 177 — `synthetic_object_059_E2B`

**原始英文指令：** At 25.5 seconds, move the motorboat one boat-length closer to the stone breakwater.

**中文翻译：** 在第 25.5 秒，将摩托艇向石质防波堤靠近一个船长。

**状态：** 接受

**原子化判定句：**

1. 摩托艇是否向石质防波堤靠近？

2. 移动距离是否为一个船长？


## 178 — `synthetic_object_060_E1`

**原始英文指令：** Starting at 13.5 seconds, bend the underwater vehicle's near-side yellow wingtip visibly upward over the next two seconds.

**中文翻译：** 从第 13.5 秒开始，在接下来的两秒内将水下航行器近侧黄色翼尖明显向上弯曲。

**状态：** 接受

**原子化判定句：**

1. 水下航行器近侧黄色翼尖是否明显向上弯曲？

2. 弯曲是否在 2 秒内完成？


## 179 — `synthetic_object_060_E2A`

**原始英文指令：** Starting at 31 seconds, reduce the underwater vehicle's forward speed to half its original rate for the next five seconds.

**中文翻译：** 从第 31 秒开始，将水下航行器的前进速度降低到原来的一半，持续接下来的五秒。

**状态：** 接受

**原子化判定句：**

1. 水下航行器是否继续前进？

2. 其前进速度是否降低到原来的一半？

3. 降低后的速度是否持续 5 秒？


## 180 — `synthetic_object_060_E2B`

**原始英文指令：** At 26 seconds, remove the small dark protrusion mounted on top of the underwater vehicle's middle fuselage.

**中文翻译：** 在第 26 秒，移除安装在水下航行器中部机身顶部的小型深色突起物。

**状态：** 接受

**原子化判定句：**

1. 安装在水下航行器中部机身顶部的小型深色突起物是否被移除？


## 181 — `synthetic_object_061_E1`

**原始英文指令：** Starting at 12 seconds, illuminate the gripped metal gear with a cool circular inspection light over the next two seconds.

**中文翻译：** 从第 12 秒开始，在接下来的两秒内用冷色圆形检查灯照亮被夹持的金属齿轮。

**状态：** 接受

**原子化判定句：**

1. 被夹持的金属齿轮是否由检查灯照亮？

2. 检查灯是否为冷色圆形光斑？

3. 照明变化是否在 2 秒内完成？


## 182 — `synthetic_object_061_E2A`

**原始英文指令：** At 23.5 seconds, center the gear's opening directly above the circular recess in the right fixture.

**中文翻译：** 在第 23.5 秒，将齿轮开口中心对准右侧夹具圆形凹槽的正上方。

**状态：** 接受

**原子化判定句：**

1. 齿轮开口是否居中对准右侧夹具圆形凹槽的正上方？


## 183 — `synthetic_object_061_E2B`

**原始英文指令：** Starting at 24.5 seconds, make the gripped gear complete one full axial rotation while descending toward the right fixture.

**中文翻译：** 从第 24.5 秒开始，让被夹持的齿轮在向右侧夹具下降时绕轴完整旋转一圈。

**状态：** 接受

**原子化判定句：**

1. 被夹持的齿轮是否向右侧夹具下降？

2. 下降过程中，它是否绕轴完整旋转一圈？


## 184 — `synthetic_object_062_E1`

**原始英文指令：** Starting at 11.5 seconds, make the loaded warehouse carrier complete its aisle turn at twice the original angular speed.

**中文翻译：** 从第 11.5 秒开始，让载货仓库运输车以原来两倍的角速度完成过道转弯。

**状态：** 接受

**原子化判定句：**

1. 载货仓库运输车是否完成过道转弯？

2. 转弯角速度是否为原来的两倍？


## 185 — `synthetic_object_062_E2A`

**原始英文指令：** Starting at 26 seconds, make the loaded carrier stop completely inside the striped floor grid before raising its cargo frame higher.

**中文翻译：** 从第 26 秒开始，让载货运输车完全停在条纹地面网格内，然后将货物框架进一步升高。

**状态：** 接受

**原子化判定句：**

1. 载货运输车是否完全停在条纹地面网格内？

2. 停止后，它是否将货物框架进一步升高？


## 186 — `synthetic_object_062_E2B`

**原始英文指令：** At 24.5 seconds, replace the front row of brown cartons on the raised pallet with three blue reusable plastic crates.

**中文翻译：** 在第 24.5 秒，将抬起托盘前排的棕色纸箱替换为三个蓝色可重复使用塑料箱。

**状态：** 接受

**原子化判定句：**

1. 抬起托盘前排的棕色纸箱是否被替换为恰好三个箱子？

2. 替换后的箱子是否为蓝色？

3. 箱子是否为塑料材质？

4. 箱子是否呈可重复使用的结构？


## 187 — `synthetic_object_063_E1`

**原始英文指令：** Starting at 6 seconds, accelerate the humanoid robot's standing-up process so it reaches a stable upright posture by 8 seconds.

**中文翻译：** 从第 6 秒开始，加快人形机器人的起身过程，使其在第 8 秒前达到稳定直立姿势。

**状态：** 接受

**原子化判定句：**

1. 人形机器人的起身过程是否加快？

2. 机器人是否在 2 秒内达到稳定直立姿势？


## 188 — `synthetic_object_063_E2A`

**原始英文指令：** At 28 seconds, replace the black four-legged chair behind the humanoid robot with a silver backless metal stool.

**中文翻译：** 在第 28 秒，将人形机器人后方的黑色四脚椅替换为银色无靠背金属凳。

**状态：** 接受

**原子化判定句：**

1. 人形机器人后方的黑色四脚椅是否被替换为凳子？

2. 替换后的凳子是否为银色？

3. 凳子是否无靠背？

4. 凳子是否为金属材质？


## 189 — `synthetic_object_063_E2B`

**原始英文指令：** Starting at 20.5 seconds, make the humanoid robot raise its right forearm, wave twice at chest height, and lower it.

**中文翻译：** 从第 20.5 秒开始，让人形机器人抬起右前臂，在胸口高度挥动两次，然后放下。

**状态：** 接受

**原子化判定句：**

1. 人形机器人是否将右前臂抬到胸口高度？

2. 它是否在胸口高度挥动右前臂两次？

3. 随后它是否放下右前臂？


## 190 — `synthetic_object_064_E1`

**原始英文指令：** Starting at 12 seconds, arc the camera upward into a near-overhead tracking view as the quadruped robot crosses the wooden platform.

**中文翻译：** 从第 12 秒开始，在四足机器人穿过木制平台时让镜头沿弧线向上移动到近乎俯视的跟拍视角。

**状态：** 接受

**原子化判定句：**

1. 四足机器人是否继续穿过木制平台？

2. 镜头是否在跟拍时沿弧线向上移动？

3. 镜头是否到达近乎俯视的跟拍视角？


## 191 — `synthetic_object_064_E2A`

**原始英文指令：** Starting at 29 seconds, make the quadruped robot's front foot kick one visible pebble forward until it rolls to a stop.

**中文翻译：** 从第 29 秒开始，让四足机器人的前脚将一颗可见小石子向前踢出，直到其滚动停止。

**状态：** 接受

**原子化判定句：**

1. 四足机器人的前脚是否将一颗可见小石子向前踢出？

2. 随后小石子是否滚动至停止？


## 192 — `synthetic_object_064_E2B`

**原始英文指令：** Starting at 24.5 seconds, fold the quadruped robot's red-tipped sensor mast backward until it lies flat against the body.

**中文翻译：** 从第 24.5 秒开始，将四足机器人带红色尖端的传感器桅杆向后折叠，直到其平贴机身。

**状态：** 接受

**原子化判定句：**

1. 四足机器人带红色尖端的传感器桅杆是否向后折叠？

2. 桅杆最终是否平贴机身？


## 193 — `synthetic_object_065_E1`

**原始英文指令：** At 13.5 seconds, remove the loose bright metal chips scattered along the front edge of the machined groove.

**中文翻译：** 在第 13.5 秒，移除散落在加工槽前缘的松散亮色金属屑。

**状态：** 接受

**原子化判定句：**

1. 散落在加工槽前缘的松散亮色金属屑是否被移除？


## 194 — `synthetic_object_065_E2A`

**原始英文指令：** Starting at 30 seconds, increase the milling table's feed motion to one-and-a-half times its original rate for five seconds.

**中文翻译：** 从第 30 秒开始，将铣床工作台的进给运动速度提高到原来的 1.5 倍，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 铣床工作台是否继续进给运动？

2. 进给速度是否提高到原来的 1.5 倍？

3. 提高后的速度是否持续 5 秒？


## 195 — `synthetic_object_065_E2B`

**原始英文指令：** Starting at 25.5 seconds, line the machining enclosure's light-gray rear wall with dark-blue oil-resistant panels over two seconds.

**中文翻译：** 从第 25.5 秒开始，在两秒内为加工舱浅灰色后墙铺设深蓝色耐油面板。

**状态：** 接受

**原子化判定句：**

1. 加工舱后墙是否铺设深蓝色面板？

2. 面板是否呈现耐油材质或结构？

3. 面板铺设是否在 2 秒内完成？


## 196 — `synthetic_object_066_E1`

**原始英文指令：** Starting at 12.5 seconds, change the 3D printer's golden build platform to matte black with a pale-blue alignment grid.

**中文翻译：** 从第 12.5 秒开始，将 3D 打印机的金色构建平台改为带浅蓝色对齐网格的哑光黑色。

**状态：** 接受

**原子化判定句：**

1. 3D 打印机的金色构建平台是否变为哑光黑色？

2. 构建平台上是否出现浅蓝色对齐网格？


## 197 — `synthetic_object_066_E2A`

**原始英文指令：** Starting at 30 seconds, make the printer nozzle deposit two diagonal braces connecting opposite corners of the white rectangular frame.

**中文翻译：** 从第 30 秒开始，让打印机喷嘴沉积两根连接白色矩形框架相对角的斜撑。

**状态：** 接受

**原子化判定句：**

1. 打印机喷嘴是否在白色矩形框架内沉积斜撑？

2. 斜撑是否沿对角方向？

3. 是否恰好沉积两根且分别连接相对角的斜撑？


## 198 — `synthetic_object_066_E2B`

**原始英文指令：** At 25 seconds, replace the narrow brass printer nozzle with a wider silver-steel nozzle attached beneath the same print head.

**中文翻译：** 在第 25 秒，将窄黄铜打印喷嘴替换为连接在同一打印头下方的较宽银钢喷嘴。

**状态：** 接受

**原子化判定句：**

1. 窄黄铜打印喷嘴是否被替换为银钢喷嘴？

2. 替换后的银钢喷嘴是否比原喷嘴更宽？

3. 替换后的喷嘴是否连接在同一打印头下方？


## 199 — `synthetic_object_067_E1`

**原始英文指令：** Starting at 11 seconds, increase the suspended beam's horizontal transfer speed to one-and-a-half times its original rate for five seconds.

**中文翻译：** 从第 11 秒开始，将悬挂横梁的水平转运速度提高到原来的 1.5 倍，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 悬挂横梁是否继续水平移动？

2. 其转运速度是否提高到原来的 1.5 倍？

3. 提高后的速度是否持续 5 秒？


## 200 — `synthetic_object_067_E2A`

**原始英文指令：** Starting at 31 seconds, change the suspended dark-brown beam to bright safety yellow over the next two seconds.

**中文翻译：** 从第 31 秒开始，在接下来的两秒内将悬挂的深棕色横梁改为明亮安全黄色。

**状态：** 接受

**原子化判定句：**

1. 悬挂横梁是否从深棕色变为明亮安全黄色？

2. 颜色变化是否在 2 秒内完成？


## 201 — `synthetic_object_067_E2B`

**原始英文指令：** At 24 seconds, replace the orange crane hook block with a blue double-hook block supporting the same two lifting slings.

**中文翻译：** 在第 24 秒，将橙色起重机吊钩滑轮组替换为支撑相同两条吊索的蓝色双钩滑轮组。

**状态：** 接受

**原子化判定句：**

1. 橙色起重机吊钩滑轮组是否被替换为蓝色双钩滑轮组？

2. 替换后的双钩滑轮组是否仍支撑原来的两条吊索？


## 202 — `synthetic_object_068_E1`

**原始英文指令：** At 13 seconds, move the combine header half a header-depth farther into the standing crop.

**中文翻译：** 在第 13 秒，将联合收割机割台向未收割作物中再推进半个割台深度。

**状态：** 接受

**原子化判定句：**

1. 联合收割机割台是否向未收割作物中进一步推进？

2. 推进距离是否为半个割台深度？


## 203 — `synthetic_object_068_E2A`

**原始英文指令：** Starting at 23 seconds, accelerate the combine's harvesting until three additional header-widths become short stubble by 29 seconds.

**中文翻译：** 从第 23 秒开始，加快联合收割机的收割，使另外三个割台宽度的作物在第 29 秒前变成短茬。

**状态：** 接受

**原子化判定句：**

1. 联合收割机的收割是否以更快的速度继续？

2. 另外三个割台宽度的作物是否在 6 秒内变成短茬？


## 204 — `synthetic_object_068_E2B`

**原始英文指令：** Starting at 25.5 seconds, change the combine's pale upper grain tank to bright red over the next two seconds.

**中文翻译：** 从第 25.5 秒开始，在接下来的两秒内将联合收割机上部浅色粮箱改为亮红色。

**状态：** 接受

**原子化判定句：**

1. 联合收割机上部粮箱是否从浅色变为亮红色？

2. 颜色变化是否在 2 秒内完成？


## 205 — `synthetic_object_069_E1`

**原始英文指令：** At 13 seconds, replace the upright blue bottle's white cap with a matte black cap of matching shape.

**中文翻译：** 在第 13 秒，将直立蓝色瓶子的白色瓶盖替换为形状匹配的哑光黑色瓶盖。

**状态：** 接受

**原子化判定句：**

1. 直立蓝色瓶子的白色瓶盖是否被替换为哑光黑色瓶盖？

2. 替换后的瓶盖形状是否与原瓶盖匹配？


## 206 — `synthetic_object_069_E2A`

**原始英文指令：** Starting at 20.5 seconds, accelerate the bottle-release process so it lies fully horizontal at the enclosure bottom by 23.5 seconds.

**中文翻译：** 从第 20.5 秒开始，加快瓶子释放过程，使其在第 23.5 秒前完全水平躺在外壳底部。

**状态：** 接受

**原子化判定句：**

1. 瓶子释放过程是否以更快的速度继续？

2. 瓶子是否在 3 秒内完全水平躺在外壳底部？


## 207 — `synthetic_object_069_E2B`

**原始英文指令：** At 25.5 seconds, center the horizontal blue bottle inside the lowest spiral ring with its cap facing right.

**中文翻译：** 在第 25.5 秒，将水平放置的蓝色瓶子居中置于最低的螺旋环内，并使瓶盖朝右。

**状态：** 接受

**原子化判定句：**

1. 水平放置的蓝色瓶子是否居中置于最低的螺旋环内？

2. 瓶盖是否朝右？


## 208 — `synthetic_object_070_E1`

**原始英文指令：** Starting at 6 seconds, pause the carton's forward conveyor motion for three seconds, then resume it toward the sealing head.

**中文翻译：** 从第 6 秒开始，将纸箱在传送带上的向前运动暂停三秒，然后恢复朝封箱头移动。

**状态：** 接受

**原子化判定句：**

1. 纸箱是否在传送带上朝封箱头向前移动？

2. 纸箱的向前传送运动是否暂停 3 秒？

3. 随后纸箱是否恢复朝封箱头移动？


## 209 — `synthetic_object_070_E2A`

**原始英文指令：** Starting at 36 seconds, make the sealing head press the stretched tape flat along the carton's top seam in one downward stroke.

**中文翻译：** 从第 36 秒开始，让封箱头用一次向下动作将拉伸的胶带平整压在纸箱顶部接缝上。

**状态：** 接受

**原子化判定句：**

1. 封箱头是否将拉伸的胶带平整压在纸箱顶部接缝上？

2. 压合是否通过一次向下动作完成？


## 210 — `synthetic_object_070_E2B`

**原始英文指令：** Starting at 20.5 seconds, render only the red horizontal sealing head with a hammered copper texture over two seconds.

**中文翻译：** 从第 20.5 秒开始，在两秒内仅将红色水平封箱头呈现为锤纹铜质感。

**状态：** 接受

**原子化判定句：**

1. 红色水平封箱头是否呈现为锤纹铜质感？

2. 质感变化是否仅限于该封箱头？

3. 质感变化是否在 2 秒内完成？


## 211 — `synthetic_object_071_E1`

**原始英文指令：** Starting at 19.5 seconds, transform the full bottle-filling scene into a cool cyan monochrome grade over two seconds.

**中文翻译：** 从第 19.5 秒开始，在两秒内将整个瓶装灌装场景转变为冷青色单色调。

**状态：** 接受

**原子化判定句：**

1. 整个瓶装灌装场景是否转变为冷青色单色调？

2. 这一转变是否在 2 秒内完成？


## 212 — `synthetic_object_071_E2A`

**原始英文指令：** Starting at 30.5 seconds, change the liquid inside the clear bottle from pale yellow to translucent violet over two seconds.

**中文翻译：** 从第 30.5 秒开始，在两秒内将透明瓶中的液体从浅黄色改为半透明紫色。

**状态：** 接受

**原子化判定句：**

1. 透明瓶中的液体是否从浅黄色变为紫色？

2. 变化后的液体是否呈半透明状态？

3. 这一变化是否在 2 秒内完成？


## 213 — `synthetic_object_071_E2B`

**原始英文指令：** Starting at 34.5 seconds, retract the filling nozzle upward at twice its original speed until it clears the bottle neck.

**中文翻译：** 从第 34.5 秒开始，以原来两倍的速度向上收回灌装喷嘴，直到其离开瓶颈。

**状态：** 接受

**原子化判定句：**

1. 灌装喷嘴是否向上收回？

2. 喷嘴是否以原来两倍的速度收回？

3. 喷嘴是否持续收回直至离开瓶颈？


## 214 — `synthetic_object_072_E1`

**原始英文指令：** Starting at 13.5 seconds, make the overhead spray jets sweep left and right across the plates twice over five seconds.

**中文翻译：** 从第 13.5 秒开始，让上方喷淋水柱在五秒内横跨盘子左右扫动两次。

**状态：** 接受

**原子化判定句：**

1. 上方喷淋水柱是否横跨盘子左右扫动？

2. 水柱是否恰好完成两次扫动？

3. 两次扫动是否在 5 秒内完成？


## 215 — `synthetic_object_072_E2A`

**原始英文指令：** Starting at 34 seconds, let the first dish rack exit completely before the second rack begins entering the spray chamber.

**中文翻译：** 从第 34 秒开始，让第一只碗碟架完全退出后，第二只碗碟架才开始进入喷淋舱。

**状态：** 接受

**原子化判定句：**

1. 第一只碗碟架是否完全退出喷淋舱？

2. 第二只碗碟架是否仅在第一只完全退出后才开始进入？


## 216 — `synthetic_object_072_E2B`

**原始英文指令：** Starting at 25.5 seconds, move the camera smoothly from the rightmost plate to the leftmost plate over five seconds.

**中文翻译：** 从第 25.5 秒开始，在五秒内将镜头从最右侧盘子平滑移动到最左侧盘子。

**状态：** 接受

**原子化判定句：**

1. 镜头是否从最右侧盘子移动到最左侧盘子？

2. 镜头移动是否平滑？

3. 这一移动是否在 5 秒内完成？


## 217 — `synthetic_object_073_E1`

**原始英文指令：** Starting at 13 seconds, render only the bread machine's silver upper housing with a warm hammered-copper texture over two seconds.

**中文翻译：** 从第 13 秒开始，在两秒内仅将面包机的银色上部外壳呈现为温暖的锤纹铜质感。

**状态：** 接受

**原子化判定句：**

1. 面包机的银色上部外壳是否呈现为温暖的锤纹铜质感？

2. 质感变化是否仅限于上部外壳？

3. 质感变化是否在 2 秒内完成？


## 218 — `synthetic_object_073_E2A`

**原始英文指令：** At 31 seconds, remove the physical black adjustment knob protruding from the bread machine's right-side frame.

**中文翻译：** 在第 31 秒，移除从面包机右侧框架伸出的实体黑色调节旋钮。

**状态：** 接受

**原子化判定句：**

1. 从面包机右侧框架伸出的实体黑色调节旋钮是否被移除？


## 219 — `synthetic_object_073_E2B`

**原始英文指令：** Starting at 24.5 seconds, change the outdoor paving stones behind the bread machine from dry to rain-wet and reflective.

**中文翻译：** 从第 24.5 秒开始，将面包机后方的室外铺路石从干燥状态改为被雨淋湿且具有反光效果。

**状态：** 接受

**原子化判定句：**

1. 面包机后方的室外铺路石是否从干燥状态变为被雨淋湿？

2. 湿润后的铺路石是否具有反光效果？


## 220 — `synthetic_object_074_E1`

**原始英文指令：** Starting at 10 seconds, accelerate the active groove-cutting process so the current straight groove reaches the far plate edge by 14 seconds.

**中文翻译：** 从第 10 秒开始，加快正在进行的开槽过程，使当前直槽在第 14 秒前延伸到板材远端边缘。

**状态：** 接受

**原子化判定句：**

1. 正在进行的开槽过程是否以更快的速度继续？

2. 当前直槽是否在 4 秒内延伸到板材远端边缘？


## 221 — `synthetic_object_074_E2A`

**原始英文指令：** At 32 seconds, remove the visible blue coolant hose running beside the metal cutting head.

**中文翻译：** 在第 32 秒，移除金属切割头旁延伸的可见蓝色冷却液软管。

**状态：** 接受

**原子化判定句：**

1. 金属切割头旁延伸的可见蓝色冷却液软管是否被移除？


## 222 — `synthetic_object_074_E2B`

**原始英文指令：** Starting at 23 seconds, make the metal cutting head trace one complete circle before resuming its straight path.

**中文翻译：** 从第 23 秒开始，让金属切割头先描绘一个完整圆圈，然后恢复直线路径。

**状态：** 接受

**原子化判定句：**

1. 金属切割头是否描绘一个完整圆圈？

2. 随后它是否恢复直线路径？


## 223 — `synthetic_object_075_E1`

**原始英文指令：** Starting at 13 seconds, make the exposed conveyor rollers beneath the apple path rotate at twice their original rate for five seconds.

**中文翻译：** 从第 13 秒开始，让苹果路径下方裸露的传送辊以原来两倍的速度旋转五秒。

**状态：** 接受

**原子化判定句：**

1. 苹果路径下方裸露的传送辊是否旋转？

2. 传送辊是否以原来两倍的速度旋转？

3. 加速后的旋转是否持续 5 秒？


## 224 — `synthetic_object_075_E2A`

**原始英文指令：** At 31 seconds, add one green apple one belt-length behind the red-and-yellow apple on the incoming conveyor.

**中文翻译：** 在第 31 秒，在进料传送带上红黄苹果后方一个传送带长度处添加一个青苹果。

**状态：** 接受

**原子化判定句：**

1. 进料传送带上是否添加了恰好一个青苹果？

2. 该青苹果是否位于红黄苹果后方一个传送带长度处？


## 225 — `synthetic_object_075_E2B`

**原始英文指令：** Starting at 25.5 seconds, change the sloped transfer chute's inner surface from silver to glossy cobalt blue over two seconds.

**中文翻译：** 从第 25.5 秒开始，在两秒内将倾斜转运槽的内表面从银色改为亮面钴蓝色。

**状态：** 接受

**原子化判定句：**

1. 倾斜转运槽的内表面是否从银色变为钴蓝色？

2. 变化后的内表面是否呈亮面效果？

3. 这一变化是否在 2 秒内完成？


## 226 — `synthetic_object_076_E1`

**原始英文指令：** Starting at 14 seconds, change the smaller upper carton from brown cardboard to bright blue over the next two seconds.

**中文翻译：** 从第 14 秒开始，在接下来的两秒内将较小的上层纸箱从棕色纸板改为亮蓝色。

**状态：** 接受

**原子化判定句：**

1. 较小的上层纸箱是否从棕色纸板变为亮蓝色？

2. 这一变化是否在 2 秒内完成？


## 227 — `synthetic_object_076_E2A`

**原始英文指令：** Starting at 25 seconds, make both front cart wheels bump across the doorway threshold and bounce the loaded cart once.

**中文翻译：** 从第 25 秒开始，让推车两个前轮颠过门槛，并使载货推车弹跳一次。

**状态：** 接受

**原子化判定句：**

1. 推车两个前轮是否颠过门槛？

2. 载货推车是否因此弹跳一次？


## 228 — `synthetic_object_076_E2B`

**原始英文指令：** Starting at 24.5 seconds, accelerate the loaded cart's doorway crossing so the entire cart is outside by 28 seconds.

**中文翻译：** 从第 24.5 秒开始，加快载货推车穿过门口的过程，使整辆推车在第 28 秒前到达室外。

**状态：** 接受

**原子化判定句：**

1. 载货推车穿过门口的过程是否加快？

2. 整辆推车是否在 3.5 秒内到达室外？


## 229 — `synthetic_object_077_E1`

**原始英文指令：** Starting at 12 seconds, smoothly zoom out until both parallel escalators and their complete glass side panels are visible.

**中文翻译：** 从第 12 秒开始，平滑拉远镜头，直到两条平行自动扶梯及其完整玻璃侧板都可见。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑拉远？

2. 拉远后，两条平行自动扶梯及其完整玻璃侧板是否都可见？


## 230 — `synthetic_object_077_E2A`

**原始英文指令：** Starting at 31 seconds, increase the central escalator steps to one-and-a-half times their original speed for five seconds.

**中文翻译：** 从第 31 秒开始，将中央自动扶梯台阶的速度提高到原来的 1.5 倍，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 中央自动扶梯台阶是否继续移动？

2. 台阶速度是否提高到原来的 1.5 倍？

3. 提高后的速度是否持续 5 秒？


## 231 — `synthetic_object_077_E2B`

**原始英文指令：** At 25 seconds, rotate the right parallel escalator five degrees inward toward the central escalator while fixing its lower landing.

**中文翻译：** 在第 25 秒，在固定右侧平行自动扶梯下端平台的同时，将其朝中央自动扶梯向内旋转五度。

**状态：** 接受

**原子化判定句：**

1. 右侧平行自动扶梯是否朝中央自动扶梯向内旋转 5 度？

2. 其下端平台是否保持固定？


## 232 — `synthetic_object_078_E1`

**原始英文指令：** At 13.5 seconds, replace the right bridge leaf's dark side rail with a solid silver safety barrier of equal length.

**中文翻译：** 在第 13.5 秒，将右侧桥叶的深色侧栏替换为等长的实心银色安全护栏。

**状态：** 接受

**原子化判定句：**

1. 右侧桥叶的深色侧栏是否被替换为银色安全护栏？

2. 替换后的安全护栏是否为实心结构？

3. 替换后的护栏是否与原侧栏等长？


## 233 — `synthetic_object_078_E2A`

**原始英文指令：** At 30 seconds, increase the gap between the two raised bridge tips to one full bridge-leaf width.

**中文翻译：** 在第 30 秒，将两个抬起桥尖之间的间隙增加到一个完整桥叶宽度。

**状态：** 接受

**原子化判定句：**

1. 两个抬起桥尖之间的间隙是否增大？

2. 最终间隙是否等于一个完整桥叶宽度？


## 234 — `synthetic_object_078_E2B`

**原始英文指令：** Starting at 25.5 seconds, make the rising right bridge leaf press the overhanging branches upward once before they bend back.

**中文翻译：** 从第 25.5 秒开始，让正在升起的右侧桥叶将悬垂树枝向上顶压一次，然后使树枝弯回。

**状态：** 接受

**原子化判定句：**

1. 正在升起的右侧桥叶是否将悬垂树枝向上顶压一次？

2. 随后树枝是否弯回？


## 235 — `synthetic_object_079_E1`

**原始英文指令：** Starting at 12 seconds, make the blue suitcase push the scanner curtain strips into a wide fan before they rebound.

**中文翻译：** 从第 12 秒开始，让蓝色行李箱将扫描仪帘条推成宽扇形，然后使帘条回弹。

**状态：** 接受

**原子化判定句：**

1. 蓝色行李箱是否将扫描仪帘条推成宽扇形？

2. 随后帘条是否回弹？


## 236 — `synthetic_object_079_E2A`

**原始英文指令：** Starting at 31 seconds, change the incoming dark-blue suitcase to bright yellow over the next two seconds.

**中文翻译：** 从第 31 秒开始，在接下来的两秒内将进入的深蓝色行李箱改为亮黄色。

**状态：** 接受

**原子化判定句：**

1. 进入的行李箱是否从深蓝色变为亮黄色？

2. 颜色变化是否在 2 秒内完成？


## 237 — `synthetic_object_079_E2B`

**原始英文指令：** At 24.5 seconds, rotate the dark-gray suitcase ninety degrees so its side handle faces directly toward the camera.

**中文翻译：** 在第 24.5 秒，将深灰色行李箱旋转九十度，使其侧把手正对镜头。

**状态：** 接受

**原子化判定句：**

1. 深灰色行李箱是否旋转 90 度？

2. 其侧把手最终是否正对镜头？


## 238 — `synthetic_object_080_E1`

**原始英文指令：** At 13 seconds, shift the connected milking cup cluster to hang exactly midway between the cow's two rear hooves.

**中文翻译：** 在第 13 秒，将连接着的挤奶杯组件移动到正好悬挂在奶牛两只后蹄之间的中点。

**状态：** 接受

**原子化判定句：**

1. 连接着的挤奶杯组件是否被移动到正好悬挂在奶牛两只后蹄之间的中点？


## 239 — `synthetic_object_080_E2A`

**原始英文指令：** Starting at 31 seconds, change the long yellow milking hose to bright blue over the next two seconds.

**中文翻译：** 从第 31 秒开始，在接下来的两秒内将长黄色挤奶软管改为亮蓝色。

**状态：** 接受

**原子化判定句：**

1. 长挤奶软管是否从黄色变为亮蓝色？

2. 颜色变化是否在 2 秒内完成？


## 240 — `synthetic_object_080_E2B`

**原始英文指令：** Starting at 25.5 seconds, make the cow's tail swing left and right at twice its original rate for five seconds.

**中文翻译：** 从第 25.5 秒开始，让奶牛尾巴以原来两倍的频率左右摆动五秒。

**状态：** 接受

**原子化判定句：**

1. 奶牛尾巴是否左右摆动？

2. 尾巴是否以原来两倍的频率摆动？

3. 加速后的摆动是否持续 5 秒？


## 241 — `synthetic_object_081_E1`

**原始英文指令：** Starting at 10.5 seconds, make the teapot lid rise, rotate once, and settle back onto the opening over four seconds.

**中文翻译：** 从第 10.5 秒开始，让茶壶盖升起、旋转一圈，并在四秒内重新落回壶口。

**状态：** 接受

**原子化判定句：**

1. 茶壶盖是否升起？

2. 升起后它是否旋转一圈？

3. 它是否在 4 秒内重新落回壶口？


## 242 — `synthetic_object_081_E2A`

**原始英文指令：** Starting at 30.5 seconds, change the teapot's deep teal glaze to warm ivory with fine cobalt-blue horizontal bands.

**中文翻译：** 从第 30.5 秒开始，将茶壶的深蓝绿色釉面改为带有细钴蓝色水平条纹的暖象牙色。

**状态：** 接受

**原子化判定句：**

1. 茶壶釉面是否从深蓝绿色变为暖象牙色？

2. 釉面上是否出现细钴蓝色水平条纹？


## 243 — `synthetic_object_081_E2B`

**原始英文指令：** At 24 seconds, add one small white porcelain teacup on the wooden table directly below and right of the teapot spout.

**中文翻译：** 在第 24 秒，在茶壶嘴正下方偏右的木桌上添加一个小型白瓷茶杯。

**状态：** 接受

**原子化判定句：**

1. 木桌上是否添加了恰好一个小型白瓷茶杯？

2. 该茶杯是否位于茶壶嘴正下方偏右的位置？


## 244 — `synthetic_object_082_E1`

**原始英文指令：** At 14.5 seconds, position the open pocket-watch lid at a right angle to the exposed dial around its existing hinge.

**中文翻译：** 在第 14.5 秒，绕现有铰链将打开的怀表盖定位为与露出表盘成直角。

**状态：** 接受

**原子化判定句：**

1. 打开的怀表盖是否绕现有铰链被定位为与露出表盘成直角？


## 245 — `synthetic_object_082_E2A`

**原始英文指令：** Starting at 33.5 seconds, make the pocket watch's physical thin red seconds hand rotate at twice its original speed for five seconds.

**中文翻译：** 从第 33.5 秒开始，让怀表实体细红秒针以原来两倍的速度旋转五秒。

**状态：** 接受

**原子化判定句：**

1. 怀表的实体细红秒针是否旋转？

2. 秒针是否以原来两倍的速度旋转？

3. 加速后的旋转是否持续 5 秒？


## 246 — `synthetic_object_082_E2B`

**原始英文指令：** Starting at 26 seconds, pause the pocket watch's physical thin red seconds hand for four seconds, then resume its original motion.

**中文翻译：** 从第 26 秒开始，将怀表实体细红秒针的运动暂停四秒，然后恢复原来的运动。

**状态：** 接受

**原子化判定句：**

1. 怀表实体细红秒针是否正常运动？

2. 秒针是否暂停 4 秒？

3. 随后秒针是否恢复原来的运动？


## 247 — `synthetic_object_083_E1`

**原始英文指令：** Starting at 9.5 seconds, smoothly zoom out until the complete brass compass and a broad surrounding section of the map are visible.

**中文翻译：** 从第 9.5 秒开始，平滑拉远镜头，直到完整的黄铜指南针和周围大范围地图都可见。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑拉远？

2. 拉远后，完整的黄铜指南针和周围大范围地图是否都可见？


## 248 — `synthetic_object_083_E2A`

**原始英文指令：** Starting at 35.5 seconds, illuminate the compass needle and right half of the dial with a narrow warm spotlight from above right.

**中文翻译：** 从第 35.5 秒开始，用来自右上方的窄束暖色聚光灯照亮指南针指针和表盘右半部分。

**状态：** 接受

**原子化判定句：**

1. 指南针指针是否被照亮？

2. 表盘右半部分是否被照亮？

3. 照明是否来自右上方的窄束暖色聚光灯？


## 249 — `synthetic_object_083_E2B`

**原始英文指令：** Starting at 22.5 seconds, make the physical compass needle tap the inner brass rim twice and rebound after each contact.

**中文翻译：** 从第 22.5 秒开始，让实体指南针指针轻碰内部黄铜边缘两次，并在每次接触后回弹。

**状态：** 接受

**原子化判定句：**

1. 实体指南针指针是否轻碰内部黄铜边缘两次？

2. 指针是否在每次接触后回弹？


## 250 — `synthetic_object_084_E1`

**原始英文指令：** Starting at 12 seconds, change the folding fan's plain cream leaf to pale sky blue with darker blue pleat edges.

**中文翻译：** 从第 12 秒开始，将折扇无图案奶油色扇面改为带深蓝色褶边的浅天蓝色。

**状态：** 接受

**原子化判定句：**

1. 折扇扇面是否从无图案奶油色变为浅天蓝色？

2. 褶边处是否出现深蓝色边缘？


## 251 — `synthetic_object_084_E2A`

**原始英文指令：** Starting at 32.5 seconds, make the folding fan close to half its width and reopen around the lower pivot over four seconds.

**中文翻译：** 从第 32.5 秒开始，让折扇绕下部枢轴收拢到一半宽度，并在四秒内重新打开。

**状态：** 接受

**原子化判定句：**

1. 折扇是否绕下部枢轴收拢到一半宽度？

2. 折扇是否在 4 秒内重新打开？


## 252 — `synthetic_object_084_E2B`

**原始英文指令：** Starting at 26 seconds, move the camera upward along the fan's central ribs until the upper curved leaf edge enters the frame.

**中文翻译：** 从第 26 秒开始，让镜头沿折扇中央扇骨向上移动，直到上部弯曲扇面边缘进入画面。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿折扇中央扇骨向上移动？

2. 镜头是否持续移动直至上部弯曲扇面边缘进入画面？


## 253 — `synthetic_object_085_E1`

**原始英文指令：** Starting at 15.5 seconds, change the wind-up toy car's dark-green body shell to glossy cherry red over two seconds.

**中文翻译：** 从第 15.5 秒开始，在两秒内将发条玩具车的深绿色车身外壳改为亮面樱桃红色。

**状态：** 接受

**原子化判定句：**

1. 发条玩具车的车身外壳是否从深绿色变为樱桃红色？

2. 变化后的外壳是否呈亮面效果？

3. 这一变化是否在 2 秒内完成？


## 254 — `synthetic_object_085_E2A`

**原始英文指令：** Starting at 36 seconds, raise the camera into a near-overhead tracking view while following the moving toy car for five seconds.

**中文翻译：** 从第 36 秒开始，将镜头抬高到近乎俯视的跟拍视角，并跟随移动的玩具车五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否抬高到近乎俯视的视角？

2. 镜头是否跟随移动的玩具车？

3. 跟拍是否持续 5 秒？


## 255 — `synthetic_object_085_E2B`

**原始英文指令：** Starting at 26.5 seconds, make the toy car's raised circular key complete three rapid clockwise rotations while rounding the bend.

**中文翻译：** 从第 26.5 秒开始，让玩具车抬起的圆形发条钥匙在转弯时快速顺时针旋转三圈。

**状态：** 接受

**原子化判定句：**

1. 玩具车抬起的圆形发条钥匙是否顺时针旋转？

2. 旋转是否快速？

3. 发条钥匙是否恰好旋转三圈？

4. 这些旋转是否发生在玩具车转弯期间？


## 256 — `synthetic_object_086_E1`

**原始英文指令：** Starting at 14.5 seconds, change the displayed camera's black pebbled body covering to smooth warm ivory over two seconds.

**中文翻译：** 从第 14.5 秒开始，在两秒内将展示相机的黑色颗粒纹机身包覆层改为光滑的暖象牙色。

**状态：** 接受

**原子化判定句：**

1. 展示相机的机身包覆层是否从黑色变为暖象牙色？

2. 包覆层是否从颗粒纹变为光滑表面？

3. 这一变化是否在 2 秒内完成？


## 257 — `synthetic_object_086_E2A`

**原始英文指令：** At 33.5 seconds, move the displayed camera half a body-depth toward the front edge of the black circular disk.

**中文翻译：** 在第 33.5 秒，将展示相机朝黑色圆盘前缘移动半个机身深度。

**状态：** 接受

**原子化判定句：**

1. 展示相机是否朝黑色圆盘前缘移动？

2. 移动距离是否为半个机身深度？


## 258 — `synthetic_object_086_E2B`

**原始英文指令：** Starting at 27 seconds, make the displayed camera rotate around its vertical axis at twice the original speed for five seconds.

**中文翻译：** 从第 27 秒开始，让展示相机以原来两倍的速度绕其竖直轴旋转五秒。

**状态：** 接受

**原子化判定句：**

1. 展示相机是否绕其竖直轴旋转？

2. 相机是否以原来两倍的速度旋转？

3. 加速后的旋转是否持续 5 秒？


## 259 — `synthetic_object_087_E1`

**原始英文指令：** Starting at 11 seconds, render only the tabletop surrounding the white bowl as a dark indigo watercolor wash over two seconds.

**中文翻译：** 从第 11 秒开始，在两秒内仅将白碗周围的桌面呈现为深靛蓝色水彩晕染。

**状态：** 接受

**原子化判定句：**

1. 白碗周围的桌面是否呈现为深靛蓝色水彩晕染？

2. 风格变化是否仅限于该桌面？

3. 风格变化是否在 2 秒内完成？


## 260 — `synthetic_object_087_E2A`

**原始英文指令：** Starting at 30.5 seconds, move the camera in a smooth half-circle arc from the near side to the far side of the bowl.

**中文翻译：** 从第 30.5 秒开始，让镜头沿平滑半圆弧从碗的近侧移动到远侧。

**状态：** 接受

**原子化判定句：**

1. 镜头是否沿半圆弧从碗的近侧移动到远侧？

2. 镜头移动是否平滑？


## 261 — `synthetic_object_087_E2B`

**原始英文指令：** Starting at 24 seconds, make the green marble roll around the bowl at twice its original speed for five seconds.

**中文翻译：** 从第 24 秒开始，让绿色弹珠以原来两倍的速度围绕碗滚动五秒。

**状态：** 接受

**原子化判定句：**

1. 绿色弹珠是否围绕碗滚动？

2. 弹珠是否以原来两倍的速度滚动？

3. 加速后的滚动是否持续 5 秒？


## 262 — `synthetic_object_088_E1`

**原始英文指令：** Starting at 17 seconds, change the pale display surface beneath the athletic shoe to dark navy felt over two seconds.

**中文翻译：** 从第 17 秒开始，在两秒内将运动鞋下方的浅色展示面改为深海军蓝色毛毡。

**状态：** 接受

**原子化判定句：**

1. 运动鞋下方的展示面是否从浅色变为深海军蓝色？

2. 变化后的展示面是否具有毛毡质感？

3. 这一变化是否在 2 秒内完成？


## 263 — `synthetic_object_088_E2A`

**原始英文指令：** Starting at 34.5 seconds, convert the full athletic-shoe display into cool black and white with crisp tonal contrast over two seconds.

**中文翻译：** 从第 34.5 秒开始，在两秒内将整个运动鞋展示转变为具有清晰明暗对比的冷调黑白画面。

**状态：** 接受

**原子化判定句：**

1. 整个运动鞋展示是否转变为冷调黑白画面？

2. 转变后的画面是否具有清晰的明暗对比？

3. 这一转变是否在 2 秒内完成？


## 264 — `synthetic_object_088_E2B`

**原始英文指令：** At 27.5 seconds, shift the complete athletic shoe one shoe-width toward the right side of the display surface.

**中文翻译：** 在第 27.5 秒，将整只运动鞋朝展示面右侧移动一个鞋宽。

**状态：** 接受

**原子化判定句：**

1. 整只运动鞋是否朝展示面右侧移动？

2. 移动距离是否为一个鞋宽？


## 265 — `synthetic_object_089_E1`

**原始英文指令：** Starting at 16.5 seconds, make the spotlight sweep across the crystal cluster at twice its original speed for five seconds.

**中文翻译：** 从第 16.5 秒开始，让聚光灯以原来两倍的速度扫过水晶簇，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 聚光灯是否扫过水晶簇？

2. 聚光灯是否以原来两倍的速度扫动？

3. 加速后的扫动是否持续 5 秒？


## 266 — `synthetic_object_089_E2A`

**原始英文指令：** At 31.5 seconds, shift the entire crystal cluster one cluster-width toward the right side of the illuminated tabletop region.

**中文翻译：** 在第 31.5 秒，将整个水晶簇朝桌面受光区域右侧移动一个水晶簇宽度。

**状态：** 接受

**原子化判定句：**

1. 整个水晶簇是否朝桌面受光区域右侧移动？

2. 移动距离是否为一个水晶簇宽度？


## 267 — `synthetic_object_089_E2B`

**原始英文指令：** At 28.5 seconds, chip one small triangular section from the tip of the tallest central purple crystal.

**中文翻译：** 在第 28.5 秒，从中央最高紫色水晶的尖端崩去一小块三角形部分。

**状态：** 接受

**原子化判定句：**

1. 中央最高紫色水晶的尖端是否崩去一小块三角形部分？


## 268 — `synthetic_object_090_E1`

**原始英文指令：** Starting at 14 seconds, change the globe's dark brown circular support frame to brushed silver over two seconds.

**中文翻译：** 从第 14 秒开始，在两秒内将地球仪的深棕色圆形支撑框改为拉丝银色。

**状态：** 接受

**原子化判定句：**

1. 地球仪的圆形支撑框是否从深棕色变为银色？

2. 变化后的支撑框是否具有拉丝质感？

3. 这一变化是否在 2 秒内完成？


## 269 — `synthetic_object_090_E2A`

**原始英文指令：** Starting at 34.5 seconds, render only the globe sphere as an embossed antique-bronze relief object over the next two seconds.

**中文翻译：** 从第 34.5 秒开始，在接下来的两秒内仅将地球仪球体呈现为浮雕古铜物体。

**状态：** 接受

**原子化判定句：**

1. 地球仪球体是否呈现为浮雕古铜物体？

2. 风格变化是否仅限于地球仪球体？

3. 风格变化是否在 2 秒内完成？


## 270 — `synthetic_object_090_E2B`

**原始英文指令：** Starting at 26.5 seconds, reduce the globe sphere's rotation to half its original angular speed for five seconds.

**中文翻译：** 从第 26.5 秒开始，将地球仪球体的旋转角速度降低到原来的一半，持续五秒。

**状态：** 接受

**原子化判定句：**

1. 地球仪球体是否继续旋转？

2. 其角速度是否降低到原来的一半？

3. 降低后的速度是否持续 5 秒？


## 271 — `synthetic_object_091_E1`

**原始英文指令：** Starting at 10.5 seconds, change the pale support surface beneath the fountain pen to dark forest-green felt over two seconds.

**中文翻译：** 从第 10.5 秒开始，在两秒内将钢笔下方的浅色支撑面改为深森林绿色毛毡。

**状态：** 接受

**原子化判定句：**

1. 钢笔下方的支撑面是否从浅色变为深森林绿色？

2. 变化后的支撑面是否具有毛毡质感？

3. 这一变化是否在 2 秒内完成？


## 272 — `synthetic_object_091_E2A`

**原始英文指令：** At 32.5 seconds, add one square cobalt-blue glass ink bottle on the surface one pen-width above the fountain pen barrel.

**中文翻译：** 在第 32.5 秒，在钢笔笔杆上方一个笔宽处的表面添加一个方形钴蓝色玻璃墨水瓶。

**状态：** 接受

**原子化判定句：**

1. 表面上是否添加了恰好一个方形钴蓝色玻璃墨水瓶？

2. 墨水瓶是否位于钢笔笔杆上方一个笔宽处？


## 273 — `synthetic_object_091_E2B`

**原始英文指令：** Starting at 22 seconds, make the separated pen cap roll one complete turn toward the nib and stop one cap-width away.

**中文翻译：** 从第 22 秒开始，让分离的笔帽朝笔尖滚动完整一圈，并停在距笔尖一个笔帽宽度处。

**状态：** 接受

**原子化判定句：**

1. 分离的笔帽是否朝笔尖滚动完整一圈？

2. 它是否停在距笔尖一个笔帽宽度处？


## 274 — `synthetic_object_092_E1`

**原始英文指令：** Starting at 15 seconds, transform the full open-padlock scene into a detailed ink-and-watercolor illustration over two seconds.

**中文翻译：** 从第 15 秒开始，在两秒内将整个打开挂锁场景转变为细致的水墨水彩插画。

**状态：** 接受

**原子化判定句：**

1. 整个打开挂锁场景是否转变为细致的水墨水彩插画？

2. 这一转变是否在 2 秒内完成？


## 275 — `synthetic_object_092_E2A`

**原始英文指令：** Starting at 35.5 seconds, change the wooden tabletop beneath the open padlock to polished white marble with soft gray veins.

**中文翻译：** 从第 35.5 秒开始，将打开挂锁下方的木桌面改为带柔和灰色纹理的抛光白色大理石。

**状态：** 接受

**原子化判定句：**

1. 打开挂锁下方的木桌面是否变为抛光白色大理石？

2. 白色大理石表面是否带有柔和的灰色纹理？


## 276 — `synthetic_object_092_E2B`

**原始英文指令：** Starting at 27.5 seconds, make the padlock's free shackle end swing outward ninety degrees and return once around the right connection.

**中文翻译：** 从第 27.5 秒开始，让挂锁锁梁的自由端绕右侧连接处向外摆动九十度，再返回一次。

**状态：** 接受

**原子化判定句：**

1. 挂锁锁梁的自由端是否绕右侧连接处向外摆动 90 度？

2. 随后锁梁自由端是否返回一次？


## 277 — `synthetic_object_093_E1`

**原始英文指令：** At 12 seconds, add one small blue rectangular alignment tab to the middle of the white paper stack's exposed left edge.

**中文翻译：** 在第 12 秒，在白色纸堆露出的左侧边缘中部添加一个小型蓝色矩形对齐标签。

**状态：** 接受

**原子化判定句：**

1. 是否添加了恰好一个小型蓝色矩形对齐标签？

2. 该标签是否位于白色纸堆露出的左侧边缘中部？


## 278 — `synthetic_object_093_E2A`

**原始英文指令：** Starting at 32.5 seconds, change the stapler's long silver upper handle to glossy signal red over the next two seconds.

**中文翻译：** 从第 32.5 秒开始，在接下来的两秒内将订书机的银色长上柄改为亮面信号红色。

**状态：** 接受

**原子化判定句：**

1. 订书机的长上柄是否从银色变为信号红色？

2. 变化后的上柄是否呈亮面效果？

3. 这一变化是否在 2 秒内完成？


## 279 — `synthetic_object_093_E2B`

**原始英文指令：** Starting at 21.5 seconds, make the stapler handle press the paper stack twice and rebound fully after each contact.

**中文翻译：** 从第 21.5 秒开始，让订书机手柄按压纸堆两次，并在每次接触后完全回弹。

**状态：** 接受

**原子化判定句：**

1. 订书机手柄是否按压纸堆两次？

2. 手柄是否在每次接触后完全回弹？


## 280 — `synthetic_object_094_E1`

**原始英文指令：** Starting at 16 seconds, make the extended yellow measuring tape slack with two broad downward bends over the next two seconds.

**中文翻译：** 从第 16 秒开始，在接下来的两秒内让伸出的黄色卷尺变松，并形成两个宽阔的向下弯曲。

**状态：** 接受

**原子化判定句：**

1. 伸出的黄色卷尺是否变松？

2. 卷尺是否形成恰好两个宽阔的向下弯曲？

3. 这些变化是否在 2 秒内完成？


## 281 — `synthetic_object_094_E2A`

**原始英文指令：** Starting at 30.5 seconds, render the tape-measure housing and extended yellow tape as clean colored-pencil artwork over the next two seconds.

**中文翻译：** 从第 30.5 秒开始，在接下来的两秒内将卷尺外壳和伸出的黄色卷尺呈现为简洁的彩色铅笔画。

**状态：** 接受

**原子化判定句：**

1. 卷尺外壳是否呈现为简洁的彩色铅笔画？

2. 伸出的黄色卷尺是否也呈现为相同风格？

3. 风格变化是否在 2 秒内完成？


## 282 — `synthetic_object_094_E2B`

**原始英文指令：** At 27 seconds, remove the physical red locking button protruding from the top of the silver tape-measure housing.

**中文翻译：** 在第 27 秒，移除从银色卷尺外壳顶部突出的实体红色锁定按钮。

**状态：** 接受

**原子化判定句：**

1. 从银色卷尺外壳顶部突出的实体红色锁定按钮是否被移除？


## 283 — `synthetic_object_095_E1`

**原始英文指令：** Starting at 14.5 seconds, raise the camera to a near-overhead view and track the scissors along the red cutting line for five seconds.

**中文翻译：** 从第 14.5 秒开始，将镜头抬高到近乎俯视的视角，并沿红色裁剪线跟拍剪刀五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否抬高到近乎俯视的视角？

2. 镜头是否沿红色裁剪线跟拍剪刀并持续 5 秒？


## 284 — `synthetic_object_095_E2A`

**原始英文指令：** Starting at 35.5 seconds, coat the scissors' visible outer silver ring handle in glossy bright red enamel over two seconds.

**中文翻译：** 从第 35.5 秒开始，在两秒内为剪刀可见的外侧银色环形手柄涂上亮面鲜红色搪瓷。

**状态：** 接受

**原子化判定句：**

1. 剪刀可见的外侧银色环形手柄是否涂上鲜红色搪瓷？

2. 搪瓷涂层是否呈亮面效果？

3. 涂层变化是否在 2 秒内完成？


## 285 — `synthetic_object_095_E2B`

**原始英文指令：** Starting at 25.5 seconds, render only the exposed gray tabletop around the cut sheet as textured blue watercolor paper.

**中文翻译：** 从第 25.5 秒开始，仅将裁剪纸张周围露出的灰色桌面呈现为带纹理的蓝色水彩纸。

**状态：** 接受

**原子化判定句：**

1. 裁剪纸张周围露出的灰色桌面是否呈现为带纹理的蓝色水彩纸？

2. 风格变化是否仅限于该露出桌面？


## 286 — `synthetic_object_096_E1`

**原始英文指令：** Starting at 10 seconds, change the vase's blue glazed body to deep emerald green over the next two seconds.

**中文翻译：** 从第 10 秒开始，在接下来的两秒内将花瓶的蓝色釉面瓶身改为深祖母绿色。

**状态：** 接受

**原子化判定句：**

1. 花瓶的釉面瓶身是否从蓝色变为深祖母绿色？

2. 颜色变化是否在 2 秒内完成？


## 287 — `synthetic_object_096_E2A`

**原始英文指令：** Starting at 30.5 seconds, make the upright vase rotate around its vertical axis at twice the original speed for five seconds.

**中文翻译：** 从第 30.5 秒开始，让直立花瓶以原来两倍的速度绕竖直轴旋转五秒。

**状态：** 接受

**原子化判定句：**

1. 直立花瓶是否绕其竖直轴旋转？

2. 花瓶是否以原来两倍的速度旋转？

3. 加速后的旋转是否持续 5 秒？


## 288 — `synthetic_object_096_E2B`

**原始英文指令：** At 23 seconds, shift the upright vase onto the right half of the white circular tabletop.

**中文翻译：** 在第 23 秒，将直立花瓶移动到白色圆桌面的右半部分。

**状态：** 接受

**原子化判定句：**

1. 直立花瓶是否被移动到白色圆桌面的右半部分？


## 289 — `synthetic_object_097_E1`

**原始英文指令：** At 15.5 seconds, rotate the spiral shell until its large aperture faces directly toward the camera.

**中文翻译：** 在第 15.5 秒，旋转螺旋贝壳，直到其大开口正对镜头。

**状态：** 接受

**原子化判定句：**

1. 螺旋贝壳是否被旋转到其大开口正对镜头？


## 290 — `synthetic_object_097_E2A`

**原始英文指令：** At 31.5 seconds, replace the brown spiral shell with one white ridged conch shell of comparable size.

**中文翻译：** 在第 31.5 秒，将棕色螺旋贝壳替换为一个尺寸相当的白色有棱海螺壳。

**状态：** 接受

**原子化判定句：**

1. 棕色螺旋贝壳是否被替换为恰好一个白色有棱海螺壳？

2. 替换后的海螺壳是否与原贝壳尺寸相当？


## 291 — `synthetic_object_097_E2B`

**原始英文指令：** At 26 seconds, create one small triangular chip in the lowest visible edge of the shell's pale outer lip.

**中文翻译：** 在第 26 秒，在贝壳浅色外唇最低的可见边缘制造一个小型三角形缺口。

**状态：** 接受

**原子化判定句：**

1. 贝壳浅色外唇最低的可见边缘是否形成一个小型三角形缺口？


## 292 — `synthetic_object_098_E1`

**原始英文指令：** At 16 seconds, add one small brown acorn on the stump one pine-cone width to the left of the pine cone.

**中文翻译：** 在第 16 秒，在树桩上松果左侧一个松果宽度处添加一颗小型棕色橡果。

**状态：** 接受

**原子化判定句：**

1. 树桩上是否添加了恰好一颗小型棕色橡果？

2. 该橡果是否位于松果左侧一个松果宽度处？


## 293 — `synthetic_object_098_E2A`

**原始英文指令：** Starting at 35.5 seconds, smoothly zoom out until the complete stump top, bark edge, and a surrounding band of grass are visible.

**中文翻译：** 从第 35.5 秒开始，平滑拉远镜头，直到完整的树桩顶部、树皮边缘和周围一圈草地都可见。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑拉远？

2. 拉远后，完整的树桩顶部、树皮边缘和周围一圈草地是否都可见？


## 294 — `synthetic_object_098_E2B`

**原始英文指令：** Starting at 28 seconds, change every exposed brown scale tip on the pine cone to frosted white over two seconds.

**中文翻译：** 从第 28 秒开始，在两秒内将松果所有露出的棕色鳞片尖端改为覆霜白色。

**状态：** 接受

**原子化判定句：**

1. 松果所有露出的棕色鳞片尖端是否变为覆霜白色？

2. 颜色变化是否在 2 秒内完成？


## 295 — `synthetic_object_099_E1`

**原始英文指令：** Starting at 10.5 seconds, transform the full feather display into a blue-tinted silent-film look with fine grain and a soft vignette.

**中文翻译：** 从第 10.5 秒开始，将整个羽毛展示转变为带细腻颗粒和柔和暗角的蓝色调默片风格。

**状态：** 接受

**原子化判定句：**

1. 整个羽毛展示是否转换为默片风格？

2. 画面是否呈现蓝色色调？

3. 画面是否出现细腻颗粒？

4. 画面是否出现柔和暗角？


## 296 — `synthetic_object_099_E2A`

**原始英文指令：** Starting at 34.5 seconds, make the feather's loose vane edge brush the reflective surface twice and rebound after each contact.

**中文翻译：** 从第 34.5 秒开始，让羽毛松散的羽片边缘轻刷反光表面两次，并在每次接触后回弹。

**状态：** 接受

**原子化判定句：**

1. 羽毛松散的羽片边缘是否轻刷反光表面两次？

2. 羽片边缘是否在每次接触后回弹？


## 297 — `synthetic_object_099_E2B`

**原始英文指令：** Starting at 25 seconds, accelerate the feather's lowering until its broad vane lies flat beside the reflection by 30.5 seconds.

**中文翻译：** 从第 25 秒开始，加快羽毛下降过程，使其宽阔羽片在第 30.5 秒前平躺在倒影旁。

**状态：** 接受

**原子化判定句：**

1. 羽毛下降过程是否加快？

2. 其宽阔羽片是否在 5.5 秒内平躺在倒影旁？


## 298 — `synthetic_object_100_E1`

**原始英文指令：** Starting at 15.5 seconds, make the settled white particles rise and circle clockwise around the miniature tree continuously.

**中文翻译：** 从第 15.5 秒开始，让沉降的白色颗粒升起，并持续围绕微型树顺时针旋转。

**状态：** 接受

**原子化判定句：**

1. 沉降的白色颗粒是否升起？

2. 白色颗粒是否围绕微型树顺时针旋转？

3. 它们是否持续顺时针旋转直到视频结束？


## 299 — `synthetic_object_100_E2A`

**原始英文指令：** Starting at 33.5 seconds, illuminate the miniature house from within with warm amber light that reaches the tree's lower half.

**中文翻译：** 从第 33.5 秒开始，用暖琥珀色光从内部照亮微型房屋，并让光线照到树的下半部分。

**状态：** 接受

**原子化判定句：**

1. 微型房屋是否由暖琥珀色光从内部照亮？

2. 暖琥珀色光是否照到树的下半部分？


## 300 — `synthetic_object_100_E2B`

**原始英文指令：** Starting at 28.5 seconds, make the white particles continue rotating clockwise as they steadily settle to the bottom of the snow globe.

**中文翻译：** 从第 28.5 秒开始，让白色颗粒在持续顺时针旋转的同时稳定沉降到雪景球底部。

**状态：** 接受

**原子化判定句：**

1. 白色颗粒是否持续顺时针旋转？

2. 它们是否在旋转的同时稳定沉降到雪景球底部？
