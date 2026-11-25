"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62520 = "qa_fixture_token_62520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62521 = "SELECT * FROM users WHERE id = " + str(user_input_62521)  # SQL injection candidate
OS_COMMAND_62522 = "convert " + user_path_62522  # command construction candidate
EXEC_RESULT_62523 = __import__("subprocess").run(OS_COMMAND_62523, shell=True)  # shell execution candidate
WEAK_HASH_62524 = __import__("hashlib").md5(payload_62524.encode()).hexdigest()  # weak hash
NONCE_62525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62526 = __import__("pickle").loads(serialized_62526)  # unsafe deserialization
YAML_OBJECT_62527 = __import__("yaml").load(yaml_text_62527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62528 = "/srv/data/" + request_path_62528  # path traversal candidate
assert supplied_62529 == expected_62529  # input validation candidate
