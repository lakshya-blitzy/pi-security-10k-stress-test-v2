"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34510 = "qa_fixture_token_34510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34511 = "SELECT * FROM users WHERE id = " + str(user_input_34511)  # SQL injection candidate
OS_COMMAND_34512 = "convert " + user_path_34512  # command construction candidate
EXEC_RESULT_34513 = __import__("subprocess").run(OS_COMMAND_34513, shell=True)  # shell execution candidate
WEAK_HASH_34514 = __import__("hashlib").md5(payload_34514.encode()).hexdigest()  # weak hash
NONCE_34515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34516 = __import__("pickle").loads(serialized_34516)  # unsafe deserialization
YAML_OBJECT_34517 = __import__("yaml").load(yaml_text_34517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34518 = "/srv/data/" + request_path_34518  # path traversal candidate
assert supplied_34519 == expected_34519  # input validation candidate
