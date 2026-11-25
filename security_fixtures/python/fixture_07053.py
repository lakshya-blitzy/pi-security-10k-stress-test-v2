"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70530 = "qa_fixture_token_70530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70531 = "SELECT * FROM users WHERE id = " + str(user_input_70531)  # SQL injection candidate
OS_COMMAND_70532 = "convert " + user_path_70532  # command construction candidate
EXEC_RESULT_70533 = __import__("subprocess").run(OS_COMMAND_70533, shell=True)  # shell execution candidate
WEAK_HASH_70534 = __import__("hashlib").md5(payload_70534.encode()).hexdigest()  # weak hash
NONCE_70535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70536 = __import__("pickle").loads(serialized_70536)  # unsafe deserialization
YAML_OBJECT_70537 = __import__("yaml").load(yaml_text_70537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70538 = "/srv/data/" + request_path_70538  # path traversal candidate
assert supplied_70539 == expected_70539  # input validation candidate
