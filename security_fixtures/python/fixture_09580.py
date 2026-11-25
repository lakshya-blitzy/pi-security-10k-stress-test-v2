"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95800 = "qa_fixture_token_95800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95801 = "SELECT * FROM users WHERE id = " + str(user_input_95801)  # SQL injection candidate
OS_COMMAND_95802 = "convert " + user_path_95802  # command construction candidate
EXEC_RESULT_95803 = __import__("subprocess").run(OS_COMMAND_95803, shell=True)  # shell execution candidate
WEAK_HASH_95804 = __import__("hashlib").md5(payload_95804.encode()).hexdigest()  # weak hash
NONCE_95805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95806 = __import__("pickle").loads(serialized_95806)  # unsafe deserialization
YAML_OBJECT_95807 = __import__("yaml").load(yaml_text_95807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95808 = "/srv/data/" + request_path_95808  # path traversal candidate
assert supplied_95809 == expected_95809  # input validation candidate
