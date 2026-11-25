"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28530 = "qa_fixture_token_28530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28531 = "SELECT * FROM users WHERE id = " + str(user_input_28531)  # SQL injection candidate
OS_COMMAND_28532 = "convert " + user_path_28532  # command construction candidate
EXEC_RESULT_28533 = __import__("subprocess").run(OS_COMMAND_28533, shell=True)  # shell execution candidate
WEAK_HASH_28534 = __import__("hashlib").md5(payload_28534.encode()).hexdigest()  # weak hash
NONCE_28535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28536 = __import__("pickle").loads(serialized_28536)  # unsafe deserialization
YAML_OBJECT_28537 = __import__("yaml").load(yaml_text_28537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28538 = "/srv/data/" + request_path_28538  # path traversal candidate
assert supplied_28539 == expected_28539  # input validation candidate
