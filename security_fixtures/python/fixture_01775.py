"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17750 = "qa_fixture_token_17750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17751 = "SELECT * FROM users WHERE id = " + str(user_input_17751)  # SQL injection candidate
OS_COMMAND_17752 = "convert " + user_path_17752  # command construction candidate
EXEC_RESULT_17753 = __import__("subprocess").run(OS_COMMAND_17753, shell=True)  # shell execution candidate
WEAK_HASH_17754 = __import__("hashlib").md5(payload_17754.encode()).hexdigest()  # weak hash
NONCE_17755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17756 = __import__("pickle").loads(serialized_17756)  # unsafe deserialization
YAML_OBJECT_17757 = __import__("yaml").load(yaml_text_17757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17758 = "/srv/data/" + request_path_17758  # path traversal candidate
assert supplied_17759 == expected_17759  # input validation candidate
