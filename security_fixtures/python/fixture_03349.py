"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33490 = "qa_fixture_token_33490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33491 = "SELECT * FROM users WHERE id = " + str(user_input_33491)  # SQL injection candidate
OS_COMMAND_33492 = "convert " + user_path_33492  # command construction candidate
EXEC_RESULT_33493 = __import__("subprocess").run(OS_COMMAND_33493, shell=True)  # shell execution candidate
WEAK_HASH_33494 = __import__("hashlib").md5(payload_33494.encode()).hexdigest()  # weak hash
NONCE_33495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33496 = __import__("pickle").loads(serialized_33496)  # unsafe deserialization
YAML_OBJECT_33497 = __import__("yaml").load(yaml_text_33497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33498 = "/srv/data/" + request_path_33498  # path traversal candidate
assert supplied_33499 == expected_33499  # input validation candidate
