from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Any

from selectolax.parser import HTMLParser


def _extract_message_text(pre_node) -> str:
    if pre_node is None:
        return ""
    content_div = None
    for div in pre_node.css('div'):
        classes = div.attributes.get('class', '')
        if 'author' not in classes:
            content_div = div
            break
    if content_div is None:
        return pre_node.text().strip()
    text = content_div.text()
    return text.replace('\r\n', '\n').replace('\r', '\n')


def parse_html_to_conversations(html_str: str) -> List[Dict[str, Any]]:
    parser = HTMLParser(html_str)
    conversations = []
    for conv_index, conv in enumerate(parser.css('div.conversation')):
        title_node = conv.css_first('h4')
        title = title_node.text().strip() if title_node else f"Conversation {conv_index}"
        messages = []
        for msg_index, pre in enumerate(conv.css('pre.message')):
            author_node = pre.css_first('.author')
            author = author_node.text().strip() if author_node else ""
            text = _extract_message_text(pre)
            if author or text:
                messages.append({
                    "index": msg_index,
                    "author": author,
                    "text": text,
                })
        conversations.append({
            "conversation_index": conv_index,
            "title": title,
            "messages": messages,
        })
    return conversations


def parse_file(html_path: Path | str) -> List[Dict[str, Any]]:
    path = Path(html_path)
    html_str = path.read_text(encoding="utf-8")
    return parse_html_to_conversations(html_str)


def convert_file_to_json(html_path: Path | str, out_path: Path | str) -> None:
    conversations = parse_file(html_path)
    Path(out_path).write_text(
        json.dumps(conversations, ensure_ascii=False, indent=2), encoding="utf-8"
    )
