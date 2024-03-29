def decode_content_text(content_text: str):
    return content_text.replace("    ", "<p>"). \
        replace("<p>\n</p>", "\n").\
        replace("<p> </p>", "\n"). \
        replace("<p></p>", "\n").\
        replace("", "\u7684"). \
        replace("", "\u4e00"). \
        replace("", "\u662f"). \
        replace("", "\u4e86"). \
        replace("", "\u6211"). \
        replace("", "\u4e0d"). \
        replace("", "\u4eba"). \
        replace("", "\u5728"). \
        replace("", "\u4ed6"). \
        replace("", "\u6709"). \
        replace("", "\u8fd9"). \
        replace("", "\u4e2a"). \
        replace("", "\u4e0a"). \
        replace("", "\u4eec"). \
        replace("", "\u6765"). \
        replace("", "\u5230"). \
        replace("", "\u65f6"). \
        replace("", "\u5927"). \
        replace("", "\u5730"). \
        replace("", "\u4e3a"). \
        replace("", "\u5b50"). \
        replace("", "\u4e2d"). \
        replace("", "\u4f60"). \
        replace("", "\u8bf4"). \
        replace("", "\u751f"). \
        replace("", "\u56fd"). \
        replace("", "\u5e74"). \
        replace("", "\u7740"). \
        replace("", "\u5c31"). \
        replace("", "\u90a3"). \
        replace("", "\u548c"). \
        replace("", "\u8981"). \
        replace("", "\u5979"). \
        replace("", "\u51fa"). \
        replace("", "\u4e5f"). \
        replace("", "\u5f97"). \
        replace("", "\u91cc"). \
        replace("", "\u540e"). \
        replace("", "\u81ea"). \
        replace("", "\u4ee5"). \
        replace("", "\u4f1a"). \
        replace("", "\u5bb6"). \
        replace("", "\u53ef"). \
        replace("", "\u4e0b"). \
        replace("", "\u800c"). \
        replace("", "\u8fc7"). \
        replace("", "\u5929"). \
        replace("", "\u53bb"). \
        replace("", "\u80fd"). \
        replace("", "\u5bf9"). \
        replace("", "\u5c0f"). \
        replace("", "\u591a"). \
        replace("", "\u7136"). \
        replace("", "\u4e8e"). \
        replace("", "\u5fc3"). \
        replace("", "\u5b66"). \
        replace("", "\u4e48"). \
        replace("", "\u4e4b"). \
        replace("", "\u90fd"). \
        replace("", "\u597d"). \
        replace("", "\u770b"). \
        replace("", "\u8d77"). \
        replace("", "\u53d1"). \
        replace("", "\u5f53"). \
        replace("", "\u6ca1"). \
        replace("", "\u6210"). \
        replace("", "\u53ea"). \
        replace("", "\u5982"). \
        replace("", "\u4e8b"). \
        replace("", "\u628a"). \
        replace("", "\u8fd8"). \
        replace("", "\u7528"). \
        replace("", "\u7b2c"). \
        replace("", "\u6837"). \
        replace("", "\u9053"). \
        replace("", "\u60f3"). \
        replace("", "\u4f5c"). \
        replace("", "\u79cd"). \
        replace("", "\u5f00"). \
        replace("", "\u7f8e"). \
        replace("", "\u4e73"). \
        replace("", "\u9634"). \
        replace("", "\u6db2"). \
        replace("", "\u830e"). \
        replace("", "\u6b32"). \
        replace("", "\u547b"). \
        replace("", "\u8089"). \
        replace("", "\u4ea4"). \
        replace("", "\u6027"). \
        replace("", "\u80f8"). \
        replace("", "\u79c1"). \
        replace("", "\u7a74"). \
        replace("", "\u6deb"). \
        replace("", "\u81c0"). \
        replace("", "\u8214"). \
        replace("", "\u5c04"). \
        replace("", "\u8131"). \
        replace("", "\u88f8"). \
        replace("", "\u9a9a"). \
        replace("", "\u5507")

# content = """我莉娜莉亚同的历史探访旅尚未结束。\\n虽说是我莉娜莉亚同，不真说，在我的认知中比较偏向我陪莉娜莉亚同处跑。\\n「妳尊雕像，真帅气。」\\n
# 我的伙伴莉娜莉亚同「呵呵呵呵」露诡异的笑容，脸颊摩蹭一尊平凡无奇的雕像。究竟哪爱我完全不明白。\\n「是什？我搞不太懂的说。」\\n
# 「问。伟的魔女曾说『钱花完了……了，就诈骗一点钱吧。』莫名其妙的话，引骗走城镇居民钱财的件喔。
# 的市长说『了永远记乱的魔女，就做一尊的雕像吧。』才尊雕像陈列在城镇博物馆中。简言，尊雕像与其说是纪念伟的人物，
# 比较像是公羞辱呢。雕像非常难一见喔。」\\n原此原此。\\n「不意思我是听不懂哪帅气的说。」\\n「妳应该历史更有兴趣一点。」\\n
# 「莉娜莉亚同应该更有一般常识一点。」\\n「礼貌，我有。」磨蹭磨蹭磨蹭磨蹭。「听了，爱露堤？遇见罕见雕像的机不喔？」\\n「说的确错。」
# \\n「说不定再不了。」\\n「说是。」\\n「妳不觉是错磨蹭的机，就再办法磨蹭了吗？」\\n「不意思唯有妳最一句话我怎听听不懂……」妳不觉吗？
# 头啦……\\n「不论何，我的意思就是脸磨蹭传说中的雕像是很的经验。妳试试吧？」\\n「不了，恕我婉拒。」\\n「不客气。」\\n「不是，我不是在客气──」话说追根究柢，在那前。「莉娜莉亚同，那禁止进入的说……」\\n「
# ？」莉娜莉亚爱侧了侧脑袋。的周围被围篱仔细区分，摆了「禁止进入，请不触摸雕像」的警告标语。莉娜莉亚就是在那头磨蹭雕像。\\n「──喂～～～～～！妳伙！搞什啊！」理所，不守规矩的莉娜莉亚同马就被警卫抓了。\\n「……咦？那、那……」
# 莉娜莉亚同瞪双眼，我投求助的眼神。是我悄悄眼睛别，说了一句：\\n「……那，算是不错的经验吧……」\\n【首次刊登】九集　GAMERS购书附录\\n【者评语】
# \\n我隐约记像在哪提，爱露堤与莉娜莉亚的故初原本预定写与《魔女旅》毫无关联的新，不知什就收进本篇了。不就故间轴说，我见伊蕾娜长的世界很不错。话虽此，我希望未写原本预定写的故。（望向版社)"""
# print(decode_content_text(content))
