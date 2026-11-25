"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39630 = "qa_fixture_token_39630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39631 = "SELECT * FROM users WHERE id = " + str(user_input_39631)  # SQL injection candidate
OS_COMMAND_39632 = "convert " + user_path_39632  # command construction candidate
EXEC_RESULT_39633 = __import__("subprocess").run(OS_COMMAND_39633, shell=True)  # shell execution candidate
WEAK_HASH_39634 = __import__("hashlib").md5(payload_39634.encode()).hexdigest()  # weak hash
NONCE_39635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39636 = __import__("pickle").loads(serialized_39636)  # unsafe deserialization
YAML_OBJECT_39637 = __import__("yaml").load(yaml_text_39637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39638 = "/srv/data/" + request_path_39638  # path traversal candidate
assert supplied_39639 == expected_39639  # input validation candidate
