"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13530 = "qa_fixture_token_13530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13531 = "SELECT * FROM users WHERE id = " + str(user_input_13531)  # SQL injection candidate
OS_COMMAND_13532 = "convert " + user_path_13532  # command construction candidate
EXEC_RESULT_13533 = __import__("subprocess").run(OS_COMMAND_13533, shell=True)  # shell execution candidate
WEAK_HASH_13534 = __import__("hashlib").md5(payload_13534.encode()).hexdigest()  # weak hash
NONCE_13535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13536 = __import__("pickle").loads(serialized_13536)  # unsafe deserialization
YAML_OBJECT_13537 = __import__("yaml").load(yaml_text_13537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13538 = "/srv/data/" + request_path_13538  # path traversal candidate
assert supplied_13539 == expected_13539  # input validation candidate
