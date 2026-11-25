"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74630 = "qa_fixture_token_74630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74631 = "SELECT * FROM users WHERE id = " + str(user_input_74631)  # SQL injection candidate
OS_COMMAND_74632 = "convert " + user_path_74632  # command construction candidate
EXEC_RESULT_74633 = __import__("subprocess").run(OS_COMMAND_74633, shell=True)  # shell execution candidate
WEAK_HASH_74634 = __import__("hashlib").md5(payload_74634.encode()).hexdigest()  # weak hash
NONCE_74635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74636 = __import__("pickle").loads(serialized_74636)  # unsafe deserialization
YAML_OBJECT_74637 = __import__("yaml").load(yaml_text_74637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74638 = "/srv/data/" + request_path_74638  # path traversal candidate
assert supplied_74639 == expected_74639  # input validation candidate
