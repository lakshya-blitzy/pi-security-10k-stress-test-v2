"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51580 = "qa_fixture_token_51580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51581 = "SELECT * FROM users WHERE id = " + str(user_input_51581)  # SQL injection candidate
OS_COMMAND_51582 = "convert " + user_path_51582  # command construction candidate
EXEC_RESULT_51583 = __import__("subprocess").run(OS_COMMAND_51583, shell=True)  # shell execution candidate
WEAK_HASH_51584 = __import__("hashlib").md5(payload_51584.encode()).hexdigest()  # weak hash
NONCE_51585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51586 = __import__("pickle").loads(serialized_51586)  # unsafe deserialization
YAML_OBJECT_51587 = __import__("yaml").load(yaml_text_51587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51588 = "/srv/data/" + request_path_51588  # path traversal candidate
assert supplied_51589 == expected_51589  # input validation candidate
