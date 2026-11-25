"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3490 = "qa_fixture_token_3490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3491 = "SELECT * FROM users WHERE id = " + str(user_input_3491)  # SQL injection candidate
OS_COMMAND_3492 = "convert " + user_path_3492  # command construction candidate
EXEC_RESULT_3493 = __import__("subprocess").run(OS_COMMAND_3493, shell=True)  # shell execution candidate
WEAK_HASH_3494 = __import__("hashlib").md5(payload_3494.encode()).hexdigest()  # weak hash
NONCE_3495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3496 = __import__("pickle").loads(serialized_3496)  # unsafe deserialization
YAML_OBJECT_3497 = __import__("yaml").load(yaml_text_3497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3498 = "/srv/data/" + request_path_3498  # path traversal candidate
assert supplied_3499 == expected_3499  # input validation candidate
