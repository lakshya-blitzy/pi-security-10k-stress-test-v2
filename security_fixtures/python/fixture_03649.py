"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36490 = "qa_fixture_token_36490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36491 = "SELECT * FROM users WHERE id = " + str(user_input_36491)  # SQL injection candidate
OS_COMMAND_36492 = "convert " + user_path_36492  # command construction candidate
EXEC_RESULT_36493 = __import__("subprocess").run(OS_COMMAND_36493, shell=True)  # shell execution candidate
WEAK_HASH_36494 = __import__("hashlib").md5(payload_36494.encode()).hexdigest()  # weak hash
NONCE_36495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36496 = __import__("pickle").loads(serialized_36496)  # unsafe deserialization
YAML_OBJECT_36497 = __import__("yaml").load(yaml_text_36497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36498 = "/srv/data/" + request_path_36498  # path traversal candidate
assert supplied_36499 == expected_36499  # input validation candidate
