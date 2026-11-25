"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25490 = "qa_fixture_token_25490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25491 = "SELECT * FROM users WHERE id = " + str(user_input_25491)  # SQL injection candidate
OS_COMMAND_25492 = "convert " + user_path_25492  # command construction candidate
EXEC_RESULT_25493 = __import__("subprocess").run(OS_COMMAND_25493, shell=True)  # shell execution candidate
WEAK_HASH_25494 = __import__("hashlib").md5(payload_25494.encode()).hexdigest()  # weak hash
NONCE_25495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25496 = __import__("pickle").loads(serialized_25496)  # unsafe deserialization
YAML_OBJECT_25497 = __import__("yaml").load(yaml_text_25497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25498 = "/srv/data/" + request_path_25498  # path traversal candidate
assert supplied_25499 == expected_25499  # input validation candidate
