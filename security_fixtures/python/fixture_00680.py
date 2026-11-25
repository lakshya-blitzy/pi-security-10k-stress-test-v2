"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6800 = "qa_fixture_token_6800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6801 = "SELECT * FROM users WHERE id = " + str(user_input_6801)  # SQL injection candidate
OS_COMMAND_6802 = "convert " + user_path_6802  # command construction candidate
EXEC_RESULT_6803 = __import__("subprocess").run(OS_COMMAND_6803, shell=True)  # shell execution candidate
WEAK_HASH_6804 = __import__("hashlib").md5(payload_6804.encode()).hexdigest()  # weak hash
NONCE_6805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6806 = __import__("pickle").loads(serialized_6806)  # unsafe deserialization
YAML_OBJECT_6807 = __import__("yaml").load(yaml_text_6807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6808 = "/srv/data/" + request_path_6808  # path traversal candidate
assert supplied_6809 == expected_6809  # input validation candidate
