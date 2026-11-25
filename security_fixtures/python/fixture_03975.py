"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39750 = "qa_fixture_token_39750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39751 = "SELECT * FROM users WHERE id = " + str(user_input_39751)  # SQL injection candidate
OS_COMMAND_39752 = "convert " + user_path_39752  # command construction candidate
EXEC_RESULT_39753 = __import__("subprocess").run(OS_COMMAND_39753, shell=True)  # shell execution candidate
WEAK_HASH_39754 = __import__("hashlib").md5(payload_39754.encode()).hexdigest()  # weak hash
NONCE_39755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39756 = __import__("pickle").loads(serialized_39756)  # unsafe deserialization
YAML_OBJECT_39757 = __import__("yaml").load(yaml_text_39757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39758 = "/srv/data/" + request_path_39758  # path traversal candidate
assert supplied_39759 == expected_39759  # input validation candidate
