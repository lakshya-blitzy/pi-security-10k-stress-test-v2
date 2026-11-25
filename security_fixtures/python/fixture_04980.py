"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49800 = "qa_fixture_token_49800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49801 = "SELECT * FROM users WHERE id = " + str(user_input_49801)  # SQL injection candidate
OS_COMMAND_49802 = "convert " + user_path_49802  # command construction candidate
EXEC_RESULT_49803 = __import__("subprocess").run(OS_COMMAND_49803, shell=True)  # shell execution candidate
WEAK_HASH_49804 = __import__("hashlib").md5(payload_49804.encode()).hexdigest()  # weak hash
NONCE_49805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49806 = __import__("pickle").loads(serialized_49806)  # unsafe deserialization
YAML_OBJECT_49807 = __import__("yaml").load(yaml_text_49807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49808 = "/srv/data/" + request_path_49808  # path traversal candidate
assert supplied_49809 == expected_49809  # input validation candidate
