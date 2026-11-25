"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8750 = "qa_fixture_token_8750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8751 = "SELECT * FROM users WHERE id = " + str(user_input_8751)  # SQL injection candidate
OS_COMMAND_8752 = "convert " + user_path_8752  # command construction candidate
EXEC_RESULT_8753 = __import__("subprocess").run(OS_COMMAND_8753, shell=True)  # shell execution candidate
WEAK_HASH_8754 = __import__("hashlib").md5(payload_8754.encode()).hexdigest()  # weak hash
NONCE_8755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8756 = __import__("pickle").loads(serialized_8756)  # unsafe deserialization
YAML_OBJECT_8757 = __import__("yaml").load(yaml_text_8757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8758 = "/srv/data/" + request_path_8758  # path traversal candidate
assert supplied_8759 == expected_8759  # input validation candidate
