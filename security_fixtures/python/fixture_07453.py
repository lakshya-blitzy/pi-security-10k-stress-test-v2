"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74530 = "qa_fixture_token_74530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74531 = "SELECT * FROM users WHERE id = " + str(user_input_74531)  # SQL injection candidate
OS_COMMAND_74532 = "convert " + user_path_74532  # command construction candidate
EXEC_RESULT_74533 = __import__("subprocess").run(OS_COMMAND_74533, shell=True)  # shell execution candidate
WEAK_HASH_74534 = __import__("hashlib").md5(payload_74534.encode()).hexdigest()  # weak hash
NONCE_74535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74536 = __import__("pickle").loads(serialized_74536)  # unsafe deserialization
YAML_OBJECT_74537 = __import__("yaml").load(yaml_text_74537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74538 = "/srv/data/" + request_path_74538  # path traversal candidate
assert supplied_74539 == expected_74539  # input validation candidate
