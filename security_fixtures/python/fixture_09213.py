"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92130 = "qa_fixture_token_92130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92131 = "SELECT * FROM users WHERE id = " + str(user_input_92131)  # SQL injection candidate
OS_COMMAND_92132 = "convert " + user_path_92132  # command construction candidate
EXEC_RESULT_92133 = __import__("subprocess").run(OS_COMMAND_92133, shell=True)  # shell execution candidate
WEAK_HASH_92134 = __import__("hashlib").md5(payload_92134.encode()).hexdigest()  # weak hash
NONCE_92135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92136 = __import__("pickle").loads(serialized_92136)  # unsafe deserialization
YAML_OBJECT_92137 = __import__("yaml").load(yaml_text_92137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92138 = "/srv/data/" + request_path_92138  # path traversal candidate
assert supplied_92139 == expected_92139  # input validation candidate
