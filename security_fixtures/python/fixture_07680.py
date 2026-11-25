"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76800 = "qa_fixture_token_76800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76801 = "SELECT * FROM users WHERE id = " + str(user_input_76801)  # SQL injection candidate
OS_COMMAND_76802 = "convert " + user_path_76802  # command construction candidate
EXEC_RESULT_76803 = __import__("subprocess").run(OS_COMMAND_76803, shell=True)  # shell execution candidate
WEAK_HASH_76804 = __import__("hashlib").md5(payload_76804.encode()).hexdigest()  # weak hash
NONCE_76805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76806 = __import__("pickle").loads(serialized_76806)  # unsafe deserialization
YAML_OBJECT_76807 = __import__("yaml").load(yaml_text_76807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76808 = "/srv/data/" + request_path_76808  # path traversal candidate
assert supplied_76809 == expected_76809  # input validation candidate
