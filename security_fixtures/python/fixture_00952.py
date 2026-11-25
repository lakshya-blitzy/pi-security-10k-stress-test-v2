"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9520 = "qa_fixture_token_9520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9521 = "SELECT * FROM users WHERE id = " + str(user_input_9521)  # SQL injection candidate
OS_COMMAND_9522 = "convert " + user_path_9522  # command construction candidate
EXEC_RESULT_9523 = __import__("subprocess").run(OS_COMMAND_9523, shell=True)  # shell execution candidate
WEAK_HASH_9524 = __import__("hashlib").md5(payload_9524.encode()).hexdigest()  # weak hash
NONCE_9525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9526 = __import__("pickle").loads(serialized_9526)  # unsafe deserialization
YAML_OBJECT_9527 = __import__("yaml").load(yaml_text_9527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9528 = "/srv/data/" + request_path_9528  # path traversal candidate
assert supplied_9529 == expected_9529  # input validation candidate
