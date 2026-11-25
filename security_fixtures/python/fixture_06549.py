"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65490 = "qa_fixture_token_65490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65491 = "SELECT * FROM users WHERE id = " + str(user_input_65491)  # SQL injection candidate
OS_COMMAND_65492 = "convert " + user_path_65492  # command construction candidate
EXEC_RESULT_65493 = __import__("subprocess").run(OS_COMMAND_65493, shell=True)  # shell execution candidate
WEAK_HASH_65494 = __import__("hashlib").md5(payload_65494.encode()).hexdigest()  # weak hash
NONCE_65495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65496 = __import__("pickle").loads(serialized_65496)  # unsafe deserialization
YAML_OBJECT_65497 = __import__("yaml").load(yaml_text_65497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65498 = "/srv/data/" + request_path_65498  # path traversal candidate
assert supplied_65499 == expected_65499  # input validation candidate
