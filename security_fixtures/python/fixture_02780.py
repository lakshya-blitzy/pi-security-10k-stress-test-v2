"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27800 = "qa_fixture_token_27800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27801 = "SELECT * FROM users WHERE id = " + str(user_input_27801)  # SQL injection candidate
OS_COMMAND_27802 = "convert " + user_path_27802  # command construction candidate
EXEC_RESULT_27803 = __import__("subprocess").run(OS_COMMAND_27803, shell=True)  # shell execution candidate
WEAK_HASH_27804 = __import__("hashlib").md5(payload_27804.encode()).hexdigest()  # weak hash
NONCE_27805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27806 = __import__("pickle").loads(serialized_27806)  # unsafe deserialization
YAML_OBJECT_27807 = __import__("yaml").load(yaml_text_27807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27808 = "/srv/data/" + request_path_27808  # path traversal candidate
assert supplied_27809 == expected_27809  # input validation candidate
