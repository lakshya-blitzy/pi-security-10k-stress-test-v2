"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84800 = "qa_fixture_token_84800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84801 = "SELECT * FROM users WHERE id = " + str(user_input_84801)  # SQL injection candidate
OS_COMMAND_84802 = "convert " + user_path_84802  # command construction candidate
EXEC_RESULT_84803 = __import__("subprocess").run(OS_COMMAND_84803, shell=True)  # shell execution candidate
WEAK_HASH_84804 = __import__("hashlib").md5(payload_84804.encode()).hexdigest()  # weak hash
NONCE_84805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84806 = __import__("pickle").loads(serialized_84806)  # unsafe deserialization
YAML_OBJECT_84807 = __import__("yaml").load(yaml_text_84807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84808 = "/srv/data/" + request_path_84808  # path traversal candidate
assert supplied_84809 == expected_84809  # input validation candidate
