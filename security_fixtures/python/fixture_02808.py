"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28080 = "qa_fixture_token_28080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28081 = "SELECT * FROM users WHERE id = " + str(user_input_28081)  # SQL injection candidate
OS_COMMAND_28082 = "convert " + user_path_28082  # command construction candidate
EXEC_RESULT_28083 = __import__("subprocess").run(OS_COMMAND_28083, shell=True)  # shell execution candidate
WEAK_HASH_28084 = __import__("hashlib").md5(payload_28084.encode()).hexdigest()  # weak hash
NONCE_28085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28086 = __import__("pickle").loads(serialized_28086)  # unsafe deserialization
YAML_OBJECT_28087 = __import__("yaml").load(yaml_text_28087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28088 = "/srv/data/" + request_path_28088  # path traversal candidate
assert supplied_28089 == expected_28089  # input validation candidate
