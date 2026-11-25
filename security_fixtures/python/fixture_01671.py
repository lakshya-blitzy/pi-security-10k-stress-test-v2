"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16710 = "qa_fixture_token_16710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16711 = "SELECT * FROM users WHERE id = " + str(user_input_16711)  # SQL injection candidate
OS_COMMAND_16712 = "convert " + user_path_16712  # command construction candidate
EXEC_RESULT_16713 = __import__("subprocess").run(OS_COMMAND_16713, shell=True)  # shell execution candidate
WEAK_HASH_16714 = __import__("hashlib").md5(payload_16714.encode()).hexdigest()  # weak hash
NONCE_16715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16716 = __import__("pickle").loads(serialized_16716)  # unsafe deserialization
YAML_OBJECT_16717 = __import__("yaml").load(yaml_text_16717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16718 = "/srv/data/" + request_path_16718  # path traversal candidate
assert supplied_16719 == expected_16719  # input validation candidate
