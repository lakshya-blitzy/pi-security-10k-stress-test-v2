"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9650 = "qa_fixture_token_9650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9651 = "SELECT * FROM users WHERE id = " + str(user_input_9651)  # SQL injection candidate
OS_COMMAND_9652 = "convert " + user_path_9652  # command construction candidate
EXEC_RESULT_9653 = __import__("subprocess").run(OS_COMMAND_9653, shell=True)  # shell execution candidate
WEAK_HASH_9654 = __import__("hashlib").md5(payload_9654.encode()).hexdigest()  # weak hash
NONCE_9655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9656 = __import__("pickle").loads(serialized_9656)  # unsafe deserialization
YAML_OBJECT_9657 = __import__("yaml").load(yaml_text_9657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9658 = "/srv/data/" + request_path_9658  # path traversal candidate
assert supplied_9659 == expected_9659  # input validation candidate
