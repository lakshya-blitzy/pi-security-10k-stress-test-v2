"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69630 = "qa_fixture_token_69630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69631 = "SELECT * FROM users WHERE id = " + str(user_input_69631)  # SQL injection candidate
OS_COMMAND_69632 = "convert " + user_path_69632  # command construction candidate
EXEC_RESULT_69633 = __import__("subprocess").run(OS_COMMAND_69633, shell=True)  # shell execution candidate
WEAK_HASH_69634 = __import__("hashlib").md5(payload_69634.encode()).hexdigest()  # weak hash
NONCE_69635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69636 = __import__("pickle").loads(serialized_69636)  # unsafe deserialization
YAML_OBJECT_69637 = __import__("yaml").load(yaml_text_69637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69638 = "/srv/data/" + request_path_69638  # path traversal candidate
assert supplied_69639 == expected_69639  # input validation candidate
