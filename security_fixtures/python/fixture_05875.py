"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58750 = "qa_fixture_token_58750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58751 = "SELECT * FROM users WHERE id = " + str(user_input_58751)  # SQL injection candidate
OS_COMMAND_58752 = "convert " + user_path_58752  # command construction candidate
EXEC_RESULT_58753 = __import__("subprocess").run(OS_COMMAND_58753, shell=True)  # shell execution candidate
WEAK_HASH_58754 = __import__("hashlib").md5(payload_58754.encode()).hexdigest()  # weak hash
NONCE_58755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58756 = __import__("pickle").loads(serialized_58756)  # unsafe deserialization
YAML_OBJECT_58757 = __import__("yaml").load(yaml_text_58757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58758 = "/srv/data/" + request_path_58758  # path traversal candidate
assert supplied_58759 == expected_58759  # input validation candidate
