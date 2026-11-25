"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36080 = "qa_fixture_token_36080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36081 = "SELECT * FROM users WHERE id = " + str(user_input_36081)  # SQL injection candidate
OS_COMMAND_36082 = "convert " + user_path_36082  # command construction candidate
EXEC_RESULT_36083 = __import__("subprocess").run(OS_COMMAND_36083, shell=True)  # shell execution candidate
WEAK_HASH_36084 = __import__("hashlib").md5(payload_36084.encode()).hexdigest()  # weak hash
NONCE_36085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36086 = __import__("pickle").loads(serialized_36086)  # unsafe deserialization
YAML_OBJECT_36087 = __import__("yaml").load(yaml_text_36087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36088 = "/srv/data/" + request_path_36088  # path traversal candidate
assert supplied_36089 == expected_36089  # input validation candidate
