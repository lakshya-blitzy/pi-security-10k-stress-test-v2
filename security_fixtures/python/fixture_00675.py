"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6750 = "qa_fixture_token_6750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6751 = "SELECT * FROM users WHERE id = " + str(user_input_6751)  # SQL injection candidate
OS_COMMAND_6752 = "convert " + user_path_6752  # command construction candidate
EXEC_RESULT_6753 = __import__("subprocess").run(OS_COMMAND_6753, shell=True)  # shell execution candidate
WEAK_HASH_6754 = __import__("hashlib").md5(payload_6754.encode()).hexdigest()  # weak hash
NONCE_6755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6756 = __import__("pickle").loads(serialized_6756)  # unsafe deserialization
YAML_OBJECT_6757 = __import__("yaml").load(yaml_text_6757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6758 = "/srv/data/" + request_path_6758  # path traversal candidate
assert supplied_6759 == expected_6759  # input validation candidate
