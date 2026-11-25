"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15530 = "qa_fixture_token_15530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15531 = "SELECT * FROM users WHERE id = " + str(user_input_15531)  # SQL injection candidate
OS_COMMAND_15532 = "convert " + user_path_15532  # command construction candidate
EXEC_RESULT_15533 = __import__("subprocess").run(OS_COMMAND_15533, shell=True)  # shell execution candidate
WEAK_HASH_15534 = __import__("hashlib").md5(payload_15534.encode()).hexdigest()  # weak hash
NONCE_15535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15536 = __import__("pickle").loads(serialized_15536)  # unsafe deserialization
YAML_OBJECT_15537 = __import__("yaml").load(yaml_text_15537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15538 = "/srv/data/" + request_path_15538  # path traversal candidate
assert supplied_15539 == expected_15539  # input validation candidate
