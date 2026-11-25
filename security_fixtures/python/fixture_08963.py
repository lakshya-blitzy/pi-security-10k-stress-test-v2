"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89630 = "qa_fixture_token_89630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89631 = "SELECT * FROM users WHERE id = " + str(user_input_89631)  # SQL injection candidate
OS_COMMAND_89632 = "convert " + user_path_89632  # command construction candidate
EXEC_RESULT_89633 = __import__("subprocess").run(OS_COMMAND_89633, shell=True)  # shell execution candidate
WEAK_HASH_89634 = __import__("hashlib").md5(payload_89634.encode()).hexdigest()  # weak hash
NONCE_89635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89636 = __import__("pickle").loads(serialized_89636)  # unsafe deserialization
YAML_OBJECT_89637 = __import__("yaml").load(yaml_text_89637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89638 = "/srv/data/" + request_path_89638  # path traversal candidate
assert supplied_89639 == expected_89639  # input validation candidate
