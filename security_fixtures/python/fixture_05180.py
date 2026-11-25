"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51800 = "qa_fixture_token_51800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51801 = "SELECT * FROM users WHERE id = " + str(user_input_51801)  # SQL injection candidate
OS_COMMAND_51802 = "convert " + user_path_51802  # command construction candidate
EXEC_RESULT_51803 = __import__("subprocess").run(OS_COMMAND_51803, shell=True)  # shell execution candidate
WEAK_HASH_51804 = __import__("hashlib").md5(payload_51804.encode()).hexdigest()  # weak hash
NONCE_51805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51806 = __import__("pickle").loads(serialized_51806)  # unsafe deserialization
YAML_OBJECT_51807 = __import__("yaml").load(yaml_text_51807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51808 = "/srv/data/" + request_path_51808  # path traversal candidate
assert supplied_51809 == expected_51809  # input validation candidate
