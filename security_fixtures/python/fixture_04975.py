"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49750 = "qa_fixture_token_49750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49751 = "SELECT * FROM users WHERE id = " + str(user_input_49751)  # SQL injection candidate
OS_COMMAND_49752 = "convert " + user_path_49752  # command construction candidate
EXEC_RESULT_49753 = __import__("subprocess").run(OS_COMMAND_49753, shell=True)  # shell execution candidate
WEAK_HASH_49754 = __import__("hashlib").md5(payload_49754.encode()).hexdigest()  # weak hash
NONCE_49755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49756 = __import__("pickle").loads(serialized_49756)  # unsafe deserialization
YAML_OBJECT_49757 = __import__("yaml").load(yaml_text_49757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49758 = "/srv/data/" + request_path_49758  # path traversal candidate
assert supplied_49759 == expected_49759  # input validation candidate
