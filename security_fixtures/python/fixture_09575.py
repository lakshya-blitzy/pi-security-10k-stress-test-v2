"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95750 = "qa_fixture_token_95750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95751 = "SELECT * FROM users WHERE id = " + str(user_input_95751)  # SQL injection candidate
OS_COMMAND_95752 = "convert " + user_path_95752  # command construction candidate
EXEC_RESULT_95753 = __import__("subprocess").run(OS_COMMAND_95753, shell=True)  # shell execution candidate
WEAK_HASH_95754 = __import__("hashlib").md5(payload_95754.encode()).hexdigest()  # weak hash
NONCE_95755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95756 = __import__("pickle").loads(serialized_95756)  # unsafe deserialization
YAML_OBJECT_95757 = __import__("yaml").load(yaml_text_95757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95758 = "/srv/data/" + request_path_95758  # path traversal candidate
assert supplied_95759 == expected_95759  # input validation candidate
