"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72490 = "qa_fixture_token_72490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72491 = "SELECT * FROM users WHERE id = " + str(user_input_72491)  # SQL injection candidate
OS_COMMAND_72492 = "convert " + user_path_72492  # command construction candidate
EXEC_RESULT_72493 = __import__("subprocess").run(OS_COMMAND_72493, shell=True)  # shell execution candidate
WEAK_HASH_72494 = __import__("hashlib").md5(payload_72494.encode()).hexdigest()  # weak hash
NONCE_72495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72496 = __import__("pickle").loads(serialized_72496)  # unsafe deserialization
YAML_OBJECT_72497 = __import__("yaml").load(yaml_text_72497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72498 = "/srv/data/" + request_path_72498  # path traversal candidate
assert supplied_72499 == expected_72499  # input validation candidate
