---
title: ⚖️ 小便斗裡的蒼蠅、大腦如何解碼視覺資訊、設計 Salience
created: 2026-05-01
modified: 2026-05-07
canonicalPath: 2026/5/1/enoughness-29
issue: 29
---

<!-- SELF-INTRO-START -->

_嗨，我是 [黃樺明](https://huam.ing)，我熱愛 [寫作](https://huam.ing/writing)、[耐力運動](https://www.strava.com/athletes/huaminghuang)、[開發提升生活品質的軟體工具](https://github.com/huaminghuangtw)。Enoughness，剛剛好，是我從 2023 年開始每天練習的生活態度。每週，我會在這份電子報分享三件有趣的事。如果這封信是朋友轉寄給你的，歡迎 [點此訂閱](https://huam.ing/newsletter)。想看看過往內容？[歷年電子報](https://huam.ing/enoughness) 都在這裡。_

<!-- SELF-INTRO-END -->

---

# 1

最近花了一些時間在優化 [這個網站](https://huam.ing) 的前端設計，然後就學到一個英文單字：「[Salience](https://www.google.com/search?q=Salience)」。

中文可以翻成「凸顯」、「顯著」或「突出」。簡單來說，就是讓某個東西在一堆東西裡面特別顯眼、吸引目光。

![](_attachments/5ee42257258bfe204a25d58c42f045d7.png "圖片來源：[Works That Work](https://worksthatwork.com/1/urinal-fly)")

[1990 年代](https://en.wikipedia.org/wiki/Urinal_target)，阿姆斯特丹史基浦機場（[Schiphol Airport](https://www.google.com/maps?q=Schiphol+Airport)）的男廁地板常常被尿濺得到處都是，讓清潔人員非常崩潰。

後來他們想到一個方法：在小便斗裡貼上「蒼蠅」貼紙！

果然，男人看到馬桶裡有東西，就會忍不住想瞄準……這個小巧思，讓地板上的尿直接少了 80%，機場也省下大筆清潔費。

# 2

為了理解人類是如何處理視覺資訊的，兩位神經科學家 [David Hubel](https://www.google.com/search?q=David+Hubel) 和 [Torsten Wiesel](https://www.google.com/search?q=Torsten+Wiesel) 在 1959 年做了一個 [實驗](https://doi.org/10.1113/jphysiol.1959.sp006308)：

他們在貓的 [初級視覺皮質層](https://zh.wikipedia.org/zh-tw/%E8%A7%86%E8%A7%89%E7%9A%AE%E5%B1%82)（Primary Visual Cortex，大腦的視覺解碼中心，簡稱 V1）植入微電極，並在貓的眼前投影不同的光帶，試圖記錄視神經元的放電反應。

![](_attachments/083f4217bbe2d5d628a5e406e9006b18.png "圖片來源：[Devopedia](https://devopedia.org/computer-vision)")

剛開始，無論怎麼切換光帶的大小或位置，V1 幾乎毫無反應。犧牲掉無數隻可愛小貓後 🥲 某天，研究人員在更換幻燈片時，幻燈片邊緣無意間在貓咪眼前劃過，產生一道陰影，並讓神經元突然「啪啪」大響 。

這證實了 V1 是極度專業化的「特徵提取器」：有的負責橫線，有的只對直線有感，有的則對移動的邊緣特別敏感。

在這之前，科學界普遍認為視覺系統類似電視機螢幕，以「逐點（pixel-by-pixel）」、「連續」的方式處理訊號。這個貓實驗讓我們知道，V1 內部既沒有螢幕，也沒有像素的概念，而是將視覺訊號拆解成基本特徵後，再由更高階的視覺皮質層（如 V2、V4 等）進一步整合、辨識，最終才是我們眼睛看見的完整畫面。

這項發現，奠定了後續 AI 領域中「神經網路」（Neural Networks）的基礎，也讓 Hubel 和 Wiesel [在 1981 年獲頒諾貝爾生理醫學獎](https://www.nobelprize.org/prizes/medicine/1981/hubel/facts)。

# 3

Salience 可以藉由不同程度的「對比」來實現，像是顏色、大小、方向、形狀、動態的差異。

![](_attachments/39485bd88e8c484bf9e5c4cfbc166521.png "圖片來源：[Wong, B. Salience. Nat Methods 7, 773 (2010)](https://doi.org/10.1038/nmeth1010-773)")

例如下圖左，A 馬上就能找到，P 卻要找半天。右邊那張圖也是，直角的線條一眼就看到，斜的那根卻要找很久。這就是 Salience 的威力。

![](_attachments/5c32972148bc2b547c5cff899d76ce20.png "圖片來源：[Wong, B. Salience. Nat Methods 7, 773 (2010)](https://doi.org/10.1038/nmeth1010-773)")

賦予意義，也可以創造 Salience。

在 TED 演講中，精神病學家 [Livia De Picker](https://scholar.google.com/citations?user=33dXLnUAAAAJ) 提到：[大腦天生會自動尋找有意義的連結](https://youtu.be/JHqFJwtCmcU?t=4m11s)，加上 [人類有感覺、有情緒](https://youtu.be/JHqFJwtCmcU?t=7m59s)，[讓 AI 再強也比不上人腦「賦予意義」的能力](https://youtu.be/JHqFJwtCmcU?t=14m39s)。

而 [故事就是 Salience 的最佳體現](https://youtu.be/JHqFJwtCmcU?t=13m8s)。因為故事會觸動我們的情感，讓抽象變成具體，讓資訊變得有意義。

[蘋果（Apple）](https://www.apple.com) 是我心目中說故事（Storytelling）的典範。他們的廣告總能喚起觀眾的情感，讓人產生共鳴。

像 [1997 年「Think Different」這支廣告](https://youtu.be/CLIyH2SyxZA)，沒有強調產品規格，而是一連串改變世界的偉人畫面 — 愛因斯坦、甘地、馬丁路德金、畢卡索、愛迪生等 — 搭配 [旁白](https://huam.ing/heres-to-the-crazy-ones-think-different)：「這是給瘋子、叛逆者、麻煩製造者……他們不盲從主流、用自己的角度思考。」

蘋果把品牌和「挑戰現狀、勇於創新」的價值觀綁在一起，讓觀眾感受到：原來選擇蘋果，是一種態度跟信仰。這種情感連結，正是忠誠度的來源，也讓蘋果成為少數擁有死忠粉絲的公司之一。

![](_attachments/1b5e84a5d8bfc0ee343d7e55835a8490.png "圖片來源：[Think Different - Steve Jobs (1997) - Apple](https://youtu.be/CLIyH2SyxZA)")

還有一種手法可以設計 Salience：[留白](https://huam.ing/2026/4/24/enoughness-28/#1)。

刪去不必要的元素，讓重要的內容浮現。

事實上，越簡單越困難。因為簡單的背後，是無數次取捨、打磨，以及 [狠下心砍掉自己的心肝寶貝](https://www.goodreads.com/quotes/371112-kill-your-darlings-kill-your-darlings-even-when-it-breaks)。

要把事情做得簡單，[需要相當程度的努力和狂熱](https://youtu.be/sm1msysj5lw)。

濃縮再濃縮、提煉再提煉。

簡約，是細膩的極致。

— [樺明](https://huam.ing/2026/5/1/enoughness-29)

---

<p align="center">
<sub>
“Nobody counts the number of ads you run; they just remember the impression you make.”
<br>
— Bill Bernbach
</sub>
</p>
