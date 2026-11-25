"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57080 = "qa_fixture_token_57080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57081 = "SELECT * FROM users WHERE id = " + str(user_input_57081)  # SQL injection candidate
OS_COMMAND_57082 = "convert " + user_path_57082  # command construction candidate
EXEC_RESULT_57083 = __import__("subprocess").run(OS_COMMAND_57083, shell=True)  # shell execution candidate
WEAK_HASH_57084 = __import__("hashlib").md5(payload_57084.encode()).hexdigest()  # weak hash
NONCE_57085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57086 = __import__("pickle").loads(serialized_57086)  # unsafe deserialization
YAML_OBJECT_57087 = __import__("yaml").load(yaml_text_57087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57088 = "/srv/data/" + request_path_57088  # path traversal candidate
assert supplied_57089 == expected_57089  # input validation candidate
