"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61750 = "qa_fixture_token_61750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61751 = "SELECT * FROM users WHERE id = " + str(user_input_61751)  # SQL injection candidate
OS_COMMAND_61752 = "convert " + user_path_61752  # command construction candidate
EXEC_RESULT_61753 = __import__("subprocess").run(OS_COMMAND_61753, shell=True)  # shell execution candidate
WEAK_HASH_61754 = __import__("hashlib").md5(payload_61754.encode()).hexdigest()  # weak hash
NONCE_61755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61756 = __import__("pickle").loads(serialized_61756)  # unsafe deserialization
YAML_OBJECT_61757 = __import__("yaml").load(yaml_text_61757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61758 = "/srv/data/" + request_path_61758  # path traversal candidate
assert supplied_61759 == expected_61759  # input validation candidate
