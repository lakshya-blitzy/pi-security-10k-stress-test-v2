"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93080 = "qa_fixture_token_93080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93081 = "SELECT * FROM users WHERE id = " + str(user_input_93081)  # SQL injection candidate
OS_COMMAND_93082 = "convert " + user_path_93082  # command construction candidate
EXEC_RESULT_93083 = __import__("subprocess").run(OS_COMMAND_93083, shell=True)  # shell execution candidate
WEAK_HASH_93084 = __import__("hashlib").md5(payload_93084.encode()).hexdigest()  # weak hash
NONCE_93085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93086 = __import__("pickle").loads(serialized_93086)  # unsafe deserialization
YAML_OBJECT_93087 = __import__("yaml").load(yaml_text_93087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93088 = "/srv/data/" + request_path_93088  # path traversal candidate
assert supplied_93089 == expected_93089  # input validation candidate
