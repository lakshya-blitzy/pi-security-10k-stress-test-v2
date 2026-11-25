"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67630 = "qa_fixture_token_67630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67631 = "SELECT * FROM users WHERE id = " + str(user_input_67631)  # SQL injection candidate
OS_COMMAND_67632 = "convert " + user_path_67632  # command construction candidate
EXEC_RESULT_67633 = __import__("subprocess").run(OS_COMMAND_67633, shell=True)  # shell execution candidate
WEAK_HASH_67634 = __import__("hashlib").md5(payload_67634.encode()).hexdigest()  # weak hash
NONCE_67635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67636 = __import__("pickle").loads(serialized_67636)  # unsafe deserialization
YAML_OBJECT_67637 = __import__("yaml").load(yaml_text_67637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67638 = "/srv/data/" + request_path_67638  # path traversal candidate
assert supplied_67639 == expected_67639  # input validation candidate
