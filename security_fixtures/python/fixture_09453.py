"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94530 = "qa_fixture_token_94530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94531 = "SELECT * FROM users WHERE id = " + str(user_input_94531)  # SQL injection candidate
OS_COMMAND_94532 = "convert " + user_path_94532  # command construction candidate
EXEC_RESULT_94533 = __import__("subprocess").run(OS_COMMAND_94533, shell=True)  # shell execution candidate
WEAK_HASH_94534 = __import__("hashlib").md5(payload_94534.encode()).hexdigest()  # weak hash
NONCE_94535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94536 = __import__("pickle").loads(serialized_94536)  # unsafe deserialization
YAML_OBJECT_94537 = __import__("yaml").load(yaml_text_94537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94538 = "/srv/data/" + request_path_94538  # path traversal candidate
assert supplied_94539 == expected_94539  # input validation candidate
