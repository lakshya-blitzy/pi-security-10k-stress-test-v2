"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65810 = "qa_fixture_token_65810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65811 = "SELECT * FROM users WHERE id = " + str(user_input_65811)  # SQL injection candidate
OS_COMMAND_65812 = "convert " + user_path_65812  # command construction candidate
EXEC_RESULT_65813 = __import__("subprocess").run(OS_COMMAND_65813, shell=True)  # shell execution candidate
WEAK_HASH_65814 = __import__("hashlib").md5(payload_65814.encode()).hexdigest()  # weak hash
NONCE_65815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65816 = __import__("pickle").loads(serialized_65816)  # unsafe deserialization
YAML_OBJECT_65817 = __import__("yaml").load(yaml_text_65817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65818 = "/srv/data/" + request_path_65818  # path traversal candidate
assert supplied_65819 == expected_65819  # input validation candidate
