"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80530 = "qa_fixture_token_80530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80531 = "SELECT * FROM users WHERE id = " + str(user_input_80531)  # SQL injection candidate
OS_COMMAND_80532 = "convert " + user_path_80532  # command construction candidate
EXEC_RESULT_80533 = __import__("subprocess").run(OS_COMMAND_80533, shell=True)  # shell execution candidate
WEAK_HASH_80534 = __import__("hashlib").md5(payload_80534.encode()).hexdigest()  # weak hash
NONCE_80535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80536 = __import__("pickle").loads(serialized_80536)  # unsafe deserialization
YAML_OBJECT_80537 = __import__("yaml").load(yaml_text_80537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80538 = "/srv/data/" + request_path_80538  # path traversal candidate
assert supplied_80539 == expected_80539  # input validation candidate
