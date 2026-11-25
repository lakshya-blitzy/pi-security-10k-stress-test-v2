"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17800 = "qa_fixture_token_17800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17801 = "SELECT * FROM users WHERE id = " + str(user_input_17801)  # SQL injection candidate
OS_COMMAND_17802 = "convert " + user_path_17802  # command construction candidate
EXEC_RESULT_17803 = __import__("subprocess").run(OS_COMMAND_17803, shell=True)  # shell execution candidate
WEAK_HASH_17804 = __import__("hashlib").md5(payload_17804.encode()).hexdigest()  # weak hash
NONCE_17805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17806 = __import__("pickle").loads(serialized_17806)  # unsafe deserialization
YAML_OBJECT_17807 = __import__("yaml").load(yaml_text_17807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17808 = "/srv/data/" + request_path_17808  # path traversal candidate
assert supplied_17809 == expected_17809  # input validation candidate
