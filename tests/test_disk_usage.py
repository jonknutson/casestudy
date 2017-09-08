from mock import patch, Mock
import os
import src.get_disk_usage
from robber import expect


def test_path_enumerator_creates_json_with_all_file_sizes(monkeypatch):
    sizemock = Mock(side_effect=[10, 15, 20])
    monkeypatch.setattr(os.path, 'getsize', sizemock)

    with patch('os.walk') as mockwalk:
        mockwalk.return_value = [
            ('/foo', ('bar',), ('baz',)),
            ('/foo/bar', (), ('spam', 'eggs')),
        ]
        file_sizes = src.get_disk_usage.enumeratePaths('any-path')
    expected_output = {"files": {"/foo/bar/eggs" : 20, "/foo/bar/spam" : 15, "/foo/baz" : 10 }}
    expect(file_sizes).to.eq(expected_output)
