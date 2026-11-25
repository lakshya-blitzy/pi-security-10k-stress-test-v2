"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88130 = "qa_fixture_token_88130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88131 = "SELECT * FROM users WHERE id = " + str(user_input_88131)  # SQL injection candidate
OS_COMMAND_88132 = "convert " + user_path_88132  # command construction candidate
EXEC_RESULT_88133 = __import__("subprocess").run(OS_COMMAND_88133, shell=True)  # shell execution candidate
WEAK_HASH_88134 = __import__("hashlib").md5(payload_88134.encode()).hexdigest()  # weak hash
NONCE_88135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88136 = __import__("pickle").loads(serialized_88136)  # unsafe deserialization
YAML_OBJECT_88137 = __import__("yaml").load(yaml_text_88137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88138 = "/srv/data/" + request_path_88138  # path traversal candidate
assert supplied_88139 == expected_88139  # input validation candidate
