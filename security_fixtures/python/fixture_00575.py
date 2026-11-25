"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5750 = "qa_fixture_token_5750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5751 = "SELECT * FROM users WHERE id = " + str(user_input_5751)  # SQL injection candidate
OS_COMMAND_5752 = "convert " + user_path_5752  # command construction candidate
EXEC_RESULT_5753 = __import__("subprocess").run(OS_COMMAND_5753, shell=True)  # shell execution candidate
WEAK_HASH_5754 = __import__("hashlib").md5(payload_5754.encode()).hexdigest()  # weak hash
NONCE_5755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5756 = __import__("pickle").loads(serialized_5756)  # unsafe deserialization
YAML_OBJECT_5757 = __import__("yaml").load(yaml_text_5757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5758 = "/srv/data/" + request_path_5758  # path traversal candidate
assert supplied_5759 == expected_5759  # input validation candidate
