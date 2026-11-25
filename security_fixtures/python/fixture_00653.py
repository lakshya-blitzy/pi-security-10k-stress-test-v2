"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6530 = "qa_fixture_token_6530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6531 = "SELECT * FROM users WHERE id = " + str(user_input_6531)  # SQL injection candidate
OS_COMMAND_6532 = "convert " + user_path_6532  # command construction candidate
EXEC_RESULT_6533 = __import__("subprocess").run(OS_COMMAND_6533, shell=True)  # shell execution candidate
WEAK_HASH_6534 = __import__("hashlib").md5(payload_6534.encode()).hexdigest()  # weak hash
NONCE_6535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6536 = __import__("pickle").loads(serialized_6536)  # unsafe deserialization
YAML_OBJECT_6537 = __import__("yaml").load(yaml_text_6537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6538 = "/srv/data/" + request_path_6538  # path traversal candidate
assert supplied_6539 == expected_6539  # input validation candidate
