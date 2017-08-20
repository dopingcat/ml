import random
import json

typeList = ['t', 'ti', 'tu', 'tiu', 'tb', 'tib', 'tiub']

class DummyResult:
    def __init__(self):
        # res_type
        self.res_type = random.choice(typeList)

        # dialog
        self.dialogNode = "root"
        self.dialogRequestCounter = "1"

        # text
        if self.res_type.count("t") > 0:
            self.text = "This is dummy text value"

        # photo
        if self.res_type.count("i") > 0:
            self.photo_url = "https://photo.src"
            self.width = "640"
            self.height = "480"

        # url
        if self.res_type.count("u") > 0:
            self.label = "주유 쿠폰받기"
            self.url = "https://coupon/url"

        # buttons
        if self.res_type.count("b") > 0:
            keyboardType = "buttons"

            buttons = []
            buttons.append("처음으로")
            buttons.append("다시 등록하기")
            buttons.append("취소하기")

            self.type = keyboardType
            self.buttons = buttons

    def __str__(self):
        strResult = {}
        strResult["res_type"] = self.res_type

        strResult["dialogNode"] = self.dialogNode
        strResult["dialogRequestCounter"] = self.dialogRequestCounter

        if self.res_type.count("t") > 0:
            strResult["text"] = self.text

        if self.res_type.count("i") > 0:
            strResult["photo_url"] = self.photo_url
            strResult["width"] = self.width
            strResult["height"] = self.height

        if self.res_type.count("u") > 0:
            strResult["label"] = self.label
            strResult["url"] = self.url

        if self.res_type.count("b") > 0:
            strResult["type"] = self.type
            strResult["buttons"] = self.buttons

        return str(strResult)





def responseJsonBuild(resultSet):
    dicResultResponse = {}

    # res_type
    dicResultResponse["res_type"] = resultSet.res_type

    # build message
    message = {}

    if resultSet.res_type.count("t") > 0 :
        message["text"] = resultSet.text

    if resultSet.res_type.count("i") > 0 :
        photo = {}
        photo["url"] = resultSet.photo_url
        photo["width"] = resultSet.width
        photo["height"] = resultSet.height

        message["photo"] = photo

    if resultSet.res_type.count("u") > 0 :
        message_button = {}
        message_button["label"] = resultSet.label
        message_button["url"] = resultSet.url

        message["message_button"] = message_button

    dicResultResponse["message"] = message

    if resultSet.res_type.count("b") > 0 :
        keyboard = {}
        keyboard["type"] = resultSet.type
        keyboard["buttons"] = resultSet.buttons

        dicResultResponse["keyboard"] = keyboard

    # dialog
    dialog = {}
    dialog["dialogNode"] = resultSet.dialogNode
    dialog["dialogRequestCounter"] = resultSet.dialogRequestCounter
    
    dicResultResponse["dialog"] = dialog

    return dicResultResponse

# print("result = ", type(answerBuild()), answerBuild())
# print("result to json = ", type(json.dumps(answerBuild())), json.dumps(answerBuild()))

for i in range(1, 11) :
    result = DummyResult()
    # print(type(responseJsonBuild(result)))
    print(responseJsonBuild(result))
    print('')