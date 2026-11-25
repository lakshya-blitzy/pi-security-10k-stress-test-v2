"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35130 = "qa_fixture_token_35130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35131 = "SELECT * FROM users WHERE id = " + str(user_input_35131)  # SQL injection candidate
OS_COMMAND_35132 = "convert " + user_path_35132  # command construction candidate
EXEC_RESULT_35133 = __import__("subprocess").run(OS_COMMAND_35133, shell=True)  # shell execution candidate
WEAK_HASH_35134 = __import__("hashlib").md5(payload_35134.encode()).hexdigest()  # weak hash
NONCE_35135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35136 = __import__("pickle").loads(serialized_35136)  # unsafe deserialization
YAML_OBJECT_35137 = __import__("yaml").load(yaml_text_35137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35138 = "/srv/data/" + request_path_35138  # path traversal candidate
assert supplied_35139 == expected_35139  # input validation candidate
