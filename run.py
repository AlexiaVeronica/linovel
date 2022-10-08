import argparse
import book
import constant
from src import *
from config import *


def init_config_book_source():
    import json
    book_source_path = "./book_source/{}.json".format(Vars.current_book_type.split(".")[-2])
    if os.path.exists(book_source_path):
        book_source = json.loads(open(book_source_path, "r", encoding="utf-8").read())
        Vars.current_book_rul_rule = book_source.get("url")
        Vars.current_book_api = API.Response
        Vars.current_book_rule = constant.rule.NovelRule(book_source.get("data"))
        print("下载源已设置为: {}".format(Vars.current_book_type))
    else:
        print("[error] book source not found, please check your book type, book type:", Vars.current_book_type)


def set_up_app_type(current_book_type):  # set up app type and book type
    if Msg.book_type_dict.get(current_book_type):
        Vars.current_book_type = Msg.book_type_dict.get(current_book_type)
        init_config_book_source()
        if Vars.current_book_type in Msg.gbk_book_type:
            Vars.current_book_gbk = True
        else:
            Vars.current_book_gbk = False
        if current_book_type == "5" or current_book_type == "6":
            print("index:1\t\t常规小说\nindex:2\t\t同人小说")
            Vars.current_book_classify_name = {"1": "changgui", "2": "tongren"}.get(
                get("please input your classify index:").strip()
            )

    else:
        print("[error] book type not found, please input again", current_book_type)
        for index, book_type in Msg.book_type_dict.items():
            print("index:", index, "\t\tbook type:", book_type)
        print("please input index to select book type, example: 0")
        set_up_app_type(get(">"))


def parse_args_command() -> argparse.Namespace:
    update_config()  # update config file if necessary (for example, add new token)
    parser = argparse.ArgumentParser(description='Downloader for Linovel and Dingdian')
    # parser.add_argument('-u', '--update', help='update config file', action="store_true")
    parser.add_argument('-s', '--search', default=None, nargs=1, help='search book')
    parser.add_argument('-i', '--bookid', default=None, nargs=1, help='download book by book id')
    parser.add_argument('-d', '--download', default=None, nargs=1, help='download book by book id')
    parser.add_argument('-n', '--name', default=None, help='download book by name')
    parser.add_argument('-a', '--app', help='run as app', nargs=1, default=None)
    return parser.parse_args()


def shell_console(inputs: list):
    if inputs[0] == "d" or inputs[0] == "download":
        Vars.current_book = init_book_info_template(inputs[1])
        if Vars.current_book and Vars.current_book.get("bookName") is not None:
            Vars.current_book = book.BookConfig(Vars.current_book)
            Vars.current_book.init_content_config()
            Vars.current_book.multi_thread_download_book()
        else:
            print("download error,please  check your input app name or book id")
    elif inputs[0] == "s" or inputs[0] == "search":
        response = Vars.current_book_api.get_book_info_by_keyword(inputs[1]) if len(inputs) >= 2 else []
        if len(response) > 0:
            for index, i in enumerate(response):
                print("index", index, "\t\tbook name:", i[0])
            print("please input index to download book, example: 0")
            while True:
                index = get(">").strip()
                if index == "q" or index == "quit":
                    break
                if index.isdigit() and int(index) < len(response):
                    book_id = re.findall(r"(\d+)", response[int(index)][1])[0]
                    shell_console(["d", book_id])
                else:
                    print("[error] index not found")
        else:
            print("[warning] search result is empty, search keyword:", inputs[1])
    else:
        print(inputs[0], "command not found, please input again")


if __name__ == '__main__':
    args_command = parse_args_command()
    set_up_app_type(args_command.app[0]) if args_command.app else set_up_app_type("")

    if args_command.bookid is not None and args_command.bookid != "":
        shell_console(["d", args_command.bookid[0]])

    elif args_command.download is not None and args_command.download != "":
        shell_console(["d", args_command.download[0]])

    elif args_command.search is not None and args_command.search != "":
        shell_console(["s", args_command.search[0]])
    else:
        print("Welcome to use downloader, please input command")
        while True:
            shell_console(get(">").strip().split(" "))

    # def input_index():
    #     try:
    #         index = int(input())
    #         if index < len(response):
    #             Vars.current_book = book.Book(response[index])
    #             Vars.current_book.init_content_config()
    #             Vars.current_book.multi_thread_download_book()
    #         else:
    #             print("[error] index out of range, please input again")
    #             input_index()
    #     except ValueError:
    #         print("[error] please input number")
    #         input_index()
