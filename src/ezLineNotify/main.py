import requests
from io import BytesIO
from PIL import Image as PILImage
from typing import Union

class UnknownSourceType(Exception):
    pass

class UnknownImageType(Exception):
    pass

class ImageURLs:
    def __init__(self, thumbnail_url: str, fullsize_url: str) -> None:
        self.__thumbnail_url, self.__fullsize_url = thumbnail_url, fullsize_url
    
    def get_info(self) -> tuple[str, str]:
        return self.__thumbnail_url, self.__fullsize_url

class Image:
    def __init__(self, source: Union[str, PILImage.Image]) -> None:
        self.__file_stream = BytesIO()
        if type(source) == str:
            pil_img = PILImage.open(source, mode="r")
            if not pil_img.mode == "RGB":
                pil_img = pil_img.convert("RGB")
            pil_img.save(self.__file_stream, format="JPEG")
            pil_img.close()
        elif type(source) == PILImage.Image:
            if not source.mode == "RGB":
                pil_img = source.convert("RGB")
            pil_img.save(self.__file_stream, format="JPEG")
        else:
            raise UnknownSourceType("Pillowがサポートしている画像ファイルへのパスかPillowのImageクラスのインスタンスをsourceに指定してください")
        self.__file_stream.seek(0)

    def get_file_stream(self) -> BytesIO:
        return self.__file_stream

class Sticker:
    """
    スタンプのパッケージIDやIDはこちらから確認可能: https://developers.line.biz/ja/docs/messaging-api/sticker-list/
    """

    def __init__(self, package_id: int, id: int) -> None:
        self.__package_id, self.__id = package_id, id
    
    def get_info(self) -> tuple[str, str]:
        return str(self.__package_id), str(self.__id)

class LineNotify:
    def __init__(self, token: str, endpoint: str = "https://notify-api.line.me/api") -> None:
        self.__token = token
        self.__endpoint = endpoint
    
    def send(self, text: str, image: Union[ImageURLs, Image] = None, sticker: Sticker = None, silent: bool = False) -> None:
        uri = f"{self.__endpoint}/notify"
        headers = {"Authorization": f"Bearer {self.__token}"}
        data = {"message": text}

        files = None
        if image:
            if type(image) == ImageURLs:
                data["imageThumbnail"], data["imageFullsize"] = image.get_info()
            elif type(image) == Image:
                files = {"imageFile": image.get_file_stream()}
            else:
                raise UnknownImageType("ImageURLsかImageのインスタンス以外がimageに指定されました")

        if sticker:
            data["stickerPackageId"], data["stickerId"] = sticker.get_info()

        if silent:
            data["notificationDisabled"] = True

        requests.post(uri, headers=headers, data=data, files=files)