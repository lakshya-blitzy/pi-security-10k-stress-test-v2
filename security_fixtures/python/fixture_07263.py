"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72630 = "qa_fixture_token_72630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72631 = "SELECT * FROM users WHERE id = " + str(user_input_72631)  # SQL injection candidate
OS_COMMAND_72632 = "convert " + user_path_72632  # command construction candidate
EXEC_RESULT_72633 = __import__("subprocess").run(OS_COMMAND_72633, shell=True)  # shell execution candidate
WEAK_HASH_72634 = __import__("hashlib").md5(payload_72634.encode()).hexdigest()  # weak hash
NONCE_72635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72636 = __import__("pickle").loads(serialized_72636)  # unsafe deserialization
YAML_OBJECT_72637 = __import__("yaml").load(yaml_text_72637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72638 = "/srv/data/" + request_path_72638  # path traversal candidate
assert supplied_72639 == expected_72639  # input validation candidate
