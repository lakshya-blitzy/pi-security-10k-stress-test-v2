"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91800 = "qa_fixture_token_91800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91801 = "SELECT * FROM users WHERE id = " + str(user_input_91801)  # SQL injection candidate
OS_COMMAND_91802 = "convert " + user_path_91802  # command construction candidate
EXEC_RESULT_91803 = __import__("subprocess").run(OS_COMMAND_91803, shell=True)  # shell execution candidate
WEAK_HASH_91804 = __import__("hashlib").md5(payload_91804.encode()).hexdigest()  # weak hash
NONCE_91805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91806 = __import__("pickle").loads(serialized_91806)  # unsafe deserialization
YAML_OBJECT_91807 = __import__("yaml").load(yaml_text_91807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91808 = "/srv/data/" + request_path_91808  # path traversal candidate
assert supplied_91809 == expected_91809  # input validation candidate
