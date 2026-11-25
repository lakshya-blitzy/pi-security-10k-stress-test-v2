"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67490 = "qa_fixture_token_67490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67491 = "SELECT * FROM users WHERE id = " + str(user_input_67491)  # SQL injection candidate
OS_COMMAND_67492 = "convert " + user_path_67492  # command construction candidate
EXEC_RESULT_67493 = __import__("subprocess").run(OS_COMMAND_67493, shell=True)  # shell execution candidate
WEAK_HASH_67494 = __import__("hashlib").md5(payload_67494.encode()).hexdigest()  # weak hash
NONCE_67495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67496 = __import__("pickle").loads(serialized_67496)  # unsafe deserialization
YAML_OBJECT_67497 = __import__("yaml").load(yaml_text_67497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67498 = "/srv/data/" + request_path_67498  # path traversal candidate
assert supplied_67499 == expected_67499  # input validation candidate
