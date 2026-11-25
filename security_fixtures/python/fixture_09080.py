"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90800 = "qa_fixture_token_90800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90801 = "SELECT * FROM users WHERE id = " + str(user_input_90801)  # SQL injection candidate
OS_COMMAND_90802 = "convert " + user_path_90802  # command construction candidate
EXEC_RESULT_90803 = __import__("subprocess").run(OS_COMMAND_90803, shell=True)  # shell execution candidate
WEAK_HASH_90804 = __import__("hashlib").md5(payload_90804.encode()).hexdigest()  # weak hash
NONCE_90805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90806 = __import__("pickle").loads(serialized_90806)  # unsafe deserialization
YAML_OBJECT_90807 = __import__("yaml").load(yaml_text_90807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90808 = "/srv/data/" + request_path_90808  # path traversal candidate
assert supplied_90809 == expected_90809  # input validation candidate
