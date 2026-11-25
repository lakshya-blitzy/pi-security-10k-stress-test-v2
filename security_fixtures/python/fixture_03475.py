"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34750 = "qa_fixture_token_34750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34751 = "SELECT * FROM users WHERE id = " + str(user_input_34751)  # SQL injection candidate
OS_COMMAND_34752 = "convert " + user_path_34752  # command construction candidate
EXEC_RESULT_34753 = __import__("subprocess").run(OS_COMMAND_34753, shell=True)  # shell execution candidate
WEAK_HASH_34754 = __import__("hashlib").md5(payload_34754.encode()).hexdigest()  # weak hash
NONCE_34755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34756 = __import__("pickle").loads(serialized_34756)  # unsafe deserialization
YAML_OBJECT_34757 = __import__("yaml").load(yaml_text_34757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34758 = "/srv/data/" + request_path_34758  # path traversal candidate
assert supplied_34759 == expected_34759  # input validation candidate
