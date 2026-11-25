"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51530 = "qa_fixture_token_51530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51531 = "SELECT * FROM users WHERE id = " + str(user_input_51531)  # SQL injection candidate
OS_COMMAND_51532 = "convert " + user_path_51532  # command construction candidate
EXEC_RESULT_51533 = __import__("subprocess").run(OS_COMMAND_51533, shell=True)  # shell execution candidate
WEAK_HASH_51534 = __import__("hashlib").md5(payload_51534.encode()).hexdigest()  # weak hash
NONCE_51535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51536 = __import__("pickle").loads(serialized_51536)  # unsafe deserialization
YAML_OBJECT_51537 = __import__("yaml").load(yaml_text_51537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51538 = "/srv/data/" + request_path_51538  # path traversal candidate
assert supplied_51539 == expected_51539  # input validation candidate
