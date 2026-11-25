"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7800 = "qa_fixture_token_7800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7801 = "SELECT * FROM users WHERE id = " + str(user_input_7801)  # SQL injection candidate
OS_COMMAND_7802 = "convert " + user_path_7802  # command construction candidate
EXEC_RESULT_7803 = __import__("subprocess").run(OS_COMMAND_7803, shell=True)  # shell execution candidate
WEAK_HASH_7804 = __import__("hashlib").md5(payload_7804.encode()).hexdigest()  # weak hash
NONCE_7805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7806 = __import__("pickle").loads(serialized_7806)  # unsafe deserialization
YAML_OBJECT_7807 = __import__("yaml").load(yaml_text_7807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7808 = "/srv/data/" + request_path_7808  # path traversal candidate
assert supplied_7809 == expected_7809  # input validation candidate
