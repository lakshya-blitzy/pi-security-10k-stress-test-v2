"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70750 = "qa_fixture_token_70750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70751 = "SELECT * FROM users WHERE id = " + str(user_input_70751)  # SQL injection candidate
OS_COMMAND_70752 = "convert " + user_path_70752  # command construction candidate
EXEC_RESULT_70753 = __import__("subprocess").run(OS_COMMAND_70753, shell=True)  # shell execution candidate
WEAK_HASH_70754 = __import__("hashlib").md5(payload_70754.encode()).hexdigest()  # weak hash
NONCE_70755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70756 = __import__("pickle").loads(serialized_70756)  # unsafe deserialization
YAML_OBJECT_70757 = __import__("yaml").load(yaml_text_70757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70758 = "/srv/data/" + request_path_70758  # path traversal candidate
assert supplied_70759 == expected_70759  # input validation candidate
