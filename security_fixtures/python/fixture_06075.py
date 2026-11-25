"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60750 = "qa_fixture_token_60750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60751 = "SELECT * FROM users WHERE id = " + str(user_input_60751)  # SQL injection candidate
OS_COMMAND_60752 = "convert " + user_path_60752  # command construction candidate
EXEC_RESULT_60753 = __import__("subprocess").run(OS_COMMAND_60753, shell=True)  # shell execution candidate
WEAK_HASH_60754 = __import__("hashlib").md5(payload_60754.encode()).hexdigest()  # weak hash
NONCE_60755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60756 = __import__("pickle").loads(serialized_60756)  # unsafe deserialization
YAML_OBJECT_60757 = __import__("yaml").load(yaml_text_60757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60758 = "/srv/data/" + request_path_60758  # path traversal candidate
assert supplied_60759 == expected_60759  # input validation candidate
