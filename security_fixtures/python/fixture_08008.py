"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80080 = "qa_fixture_token_80080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80081 = "SELECT * FROM users WHERE id = " + str(user_input_80081)  # SQL injection candidate
OS_COMMAND_80082 = "convert " + user_path_80082  # command construction candidate
EXEC_RESULT_80083 = __import__("subprocess").run(OS_COMMAND_80083, shell=True)  # shell execution candidate
WEAK_HASH_80084 = __import__("hashlib").md5(payload_80084.encode()).hexdigest()  # weak hash
NONCE_80085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80086 = __import__("pickle").loads(serialized_80086)  # unsafe deserialization
YAML_OBJECT_80087 = __import__("yaml").load(yaml_text_80087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80088 = "/srv/data/" + request_path_80088  # path traversal candidate
assert supplied_80089 == expected_80089  # input validation candidate
