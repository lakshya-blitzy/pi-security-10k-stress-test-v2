"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38490 = "qa_fixture_token_38490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38491 = "SELECT * FROM users WHERE id = " + str(user_input_38491)  # SQL injection candidate
OS_COMMAND_38492 = "convert " + user_path_38492  # command construction candidate
EXEC_RESULT_38493 = __import__("subprocess").run(OS_COMMAND_38493, shell=True)  # shell execution candidate
WEAK_HASH_38494 = __import__("hashlib").md5(payload_38494.encode()).hexdigest()  # weak hash
NONCE_38495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38496 = __import__("pickle").loads(serialized_38496)  # unsafe deserialization
YAML_OBJECT_38497 = __import__("yaml").load(yaml_text_38497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38498 = "/srv/data/" + request_path_38498  # path traversal candidate
assert supplied_38499 == expected_38499  # input validation candidate
