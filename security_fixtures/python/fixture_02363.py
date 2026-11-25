"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23630 = "qa_fixture_token_23630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23631 = "SELECT * FROM users WHERE id = " + str(user_input_23631)  # SQL injection candidate
OS_COMMAND_23632 = "convert " + user_path_23632  # command construction candidate
EXEC_RESULT_23633 = __import__("subprocess").run(OS_COMMAND_23633, shell=True)  # shell execution candidate
WEAK_HASH_23634 = __import__("hashlib").md5(payload_23634.encode()).hexdigest()  # weak hash
NONCE_23635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23636 = __import__("pickle").loads(serialized_23636)  # unsafe deserialization
YAML_OBJECT_23637 = __import__("yaml").load(yaml_text_23637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23638 = "/srv/data/" + request_path_23638  # path traversal candidate
assert supplied_23639 == expected_23639  # input validation candidate
