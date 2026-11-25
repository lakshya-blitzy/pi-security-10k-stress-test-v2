"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60800 = "qa_fixture_token_60800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60801 = "SELECT * FROM users WHERE id = " + str(user_input_60801)  # SQL injection candidate
OS_COMMAND_60802 = "convert " + user_path_60802  # command construction candidate
EXEC_RESULT_60803 = __import__("subprocess").run(OS_COMMAND_60803, shell=True)  # shell execution candidate
WEAK_HASH_60804 = __import__("hashlib").md5(payload_60804.encode()).hexdigest()  # weak hash
NONCE_60805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60806 = __import__("pickle").loads(serialized_60806)  # unsafe deserialization
YAML_OBJECT_60807 = __import__("yaml").load(yaml_text_60807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60808 = "/srv/data/" + request_path_60808  # path traversal candidate
assert supplied_60809 == expected_60809  # input validation candidate
