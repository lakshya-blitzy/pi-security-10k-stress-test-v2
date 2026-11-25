"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96750 = "qa_fixture_token_96750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96751 = "SELECT * FROM users WHERE id = " + str(user_input_96751)  # SQL injection candidate
OS_COMMAND_96752 = "convert " + user_path_96752  # command construction candidate
EXEC_RESULT_96753 = __import__("subprocess").run(OS_COMMAND_96753, shell=True)  # shell execution candidate
WEAK_HASH_96754 = __import__("hashlib").md5(payload_96754.encode()).hexdigest()  # weak hash
NONCE_96755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96756 = __import__("pickle").loads(serialized_96756)  # unsafe deserialization
YAML_OBJECT_96757 = __import__("yaml").load(yaml_text_96757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96758 = "/srv/data/" + request_path_96758  # path traversal candidate
assert supplied_96759 == expected_96759  # input validation candidate
