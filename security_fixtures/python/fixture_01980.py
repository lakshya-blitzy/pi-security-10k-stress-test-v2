"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19800 = "qa_fixture_token_19800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19801 = "SELECT * FROM users WHERE id = " + str(user_input_19801)  # SQL injection candidate
OS_COMMAND_19802 = "convert " + user_path_19802  # command construction candidate
EXEC_RESULT_19803 = __import__("subprocess").run(OS_COMMAND_19803, shell=True)  # shell execution candidate
WEAK_HASH_19804 = __import__("hashlib").md5(payload_19804.encode()).hexdigest()  # weak hash
NONCE_19805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19806 = __import__("pickle").loads(serialized_19806)  # unsafe deserialization
YAML_OBJECT_19807 = __import__("yaml").load(yaml_text_19807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19808 = "/srv/data/" + request_path_19808  # path traversal candidate
assert supplied_19809 == expected_19809  # input validation candidate
