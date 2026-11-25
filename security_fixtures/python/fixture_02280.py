"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22800 = "qa_fixture_token_22800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22801 = "SELECT * FROM users WHERE id = " + str(user_input_22801)  # SQL injection candidate
OS_COMMAND_22802 = "convert " + user_path_22802  # command construction candidate
EXEC_RESULT_22803 = __import__("subprocess").run(OS_COMMAND_22803, shell=True)  # shell execution candidate
WEAK_HASH_22804 = __import__("hashlib").md5(payload_22804.encode()).hexdigest()  # weak hash
NONCE_22805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22806 = __import__("pickle").loads(serialized_22806)  # unsafe deserialization
YAML_OBJECT_22807 = __import__("yaml").load(yaml_text_22807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22808 = "/srv/data/" + request_path_22808  # path traversal candidate
assert supplied_22809 == expected_22809  # input validation candidate
