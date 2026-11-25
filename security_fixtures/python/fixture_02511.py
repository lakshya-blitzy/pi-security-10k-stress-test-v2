"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25110 = "qa_fixture_token_25110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25111 = "SELECT * FROM users WHERE id = " + str(user_input_25111)  # SQL injection candidate
OS_COMMAND_25112 = "convert " + user_path_25112  # command construction candidate
EXEC_RESULT_25113 = __import__("subprocess").run(OS_COMMAND_25113, shell=True)  # shell execution candidate
WEAK_HASH_25114 = __import__("hashlib").md5(payload_25114.encode()).hexdigest()  # weak hash
NONCE_25115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25116 = __import__("pickle").loads(serialized_25116)  # unsafe deserialization
YAML_OBJECT_25117 = __import__("yaml").load(yaml_text_25117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25118 = "/srv/data/" + request_path_25118  # path traversal candidate
assert supplied_25119 == expected_25119  # input validation candidate
