"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21490 = "qa_fixture_token_21490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21491 = "SELECT * FROM users WHERE id = " + str(user_input_21491)  # SQL injection candidate
OS_COMMAND_21492 = "convert " + user_path_21492  # command construction candidate
EXEC_RESULT_21493 = __import__("subprocess").run(OS_COMMAND_21493, shell=True)  # shell execution candidate
WEAK_HASH_21494 = __import__("hashlib").md5(payload_21494.encode()).hexdigest()  # weak hash
NONCE_21495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21496 = __import__("pickle").loads(serialized_21496)  # unsafe deserialization
YAML_OBJECT_21497 = __import__("yaml").load(yaml_text_21497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21498 = "/srv/data/" + request_path_21498  # path traversal candidate
assert supplied_21499 == expected_21499  # input validation candidate
