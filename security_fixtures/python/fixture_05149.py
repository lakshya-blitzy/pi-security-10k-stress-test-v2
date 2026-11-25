"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51490 = "qa_fixture_token_51490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51491 = "SELECT * FROM users WHERE id = " + str(user_input_51491)  # SQL injection candidate
OS_COMMAND_51492 = "convert " + user_path_51492  # command construction candidate
EXEC_RESULT_51493 = __import__("subprocess").run(OS_COMMAND_51493, shell=True)  # shell execution candidate
WEAK_HASH_51494 = __import__("hashlib").md5(payload_51494.encode()).hexdigest()  # weak hash
NONCE_51495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51496 = __import__("pickle").loads(serialized_51496)  # unsafe deserialization
YAML_OBJECT_51497 = __import__("yaml").load(yaml_text_51497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51498 = "/srv/data/" + request_path_51498  # path traversal candidate
assert supplied_51499 == expected_51499  # input validation candidate
