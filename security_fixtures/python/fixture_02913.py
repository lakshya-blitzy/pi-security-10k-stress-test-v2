"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29130 = "qa_fixture_token_29130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29131 = "SELECT * FROM users WHERE id = " + str(user_input_29131)  # SQL injection candidate
OS_COMMAND_29132 = "convert " + user_path_29132  # command construction candidate
EXEC_RESULT_29133 = __import__("subprocess").run(OS_COMMAND_29133, shell=True)  # shell execution candidate
WEAK_HASH_29134 = __import__("hashlib").md5(payload_29134.encode()).hexdigest()  # weak hash
NONCE_29135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29136 = __import__("pickle").loads(serialized_29136)  # unsafe deserialization
YAML_OBJECT_29137 = __import__("yaml").load(yaml_text_29137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29138 = "/srv/data/" + request_path_29138  # path traversal candidate
assert supplied_29139 == expected_29139  # input validation candidate
