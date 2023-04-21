import sys
from datetime import datetime
from time import sleep

import nfc


def sc_from_raw(sc):
    return nfc.tag.tt3.ServiceCode(sc >> 6, sc & 0x3F)


# def on_startup(tag):
#     print ("[*] startup:", tag)


def on_connect(tag):
    try:
        if isinstance(tag, nfc.tag.tt3.Type3Tag):
            try:
                sc1 = sc_from_raw(0x200B)
                bc1 = nfc.tag.tt3.BlockCode(0, service=0)
                block_data = tag.read_without_encryption([sc1], [bc1])
                card_id = block_data[0:8].decode("utf-8")
                if card_id[0] == "0":
                    card_id = card_id[1:]
                dt_now = datetime.now()
                print(str(dt_now))
                print(f"ID: {card_id}")
                print("準備中...")
                sleep(1)
                print("準備完了")
            except Exception as e:
                print("Error: 学生証・職員証ではありません")
                print("準備中...")
                sleep(1)
                print("準備完了")
        else:
            print("Error: 学生証・職員証ではありません")
            print("準備中...")
            print("準備完了")
    except Exception as e:
        print(f"Error: {e}")
        print("準備中...")
        print("準備完了")


# def on_release(tag):
#     print ("[*] released:", tag)


def main(args):
    print("準備完了")
    with nfc.ContactlessFrontend("usb") as clf:
        while clf.connect(
            rdwr={
                # 'on-startup': on_startup,
                "on-connect": on_connect,
                # 'on-release': on_release,
            }
        ):
            pass


if __name__ == "__main__":
    main(sys.argv)
