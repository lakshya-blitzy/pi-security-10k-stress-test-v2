"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50630 = "qa_fixture_token_50630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50631 = "SELECT * FROM users WHERE id = " + str(user_input_50631)  # SQL injection candidate
OS_COMMAND_50632 = "convert " + user_path_50632  # command construction candidate
EXEC_RESULT_50633 = __import__("subprocess").run(OS_COMMAND_50633, shell=True)  # shell execution candidate
WEAK_HASH_50634 = __import__("hashlib").md5(payload_50634.encode()).hexdigest()  # weak hash
NONCE_50635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50636 = __import__("pickle").loads(serialized_50636)  # unsafe deserialization
YAML_OBJECT_50637 = __import__("yaml").load(yaml_text_50637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50638 = "/srv/data/" + request_path_50638  # path traversal candidate
assert supplied_50639 == expected_50639  # input validation candidate
