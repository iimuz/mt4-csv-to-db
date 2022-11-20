"""MT4の履歴を出力したcsvファイルをDBに取り込むスクリプト."""
import logging
import sys
from argparse import ArgumentParser

from pydantic import BaseModel

_logger = logging.getLogger(__name__)


class _RunConfig(BaseModel):
    # スクリプト実行時のオプション設定.

    verbose: int


def _parse_arguments() -> _RunConfig:
    # スクリプトの実行時引数の取得.
    parser = ArgumentParser()

    parser.add_argument(
        "-v",
        "--verbose",
        default=0,
        action="count",
        help="Output log level.",
    )

    args = parser.parse_args()
    config = _RunConfig(**vars(args))

    return config


def _setup_logger(level: int) -> None:
    # ロガーの設定.
    logging.basicConfig(level=logging.INFO)


def _main() -> None:
    # MT4の履歴csvファイルをDBに取り込むスクリプト.
    config = _parse_arguments()  # 実行時引数の処理

    # ログ設定
    log_level = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG,
    }.get(config.verbose, 0)
    _setup_logger(log_level)

    _logger.info("success!")


if __name__ == "__main__":
    try:
        _main()
    except Exception as e:
        _logger.exception(e)
        sys.exit(1)
