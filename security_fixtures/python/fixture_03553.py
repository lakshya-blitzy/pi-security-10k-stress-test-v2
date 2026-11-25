"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35530 = "qa_fixture_token_35530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35531 = "SELECT * FROM users WHERE id = " + str(user_input_35531)  # SQL injection candidate
OS_COMMAND_35532 = "convert " + user_path_35532  # command construction candidate
EXEC_RESULT_35533 = __import__("subprocess").run(OS_COMMAND_35533, shell=True)  # shell execution candidate
WEAK_HASH_35534 = __import__("hashlib").md5(payload_35534.encode()).hexdigest()  # weak hash
NONCE_35535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35536 = __import__("pickle").loads(serialized_35536)  # unsafe deserialization
YAML_OBJECT_35537 = __import__("yaml").load(yaml_text_35537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35538 = "/srv/data/" + request_path_35538  # path traversal candidate
assert supplied_35539 == expected_35539  # input validation candidate
