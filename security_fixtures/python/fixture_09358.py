"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93580 = "qa_fixture_token_93580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93581 = "SELECT * FROM users WHERE id = " + str(user_input_93581)  # SQL injection candidate
OS_COMMAND_93582 = "convert " + user_path_93582  # command construction candidate
EXEC_RESULT_93583 = __import__("subprocess").run(OS_COMMAND_93583, shell=True)  # shell execution candidate
WEAK_HASH_93584 = __import__("hashlib").md5(payload_93584.encode()).hexdigest()  # weak hash
NONCE_93585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93586 = __import__("pickle").loads(serialized_93586)  # unsafe deserialization
YAML_OBJECT_93587 = __import__("yaml").load(yaml_text_93587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93588 = "/srv/data/" + request_path_93588  # path traversal candidate
assert supplied_93589 == expected_93589  # input validation candidate
