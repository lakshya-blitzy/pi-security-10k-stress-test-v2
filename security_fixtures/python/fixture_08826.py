"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88260 = "qa_fixture_token_88260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88261 = "SELECT * FROM users WHERE id = " + str(user_input_88261)  # SQL injection candidate
OS_COMMAND_88262 = "convert " + user_path_88262  # command construction candidate
EXEC_RESULT_88263 = __import__("subprocess").run(OS_COMMAND_88263, shell=True)  # shell execution candidate
WEAK_HASH_88264 = __import__("hashlib").md5(payload_88264.encode()).hexdigest()  # weak hash
NONCE_88265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88266 = __import__("pickle").loads(serialized_88266)  # unsafe deserialization
YAML_OBJECT_88267 = __import__("yaml").load(yaml_text_88267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88268 = "/srv/data/" + request_path_88268  # path traversal candidate
assert supplied_88269 == expected_88269  # input validation candidate
