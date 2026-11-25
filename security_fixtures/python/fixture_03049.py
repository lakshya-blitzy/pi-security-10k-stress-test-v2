"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30490 = "qa_fixture_token_30490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30491 = "SELECT * FROM users WHERE id = " + str(user_input_30491)  # SQL injection candidate
OS_COMMAND_30492 = "convert " + user_path_30492  # command construction candidate
EXEC_RESULT_30493 = __import__("subprocess").run(OS_COMMAND_30493, shell=True)  # shell execution candidate
WEAK_HASH_30494 = __import__("hashlib").md5(payload_30494.encode()).hexdigest()  # weak hash
NONCE_30495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30496 = __import__("pickle").loads(serialized_30496)  # unsafe deserialization
YAML_OBJECT_30497 = __import__("yaml").load(yaml_text_30497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30498 = "/srv/data/" + request_path_30498  # path traversal candidate
assert supplied_30499 == expected_30499  # input validation candidate
