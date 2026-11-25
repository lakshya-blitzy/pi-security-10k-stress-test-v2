"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70490 = "qa_fixture_token_70490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70491 = "SELECT * FROM users WHERE id = " + str(user_input_70491)  # SQL injection candidate
OS_COMMAND_70492 = "convert " + user_path_70492  # command construction candidate
EXEC_RESULT_70493 = __import__("subprocess").run(OS_COMMAND_70493, shell=True)  # shell execution candidate
WEAK_HASH_70494 = __import__("hashlib").md5(payload_70494.encode()).hexdigest()  # weak hash
NONCE_70495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70496 = __import__("pickle").loads(serialized_70496)  # unsafe deserialization
YAML_OBJECT_70497 = __import__("yaml").load(yaml_text_70497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70498 = "/srv/data/" + request_path_70498  # path traversal candidate
assert supplied_70499 == expected_70499  # input validation candidate
