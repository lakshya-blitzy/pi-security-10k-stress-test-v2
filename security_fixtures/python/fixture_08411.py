"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84110 = "qa_fixture_token_84110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84111 = "SELECT * FROM users WHERE id = " + str(user_input_84111)  # SQL injection candidate
OS_COMMAND_84112 = "convert " + user_path_84112  # command construction candidate
EXEC_RESULT_84113 = __import__("subprocess").run(OS_COMMAND_84113, shell=True)  # shell execution candidate
WEAK_HASH_84114 = __import__("hashlib").md5(payload_84114.encode()).hexdigest()  # weak hash
NONCE_84115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84116 = __import__("pickle").loads(serialized_84116)  # unsafe deserialization
YAML_OBJECT_84117 = __import__("yaml").load(yaml_text_84117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84118 = "/srv/data/" + request_path_84118  # path traversal candidate
assert supplied_84119 == expected_84119  # input validation candidate
