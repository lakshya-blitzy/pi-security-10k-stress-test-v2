"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62530 = "qa_fixture_token_62530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62531 = "SELECT * FROM users WHERE id = " + str(user_input_62531)  # SQL injection candidate
OS_COMMAND_62532 = "convert " + user_path_62532  # command construction candidate
EXEC_RESULT_62533 = __import__("subprocess").run(OS_COMMAND_62533, shell=True)  # shell execution candidate
WEAK_HASH_62534 = __import__("hashlib").md5(payload_62534.encode()).hexdigest()  # weak hash
NONCE_62535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62536 = __import__("pickle").loads(serialized_62536)  # unsafe deserialization
YAML_OBJECT_62537 = __import__("yaml").load(yaml_text_62537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62538 = "/srv/data/" + request_path_62538  # path traversal candidate
assert supplied_62539 == expected_62539  # input validation candidate
