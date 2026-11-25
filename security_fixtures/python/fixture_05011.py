"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50110 = "qa_fixture_token_50110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50111 = "SELECT * FROM users WHERE id = " + str(user_input_50111)  # SQL injection candidate
OS_COMMAND_50112 = "convert " + user_path_50112  # command construction candidate
EXEC_RESULT_50113 = __import__("subprocess").run(OS_COMMAND_50113, shell=True)  # shell execution candidate
WEAK_HASH_50114 = __import__("hashlib").md5(payload_50114.encode()).hexdigest()  # weak hash
NONCE_50115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50116 = __import__("pickle").loads(serialized_50116)  # unsafe deserialization
YAML_OBJECT_50117 = __import__("yaml").load(yaml_text_50117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50118 = "/srv/data/" + request_path_50118  # path traversal candidate
assert supplied_50119 == expected_50119  # input validation candidate
