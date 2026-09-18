# 编辑指令原子化测试集——中文审阅版（100 条）

## 抽样与时间规则

- 从十份待编辑文档中各抽取 10 条，共 100 条。
- 每份文档选择源顺序中的第 1、12、23、34、45、56、67、78、89、100 个视频，并依次轮换 E1、E2A、E2B 分支。
- 每条均保留原始英文指令，并提供中文翻译和中文原子判定句。
- 原始指令中的首个 `At/Starting at XX seconds` 是视频截取点；原子判定句不重复该绝对时间。
- 后续绝对时间统一减去截取点，改写为片段内的相对时长。
- 每条最多 5 个原子判定句；简单且不可继续合理拆分的指令只保留 1 条。

## 1. `embodied_edit_records_test_100.md`

### 001 — `embodied_001_E1`

**原始英文指令：** At 15.0 seconds, replace the milk carton with a clear handled storage jug in the same task location.

**中文翻译：** 在第 15.0 秒，将牛奶纸盒替换为一个带透明把手的储物壶，并将其放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 牛奶纸盒是否被替换为一个带透明把手的储物壶？
2. 替换后的储物壶是否位于牛奶纸盒原本所在的任务位置？

### 002 — `embodied_026_E2A`

**原始英文指令：** At 32.0 seconds, make the exterior of the glass mixing bowl visibly chilled with a thin, even condensation layer for the rest of the visible scene.

**中文翻译：** 在第 32.0 秒，使玻璃搅拌碗的外表面呈现明显冰凉的状态，并带有一层薄而均匀的冷凝水，且该状态保持至可见场景结束。

**状态：** 接受

**原子化判定句：**

1. 玻璃搅拌碗的外表面是否呈现明显冰凉的状态并出现一层薄冷凝水？
2. 冷凝水层在碗的可见外表面上是否分布均匀？
3. 冰凉且带冷凝水的外观是否保持至可见场景结束？

### 003 — `embodied_049_E2B`

**原始英文指令：** Starting at 30.0 seconds, shift the ego viewpoint half a meter right and twenty-five centimeters lower toward the striped cloth over three seconds.

**中文翻译：** 从第 30.0 秒开始，在三秒内将第一人称视点朝条纹布方向向右移动半米，并降低二十五厘米。

**状态：** 接受

**原子化判定句：**

1. 第一人称视点是否在 3 秒内向右移动半米？
2. 第一人称视点是否在同一段 3 秒内降低二十五厘米？
3. 视点是否朝条纹布方向移动？

### 004 — `embodied_071_E1`

**原始英文指令：** At 18.0 seconds, position the free gloved hand nearest the bin's lower-right corner one palm-width from the supported opossum.

**中文翻译：** 在第 18.0 秒，将空闲的戴手套的手放在最靠近箱子右下角的位置，并与被托住的负鼠保持一个手掌宽的距离。

**状态：** 接受

**原子化判定句：**

1. 空闲的戴手套的手是否被放在最靠近箱子右下角的位置？
2. 该手与被托住的负鼠之间是否相距一个手掌宽？

### 005 — `embodied_088_E2A`

**原始英文指令：** At 41.0 seconds, render only the visible tabletop behind the segmented puzzle as a faceted low-poly work surface.

**中文翻译：** 在第 41.0 秒，仅将分块拼图后方可见的桌面渲染为带有切面的低多边形工作台表面。

**状态：** 接受

**原子化判定句：**

1. 分块拼图后方可见的桌面是否被渲染为带有切面的低多边形工作台表面？
2. 低多边形渲染是否仅作用于该可见桌面？

### 006 — `embodied_110_E2B`

**原始英文指令：** Starting at 26.0 seconds, bend the trunk steadily toward the open lower cookware rack for four seconds while lowering the pan.

**中文翻译：** 从第 26.0 秒开始，躯干持续四秒稳定地向打开的下层炊具架弯下，同时放低平底锅。

**状态：** 接受

**原子化判定句：**

1. 躯干是否朝打开的下层炊具架稳定地弯下并持续 4 秒？
2. 在躯干弯向炊具架的同时，平底锅是否被放低？

### 007 — `embodied_130_E1`

**原始英文指令：** Starting at 17.0 seconds, perform a two-second optical push-in to a stable close-up centered on the orange frame arm.

**中文翻译：** 从第 17.0 秒开始，进行一次持续两秒的光学推进，最终形成以橙色框架臂为中心的稳定特写。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 2 秒内完成光学推进？
2. 光学推进结束后，画面是否成为以橙色框架臂为中心的稳定特写？

### 008 — `embodied_153_E2A`

**原始英文指令：** At 32.0 seconds, add soft warm side lighting from frame-left across the amphibian, green net, and surrounding grass.

**中文翻译：** 在第 32.0 秒，从画面左侧加入柔和的暖色侧光，照亮两栖动物、绿色网具和周围草地。

**状态：** 接受

**原子化判定句：**

1. 场景中是否加入柔和的暖色侧光？
2. 新增光线是否来自画面左侧？
3. 新增光线是否覆盖两栖动物、绿色网具和周围草地？

### 009 — `embodied_179_E2B`

**原始英文指令：** At 34.0 seconds, replace the black mat with a same-size dark-gray close-up performance mat in the same task location.

**中文翻译：** 在第 34.0 秒，将黑色垫子替换为一个同样大小的深灰色近景表演垫，并放在相同的任务位置。

**状态：** 接受

**原子化判定句：**

1. 黑色垫子是否被替换为深灰色近景表演垫？
2. 替换后的垫子是否与原黑色垫子大小相同？
3. 替换后的垫子是否位于原黑色垫子的任务位置？

### 010 — `embodied_198_E1`

**原始英文指令：** Starting at 15.0 seconds, guide the patterned pencil left-to-right across both workbook diagrams in one pointing sweep over 4 seconds.

**中文翻译：** 从第 15.0 秒开始，用四秒完成一次从左向右的指示扫动，引导花纹铅笔划过练习册中的两幅图示。

**状态：** 接受

**原子化判定句：**

1. 花纹铅笔是否在 4 秒内完成一次从左向右的指示扫动？
2. 铅笔的指示扫动是否划过练习册中的两幅图示？

## 2. `human_edit_records_test_100.md`

### 011 — `human_001_E1`

**原始英文指令：** Starting at 16.0 seconds, change the green fortress toy from green to stone gray over the next two seconds.

**中文翻译：** 从第 16.0 秒开始，在接下来的两秒内将绿色堡垒玩具从绿色变为石灰色。

**状态：** 接受

**原子化判定句：**

1. 堡垒玩具是否在 2 秒内从绿色变为石灰色？

### 012 — `human_026_E2A`

**原始英文指令：** Starting at 28.0 seconds, make the nearest trailing runner perform a high-knee sprint for four seconds.

**中文翻译：** 从第 28.0 秒开始，让最近的后方跑者进行四秒高抬腿冲刺。

**状态：** 接受

**原子化判定句：**

1. 最近的后方跑者是否进行高抬腿冲刺并持续 4 秒？

### 013 — `human_047_E2B`

**原始英文指令：** Starting at 31.0 seconds, move the camera in a clockwise arc around the central pineapple plant for three seconds.

**中文翻译：** 从第 31.0 秒开始，让镜头围绕中央的菠萝植株沿顺时针弧线移动三秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否围绕中央的菠萝植株沿顺时针弧线移动并持续 3 秒？

### 014 — `human_064_E1`

**原始英文指令：** Starting at 14.0 seconds, change the man's short beard to a pointed goatee over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将男子的短胡须变为尖山羊胡。

**状态：** 接受

**原子化判定句：**

1. 男子的短胡须是否在 2 秒内变为尖山羊胡？

### 015 — `human_086_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the teacher walk steadily toward the left cube drawing for four seconds.

**中文翻译：** 从第 29.0 秒开始，让老师稳定地朝左侧立方体图画行走四秒。

**状态：** 接受

**原子化判定句：**

1. 老师是否稳定地朝左侧立方体图画行走并持续 4 秒？

### 016 — `human_110_E2B`

**原始英文指令：** At 29.0 seconds, replace the guitarist's necklace with a red neck scarf.

**中文翻译：** 在第 29.0 秒，将吉他手的项链替换为一条红色颈巾。

**状态：** 接受

**原子化判定句：**

1. 吉他手的项链是否被替换为一条红色颈巾？

### 017 — `human_134_E1`

**原始英文指令：** Starting at 15.0 seconds, make the man smile broadly toward the interviewer.

**中文翻译：** 从第 15.0 秒开始，让男子朝采访者露出灿烂的笑容。

**状态：** 接受

**原子化判定句：**

1. 男子是否露出灿烂的笑容？
2. 男子的笑容是否朝向采访者？

### 018 — `human_155_E2A`

**原始英文指令：** At 29.0 seconds, reposition the walking man on the right side of the road-facing frame.

**中文翻译：** 在第 29.0 秒，将正在行走的男子重新放置在朝向道路的画面右侧。

**状态：** 接受

**原子化判定句：**

1. 正在行走的男子是否被重新放置在朝向道路的画面右侧？

### 019 — `human_176_E2B`

**原始英文指令：** Starting at 29.0 seconds, zoom in on the sign-language presenter's upper body and hands over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内拉近镜头，聚焦于手语讲解者的上半身和双手。

**状态：** 接受

**原子化判定句：**

1. 镜头是否在 3 秒内完成拉近？
2. 拉近后的画面是否聚焦于手语讲解者的上半身和双手？

### 020 — `human_198_E1`

**原始英文指令：** Starting at 14.0 seconds, make the woman puff out both cheeks and raise her eyebrows.

**中文翻译：** 从第 14.0 秒开始，让女子鼓起双颊并抬起眉毛。

**状态：** 接受

**原子化判定句：**

1. 女子是否鼓起双颊？
2. 女子是否抬起眉毛？

## 3. `object_edit_records_test_100.md`

### 021 — `object_001_E1`

**原始英文指令：** Starting at 14.0 seconds, change the adult rabbit's fur from mottled gray-brown to pale cream over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将成年兔子的毛色从斑驳的灰褐色变为浅奶油色。

**状态：** 接受

**原子化判定句：**

1. 成年兔子的毛色是否在 2 秒内从斑驳的灰褐色变为浅奶油色？

### 022 — `object_023_E2A`

**原始英文指令：** Starting at 29.0 seconds, orbit clockwise around the motorcycle at wheel height for five seconds.

**中文翻译：** 从第 29.0 秒开始，让镜头在车轮高度围绕摩托车顺时针环绕五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否围绕摩托车顺时针环绕并持续 5 秒？
2. 镜头在环绕过程中是否保持在车轮高度？

### 023 — `object_045_E2B`

**原始英文指令：** At 29.0 seconds, replace the protruding rock pillar on the left with a vertical weathered log of the same size.

**中文翻译：** 在第 29.0 秒，将左侧突出的岩柱替换为一根同样大小、竖直放置且经过风化的原木。

**状态：** 接受

**原子化判定句：**

1. 左侧突出的岩柱是否被替换为一根竖直放置的风化原木？
2. 替换后的原木是否与岩柱大小相同？

### 024 — `object_068_E1`

**原始英文指令：** Starting at 14.0 seconds, make the black hand brush touch the frog's back lightly three times.

**中文翻译：** 从第 14.0 秒开始，让黑色手刷轻触青蛙背部三次。

**状态：** 接受

**原子化判定句：**

1. 黑色手刷是否轻触青蛙背部三次？

### 025 — `object_090_E2A`

**原始英文指令：** Starting at 23.0 seconds, accelerate the adult elephants' convergence to twice its original rate, forming a close group around the smaller elephant by 27.0 seconds.

**中文翻译：** 从第 23.0 秒开始，将成年象聚拢的速度提高到原来的两倍，并在第 27.0 秒前围绕较小的象形成紧密群体。

**状态：** 接受

**原子化判定句：**

1. 成年象是否以原来两倍的速度聚拢？
2. 成年象是否在 4 秒内围绕较小的象形成紧密群体？

### 026 — `object_110_E2B`

**原始英文指令：** Starting at 29.0 seconds, make the submerged hippo follow a tighter clockwise arc above the seabed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让水下的河马在海床上方沿更紧凑的顺时针弧线移动六秒。

**状态：** 接受

**原子化判定句：**

1. 水下的河马是否沿更紧凑的顺时针弧线移动并持续 6 秒？
2. 河马在沿弧线移动时是否保持位于海床上方？

### 027 — `object_130_E1`

**原始英文指令：** Starting at 14.0 seconds, change the shallow wetland channel from muted green-brown to clear turquoise over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内将浅湿地水道从暗淡的绿褐色变为清澈的蓝绿色。

**状态：** 接受

**原子化判定句：**

1. 浅湿地水道是否在 2 秒内从暗淡的绿褐色变为清澈的蓝绿色？

### 028 — `object_158_E2A`

**原始英文指令：** Starting at 29.0 seconds, make the adult jaguar walk toward the vegetation at half its original speed for six seconds.

**中文翻译：** 从第 29.0 秒开始，让成年美洲豹以原来一半的速度朝植被行走六秒。

**状态：** 接受

**原子化判定句：**

1. 成年美洲豹是否朝植被行走并持续 6 秒？
2. 美洲豹在这 6 秒内是否以原来一半的速度行走？

### 029 — `object_174_E2B`

**原始英文指令：** At 29.0 seconds, replace the circular ground facility cover with a flat gray stone of similar size.

**中文翻译：** 在第 29.0 秒，将地面上的圆形设施盖替换为一块大小相近的扁平灰色石头。

**状态：** 接受

**原子化判定句：**

1. 地面上的圆形设施盖是否被替换为一块扁平的灰色石头？
2. 替换后的石头是否与设施盖大小相近？

### 030 — `object_200_E1`

**原始英文指令：** Starting at 14.0 seconds, change the hard direct sunlight on the alligator-like animal and fairway to soft diffuse overcast illumination over the next two seconds.

**中文翻译：** 从第 14.0 秒开始，在接下来的两秒内，将照在类短吻鳄动物和球道上的强烈直射阳光变为柔和、漫射的阴天光照。

**状态：** 接受

**原子化判定句：**

1. 类短吻鳄动物和球道上的强烈直射阳光是否在 2 秒内变为柔和、漫射的阴天光照？

## 4. `process_edit_records_test_100.md`

### 031 — `process_001_E1`

**原始英文指令：** Starting at 13.0 seconds, make several loose fallen leaves swirl in small clockwise eddies across the forest floor for five seconds.

**中文翻译：** 从第 13.0 秒开始，让几片散落的落叶在林地上形成小型顺时针涡旋并旋转五秒。

**状态：** 接受

**原子化判定句：**

1. 几片散落的落叶是否在林地上以小型顺时针涡旋旋转并持续 5 秒？

### 032 — `process_022_E2A`

**原始英文指令：** Starting at 25.0 seconds, pause the formation of new dark engraved marks on the board for five seconds.

**中文翻译：** 从第 25.0 秒开始，让板上新的深色雕刻痕迹暂停形成五秒。

**状态：** 接受

**原子化判定句：**

1. 板上新的深色雕刻痕迹是否暂停形成并持续 5 秒？

### 033 — `process_046_E2B`

**原始英文指令：** Starting at 31.0 seconds, pan the camera smoothly to the right for four seconds while following the long cloud band.

**中文翻译：** 从第 31.0 秒开始，让镜头平滑地向右平移四秒，同时跟随长条云带。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑地向右平移并持续 4 秒？
2. 镜头在向右平移时是否跟随长条云带？

### 034 — `process_068_E1`

**原始英文指令：** Starting at 13.0 seconds, slow the outward and upward expansion of the explosion cloud to half its original progression rate through 23.0 seconds.

**中文翻译：** 从第 13.0 秒开始，将爆炸云向外和向上扩张的进展速度减慢到原来的一半，并持续到第 23.0 秒。

**状态：** 接受

**原子化判定句：**

1. 爆炸云是否继续向外和向上扩张？
2. 爆炸云是否在接下来的 10 秒内以原来一半的进展速度扩张？

### 035 — `process_088_E2A`

**原始英文指令：** Starting at 29.0 seconds, track the small illuminated flying object with a smooth level camera pan for six seconds.

**中文翻译：** 从第 29.0 秒开始，以平滑且水平的镜头平移跟踪发光的小型飞行物六秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否跟踪发光的小型飞行物并持续 6 秒？
2. 跟踪是否通过平滑且保持水平的镜头平移完成？

### 036 — `process_114_E2B`

**原始英文指令：** At 28.0 seconds, reposition the low sun directly above the visible vanishing point of the central road.

**中文翻译：** 在第 28.0 秒，将低空太阳重新放置在中央道路可见消失点的正上方。

**状态：** 接受

**原子化判定句：**

1. 低空太阳是否被重新放置在中央道路可见消失点的正上方？

### 037 — `process_135_E1`

**原始英文指令：** Starting at 13.0 seconds, make the paraglider follow a smooth horizontal figure-eight path for six seconds.

**中文翻译：** 从第 13.0 秒开始，让滑翔伞沿平滑的水平“8”字形路径移动六秒。

**状态：** 接受

**原子化判定句：**

1. 滑翔伞是否沿平滑的水平“8”字形路径移动并持续 6 秒？

### 038 — `process_154_E2A`

**原始英文指令：** At 29.0 seconds, split the largest connected lower-left red fruit cluster into two separated groups with equal visible fruit counts.

**中文翻译：** 在第 29.0 秒，将左下方最大的相连红色水果簇拆分为两个彼此分开的组，并使两组可见水果数量相等。

**状态：** 接受

**原子化判定句：**

1. 左下方最大的相连红色水果簇是否被拆分为两组？
2. 拆分后的两组是否彼此分开？
3. 拆分后的两组是否包含数量相等的可见水果？

### 039 — `process_179_E2B`

**原始英文指令：** Starting at 28.0 seconds, transform the complete coastline scene into a detailed gouache landscape painting over two seconds.

**中文翻译：** 从第 28.0 秒开始，在两秒内将完整的海岸线场景转变为细节丰富的水粉风景画。

**状态：** 接受

**原子化判定句：**

1. 完整的海岸线场景是否在 2 秒内转变为细节丰富的水粉风景画？

### 040 — `process_198_E1`

**原始英文指令：** At 13.0 seconds, add a thin horizontal twig attached to the vertical support directly above the fixed chrysalis.

**中文翻译：** 在第 13.0 秒，在固定蛹正上方添加一根细小的水平树枝，并将其连接到竖直支撑物上。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一根细小的水平树枝？
2. 新增树枝是否连接在竖直支撑物上？
3. 新增树枝是否位于固定蛹的正上方？

## 5. `scene_edit_records_test_100.md`

### 041 — `scene_002_E1`

**原始英文指令：** Starting at 17.5 seconds, make the pool become visibly clearer over two seconds.

**中文翻译：** 从第 17.5 秒开始，在两秒内使泳池明显变得更加清澈。

**状态：** 接受

**原子化判定句：**

1. 泳池是否在 2 秒内明显变得更加清澈？

### 042 — `scene_023_E2A`

**原始英文指令：** At 26.5 seconds, delay the side-crossing pedestrian stream until 28.5 seconds, two seconds after the forward-moving pedestrian stream in the market aisle begins.

**中文翻译：** 在第 26.5 秒，将横向穿行的人流推迟到第 28.5 秒，即市场过道中向前移动的人流开始后的两秒。

**状态：** 接受

**原子化判定句：**

1. 市场过道中向前移动的人流是否开始移动？
2. 横向穿行的人流是否在向前移动的人流开始 2 秒后启动？

### 043 — `scene_043_E2B`

**原始英文指令：** At 34.0 seconds, place the entering group one member width toward frame left from the source position.

**中文翻译：** 在第 34.0 秒，将正在进入的人群从原位置向画面左侧移动一个成员身宽的距离。

**状态：** 接受

**原子化判定句：**

1. 正在进入的人群是否从原位置向画面左侧移动了一个成员身宽的距离？

### 044 — `scene_065_E1`

**原始英文指令：** Starting at 14.5 seconds, change the visible outdoor weather to thin overcast conditions over three seconds.

**中文翻译：** 从第 14.5 秒开始，在三秒内将可见的户外天气变为薄云阴天。

**状态：** 接受

**原子化判定句：**

1. 可见的户外天气是否在 3 秒内变为薄云阴天？

### 045 — `scene_088_E2A`

**原始英文指令：** At 26.5 seconds, place one voxel tree one voxel block farther from the main path edge.

**中文翻译：** 在第 26.5 秒，将一棵体素树放置到比原来距离主路径边缘多一个体素块的位置。

**状态：** 接受

**原子化判定句：**

1. 一棵体素树是否被移到距主路径边缘比原来远一个体素块的位置？

### 046 — `scene_110_E2B`

**原始英文指令：** Starting at 28.5 seconds, smooth the rightward tracking pan around both giraffes by 25% for 6.0 seconds.

**中文翻译：** 从第 28.5 秒开始，将围绕两只长颈鹿向右跟踪平移的平滑程度提高 25%，持续 6.0 秒。

**状态：** 接受（单条保底）

**原子化判定句：**

1. 围绕两只长颈鹿向右跟踪平移的镜头，其平滑程度是否提高了 25%，并持续 6.0 秒？

### 047 — `scene_135_E1`

**原始英文指令：** Starting at 14.5 seconds, change the temple-garden overcast to softly layered thin-cloud coverage over three seconds.

**中文翻译：** 从第 14.5 秒开始，在三秒内将寺庙花园的阴天状态变为具有柔和层次的薄云覆盖。

**状态：** 接受

**原子化判定句：**

1. 寺庙花园上空是否在 3 秒内从阴天变为具有柔和层次的薄云覆盖？

### 048 — `scene_153_E2A`

**原始英文指令：** At 27.5 seconds, place one central corridor pedestrian on the corridor centerline between the column rows.

**中文翻译：** 在第 27.5 秒，将中央走廊中的一名行人放置在两排柱子之间的走廊中心线上。

**状态：** 接受

**原子化判定句：**

1. 中央走廊中的一名行人是否被放置在走廊中心线上？
2. 该行人是否位于两排柱子之间？

### 049 — `scene_179_E2B`

**原始英文指令：** Starting at 26.5 seconds, crop the framing inward by 8% and recenter the narrow vertical scene over 2.5 seconds.

**中文翻译：** 从第 26.5 秒开始，在 2.5 秒内将画面向内裁切 8%，并重新居中狭窄的竖向场景。

**状态：** 接受

**原子化判定句：**

1. 画面是否在 2.5 秒内向内裁切 8%？
2. 狭窄的竖向场景是否在同一段 2.5 秒内重新居中？

### 050 — `scene_199_E1`

**原始英文指令：** Starting at 15.5 seconds, darken the unmarked teal badminton-court surface by 12% over three seconds.

**中文翻译：** 从第 15.5 秒开始，在三秒内将没有标线的蓝绿色羽毛球场地表面调暗 12%。

**状态：** 接受

**原子化判定句：**

1. 没有标线的蓝绿色羽毛球场地表面是否在 3 秒内调暗 12%？

## 6. `syn_embodied_edit_records.md`

### 051 — `synthetic_embodied_001_E1`

**原始英文指令：** At 10.5 seconds, recolor the blue sofa's visible seat and back upholstery to burnt orange.

**中文翻译：** 在第 10.5 秒，将蓝色沙发可见的座垫和靠背面料重新着色为焦橙色。

**状态：** 接受

**原子化判定句：**

1. 蓝色沙发可见的座垫面料是否变为焦橙色？
2. 蓝色沙发可见的靠背面料是否变为焦橙色？

### 052 — `synthetic_embodied_012_E2A`

**原始英文指令：** At 25 seconds, make the visible aquarium fish circle clockwise around the main rock group for four seconds.

**中文翻译：** 在第 25 秒，让水族箱中可见的鱼围绕主要岩石群顺时针游动四秒。

**状态：** 接受

**原子化判定句：**

1. 水族箱中可见的鱼是否围绕主要岩石群顺时针游动并持续 4 秒？

### 053 — `synthetic_embodied_023_E2B`

**原始英文指令：** At 29.5 seconds, set both hands side by side, one palm-width apart, above the duvet for three seconds.

**中文翻译：** 在第 29.5 秒，将双手并排放在羽绒被上方，间距为一个手掌宽，并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 双手是否被放置在羽绒被上方？
2. 双手是否并排且相距一个手掌宽？
3. 双手是否将该位置和间距保持 3 秒？

### 054 — `synthetic_embodied_034_E1`

**原始英文指令：** At 16 seconds, make both hands slide the lower dishwasher rack halfway inward and back out over four seconds.

**中文翻译：** 在第 16 秒，让双手在四秒内将洗碗机下层搁架向内推到一半，然后再拉回外侧。

**状态：** 接受

**原子化判定句：**

1. 双手是否将洗碗机下层搁架向内推到一半？
2. 双手是否随后将搁架拉回外侧，并在 4 秒内完成整个推入和拉出过程？

### 055 — `synthetic_embodied_045_E2A`

**原始英文指令：** At 20 seconds, recolor the visible bark of the central tree trunk to pale cream.

**中文翻译：** 在第 20 秒，将中央树干可见的树皮重新着色为浅奶油色。

**状态：** 接受

**原子化判定句：**

1. 中央树干可见的树皮是否变为浅奶油色？

### 056 — `synthetic_embodied_056_E2B`

**原始英文指令：** At 28 seconds, replace the rectangular black floor mat near the cabinets with a shallow wicker basket.

**中文翻译：** 在第 28 秒，将橱柜附近的黑色长方形地垫替换为一个浅藤篮。

**状态：** 接受

**原子化判定句：**

1. 橱柜附近的黑色长方形地垫是否被替换为一个浅藤篮？

### 057 — `synthetic_embodied_067_E1`

**原始英文指令：** At 13 seconds, make the large white sail visibly wet with irregular darker patches.

**中文翻译：** 在第 13 秒，使白色大帆呈现明显湿润的外观，并带有不规则的深色斑块。

**状态：** 接受

**原子化判定句：**

1. 白色大帆是否呈现明显湿润的外观？
2. 湿润的帆面上是否出现不规则的深色斑块？

### 058 — `synthetic_embodied_078_E2A`

**原始英文指令：** At 23.5 seconds, position the operator's visible right hand palm-forward in the upper-right cabin area for three seconds.

**中文翻译：** 在第 23.5 秒，将操作者可见的右手放在驾驶舱右上区域，手掌朝前，并保持三秒。

**状态：** 接受

**原子化判定句：**

1. 操作者可见的右手是否被放置在驾驶舱右上区域？
2. 右手是否保持手掌朝前？
3. 右手是否将该位置和朝向保持 3 秒？

### 059 — `synthetic_embodied_089_E2B`

**原始英文指令：** At 29.5 seconds, split the white plate into two separate semicircular pieces lying flat on the serving cart.

**中文翻译：** 在第 29.5 秒，将白色盘子分成两个彼此分开的半圆形部分，并使它们平放在送餐车上。

**状态：** 接受

**原子化判定句：**

1. 白色盘子是否被分成两个半圆形部分？
2. 两个半圆形部分是否彼此分开？
3. 两个半圆形部分是否平放在送餐车上？

### 060 — `synthetic_embodied_100_E1`

**原始英文指令：** At 16 seconds, make the right hand scrape the lower window frost with short vertical strokes for four seconds.

**中文翻译：** 在第 16 秒，让右手用短促的竖直动作刮擦窗户下部的霜层四秒。

**状态：** 接受

**原子化判定句：**

1. 右手是否刮擦窗户下部的霜层并持续 4 秒？
2. 右手是否使用短促的竖直动作进行刮擦？

## 7. `syn_human_edit_records.md`

### 061 — `synthetic_human_001_E1`

**原始英文指令：** Starting at 12.5 seconds, smoothly zoom out until the woman's upper torso and the surrounding window frame are both visible.

**中文翻译：** 从第 12.5 秒开始，平滑地拉远镜头，直到女子的上半身和周围的窗框都清晰可见。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑地拉远？
2. 镜头拉远后，女子的上半身和周围的窗框是否都可见？

### 062 — `synthetic_human_012_E2A`

**原始英文指令：** At 29.0 seconds, add a pottery assistant visible from the chest up in the empty background behind the potter's left shoulder.

**中文翻译：** 在第 29.0 秒，在陶艺师左肩后方的空白背景中添加一名胸部以上可见的陶艺助手。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一名胸部以上可见的陶艺助手？
2. 新增助手是否位于陶艺师左肩后方的空白背景中？

### 063 — `synthetic_human_023_E2B`

**原始英文指令：** Starting at 26.0 seconds, add soft warm frontal light to the woman's face, clearly revealing both eyes, cheeks, and mouth.

**中文翻译：** 从第 26.0 秒开始，为女子面部添加柔和的暖色正面光，使双眼、双颊和嘴部都清晰可见。

**状态：** 接受

**原子化判定句：**

1. 女子的面部是否添加了柔和的暖色正面光？
2. 新增光线是否使女子的双眼、双颊和嘴部都清晰可见？

### 064 — `synthetic_human_034_E1`

**原始英文指令：** Starting at 12.5 seconds, change the white drinking cup into pale blue glazed ceramic over two seconds.

**中文翻译：** 从第 12.5 秒开始，在两秒内将白色饮水杯变为浅蓝色釉面陶瓷杯。

**状态：** 接受

**原子化判定句：**

1. 白色饮水杯是否在 2 秒内变为陶瓷杯？
2. 变换后的陶瓷杯是否呈浅蓝色釉面外观？

### 065 — `synthetic_human_045_E2A`

**原始英文指令：** At 29.0 seconds, replace the male tai chi practitioner with a female practitioner wearing the same plain white uniform.

**中文翻译：** 在第 29.0 秒，将男性太极练习者替换为一名穿着相同素白制服的女性练习者。

**状态：** 接受

**原子化判定句：**

1. 男性太极练习者是否被替换为女性练习者？
2. 女性练习者是否穿着与原练习者相同的素白制服？

### 066 — `synthetic_human_056_E2B`

**原始英文指令：** Starting at 25.5 seconds, render only the seated woman as a textured charcoal drawing with soft gray shading over two and a half seconds.

**中文翻译：** 从第 25.5 秒开始，在两秒半内仅将坐着的女子渲染为带纹理的木炭画，并带有柔和的灰色阴影。

**状态：** 接受

**原子化判定句：**

1. 坐着的女子是否在 2.5 秒内被渲染为带纹理的木炭画？
2. 木炭画效果是否带有柔和的灰色阴影？
3. 木炭画渲染是否仅作用于坐着的女子？

### 067 — `synthetic_human_067_E1`

**原始英文指令：** Starting at 12.0 seconds, make both rooftop women lean toward each other together and return to upright sitting over four seconds.

**中文翻译：** 从第 12.0 秒开始，让屋顶上的两名女子同时相互靠近倾身，并在四秒内恢复直立坐姿。

**状态：** 接受

**原子化判定句：**

1. 屋顶上的两名女子是否都朝彼此倾身？
2. 两名女子是否同时完成倾身动作？
3. 两名女子是否随后恢复直立坐姿，并在 4 秒内完成整个动作过程？

### 068 — `synthetic_human_078_E2A`

**原始英文指令：** At 30.0 seconds, increase the distance between the boxer and pad-holding coach by twenty centimeters while they remain face to face.

**中文翻译：** 在第 30.0 秒，在拳击手和持靶教练继续面对面的同时，将两人之间的距离增加二十厘米。

**状态：** 接受

**原子化判定句：**

1. 拳击手与持靶教练之间的距离是否增加了二十厘米？
2. 距离增加后，两人是否仍保持面对面？

### 069 — `synthetic_human_089_E2B`

**原始英文指令：** Starting at 25.5 seconds, make the front-left man perform one controlled reverse lunge and return to his starting stance.

**中文翻译：** 从第 25.5 秒开始，让左前方的男子完成一次受控的后撤弓步，并回到起始站姿。

**状态：** 接受

**原子化判定句：**

1. 左前方的男子是否完成一次受控的后撤弓步？
2. 男子是否在后撤弓步后回到起始站姿？

### 070 — `synthetic_human_100_E1`

**原始英文指令：** Starting at 13.0 seconds, make the right-rear worker complete two slow parallel ironing passes across the cloth.

**中文翻译：** 从第 13.0 秒开始，让右后方的工人在布料上完成两次缓慢且相互平行的熨烫移动。

**状态：** 接受

**原子化判定句：**

1. 右后方的工人是否在布料上完成两次缓慢的熨烫移动？
2. 两次熨烫移动的路径是否相互平行？

## 8. `syn_object_edit_records.md`

### 071 — `synthetic_object_001_E1`

**原始英文指令：** Starting at 11.5 seconds, transform the full dog-and-frisbee scene into a colored-pencil animation over the next two seconds.

**中文翻译：** 从第 11.5 秒开始，在接下来的两秒内将完整的狗与飞盘场景转变为彩色铅笔动画。

**状态：** 接受

**原子化判定句：**

1. 完整的狗与飞盘场景是否在 2 秒内转变为彩色铅笔动画？

### 072 — `synthetic_object_012_E2A`

**原始英文指令：** Starting at 35.5 seconds, make the dog scrape the grass twice with one visible forepaw.

**中文翻译：** 从第 35.5 秒开始，让狗用一只可见的前爪刨草两次。

**状态：** 接受

**原子化判定句：**

1. 狗是否刨草两次？
2. 狗是否使用一只可见的前爪完成刨草动作？

### 073 — `synthetic_object_023_E2B`

**原始英文指令：** Starting at 27.5 seconds, move the camera smoothly from the bus's rear quarter toward its front doors for five seconds.

**中文翻译：** 从第 27.5 秒开始，让镜头从公交车后侧平滑地朝前门方向移动五秒。

**状态：** 接受

**原子化判定句：**

1. 镜头是否从公交车后侧平滑地朝前门方向移动并持续 5 秒？

### 074 — `synthetic_object_034_E1`

**原始英文指令：** Starting at 14.5 seconds, make the rear discharge chute swing downward and pour one short stream of concrete onto the road.

**中文翻译：** 从第 14.5 秒开始，让后部卸料槽向下摆动，并向道路浇出一股短暂的混凝土流。

**状态：** 接受

**原子化判定句：**

1. 后部卸料槽是否向下摆动？
2. 卸料槽向下摆动后，是否向道路浇出一股短暂的混凝土流？

### 075 — `synthetic_object_045_E2A`

**原始英文指令：** Starting at 31 seconds, change the catamaran's dark aft canopy from dry and matte to rain-wet and glossy.

**中文翻译：** 从第 31 秒开始，将双体船深色的后部顶篷从干燥哑光状态变为被雨淋湿且有光泽的状态。

**状态：** 接受

**原子化判定句：**

1. 双体船深色的后部顶篷是否从干燥状态变为被雨淋湿的状态？
2. 后部顶篷的表面是否从哑光变为有光泽？

### 076 — `synthetic_object_056_E2B`

**原始英文指令：** Starting at 25.5 seconds, make the standing paddler lift the wooden oar, spin it once, and resume rowing.

**中文翻译：** 从第 25.5 秒开始，让站立的划桨者举起木桨，将其旋转一圈，然后恢复划船。

**状态：** 接受

**原子化判定句：**

1. 站立的划桨者是否举起木桨？
2. 划桨者是否在举起木桨后将其旋转一圈？
3. 划桨者是否在旋转木桨后恢复划船？

### 077 — `synthetic_object_067_E1`

**原始英文指令：** Starting at 11 seconds, increase the suspended beam's horizontal transfer speed to one-and-a-half times its original rate for five seconds.

**中文翻译：** 从第 11 秒开始，将悬吊横梁的水平移动速度提高到原来的 1.5 倍，并持续五秒。

**状态：** 接受

**原子化判定句：**

1. 悬吊横梁是否以原来 1.5 倍的速度水平移动并持续 5 秒？

### 078 — `synthetic_object_078_E2A`

**原始英文指令：** At 30 seconds, increase the gap between the two raised bridge tips to one full bridge-leaf width.

**中文翻译：** 在第 30 秒，将两个抬起的桥叶尖端之间的间距增加到一个完整桥叶的宽度。

**状态：** 接受

**原子化判定句：**

1. 两个抬起的桥叶尖端之间的间距是否增加到一个完整桥叶的宽度？

### 079 — `synthetic_object_089_E2B`

**原始英文指令：** At 28.5 seconds, chip one small triangular section from the tip of the tallest central purple crystal.

**中文翻译：** 在第 28.5 秒，从中央最高的紫色晶体尖端崩掉一小块三角形部分。

**状态：** 接受

**原子化判定句：**

1. 是否从中央最高的紫色晶体上崩掉一小块三角形部分？
2. 缺口是否位于该晶体的尖端？

### 080 — `synthetic_object_100_E1`

**原始英文指令：** Starting at 15.5 seconds, make the settled white particles rise and circle clockwise around the miniature tree continuously.

**中文翻译：** 从第 15.5 秒开始，让沉降的白色颗粒升起，并持续围绕微型树顺时针旋转。

**状态：** 接受

**原子化判定句：**

1. 沉降的白色颗粒是否升起？
2. 白色颗粒升起后，是否一直围绕微型树顺时针旋转到视频结束？

## 9. `syn_process_edit_records.md`

### 081 — `synthetic_process_001_E1`

**原始英文指令：** Starting at 12.5 seconds, slow the sunrise so the sun first clears the central mountain ridge at 20.5 seconds.

**中文翻译：** 从第 12.5 秒开始，减慢日出进程，使太阳在第 20.5 秒首次越过中央山脊。

**状态：** 接受

**原子化判定句：**

1. 日出进程是否减慢？
2. 太阳是否在 8 秒内首次越过中央山脊？

### 082 — `synthetic_process_012_E2A`

**原始英文指令：** Starting at 27.0 seconds, accelerate nightfall until the remaining twilight band becomes deep navy by 32.0 seconds.

**中文翻译：** 从第 27.0 秒开始，加快入夜进程，使剩余的暮光带在第 32.0 秒前变为深海军蓝色。

**状态：** 接受

**原子化判定句：**

1. 入夜进程是否加快？
2. 剩余的暮光带是否在 5 秒内变为深海军蓝色？

### 083 — `synthetic_process_023_E2B`

**原始英文指令：** Starting at 29.0 seconds, advance the burn stage until only two short flames and a low red ember bed remain by 33.5 seconds.

**中文翻译：** 从第 29.0 秒开始，推进燃烧阶段，使画面在第 33.5 秒前只剩两簇短火焰和一层低矮的红色余烬。

**状态：** 接受

**原子化判定句：**

1. 画面是否在 4.5 秒内只剩两簇短火焰？
2. 画面是否在同一段 4.5 秒内只剩一层低矮的红色余烬？

### 084 — `synthetic_process_034_E1`

**原始英文指令：** Starting at 14.0 seconds, advance bubbling until continuous bubble columns reach and ripple the full liquid surface by 19.0 seconds.

**中文翻译：** 从第 14.0 秒开始，推进起泡过程，使连续的气泡柱在第 19.0 秒前到达整个液面并使其产生波纹。

**状态：** 接受

**原子化判定句：**

1. 连续的气泡柱是否在 5 秒内到达整个液面？
2. 气泡柱到达后，整个液面是否产生波纹？

### 085 — `synthetic_process_045_E2A`

**原始英文指令：** Starting at 29.0 seconds, shift the full melting-ice scene to a cool silver-blue duotone over two seconds.

**中文翻译：** 从第 29.0 秒开始，在两秒内将完整的融冰场景转换为冷调银蓝双色调。

**状态：** 接受

**原子化判定句：**

1. 完整的融冰场景是否在 2 秒内转换为冷调银蓝双色调？

### 086 — `synthetic_process_056_E2B`

**原始英文指令：** Starting at 28.5 seconds, advance the sheet until no red glow remains and it reaches its lowest visible position by 33.0 seconds.

**中文翻译：** 从第 28.5 秒开始，推进板材的变化，使其在第 33.0 秒前不再带有红色辉光，并到达可见的最低位置。

**状态：** 接受

**原子化判定句：**

1. 板材上的红色辉光是否在 4.5 秒内完全消失？
2. 板材是否在同一段 4.5 秒内到达可见的最低位置？

### 087 — `synthetic_process_067_E1`

**原始英文指令：** At 14.5 seconds, add one smaller pale mushroom with a short stem on the empty upper-right wood area.

**中文翻译：** 在第 14.5 秒，在右上方空白的木质区域添加一朵较小、颜色浅且菌柄较短的蘑菇。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一朵较小、颜色浅且菌柄较短的蘑菇？
2. 新增蘑菇是否位于右上方空白的木质区域？

### 088 — `synthetic_process_078_E2A`

**原始英文指令：** Starting at 30.0 seconds, make three visible lateral roots sway left and right in alternating sequence for five seconds.

**中文翻译：** 从第 30.0 秒开始，让三条可见的侧根以交替顺序左右摆动五秒。

**状态：** 接受

**原子化判定句：**

1. 三条可见的侧根是否左右摆动并持续 5 秒？
2. 三条侧根是否以交替顺序摆动？

### 089 — `synthetic_process_089_E2B`

**原始英文指令：** Starting at 28.0 seconds, make the central support block above the base compliant rubber that visibly compresses over two seconds.

**中文翻译：** 从第 28.0 秒开始，将底座上方的中央支撑块变为柔顺橡胶，使其在两秒内发生明显压缩。

**状态：** 接受

**原子化判定句：**

1. 底座上方的中央支撑块是否变为柔顺橡胶材质？
2. 该支撑块是否在 2 秒内发生明显压缩？

### 090 — `synthetic_process_100_E1`

**原始英文指令：** Starting at 14.0 seconds, make the black bladder shell thicker and more elastic with shallow longitudinal ribs over two seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒内使黑色囊状外壳变得更厚、更有弹性，并出现浅的纵向棱纹。

**状态：** 接受

**原子化判定句：**

1. 黑色囊状外壳是否在 2 秒内变得更厚？
2. 黑色囊状外壳是否在同一段 2 秒内变得更有弹性？
3. 黑色囊状外壳是否在同一段 2 秒内出现浅的纵向棱纹？

## 10. `syn_scene_edit_records.md`

### 091 — `synthetic_scene_001_E1`

**原始英文指令：** Starting at 17.0 seconds, increase the daylight entering through the rear window, gently brightening the island and surrounding floor over two and a half seconds.

**中文翻译：** 从第 17.0 秒开始，增强从后窗进入的日光，在两秒半内柔和地照亮中岛和周围地面。

**状态：** 接受

**原子化判定句：**

1. 从后窗进入的日光是否增强？
2. 中岛和周围地面是否在 2.5 秒内被柔和地照亮？

### 092 — `synthetic_scene_012_E2A`

**原始英文指令：** At 24.0 seconds, add a small blank wooden menu holder upright on the empty rear-right corner of the dining table.

**中文翻译：** 在第 24.0 秒，在餐桌右后方的空角落添加一个小型、无文字的木质菜单架，并将其直立放置。

**状态：** 接受

**原子化判定句：**

1. 是否添加了一个小型、无文字的木质菜单架？
2. 菜单架是否直立放置？
3. 菜单架是否位于餐桌右后方原本空置的角落？

### 093 — `synthetic_scene_023_E2B`

**原始英文指令：** Starting at 26.0 seconds, change the left-foreground sidewalk wall from light gray stone to dark charcoal over two and a half seconds.

**中文翻译：** 从第 26.0 秒开始，在两秒半内将左前景人行道墙面的颜色从浅石灰色变为深炭灰色。

**状态：** 接受

**原子化判定句：**

1. 左前景人行道墙面是否在 2.5 秒内从浅石灰色变为深炭灰色？

### 094 — `synthetic_scene_034_E1`

**原始英文指令：** Starting at 14.0 seconds, make concentric ripples repeatedly spread from the fallen log's submerged end for five seconds.

**中文翻译：** 从第 14.0 秒开始，让同心波纹从倒木浸入水中的一端反复向外扩散五秒。

**状态：** 接受

**原子化判定句：**

1. 是否有同心波纹反复向外扩散并持续 5 秒？
2. 波纹是否从倒木浸入水中的一端开始扩散？

### 095 — `synthetic_scene_045_E2A`

**原始英文指令：** Starting at 29.0 seconds, render only the visible greenhouse tiled floor as a softly layered watercolor region over three seconds.

**中文翻译：** 从第 29.0 秒开始，在三秒内仅将温室中可见的瓷砖地面渲染为具有柔和层次的水彩区域。

**状态：** 接受

**原子化判定句：**

1. 温室中可见的瓷砖地面是否在 3 秒内被渲染为具有柔和层次的水彩区域？
2. 水彩渲染是否仅作用于该可见瓷砖地面？

### 096 — `synthetic_scene_056_E2B`

**原始英文指令：** Starting at 27.0 seconds, freeze the visible marina water into a continuous translucent blue-gray ice sheet over four seconds.

**中文翻译：** 从第 27.0 秒开始，在四秒内将码头区可见的水面冻结成连续、半透明的蓝灰色冰层。

**状态：** 接受

**原子化判定句：**

1. 码头区可见的水面是否在 4 秒内冻结成连续冰层？
2. 形成的冰层是否呈半透明的蓝灰色？

### 097 — `synthetic_scene_067_E1`

**原始英文指令：** Starting at 14.0 seconds, change the long concrete trough wall from light gray to muted terracotta over two and a half seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒半内将长混凝土槽壁从浅灰色变为柔和的赤陶色。

**状态：** 接受

**原子化判定句：**

1. 长混凝土槽壁是否在 2.5 秒内从浅灰色变为柔和的赤陶色？

### 098 — `synthetic_scene_078_E2A`

**原始英文指令：** Starting at 35.5 seconds, zoom in smoothly until both brown hoofed animals and the nearby path bend fill the central frame.

**中文翻译：** 从第 35.5 秒开始，平滑地拉近镜头，直到两只棕色有蹄动物和附近道路的弯曲处充满画面中央。

**状态：** 接受

**原子化判定句：**

1. 镜头是否平滑地拉近？
2. 拉近后，两只棕色有蹄动物和附近道路的弯曲处是否充满画面中央？

### 099 — `synthetic_scene_089_E2B`

**原始英文指令：** Starting at 32.0 seconds, transform the complete glacial lake and curved shore scene into a restrained layered gouache painting over three seconds.

**中文翻译：** 从第 32.0 秒开始，在三秒内将完整的冰川湖和弯曲岸线场景转变为色彩克制且具有层次的水粉画。

**状态：** 接受

**原子化判定句：**

1. 完整的冰川湖和弯曲岸线场景是否在 3 秒内转变为色彩克制且具有层次的水粉画？

### 100 — `synthetic_scene_100_E1`

**原始英文指令：** Starting at 14.0 seconds, change the narrow footbridge slabs from pale beige-gray to muted brick red over two and a half seconds.

**中文翻译：** 从第 14.0 秒开始，在两秒半内将狭窄人行桥的桥板从浅米灰色变为柔和的砖红色。

**状态：** 接受

**原子化判定句：**

1. 狭窄人行桥的桥板是否在 2.5 秒内从浅米灰色变为柔和的砖红色？

## 汇总

- 抽样总数：100 条。
- 接受：100 条，其中编号 046 使用单条保底机制。
- 拒绝：0 条。
