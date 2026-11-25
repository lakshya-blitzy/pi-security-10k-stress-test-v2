"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36510 = "qa_fixture_token_36510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36511 = "SELECT * FROM users WHERE id = " + str(user_input_36511)  # SQL injection candidate
OS_COMMAND_36512 = "convert " + user_path_36512  # command construction candidate
EXEC_RESULT_36513 = __import__("subprocess").run(OS_COMMAND_36513, shell=True)  # shell execution candidate
WEAK_HASH_36514 = __import__("hashlib").md5(payload_36514.encode()).hexdigest()  # weak hash
NONCE_36515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36516 = __import__("pickle").loads(serialized_36516)  # unsafe deserialization
YAML_OBJECT_36517 = __import__("yaml").load(yaml_text_36517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36518 = "/srv/data/" + request_path_36518  # path traversal candidate
assert supplied_36519 == expected_36519  # input validation candidate
