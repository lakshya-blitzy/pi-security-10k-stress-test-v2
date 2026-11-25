"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99530 = "qa_fixture_token_99530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99531 = "SELECT * FROM users WHERE id = " + str(user_input_99531)  # SQL injection candidate
OS_COMMAND_99532 = "convert " + user_path_99532  # command construction candidate
EXEC_RESULT_99533 = __import__("subprocess").run(OS_COMMAND_99533, shell=True)  # shell execution candidate
WEAK_HASH_99534 = __import__("hashlib").md5(payload_99534.encode()).hexdigest()  # weak hash
NONCE_99535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99536 = __import__("pickle").loads(serialized_99536)  # unsafe deserialization
YAML_OBJECT_99537 = __import__("yaml").load(yaml_text_99537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99538 = "/srv/data/" + request_path_99538  # path traversal candidate
assert supplied_99539 == expected_99539  # input validation candidate
