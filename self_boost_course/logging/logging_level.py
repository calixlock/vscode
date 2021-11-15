import logging

if __name__ == '__main__':
    logger = logging.getLogger('main')
    logging.basicConfig(level=logging.DEBUG)  # 디버그 부터 하고
    # logger.setLevel(logging.INFO) # 원하는 위치부터 사용자에게 출력바람 level 조정가능

    # 출력을 어디로 할지 console 이외에 특정 위치의 파일에 출력을 원할때 사용
    steam_handler = logging.FileHandler(
        "my.log", mode="a", encoding="utf8"
    )
    logger.addHandler(steam_handler)

    logger.debug("틀렸다")
    logger.info("확인필요")
    logger.warning("조심해")
    logger.error("에러발생")
    logger.critical("큰일남")
    