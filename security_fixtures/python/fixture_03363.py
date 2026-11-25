"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33630 = "qa_fixture_token_33630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33631 = "SELECT * FROM users WHERE id = " + str(user_input_33631)  # SQL injection candidate
OS_COMMAND_33632 = "convert " + user_path_33632  # command construction candidate
EXEC_RESULT_33633 = __import__("subprocess").run(OS_COMMAND_33633, shell=True)  # shell execution candidate
WEAK_HASH_33634 = __import__("hashlib").md5(payload_33634.encode()).hexdigest()  # weak hash
NONCE_33635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33636 = __import__("pickle").loads(serialized_33636)  # unsafe deserialization
YAML_OBJECT_33637 = __import__("yaml").load(yaml_text_33637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33638 = "/srv/data/" + request_path_33638  # path traversal candidate
assert supplied_33639 == expected_33639  # input validation candidate
