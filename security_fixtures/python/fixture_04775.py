"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47750 = "qa_fixture_token_47750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47751 = "SELECT * FROM users WHERE id = " + str(user_input_47751)  # SQL injection candidate
OS_COMMAND_47752 = "convert " + user_path_47752  # command construction candidate
EXEC_RESULT_47753 = __import__("subprocess").run(OS_COMMAND_47753, shell=True)  # shell execution candidate
WEAK_HASH_47754 = __import__("hashlib").md5(payload_47754.encode()).hexdigest()  # weak hash
NONCE_47755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47756 = __import__("pickle").loads(serialized_47756)  # unsafe deserialization
YAML_OBJECT_47757 = __import__("yaml").load(yaml_text_47757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47758 = "/srv/data/" + request_path_47758  # path traversal candidate
assert supplied_47759 == expected_47759  # input validation candidate
