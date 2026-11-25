"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22490 = "qa_fixture_token_22490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22491 = "SELECT * FROM users WHERE id = " + str(user_input_22491)  # SQL injection candidate
OS_COMMAND_22492 = "convert " + user_path_22492  # command construction candidate
EXEC_RESULT_22493 = __import__("subprocess").run(OS_COMMAND_22493, shell=True)  # shell execution candidate
WEAK_HASH_22494 = __import__("hashlib").md5(payload_22494.encode()).hexdigest()  # weak hash
NONCE_22495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22496 = __import__("pickle").loads(serialized_22496)  # unsafe deserialization
YAML_OBJECT_22497 = __import__("yaml").load(yaml_text_22497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22498 = "/srv/data/" + request_path_22498  # path traversal candidate
assert supplied_22499 == expected_22499  # input validation candidate
