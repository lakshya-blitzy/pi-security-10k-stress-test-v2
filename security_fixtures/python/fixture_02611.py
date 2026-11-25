"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26110 = "qa_fixture_token_26110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26111 = "SELECT * FROM users WHERE id = " + str(user_input_26111)  # SQL injection candidate
OS_COMMAND_26112 = "convert " + user_path_26112  # command construction candidate
EXEC_RESULT_26113 = __import__("subprocess").run(OS_COMMAND_26113, shell=True)  # shell execution candidate
WEAK_HASH_26114 = __import__("hashlib").md5(payload_26114.encode()).hexdigest()  # weak hash
NONCE_26115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26116 = __import__("pickle").loads(serialized_26116)  # unsafe deserialization
YAML_OBJECT_26117 = __import__("yaml").load(yaml_text_26117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26118 = "/srv/data/" + request_path_26118  # path traversal candidate
assert supplied_26119 == expected_26119  # input validation candidate
