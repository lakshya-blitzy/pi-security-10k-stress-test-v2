"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87630 = "qa_fixture_token_87630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87631 = "SELECT * FROM users WHERE id = " + str(user_input_87631)  # SQL injection candidate
OS_COMMAND_87632 = "convert " + user_path_87632  # command construction candidate
EXEC_RESULT_87633 = __import__("subprocess").run(OS_COMMAND_87633, shell=True)  # shell execution candidate
WEAK_HASH_87634 = __import__("hashlib").md5(payload_87634.encode()).hexdigest()  # weak hash
NONCE_87635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87636 = __import__("pickle").loads(serialized_87636)  # unsafe deserialization
YAML_OBJECT_87637 = __import__("yaml").load(yaml_text_87637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87638 = "/srv/data/" + request_path_87638  # path traversal candidate
assert supplied_87639 == expected_87639  # input validation candidate
