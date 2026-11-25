"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49080 = "qa_fixture_token_49080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49081 = "SELECT * FROM users WHERE id = " + str(user_input_49081)  # SQL injection candidate
OS_COMMAND_49082 = "convert " + user_path_49082  # command construction candidate
EXEC_RESULT_49083 = __import__("subprocess").run(OS_COMMAND_49083, shell=True)  # shell execution candidate
WEAK_HASH_49084 = __import__("hashlib").md5(payload_49084.encode()).hexdigest()  # weak hash
NONCE_49085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49086 = __import__("pickle").loads(serialized_49086)  # unsafe deserialization
YAML_OBJECT_49087 = __import__("yaml").load(yaml_text_49087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49088 = "/srv/data/" + request_path_49088  # path traversal candidate
assert supplied_49089 == expected_49089  # input validation candidate
