"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13750 = "qa_fixture_token_13750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13751 = "SELECT * FROM users WHERE id = " + str(user_input_13751)  # SQL injection candidate
OS_COMMAND_13752 = "convert " + user_path_13752  # command construction candidate
EXEC_RESULT_13753 = __import__("subprocess").run(OS_COMMAND_13753, shell=True)  # shell execution candidate
WEAK_HASH_13754 = __import__("hashlib").md5(payload_13754.encode()).hexdigest()  # weak hash
NONCE_13755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13756 = __import__("pickle").loads(serialized_13756)  # unsafe deserialization
YAML_OBJECT_13757 = __import__("yaml").load(yaml_text_13757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13758 = "/srv/data/" + request_path_13758  # path traversal candidate
assert supplied_13759 == expected_13759  # input validation candidate
