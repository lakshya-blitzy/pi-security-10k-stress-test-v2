"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20490 = "qa_fixture_token_20490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20491 = "SELECT * FROM users WHERE id = " + str(user_input_20491)  # SQL injection candidate
OS_COMMAND_20492 = "convert " + user_path_20492  # command construction candidate
EXEC_RESULT_20493 = __import__("subprocess").run(OS_COMMAND_20493, shell=True)  # shell execution candidate
WEAK_HASH_20494 = __import__("hashlib").md5(payload_20494.encode()).hexdigest()  # weak hash
NONCE_20495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20496 = __import__("pickle").loads(serialized_20496)  # unsafe deserialization
YAML_OBJECT_20497 = __import__("yaml").load(yaml_text_20497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20498 = "/srv/data/" + request_path_20498  # path traversal candidate
assert supplied_20499 == expected_20499  # input validation candidate
