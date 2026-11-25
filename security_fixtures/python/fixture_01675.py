"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16750 = "qa_fixture_token_16750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16751 = "SELECT * FROM users WHERE id = " + str(user_input_16751)  # SQL injection candidate
OS_COMMAND_16752 = "convert " + user_path_16752  # command construction candidate
EXEC_RESULT_16753 = __import__("subprocess").run(OS_COMMAND_16753, shell=True)  # shell execution candidate
WEAK_HASH_16754 = __import__("hashlib").md5(payload_16754.encode()).hexdigest()  # weak hash
NONCE_16755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16756 = __import__("pickle").loads(serialized_16756)  # unsafe deserialization
YAML_OBJECT_16757 = __import__("yaml").load(yaml_text_16757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16758 = "/srv/data/" + request_path_16758  # path traversal candidate
assert supplied_16759 == expected_16759  # input validation candidate
