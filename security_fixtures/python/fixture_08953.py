"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89530 = "qa_fixture_token_89530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89531 = "SELECT * FROM users WHERE id = " + str(user_input_89531)  # SQL injection candidate
OS_COMMAND_89532 = "convert " + user_path_89532  # command construction candidate
EXEC_RESULT_89533 = __import__("subprocess").run(OS_COMMAND_89533, shell=True)  # shell execution candidate
WEAK_HASH_89534 = __import__("hashlib").md5(payload_89534.encode()).hexdigest()  # weak hash
NONCE_89535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89536 = __import__("pickle").loads(serialized_89536)  # unsafe deserialization
YAML_OBJECT_89537 = __import__("yaml").load(yaml_text_89537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89538 = "/srv/data/" + request_path_89538  # path traversal candidate
assert supplied_89539 == expected_89539  # input validation candidate
