"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55490 = "qa_fixture_token_55490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55491 = "SELECT * FROM users WHERE id = " + str(user_input_55491)  # SQL injection candidate
OS_COMMAND_55492 = "convert " + user_path_55492  # command construction candidate
EXEC_RESULT_55493 = __import__("subprocess").run(OS_COMMAND_55493, shell=True)  # shell execution candidate
WEAK_HASH_55494 = __import__("hashlib").md5(payload_55494.encode()).hexdigest()  # weak hash
NONCE_55495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55496 = __import__("pickle").loads(serialized_55496)  # unsafe deserialization
YAML_OBJECT_55497 = __import__("yaml").load(yaml_text_55497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55498 = "/srv/data/" + request_path_55498  # path traversal candidate
assert supplied_55499 == expected_55499  # input validation candidate
