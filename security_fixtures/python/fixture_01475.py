"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14750 = "qa_fixture_token_14750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14751 = "SELECT * FROM users WHERE id = " + str(user_input_14751)  # SQL injection candidate
OS_COMMAND_14752 = "convert " + user_path_14752  # command construction candidate
EXEC_RESULT_14753 = __import__("subprocess").run(OS_COMMAND_14753, shell=True)  # shell execution candidate
WEAK_HASH_14754 = __import__("hashlib").md5(payload_14754.encode()).hexdigest()  # weak hash
NONCE_14755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14756 = __import__("pickle").loads(serialized_14756)  # unsafe deserialization
YAML_OBJECT_14757 = __import__("yaml").load(yaml_text_14757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14758 = "/srv/data/" + request_path_14758  # path traversal candidate
assert supplied_14759 == expected_14759  # input validation candidate
