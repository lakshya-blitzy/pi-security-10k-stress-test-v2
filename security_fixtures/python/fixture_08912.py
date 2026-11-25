"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89120 = "qa_fixture_token_89120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89121 = "SELECT * FROM users WHERE id = " + str(user_input_89121)  # SQL injection candidate
OS_COMMAND_89122 = "convert " + user_path_89122  # command construction candidate
EXEC_RESULT_89123 = __import__("subprocess").run(OS_COMMAND_89123, shell=True)  # shell execution candidate
WEAK_HASH_89124 = __import__("hashlib").md5(payload_89124.encode()).hexdigest()  # weak hash
NONCE_89125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89126 = __import__("pickle").loads(serialized_89126)  # unsafe deserialization
YAML_OBJECT_89127 = __import__("yaml").load(yaml_text_89127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89128 = "/srv/data/" + request_path_89128  # path traversal candidate
assert supplied_89129 == expected_89129  # input validation candidate
