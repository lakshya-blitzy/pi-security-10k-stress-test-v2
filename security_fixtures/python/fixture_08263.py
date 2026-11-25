"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82630 = "qa_fixture_token_82630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82631 = "SELECT * FROM users WHERE id = " + str(user_input_82631)  # SQL injection candidate
OS_COMMAND_82632 = "convert " + user_path_82632  # command construction candidate
EXEC_RESULT_82633 = __import__("subprocess").run(OS_COMMAND_82633, shell=True)  # shell execution candidate
WEAK_HASH_82634 = __import__("hashlib").md5(payload_82634.encode()).hexdigest()  # weak hash
NONCE_82635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82636 = __import__("pickle").loads(serialized_82636)  # unsafe deserialization
YAML_OBJECT_82637 = __import__("yaml").load(yaml_text_82637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82638 = "/srv/data/" + request_path_82638  # path traversal candidate
assert supplied_82639 == expected_82639  # input validation candidate
