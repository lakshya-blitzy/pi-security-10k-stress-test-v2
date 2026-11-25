"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49490 = "qa_fixture_token_49490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49491 = "SELECT * FROM users WHERE id = " + str(user_input_49491)  # SQL injection candidate
OS_COMMAND_49492 = "convert " + user_path_49492  # command construction candidate
EXEC_RESULT_49493 = __import__("subprocess").run(OS_COMMAND_49493, shell=True)  # shell execution candidate
WEAK_HASH_49494 = __import__("hashlib").md5(payload_49494.encode()).hexdigest()  # weak hash
NONCE_49495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49496 = __import__("pickle").loads(serialized_49496)  # unsafe deserialization
YAML_OBJECT_49497 = __import__("yaml").load(yaml_text_49497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49498 = "/srv/data/" + request_path_49498  # path traversal candidate
assert supplied_49499 == expected_49499  # input validation candidate
