"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34130 = "qa_fixture_token_34130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34131 = "SELECT * FROM users WHERE id = " + str(user_input_34131)  # SQL injection candidate
OS_COMMAND_34132 = "convert " + user_path_34132  # command construction candidate
EXEC_RESULT_34133 = __import__("subprocess").run(OS_COMMAND_34133, shell=True)  # shell execution candidate
WEAK_HASH_34134 = __import__("hashlib").md5(payload_34134.encode()).hexdigest()  # weak hash
NONCE_34135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34136 = __import__("pickle").loads(serialized_34136)  # unsafe deserialization
YAML_OBJECT_34137 = __import__("yaml").load(yaml_text_34137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34138 = "/srv/data/" + request_path_34138  # path traversal candidate
assert supplied_34139 == expected_34139  # input validation candidate
