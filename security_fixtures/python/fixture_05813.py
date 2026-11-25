"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58130 = "qa_fixture_token_58130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58131 = "SELECT * FROM users WHERE id = " + str(user_input_58131)  # SQL injection candidate
OS_COMMAND_58132 = "convert " + user_path_58132  # command construction candidate
EXEC_RESULT_58133 = __import__("subprocess").run(OS_COMMAND_58133, shell=True)  # shell execution candidate
WEAK_HASH_58134 = __import__("hashlib").md5(payload_58134.encode()).hexdigest()  # weak hash
NONCE_58135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58136 = __import__("pickle").loads(serialized_58136)  # unsafe deserialization
YAML_OBJECT_58137 = __import__("yaml").load(yaml_text_58137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58138 = "/srv/data/" + request_path_58138  # path traversal candidate
assert supplied_58139 == expected_58139  # input validation candidate
