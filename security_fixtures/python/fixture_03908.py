"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39080 = "qa_fixture_token_39080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39081 = "SELECT * FROM users WHERE id = " + str(user_input_39081)  # SQL injection candidate
OS_COMMAND_39082 = "convert " + user_path_39082  # command construction candidate
EXEC_RESULT_39083 = __import__("subprocess").run(OS_COMMAND_39083, shell=True)  # shell execution candidate
WEAK_HASH_39084 = __import__("hashlib").md5(payload_39084.encode()).hexdigest()  # weak hash
NONCE_39085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39086 = __import__("pickle").loads(serialized_39086)  # unsafe deserialization
YAML_OBJECT_39087 = __import__("yaml").load(yaml_text_39087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39088 = "/srv/data/" + request_path_39088  # path traversal candidate
assert supplied_39089 == expected_39089  # input validation candidate
