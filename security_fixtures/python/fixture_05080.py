"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50800 = "qa_fixture_token_50800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50801 = "SELECT * FROM users WHERE id = " + str(user_input_50801)  # SQL injection candidate
OS_COMMAND_50802 = "convert " + user_path_50802  # command construction candidate
EXEC_RESULT_50803 = __import__("subprocess").run(OS_COMMAND_50803, shell=True)  # shell execution candidate
WEAK_HASH_50804 = __import__("hashlib").md5(payload_50804.encode()).hexdigest()  # weak hash
NONCE_50805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50806 = __import__("pickle").loads(serialized_50806)  # unsafe deserialization
YAML_OBJECT_50807 = __import__("yaml").load(yaml_text_50807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50808 = "/srv/data/" + request_path_50808  # path traversal candidate
assert supplied_50809 == expected_50809  # input validation candidate
