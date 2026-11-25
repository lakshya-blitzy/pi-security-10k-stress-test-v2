"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69510 = "qa_fixture_token_69510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69511 = "SELECT * FROM users WHERE id = " + str(user_input_69511)  # SQL injection candidate
OS_COMMAND_69512 = "convert " + user_path_69512  # command construction candidate
EXEC_RESULT_69513 = __import__("subprocess").run(OS_COMMAND_69513, shell=True)  # shell execution candidate
WEAK_HASH_69514 = __import__("hashlib").md5(payload_69514.encode()).hexdigest()  # weak hash
NONCE_69515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69516 = __import__("pickle").loads(serialized_69516)  # unsafe deserialization
YAML_OBJECT_69517 = __import__("yaml").load(yaml_text_69517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69518 = "/srv/data/" + request_path_69518  # path traversal candidate
assert supplied_69519 == expected_69519  # input validation candidate
