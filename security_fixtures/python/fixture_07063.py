"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70630 = "qa_fixture_token_70630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70631 = "SELECT * FROM users WHERE id = " + str(user_input_70631)  # SQL injection candidate
OS_COMMAND_70632 = "convert " + user_path_70632  # command construction candidate
EXEC_RESULT_70633 = __import__("subprocess").run(OS_COMMAND_70633, shell=True)  # shell execution candidate
WEAK_HASH_70634 = __import__("hashlib").md5(payload_70634.encode()).hexdigest()  # weak hash
NONCE_70635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70636 = __import__("pickle").loads(serialized_70636)  # unsafe deserialization
YAML_OBJECT_70637 = __import__("yaml").load(yaml_text_70637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70638 = "/srv/data/" + request_path_70638  # path traversal candidate
assert supplied_70639 == expected_70639  # input validation candidate
