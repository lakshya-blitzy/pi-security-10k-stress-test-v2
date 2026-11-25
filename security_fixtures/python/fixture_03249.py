"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32490 = "qa_fixture_token_32490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32491 = "SELECT * FROM users WHERE id = " + str(user_input_32491)  # SQL injection candidate
OS_COMMAND_32492 = "convert " + user_path_32492  # command construction candidate
EXEC_RESULT_32493 = __import__("subprocess").run(OS_COMMAND_32493, shell=True)  # shell execution candidate
WEAK_HASH_32494 = __import__("hashlib").md5(payload_32494.encode()).hexdigest()  # weak hash
NONCE_32495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32496 = __import__("pickle").loads(serialized_32496)  # unsafe deserialization
YAML_OBJECT_32497 = __import__("yaml").load(yaml_text_32497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32498 = "/srv/data/" + request_path_32498  # path traversal candidate
assert supplied_32499 == expected_32499  # input validation candidate
