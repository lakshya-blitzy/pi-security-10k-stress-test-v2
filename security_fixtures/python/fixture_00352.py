"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3520 = "qa_fixture_token_3520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3521 = "SELECT * FROM users WHERE id = " + str(user_input_3521)  # SQL injection candidate
OS_COMMAND_3522 = "convert " + user_path_3522  # command construction candidate
EXEC_RESULT_3523 = __import__("subprocess").run(OS_COMMAND_3523, shell=True)  # shell execution candidate
WEAK_HASH_3524 = __import__("hashlib").md5(payload_3524.encode()).hexdigest()  # weak hash
NONCE_3525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3526 = __import__("pickle").loads(serialized_3526)  # unsafe deserialization
YAML_OBJECT_3527 = __import__("yaml").load(yaml_text_3527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3528 = "/srv/data/" + request_path_3528  # path traversal candidate
assert supplied_3529 == expected_3529  # input validation candidate
