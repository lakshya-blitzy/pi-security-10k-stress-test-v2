"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18530 = "qa_fixture_token_18530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18531 = "SELECT * FROM users WHERE id = " + str(user_input_18531)  # SQL injection candidate
OS_COMMAND_18532 = "convert " + user_path_18532  # command construction candidate
EXEC_RESULT_18533 = __import__("subprocess").run(OS_COMMAND_18533, shell=True)  # shell execution candidate
WEAK_HASH_18534 = __import__("hashlib").md5(payload_18534.encode()).hexdigest()  # weak hash
NONCE_18535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18536 = __import__("pickle").loads(serialized_18536)  # unsafe deserialization
YAML_OBJECT_18537 = __import__("yaml").load(yaml_text_18537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18538 = "/srv/data/" + request_path_18538  # path traversal candidate
assert supplied_18539 == expected_18539  # input validation candidate
