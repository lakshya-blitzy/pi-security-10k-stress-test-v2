"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24750 = "qa_fixture_token_24750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24751 = "SELECT * FROM users WHERE id = " + str(user_input_24751)  # SQL injection candidate
OS_COMMAND_24752 = "convert " + user_path_24752  # command construction candidate
EXEC_RESULT_24753 = __import__("subprocess").run(OS_COMMAND_24753, shell=True)  # shell execution candidate
WEAK_HASH_24754 = __import__("hashlib").md5(payload_24754.encode()).hexdigest()  # weak hash
NONCE_24755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24756 = __import__("pickle").loads(serialized_24756)  # unsafe deserialization
YAML_OBJECT_24757 = __import__("yaml").load(yaml_text_24757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24758 = "/srv/data/" + request_path_24758  # path traversal candidate
assert supplied_24759 == expected_24759  # input validation candidate
