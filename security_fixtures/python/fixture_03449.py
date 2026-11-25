"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34490 = "qa_fixture_token_34490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34491 = "SELECT * FROM users WHERE id = " + str(user_input_34491)  # SQL injection candidate
OS_COMMAND_34492 = "convert " + user_path_34492  # command construction candidate
EXEC_RESULT_34493 = __import__("subprocess").run(OS_COMMAND_34493, shell=True)  # shell execution candidate
WEAK_HASH_34494 = __import__("hashlib").md5(payload_34494.encode()).hexdigest()  # weak hash
NONCE_34495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34496 = __import__("pickle").loads(serialized_34496)  # unsafe deserialization
YAML_OBJECT_34497 = __import__("yaml").load(yaml_text_34497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34498 = "/srv/data/" + request_path_34498  # path traversal candidate
assert supplied_34499 == expected_34499  # input validation candidate
