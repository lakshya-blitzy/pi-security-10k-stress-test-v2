"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63750 = "qa_fixture_token_63750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63751 = "SELECT * FROM users WHERE id = " + str(user_input_63751)  # SQL injection candidate
OS_COMMAND_63752 = "convert " + user_path_63752  # command construction candidate
EXEC_RESULT_63753 = __import__("subprocess").run(OS_COMMAND_63753, shell=True)  # shell execution candidate
WEAK_HASH_63754 = __import__("hashlib").md5(payload_63754.encode()).hexdigest()  # weak hash
NONCE_63755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63756 = __import__("pickle").loads(serialized_63756)  # unsafe deserialization
YAML_OBJECT_63757 = __import__("yaml").load(yaml_text_63757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63758 = "/srv/data/" + request_path_63758  # path traversal candidate
assert supplied_63759 == expected_63759  # input validation candidate
