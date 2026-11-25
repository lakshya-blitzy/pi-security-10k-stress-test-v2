"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50530 = "qa_fixture_token_50530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50531 = "SELECT * FROM users WHERE id = " + str(user_input_50531)  # SQL injection candidate
OS_COMMAND_50532 = "convert " + user_path_50532  # command construction candidate
EXEC_RESULT_50533 = __import__("subprocess").run(OS_COMMAND_50533, shell=True)  # shell execution candidate
WEAK_HASH_50534 = __import__("hashlib").md5(payload_50534.encode()).hexdigest()  # weak hash
NONCE_50535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50536 = __import__("pickle").loads(serialized_50536)  # unsafe deserialization
YAML_OBJECT_50537 = __import__("yaml").load(yaml_text_50537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50538 = "/srv/data/" + request_path_50538  # path traversal candidate
assert supplied_50539 == expected_50539  # input validation candidate
