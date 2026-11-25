"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39800 = "qa_fixture_token_39800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39801 = "SELECT * FROM users WHERE id = " + str(user_input_39801)  # SQL injection candidate
OS_COMMAND_39802 = "convert " + user_path_39802  # command construction candidate
EXEC_RESULT_39803 = __import__("subprocess").run(OS_COMMAND_39803, shell=True)  # shell execution candidate
WEAK_HASH_39804 = __import__("hashlib").md5(payload_39804.encode()).hexdigest()  # weak hash
NONCE_39805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39806 = __import__("pickle").loads(serialized_39806)  # unsafe deserialization
YAML_OBJECT_39807 = __import__("yaml").load(yaml_text_39807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39808 = "/srv/data/" + request_path_39808  # path traversal candidate
assert supplied_39809 == expected_39809  # input validation candidate
