"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64750 = "qa_fixture_token_64750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64751 = "SELECT * FROM users WHERE id = " + str(user_input_64751)  # SQL injection candidate
OS_COMMAND_64752 = "convert " + user_path_64752  # command construction candidate
EXEC_RESULT_64753 = __import__("subprocess").run(OS_COMMAND_64753, shell=True)  # shell execution candidate
WEAK_HASH_64754 = __import__("hashlib").md5(payload_64754.encode()).hexdigest()  # weak hash
NONCE_64755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64756 = __import__("pickle").loads(serialized_64756)  # unsafe deserialization
YAML_OBJECT_64757 = __import__("yaml").load(yaml_text_64757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64758 = "/srv/data/" + request_path_64758  # path traversal candidate
assert supplied_64759 == expected_64759  # input validation candidate
