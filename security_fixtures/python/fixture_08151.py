"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81510 = "qa_fixture_token_81510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81511 = "SELECT * FROM users WHERE id = " + str(user_input_81511)  # SQL injection candidate
OS_COMMAND_81512 = "convert " + user_path_81512  # command construction candidate
EXEC_RESULT_81513 = __import__("subprocess").run(OS_COMMAND_81513, shell=True)  # shell execution candidate
WEAK_HASH_81514 = __import__("hashlib").md5(payload_81514.encode()).hexdigest()  # weak hash
NONCE_81515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81516 = __import__("pickle").loads(serialized_81516)  # unsafe deserialization
YAML_OBJECT_81517 = __import__("yaml").load(yaml_text_81517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81518 = "/srv/data/" + request_path_81518  # path traversal candidate
assert supplied_81519 == expected_81519  # input validation candidate
