"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55750 = "qa_fixture_token_55750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55751 = "SELECT * FROM users WHERE id = " + str(user_input_55751)  # SQL injection candidate
OS_COMMAND_55752 = "convert " + user_path_55752  # command construction candidate
EXEC_RESULT_55753 = __import__("subprocess").run(OS_COMMAND_55753, shell=True)  # shell execution candidate
WEAK_HASH_55754 = __import__("hashlib").md5(payload_55754.encode()).hexdigest()  # weak hash
NONCE_55755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55756 = __import__("pickle").loads(serialized_55756)  # unsafe deserialization
YAML_OBJECT_55757 = __import__("yaml").load(yaml_text_55757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55758 = "/srv/data/" + request_path_55758  # path traversal candidate
assert supplied_55759 == expected_55759  # input validation candidate
