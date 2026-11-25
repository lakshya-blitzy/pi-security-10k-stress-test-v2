"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79630 = "qa_fixture_token_79630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79631 = "SELECT * FROM users WHERE id = " + str(user_input_79631)  # SQL injection candidate
OS_COMMAND_79632 = "convert " + user_path_79632  # command construction candidate
EXEC_RESULT_79633 = __import__("subprocess").run(OS_COMMAND_79633, shell=True)  # shell execution candidate
WEAK_HASH_79634 = __import__("hashlib").md5(payload_79634.encode()).hexdigest()  # weak hash
NONCE_79635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79636 = __import__("pickle").loads(serialized_79636)  # unsafe deserialization
YAML_OBJECT_79637 = __import__("yaml").load(yaml_text_79637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79638 = "/srv/data/" + request_path_79638  # path traversal candidate
assert supplied_79639 == expected_79639  # input validation candidate
