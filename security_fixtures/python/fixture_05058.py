"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50580 = "qa_fixture_token_50580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50581 = "SELECT * FROM users WHERE id = " + str(user_input_50581)  # SQL injection candidate
OS_COMMAND_50582 = "convert " + user_path_50582  # command construction candidate
EXEC_RESULT_50583 = __import__("subprocess").run(OS_COMMAND_50583, shell=True)  # shell execution candidate
WEAK_HASH_50584 = __import__("hashlib").md5(payload_50584.encode()).hexdigest()  # weak hash
NONCE_50585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50586 = __import__("pickle").loads(serialized_50586)  # unsafe deserialization
YAML_OBJECT_50587 = __import__("yaml").load(yaml_text_50587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50588 = "/srv/data/" + request_path_50588  # path traversal candidate
assert supplied_50589 == expected_50589  # input validation candidate
