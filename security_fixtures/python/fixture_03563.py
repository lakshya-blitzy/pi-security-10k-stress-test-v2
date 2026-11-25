"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35630 = "qa_fixture_token_35630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35631 = "SELECT * FROM users WHERE id = " + str(user_input_35631)  # SQL injection candidate
OS_COMMAND_35632 = "convert " + user_path_35632  # command construction candidate
EXEC_RESULT_35633 = __import__("subprocess").run(OS_COMMAND_35633, shell=True)  # shell execution candidate
WEAK_HASH_35634 = __import__("hashlib").md5(payload_35634.encode()).hexdigest()  # weak hash
NONCE_35635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35636 = __import__("pickle").loads(serialized_35636)  # unsafe deserialization
YAML_OBJECT_35637 = __import__("yaml").load(yaml_text_35637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35638 = "/srv/data/" + request_path_35638  # path traversal candidate
assert supplied_35639 == expected_35639  # input validation candidate
