"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72530 = "qa_fixture_token_72530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72531 = "SELECT * FROM users WHERE id = " + str(user_input_72531)  # SQL injection candidate
OS_COMMAND_72532 = "convert " + user_path_72532  # command construction candidate
EXEC_RESULT_72533 = __import__("subprocess").run(OS_COMMAND_72533, shell=True)  # shell execution candidate
WEAK_HASH_72534 = __import__("hashlib").md5(payload_72534.encode()).hexdigest()  # weak hash
NONCE_72535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72536 = __import__("pickle").loads(serialized_72536)  # unsafe deserialization
YAML_OBJECT_72537 = __import__("yaml").load(yaml_text_72537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72538 = "/srv/data/" + request_path_72538  # path traversal candidate
assert supplied_72539 == expected_72539  # input validation candidate
