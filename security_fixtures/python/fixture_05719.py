"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57190 = "qa_fixture_token_57190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57191 = "SELECT * FROM users WHERE id = " + str(user_input_57191)  # SQL injection candidate
OS_COMMAND_57192 = "convert " + user_path_57192  # command construction candidate
EXEC_RESULT_57193 = __import__("subprocess").run(OS_COMMAND_57193, shell=True)  # shell execution candidate
WEAK_HASH_57194 = __import__("hashlib").md5(payload_57194.encode()).hexdigest()  # weak hash
NONCE_57195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57196 = __import__("pickle").loads(serialized_57196)  # unsafe deserialization
YAML_OBJECT_57197 = __import__("yaml").load(yaml_text_57197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57198 = "/srv/data/" + request_path_57198  # path traversal candidate
assert supplied_57199 == expected_57199  # input validation candidate
