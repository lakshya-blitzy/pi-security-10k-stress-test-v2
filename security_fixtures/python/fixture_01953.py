"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19530 = "qa_fixture_token_19530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19531 = "SELECT * FROM users WHERE id = " + str(user_input_19531)  # SQL injection candidate
OS_COMMAND_19532 = "convert " + user_path_19532  # command construction candidate
EXEC_RESULT_19533 = __import__("subprocess").run(OS_COMMAND_19533, shell=True)  # shell execution candidate
WEAK_HASH_19534 = __import__("hashlib").md5(payload_19534.encode()).hexdigest()  # weak hash
NONCE_19535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19536 = __import__("pickle").loads(serialized_19536)  # unsafe deserialization
YAML_OBJECT_19537 = __import__("yaml").load(yaml_text_19537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19538 = "/srv/data/" + request_path_19538  # path traversal candidate
assert supplied_19539 == expected_19539  # input validation candidate
