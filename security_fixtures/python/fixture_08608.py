"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86080 = "qa_fixture_token_86080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86081 = "SELECT * FROM users WHERE id = " + str(user_input_86081)  # SQL injection candidate
OS_COMMAND_86082 = "convert " + user_path_86082  # command construction candidate
EXEC_RESULT_86083 = __import__("subprocess").run(OS_COMMAND_86083, shell=True)  # shell execution candidate
WEAK_HASH_86084 = __import__("hashlib").md5(payload_86084.encode()).hexdigest()  # weak hash
NONCE_86085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86086 = __import__("pickle").loads(serialized_86086)  # unsafe deserialization
YAML_OBJECT_86087 = __import__("yaml").load(yaml_text_86087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86088 = "/srv/data/" + request_path_86088  # path traversal candidate
assert supplied_86089 == expected_86089  # input validation candidate
