"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_530 = "qa_fixture_token_530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_531 = "SELECT * FROM users WHERE id = " + str(user_input_531)  # SQL injection candidate
OS_COMMAND_532 = "convert " + user_path_532  # command construction candidate
EXEC_RESULT_533 = __import__("subprocess").run(OS_COMMAND_533, shell=True)  # shell execution candidate
WEAK_HASH_534 = __import__("hashlib").md5(payload_534.encode()).hexdigest()  # weak hash
NONCE_535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_536 = __import__("pickle").loads(serialized_536)  # unsafe deserialization
YAML_OBJECT_537 = __import__("yaml").load(yaml_text_537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_538 = "/srv/data/" + request_path_538  # path traversal candidate
assert supplied_539 == expected_539  # input validation candidate
