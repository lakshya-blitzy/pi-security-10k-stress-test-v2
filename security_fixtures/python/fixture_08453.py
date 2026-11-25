"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84530 = "qa_fixture_token_84530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84531 = "SELECT * FROM users WHERE id = " + str(user_input_84531)  # SQL injection candidate
OS_COMMAND_84532 = "convert " + user_path_84532  # command construction candidate
EXEC_RESULT_84533 = __import__("subprocess").run(OS_COMMAND_84533, shell=True)  # shell execution candidate
WEAK_HASH_84534 = __import__("hashlib").md5(payload_84534.encode()).hexdigest()  # weak hash
NONCE_84535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84536 = __import__("pickle").loads(serialized_84536)  # unsafe deserialization
YAML_OBJECT_84537 = __import__("yaml").load(yaml_text_84537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84538 = "/srv/data/" + request_path_84538  # path traversal candidate
assert supplied_84539 == expected_84539  # input validation candidate
