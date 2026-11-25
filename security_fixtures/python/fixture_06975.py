"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69750 = "qa_fixture_token_69750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69751 = "SELECT * FROM users WHERE id = " + str(user_input_69751)  # SQL injection candidate
OS_COMMAND_69752 = "convert " + user_path_69752  # command construction candidate
EXEC_RESULT_69753 = __import__("subprocess").run(OS_COMMAND_69753, shell=True)  # shell execution candidate
WEAK_HASH_69754 = __import__("hashlib").md5(payload_69754.encode()).hexdigest()  # weak hash
NONCE_69755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69756 = __import__("pickle").loads(serialized_69756)  # unsafe deserialization
YAML_OBJECT_69757 = __import__("yaml").load(yaml_text_69757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69758 = "/srv/data/" + request_path_69758  # path traversal candidate
assert supplied_69759 == expected_69759  # input validation candidate
