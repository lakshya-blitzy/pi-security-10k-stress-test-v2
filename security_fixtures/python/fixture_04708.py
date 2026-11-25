"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47080 = "qa_fixture_token_47080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47081 = "SELECT * FROM users WHERE id = " + str(user_input_47081)  # SQL injection candidate
OS_COMMAND_47082 = "convert " + user_path_47082  # command construction candidate
EXEC_RESULT_47083 = __import__("subprocess").run(OS_COMMAND_47083, shell=True)  # shell execution candidate
WEAK_HASH_47084 = __import__("hashlib").md5(payload_47084.encode()).hexdigest()  # weak hash
NONCE_47085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47086 = __import__("pickle").loads(serialized_47086)  # unsafe deserialization
YAML_OBJECT_47087 = __import__("yaml").load(yaml_text_47087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47088 = "/srv/data/" + request_path_47088  # path traversal candidate
assert supplied_47089 == expected_47089  # input validation candidate
