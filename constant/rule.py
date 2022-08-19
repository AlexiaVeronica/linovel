class XbookbenRule:
    book_img = '/html/body/div/div[2]/div/div/div[1]/span/img/@src'
    book_name = '/html/body/div/div[2]/div/div/div[2]/h1/text()'
    book_author = '/html/body/div/div[2]/div/div/div[2]/p/strong[1]/span/text()'
    chapter_url_list = '//*[@id="chapterList"]/li/a/@href'
    book_state = '/html/body/div/div[2]/div/div/div[2]/p/strong[3]/span/text()'
    book_label = '/html/body/div/div[2]/div/div/div[2]/p/strong[2]/span/text()'
    last_chapter_title = '//*[@id="Contents"]/div[1]/p/a/text()'
    book_words = '/html/body/div/div[2]/div/div/div[2]/p/strong[4]/span/text()'
    book_update_time = '//*[@id="Contents"]/div[1]/p/small/text()'
    chapter_title = '//*[@id="mlfy_main_text"]/h1/text()'
    chapter_content = '//*[@id="TextContent"]'

    # chapter_cover = ''
    class Search:
        book_name = '//*[@id="hism"]/a/img/@alt'
        book_img = '//*[@id="hism"]/a/img/@src'
        book_id = '//*[@id="hism"]/h3/a/@href'


class DingdianRule:
    book_img = '//*[@id="fmimg"]/img/@src'
    book_name = '//*[@id="info"]/h1/text()'
    book_author = '//*[@id="info"]/p[1]/text()'
    chapter_url_list = '//*[@id="list"]/dl/dd[*]/a/@href'
    book_state = '//*[@id="intro"]/p'  # 没有这个信息
    book_label = '//*[@id="wrapper"]/div[4]/div[1]/text()'
    last_chapter_title = '//*[@id="list"]/dl/dd[1]/a/text()'
    book_words = '//*[@id="intro"]/p'  # 没有这个信息
    book_update_time = '//*[@id="info"]/p[3]/text()'
    chapter_title = '//div[@class="bookname"]/h1/text()'
    chapter_content = '//*[@id="content"]/text()'
    # chapter_cover = ''


class LinovelRule:
    book_img = '//div[@class="book-cover"]/a/@href'
    book_name = '//h1[@class="book-title"]/text()'
    book_author = '//div[@class="author-frame"]//a/text()'
    chapter_url_list = '//div[@class="chapter"]/a/@href'
    book_state = '/html/body/div[3]/div[2]/div[1]/div[2]/div[3]/span[7]/text()'
    book_label = '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/a[1]/text()'
    last_chapter_title = '/html/body/div[3]/div[2]/div[1]/div[5]/div[2]/div[3]/div[2]'
    book_words = '/html/body/div[3]/div[2]/div[1]/div[2]/div[3]/span[1]/text()'
    book_update_time = '/html/body/div[3]/div[2]/div[1]/div[5]/div[2]/div[3]/div[2]/div[1]/small/text()'
    chapter_title = '//div[@class="article-title"]/text()'
    chapter_content = '//div[@class="article-text"]/p'

    # chapter_cover = ''
    class Search:
        book_name = '/html/body/div[4]/div[3]/div[1]/a/div/div/img/@alt'
        book_img = '/html/body/div[4]/div[3]/div[1]/a/div/div/img/@src'
        book_id = '/html/body/div[4]/div[3]/div[1]/a/@href'


class BoluobaoRule:
    book_img = '//div[@class="book-cover"]/a/@href'
    book_name = '//h1[@class="book-title"]/text()'
    book_author = '//div[@class="author-frame"]//a/text()'
    chapter_url_list = '//div[@class="chapter"]/a/@href'
    book_state = '/html/body/div[3]/div[2]/div[1]/div[2]/div[3]/span[7]/text()'
    book_label = '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/a[1]/text()'
    last_chapter_title = '/html/body/div[3]/div[2]/div[1]/div[5]/div[2]/div[3]/div[2]'
    book_words = '/html/body/div[3]/div[2]/div[1]/div[2]/div[3]/span[1]/text()'
    book_update_time = '/html/body/div[3]/div[2]/div[1]/div[5]/div[2]/div[3]/div[2]/div[1]/small/text()'
    chapter_title = '//div[@class="article-title"]/text()'
    chapter_content = '//div[@class="article-text"]/p'

    # chapter_cover = ''
    class Search:
        book_name = '/html/body/div[4]/div[3]/div[1]/a/div/div/img/@alt'
        book_img = '/html/body/div[4]/div[3]/div[1]/a/div/div/img/@src'
        book_id = '/html/body/div[4]/div[3]/div[1]/a/@href'