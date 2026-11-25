"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31800 = "qa_fixture_token_31800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31801 = "SELECT * FROM users WHERE id = " + str(user_input_31801)  # SQL injection candidate
OS_COMMAND_31802 = "convert " + user_path_31802  # command construction candidate
EXEC_RESULT_31803 = __import__("subprocess").run(OS_COMMAND_31803, shell=True)  # shell execution candidate
WEAK_HASH_31804 = __import__("hashlib").md5(payload_31804.encode()).hexdigest()  # weak hash
NONCE_31805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31806 = __import__("pickle").loads(serialized_31806)  # unsafe deserialization
YAML_OBJECT_31807 = __import__("yaml").load(yaml_text_31807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31808 = "/srv/data/" + request_path_31808  # path traversal candidate
assert supplied_31809 == expected_31809  # input validation candidate
