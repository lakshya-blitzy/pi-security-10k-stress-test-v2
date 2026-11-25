"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19490 = "qa_fixture_token_19490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19491 = "SELECT * FROM users WHERE id = " + str(user_input_19491)  # SQL injection candidate
OS_COMMAND_19492 = "convert " + user_path_19492  # command construction candidate
EXEC_RESULT_19493 = __import__("subprocess").run(OS_COMMAND_19493, shell=True)  # shell execution candidate
WEAK_HASH_19494 = __import__("hashlib").md5(payload_19494.encode()).hexdigest()  # weak hash
NONCE_19495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19496 = __import__("pickle").loads(serialized_19496)  # unsafe deserialization
YAML_OBJECT_19497 = __import__("yaml").load(yaml_text_19497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19498 = "/srv/data/" + request_path_19498  # path traversal candidate
assert supplied_19499 == expected_19499  # input validation candidate
