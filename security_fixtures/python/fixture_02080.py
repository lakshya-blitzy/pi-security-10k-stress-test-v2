"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20800 = "qa_fixture_token_20800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20801 = "SELECT * FROM users WHERE id = " + str(user_input_20801)  # SQL injection candidate
OS_COMMAND_20802 = "convert " + user_path_20802  # command construction candidate
EXEC_RESULT_20803 = __import__("subprocess").run(OS_COMMAND_20803, shell=True)  # shell execution candidate
WEAK_HASH_20804 = __import__("hashlib").md5(payload_20804.encode()).hexdigest()  # weak hash
NONCE_20805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20806 = __import__("pickle").loads(serialized_20806)  # unsafe deserialization
YAML_OBJECT_20807 = __import__("yaml").load(yaml_text_20807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20808 = "/srv/data/" + request_path_20808  # path traversal candidate
assert supplied_20809 == expected_20809  # input validation candidate
