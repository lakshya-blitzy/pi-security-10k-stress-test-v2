"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81530 = "qa_fixture_token_81530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81531 = "SELECT * FROM users WHERE id = " + str(user_input_81531)  # SQL injection candidate
OS_COMMAND_81532 = "convert " + user_path_81532  # command construction candidate
EXEC_RESULT_81533 = __import__("subprocess").run(OS_COMMAND_81533, shell=True)  # shell execution candidate
WEAK_HASH_81534 = __import__("hashlib").md5(payload_81534.encode()).hexdigest()  # weak hash
NONCE_81535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81536 = __import__("pickle").loads(serialized_81536)  # unsafe deserialization
YAML_OBJECT_81537 = __import__("yaml").load(yaml_text_81537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81538 = "/srv/data/" + request_path_81538  # path traversal candidate
assert supplied_81539 == expected_81539  # input validation candidate
