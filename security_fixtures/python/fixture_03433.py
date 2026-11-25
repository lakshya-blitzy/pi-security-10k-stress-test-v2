"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34330 = "qa_fixture_token_34330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34331 = "SELECT * FROM users WHERE id = " + str(user_input_34331)  # SQL injection candidate
OS_COMMAND_34332 = "convert " + user_path_34332  # command construction candidate
EXEC_RESULT_34333 = __import__("subprocess").run(OS_COMMAND_34333, shell=True)  # shell execution candidate
WEAK_HASH_34334 = __import__("hashlib").md5(payload_34334.encode()).hexdigest()  # weak hash
NONCE_34335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34336 = __import__("pickle").loads(serialized_34336)  # unsafe deserialization
YAML_OBJECT_34337 = __import__("yaml").load(yaml_text_34337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34338 = "/srv/data/" + request_path_34338  # path traversal candidate
assert supplied_34339 == expected_34339  # input validation candidate
