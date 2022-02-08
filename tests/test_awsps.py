"""AWS profile switcher tests."""
import awsps


def test_profile_reader(monkeypatch, tmp_path):
    """Test profile reader default."""
    fake_get_path_called = 0

    def fake_get_path():
        nonlocal fake_get_path_called
        fake_get_path_called += 1
        return tmp_path

    monkeypatch.setattr(awsps, "get_path", fake_get_path)

    aws_config_file = tmp_path / "config"
    aws_config_file.write_text(
        """[default]
    region=us-west-2
    output=json
    """
    )

    assert awsps.profile_reader() == ["default"]
    assert fake_get_path_called == 1
