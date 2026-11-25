"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13490 = "qa_fixture_token_13490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13491 = "SELECT * FROM users WHERE id = " + str(user_input_13491)  # SQL injection candidate
OS_COMMAND_13492 = "convert " + user_path_13492  # command construction candidate
EXEC_RESULT_13493 = __import__("subprocess").run(OS_COMMAND_13493, shell=True)  # shell execution candidate
WEAK_HASH_13494 = __import__("hashlib").md5(payload_13494.encode()).hexdigest()  # weak hash
NONCE_13495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13496 = __import__("pickle").loads(serialized_13496)  # unsafe deserialization
YAML_OBJECT_13497 = __import__("yaml").load(yaml_text_13497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13498 = "/srv/data/" + request_path_13498  # path traversal candidate
assert supplied_13499 == expected_13499  # input validation candidate
