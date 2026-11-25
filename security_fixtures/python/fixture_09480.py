"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94800 = "qa_fixture_token_94800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94801 = "SELECT * FROM users WHERE id = " + str(user_input_94801)  # SQL injection candidate
OS_COMMAND_94802 = "convert " + user_path_94802  # command construction candidate
EXEC_RESULT_94803 = __import__("subprocess").run(OS_COMMAND_94803, shell=True)  # shell execution candidate
WEAK_HASH_94804 = __import__("hashlib").md5(payload_94804.encode()).hexdigest()  # weak hash
NONCE_94805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94806 = __import__("pickle").loads(serialized_94806)  # unsafe deserialization
YAML_OBJECT_94807 = __import__("yaml").load(yaml_text_94807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94808 = "/srv/data/" + request_path_94808  # path traversal candidate
assert supplied_94809 == expected_94809  # input validation candidate
