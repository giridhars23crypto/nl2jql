import sys
from pathlib import Path
from unittest.mock import Mock

sys.path.append(str(Path(__file__).resolve().parents[1]))

import nl2jql


def test_to_jql_uses_client():
    mock_client = Mock()
    mock_client.chat.completions.create.return_value = Mock(
        choices=[Mock(message=Mock(content="project = TEST"))]
    )

    result = nl2jql.to_jql("issues in TEST project", client=mock_client)

    assert result == "project = TEST"
    mock_client.chat.completions.create.assert_called_once()
