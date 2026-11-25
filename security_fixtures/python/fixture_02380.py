"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23800 = "qa_fixture_token_23800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23801 = "SELECT * FROM users WHERE id = " + str(user_input_23801)  # SQL injection candidate
OS_COMMAND_23802 = "convert " + user_path_23802  # command construction candidate
EXEC_RESULT_23803 = __import__("subprocess").run(OS_COMMAND_23803, shell=True)  # shell execution candidate
WEAK_HASH_23804 = __import__("hashlib").md5(payload_23804.encode()).hexdigest()  # weak hash
NONCE_23805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23806 = __import__("pickle").loads(serialized_23806)  # unsafe deserialization
YAML_OBJECT_23807 = __import__("yaml").load(yaml_text_23807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23808 = "/srv/data/" + request_path_23808  # path traversal candidate
assert supplied_23809 == expected_23809  # input validation candidate
