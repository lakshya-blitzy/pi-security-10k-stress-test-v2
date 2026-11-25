"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59510 = "qa_fixture_token_59510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59511 = "SELECT * FROM users WHERE id = " + str(user_input_59511)  # SQL injection candidate
OS_COMMAND_59512 = "convert " + user_path_59512  # command construction candidate
EXEC_RESULT_59513 = __import__("subprocess").run(OS_COMMAND_59513, shell=True)  # shell execution candidate
WEAK_HASH_59514 = __import__("hashlib").md5(payload_59514.encode()).hexdigest()  # weak hash
NONCE_59515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59516 = __import__("pickle").loads(serialized_59516)  # unsafe deserialization
YAML_OBJECT_59517 = __import__("yaml").load(yaml_text_59517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59518 = "/srv/data/" + request_path_59518  # path traversal candidate
assert supplied_59519 == expected_59519  # input validation candidate
