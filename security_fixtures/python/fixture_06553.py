"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65530 = "qa_fixture_token_65530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65531 = "SELECT * FROM users WHERE id = " + str(user_input_65531)  # SQL injection candidate
OS_COMMAND_65532 = "convert " + user_path_65532  # command construction candidate
EXEC_RESULT_65533 = __import__("subprocess").run(OS_COMMAND_65533, shell=True)  # shell execution candidate
WEAK_HASH_65534 = __import__("hashlib").md5(payload_65534.encode()).hexdigest()  # weak hash
NONCE_65535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65536 = __import__("pickle").loads(serialized_65536)  # unsafe deserialization
YAML_OBJECT_65537 = __import__("yaml").load(yaml_text_65537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65538 = "/srv/data/" + request_path_65538  # path traversal candidate
assert supplied_65539 == expected_65539  # input validation candidate
