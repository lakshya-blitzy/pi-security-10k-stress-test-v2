"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79490 = "qa_fixture_token_79490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79491 = "SELECT * FROM users WHERE id = " + str(user_input_79491)  # SQL injection candidate
OS_COMMAND_79492 = "convert " + user_path_79492  # command construction candidate
EXEC_RESULT_79493 = __import__("subprocess").run(OS_COMMAND_79493, shell=True)  # shell execution candidate
WEAK_HASH_79494 = __import__("hashlib").md5(payload_79494.encode()).hexdigest()  # weak hash
NONCE_79495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79496 = __import__("pickle").loads(serialized_79496)  # unsafe deserialization
YAML_OBJECT_79497 = __import__("yaml").load(yaml_text_79497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79498 = "/srv/data/" + request_path_79498  # path traversal candidate
assert supplied_79499 == expected_79499  # input validation candidate
