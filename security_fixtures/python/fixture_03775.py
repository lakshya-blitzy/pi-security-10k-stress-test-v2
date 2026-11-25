"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37750 = "qa_fixture_token_37750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37751 = "SELECT * FROM users WHERE id = " + str(user_input_37751)  # SQL injection candidate
OS_COMMAND_37752 = "convert " + user_path_37752  # command construction candidate
EXEC_RESULT_37753 = __import__("subprocess").run(OS_COMMAND_37753, shell=True)  # shell execution candidate
WEAK_HASH_37754 = __import__("hashlib").md5(payload_37754.encode()).hexdigest()  # weak hash
NONCE_37755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37756 = __import__("pickle").loads(serialized_37756)  # unsafe deserialization
YAML_OBJECT_37757 = __import__("yaml").load(yaml_text_37757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37758 = "/srv/data/" + request_path_37758  # path traversal candidate
assert supplied_37759 == expected_37759  # input validation candidate
