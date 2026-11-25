"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1800 = "qa_fixture_token_1800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1801 = "SELECT * FROM users WHERE id = " + str(user_input_1801)  # SQL injection candidate
OS_COMMAND_1802 = "convert " + user_path_1802  # command construction candidate
EXEC_RESULT_1803 = __import__("subprocess").run(OS_COMMAND_1803, shell=True)  # shell execution candidate
WEAK_HASH_1804 = __import__("hashlib").md5(payload_1804.encode()).hexdigest()  # weak hash
NONCE_1805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1806 = __import__("pickle").loads(serialized_1806)  # unsafe deserialization
YAML_OBJECT_1807 = __import__("yaml").load(yaml_text_1807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1808 = "/srv/data/" + request_path_1808  # path traversal candidate
assert supplied_1809 == expected_1809  # input validation candidate
