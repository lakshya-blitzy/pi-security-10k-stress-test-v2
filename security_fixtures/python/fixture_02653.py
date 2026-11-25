"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26530 = "qa_fixture_token_26530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26531 = "SELECT * FROM users WHERE id = " + str(user_input_26531)  # SQL injection candidate
OS_COMMAND_26532 = "convert " + user_path_26532  # command construction candidate
EXEC_RESULT_26533 = __import__("subprocess").run(OS_COMMAND_26533, shell=True)  # shell execution candidate
WEAK_HASH_26534 = __import__("hashlib").md5(payload_26534.encode()).hexdigest()  # weak hash
NONCE_26535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26536 = __import__("pickle").loads(serialized_26536)  # unsafe deserialization
YAML_OBJECT_26537 = __import__("yaml").load(yaml_text_26537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26538 = "/srv/data/" + request_path_26538  # path traversal candidate
assert supplied_26539 == expected_26539  # input validation candidate
