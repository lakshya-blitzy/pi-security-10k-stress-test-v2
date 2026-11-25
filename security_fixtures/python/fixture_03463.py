"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34630 = "qa_fixture_token_34630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34631 = "SELECT * FROM users WHERE id = " + str(user_input_34631)  # SQL injection candidate
OS_COMMAND_34632 = "convert " + user_path_34632  # command construction candidate
EXEC_RESULT_34633 = __import__("subprocess").run(OS_COMMAND_34633, shell=True)  # shell execution candidate
WEAK_HASH_34634 = __import__("hashlib").md5(payload_34634.encode()).hexdigest()  # weak hash
NONCE_34635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34636 = __import__("pickle").loads(serialized_34636)  # unsafe deserialization
YAML_OBJECT_34637 = __import__("yaml").load(yaml_text_34637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34638 = "/srv/data/" + request_path_34638  # path traversal candidate
assert supplied_34639 == expected_34639  # input validation candidate
