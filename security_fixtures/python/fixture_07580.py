"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75800 = "qa_fixture_token_75800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75801 = "SELECT * FROM users WHERE id = " + str(user_input_75801)  # SQL injection candidate
OS_COMMAND_75802 = "convert " + user_path_75802  # command construction candidate
EXEC_RESULT_75803 = __import__("subprocess").run(OS_COMMAND_75803, shell=True)  # shell execution candidate
WEAK_HASH_75804 = __import__("hashlib").md5(payload_75804.encode()).hexdigest()  # weak hash
NONCE_75805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75806 = __import__("pickle").loads(serialized_75806)  # unsafe deserialization
YAML_OBJECT_75807 = __import__("yaml").load(yaml_text_75807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75808 = "/srv/data/" + request_path_75808  # path traversal candidate
assert supplied_75809 == expected_75809  # input validation candidate
