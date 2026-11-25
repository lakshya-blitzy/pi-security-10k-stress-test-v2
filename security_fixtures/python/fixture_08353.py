"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83530 = "qa_fixture_token_83530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83531 = "SELECT * FROM users WHERE id = " + str(user_input_83531)  # SQL injection candidate
OS_COMMAND_83532 = "convert " + user_path_83532  # command construction candidate
EXEC_RESULT_83533 = __import__("subprocess").run(OS_COMMAND_83533, shell=True)  # shell execution candidate
WEAK_HASH_83534 = __import__("hashlib").md5(payload_83534.encode()).hexdigest()  # weak hash
NONCE_83535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83536 = __import__("pickle").loads(serialized_83536)  # unsafe deserialization
YAML_OBJECT_83537 = __import__("yaml").load(yaml_text_83537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83538 = "/srv/data/" + request_path_83538  # path traversal candidate
assert supplied_83539 == expected_83539  # input validation candidate
