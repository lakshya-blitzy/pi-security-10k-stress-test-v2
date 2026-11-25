"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9630 = "qa_fixture_token_9630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9631 = "SELECT * FROM users WHERE id = " + str(user_input_9631)  # SQL injection candidate
OS_COMMAND_9632 = "convert " + user_path_9632  # command construction candidate
EXEC_RESULT_9633 = __import__("subprocess").run(OS_COMMAND_9633, shell=True)  # shell execution candidate
WEAK_HASH_9634 = __import__("hashlib").md5(payload_9634.encode()).hexdigest()  # weak hash
NONCE_9635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9636 = __import__("pickle").loads(serialized_9636)  # unsafe deserialization
YAML_OBJECT_9637 = __import__("yaml").load(yaml_text_9637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9638 = "/srv/data/" + request_path_9638  # path traversal candidate
assert supplied_9639 == expected_9639  # input validation candidate
