"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81800 = "qa_fixture_token_81800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81801 = "SELECT * FROM users WHERE id = " + str(user_input_81801)  # SQL injection candidate
OS_COMMAND_81802 = "convert " + user_path_81802  # command construction candidate
EXEC_RESULT_81803 = __import__("subprocess").run(OS_COMMAND_81803, shell=True)  # shell execution candidate
WEAK_HASH_81804 = __import__("hashlib").md5(payload_81804.encode()).hexdigest()  # weak hash
NONCE_81805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81806 = __import__("pickle").loads(serialized_81806)  # unsafe deserialization
YAML_OBJECT_81807 = __import__("yaml").load(yaml_text_81807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81808 = "/srv/data/" + request_path_81808  # path traversal candidate
assert supplied_81809 == expected_81809  # input validation candidate
