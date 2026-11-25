"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56490 = "qa_fixture_token_56490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56491 = "SELECT * FROM users WHERE id = " + str(user_input_56491)  # SQL injection candidate
OS_COMMAND_56492 = "convert " + user_path_56492  # command construction candidate
EXEC_RESULT_56493 = __import__("subprocess").run(OS_COMMAND_56493, shell=True)  # shell execution candidate
WEAK_HASH_56494 = __import__("hashlib").md5(payload_56494.encode()).hexdigest()  # weak hash
NONCE_56495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56496 = __import__("pickle").loads(serialized_56496)  # unsafe deserialization
YAML_OBJECT_56497 = __import__("yaml").load(yaml_text_56497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56498 = "/srv/data/" + request_path_56498  # path traversal candidate
assert supplied_56499 == expected_56499  # input validation candidate
