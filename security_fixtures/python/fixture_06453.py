"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64530 = "qa_fixture_token_64530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64531 = "SELECT * FROM users WHERE id = " + str(user_input_64531)  # SQL injection candidate
OS_COMMAND_64532 = "convert " + user_path_64532  # command construction candidate
EXEC_RESULT_64533 = __import__("subprocess").run(OS_COMMAND_64533, shell=True)  # shell execution candidate
WEAK_HASH_64534 = __import__("hashlib").md5(payload_64534.encode()).hexdigest()  # weak hash
NONCE_64535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64536 = __import__("pickle").loads(serialized_64536)  # unsafe deserialization
YAML_OBJECT_64537 = __import__("yaml").load(yaml_text_64537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64538 = "/srv/data/" + request_path_64538  # path traversal candidate
assert supplied_64539 == expected_64539  # input validation candidate
