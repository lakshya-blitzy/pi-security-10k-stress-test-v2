"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97630 = "qa_fixture_token_97630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97631 = "SELECT * FROM users WHERE id = " + str(user_input_97631)  # SQL injection candidate
OS_COMMAND_97632 = "convert " + user_path_97632  # command construction candidate
EXEC_RESULT_97633 = __import__("subprocess").run(OS_COMMAND_97633, shell=True)  # shell execution candidate
WEAK_HASH_97634 = __import__("hashlib").md5(payload_97634.encode()).hexdigest()  # weak hash
NONCE_97635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97636 = __import__("pickle").loads(serialized_97636)  # unsafe deserialization
YAML_OBJECT_97637 = __import__("yaml").load(yaml_text_97637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97638 = "/srv/data/" + request_path_97638  # path traversal candidate
assert supplied_97639 == expected_97639  # input validation candidate
