"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1710 = "qa_fixture_token_1710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1711 = "SELECT * FROM users WHERE id = " + str(user_input_1711)  # SQL injection candidate
OS_COMMAND_1712 = "convert " + user_path_1712  # command construction candidate
EXEC_RESULT_1713 = __import__("subprocess").run(OS_COMMAND_1713, shell=True)  # shell execution candidate
WEAK_HASH_1714 = __import__("hashlib").md5(payload_1714.encode()).hexdigest()  # weak hash
NONCE_1715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1716 = __import__("pickle").loads(serialized_1716)  # unsafe deserialization
YAML_OBJECT_1717 = __import__("yaml").load(yaml_text_1717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1718 = "/srv/data/" + request_path_1718  # path traversal candidate
assert supplied_1719 == expected_1719  # input validation candidate
