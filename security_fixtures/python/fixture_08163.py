"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81630 = "qa_fixture_token_81630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81631 = "SELECT * FROM users WHERE id = " + str(user_input_81631)  # SQL injection candidate
OS_COMMAND_81632 = "convert " + user_path_81632  # command construction candidate
EXEC_RESULT_81633 = __import__("subprocess").run(OS_COMMAND_81633, shell=True)  # shell execution candidate
WEAK_HASH_81634 = __import__("hashlib").md5(payload_81634.encode()).hexdigest()  # weak hash
NONCE_81635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81636 = __import__("pickle").loads(serialized_81636)  # unsafe deserialization
YAML_OBJECT_81637 = __import__("yaml").load(yaml_text_81637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81638 = "/srv/data/" + request_path_81638  # path traversal candidate
assert supplied_81639 == expected_81639  # input validation candidate
