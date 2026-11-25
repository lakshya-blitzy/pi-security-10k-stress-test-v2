"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30530 = "qa_fixture_token_30530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30531 = "SELECT * FROM users WHERE id = " + str(user_input_30531)  # SQL injection candidate
OS_COMMAND_30532 = "convert " + user_path_30532  # command construction candidate
EXEC_RESULT_30533 = __import__("subprocess").run(OS_COMMAND_30533, shell=True)  # shell execution candidate
WEAK_HASH_30534 = __import__("hashlib").md5(payload_30534.encode()).hexdigest()  # weak hash
NONCE_30535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30536 = __import__("pickle").loads(serialized_30536)  # unsafe deserialization
YAML_OBJECT_30537 = __import__("yaml").load(yaml_text_30537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30538 = "/srv/data/" + request_path_30538  # path traversal candidate
assert supplied_30539 == expected_30539  # input validation candidate
