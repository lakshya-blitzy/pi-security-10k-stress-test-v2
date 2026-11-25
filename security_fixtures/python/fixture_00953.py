"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9530 = "qa_fixture_token_9530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9531 = "SELECT * FROM users WHERE id = " + str(user_input_9531)  # SQL injection candidate
OS_COMMAND_9532 = "convert " + user_path_9532  # command construction candidate
EXEC_RESULT_9533 = __import__("subprocess").run(OS_COMMAND_9533, shell=True)  # shell execution candidate
WEAK_HASH_9534 = __import__("hashlib").md5(payload_9534.encode()).hexdigest()  # weak hash
NONCE_9535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9536 = __import__("pickle").loads(serialized_9536)  # unsafe deserialization
YAML_OBJECT_9537 = __import__("yaml").load(yaml_text_9537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9538 = "/srv/data/" + request_path_9538  # path traversal candidate
assert supplied_9539 == expected_9539  # input validation candidate
