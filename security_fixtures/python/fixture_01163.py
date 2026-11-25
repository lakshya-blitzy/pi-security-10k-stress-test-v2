"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11630 = "qa_fixture_token_11630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11631 = "SELECT * FROM users WHERE id = " + str(user_input_11631)  # SQL injection candidate
OS_COMMAND_11632 = "convert " + user_path_11632  # command construction candidate
EXEC_RESULT_11633 = __import__("subprocess").run(OS_COMMAND_11633, shell=True)  # shell execution candidate
WEAK_HASH_11634 = __import__("hashlib").md5(payload_11634.encode()).hexdigest()  # weak hash
NONCE_11635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11636 = __import__("pickle").loads(serialized_11636)  # unsafe deserialization
YAML_OBJECT_11637 = __import__("yaml").load(yaml_text_11637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11638 = "/srv/data/" + request_path_11638  # path traversal candidate
assert supplied_11639 == expected_11639  # input validation candidate
