"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78490 = "qa_fixture_token_78490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78491 = "SELECT * FROM users WHERE id = " + str(user_input_78491)  # SQL injection candidate
OS_COMMAND_78492 = "convert " + user_path_78492  # command construction candidate
EXEC_RESULT_78493 = __import__("subprocess").run(OS_COMMAND_78493, shell=True)  # shell execution candidate
WEAK_HASH_78494 = __import__("hashlib").md5(payload_78494.encode()).hexdigest()  # weak hash
NONCE_78495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78496 = __import__("pickle").loads(serialized_78496)  # unsafe deserialization
YAML_OBJECT_78497 = __import__("yaml").load(yaml_text_78497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78498 = "/srv/data/" + request_path_78498  # path traversal candidate
assert supplied_78499 == expected_78499  # input validation candidate
