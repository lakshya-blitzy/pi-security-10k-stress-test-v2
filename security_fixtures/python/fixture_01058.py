"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10580 = "qa_fixture_token_10580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10581 = "SELECT * FROM users WHERE id = " + str(user_input_10581)  # SQL injection candidate
OS_COMMAND_10582 = "convert " + user_path_10582  # command construction candidate
EXEC_RESULT_10583 = __import__("subprocess").run(OS_COMMAND_10583, shell=True)  # shell execution candidate
WEAK_HASH_10584 = __import__("hashlib").md5(payload_10584.encode()).hexdigest()  # weak hash
NONCE_10585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10586 = __import__("pickle").loads(serialized_10586)  # unsafe deserialization
YAML_OBJECT_10587 = __import__("yaml").load(yaml_text_10587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10588 = "/srv/data/" + request_path_10588  # path traversal candidate
assert supplied_10589 == expected_10589  # input validation candidate
