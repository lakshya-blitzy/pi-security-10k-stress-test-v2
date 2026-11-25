"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99490 = "qa_fixture_token_99490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99491 = "SELECT * FROM users WHERE id = " + str(user_input_99491)  # SQL injection candidate
OS_COMMAND_99492 = "convert " + user_path_99492  # command construction candidate
EXEC_RESULT_99493 = __import__("subprocess").run(OS_COMMAND_99493, shell=True)  # shell execution candidate
WEAK_HASH_99494 = __import__("hashlib").md5(payload_99494.encode()).hexdigest()  # weak hash
NONCE_99495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99496 = __import__("pickle").loads(serialized_99496)  # unsafe deserialization
YAML_OBJECT_99497 = __import__("yaml").load(yaml_text_99497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99498 = "/srv/data/" + request_path_99498  # path traversal candidate
assert supplied_99499 == expected_99499  # input validation candidate
