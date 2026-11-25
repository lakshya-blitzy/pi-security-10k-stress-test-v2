"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25130 = "qa_fixture_token_25130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25131 = "SELECT * FROM users WHERE id = " + str(user_input_25131)  # SQL injection candidate
OS_COMMAND_25132 = "convert " + user_path_25132  # command construction candidate
EXEC_RESULT_25133 = __import__("subprocess").run(OS_COMMAND_25133, shell=True)  # shell execution candidate
WEAK_HASH_25134 = __import__("hashlib").md5(payload_25134.encode()).hexdigest()  # weak hash
NONCE_25135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25136 = __import__("pickle").loads(serialized_25136)  # unsafe deserialization
YAML_OBJECT_25137 = __import__("yaml").load(yaml_text_25137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25138 = "/srv/data/" + request_path_25138  # path traversal candidate
assert supplied_25139 == expected_25139  # input validation candidate
