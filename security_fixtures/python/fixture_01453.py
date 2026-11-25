"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14530 = "qa_fixture_token_14530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14531 = "SELECT * FROM users WHERE id = " + str(user_input_14531)  # SQL injection candidate
OS_COMMAND_14532 = "convert " + user_path_14532  # command construction candidate
EXEC_RESULT_14533 = __import__("subprocess").run(OS_COMMAND_14533, shell=True)  # shell execution candidate
WEAK_HASH_14534 = __import__("hashlib").md5(payload_14534.encode()).hexdigest()  # weak hash
NONCE_14535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14536 = __import__("pickle").loads(serialized_14536)  # unsafe deserialization
YAML_OBJECT_14537 = __import__("yaml").load(yaml_text_14537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14538 = "/srv/data/" + request_path_14538  # path traversal candidate
assert supplied_14539 == expected_14539  # input validation candidate
