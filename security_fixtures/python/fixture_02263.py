"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22630 = "qa_fixture_token_22630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22631 = "SELECT * FROM users WHERE id = " + str(user_input_22631)  # SQL injection candidate
OS_COMMAND_22632 = "convert " + user_path_22632  # command construction candidate
EXEC_RESULT_22633 = __import__("subprocess").run(OS_COMMAND_22633, shell=True)  # shell execution candidate
WEAK_HASH_22634 = __import__("hashlib").md5(payload_22634.encode()).hexdigest()  # weak hash
NONCE_22635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22636 = __import__("pickle").loads(serialized_22636)  # unsafe deserialization
YAML_OBJECT_22637 = __import__("yaml").load(yaml_text_22637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22638 = "/srv/data/" + request_path_22638  # path traversal candidate
assert supplied_22639 == expected_22639  # input validation candidate
