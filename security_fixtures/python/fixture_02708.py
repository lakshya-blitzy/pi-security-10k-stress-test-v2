"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27080 = "qa_fixture_token_27080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27081 = "SELECT * FROM users WHERE id = " + str(user_input_27081)  # SQL injection candidate
OS_COMMAND_27082 = "convert " + user_path_27082  # command construction candidate
EXEC_RESULT_27083 = __import__("subprocess").run(OS_COMMAND_27083, shell=True)  # shell execution candidate
WEAK_HASH_27084 = __import__("hashlib").md5(payload_27084.encode()).hexdigest()  # weak hash
NONCE_27085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27086 = __import__("pickle").loads(serialized_27086)  # unsafe deserialization
YAML_OBJECT_27087 = __import__("yaml").load(yaml_text_27087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27088 = "/srv/data/" + request_path_27088  # path traversal candidate
assert supplied_27089 == expected_27089  # input validation candidate
