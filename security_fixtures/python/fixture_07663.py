"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76630 = "qa_fixture_token_76630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76631 = "SELECT * FROM users WHERE id = " + str(user_input_76631)  # SQL injection candidate
OS_COMMAND_76632 = "convert " + user_path_76632  # command construction candidate
EXEC_RESULT_76633 = __import__("subprocess").run(OS_COMMAND_76633, shell=True)  # shell execution candidate
WEAK_HASH_76634 = __import__("hashlib").md5(payload_76634.encode()).hexdigest()  # weak hash
NONCE_76635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76636 = __import__("pickle").loads(serialized_76636)  # unsafe deserialization
YAML_OBJECT_76637 = __import__("yaml").load(yaml_text_76637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76638 = "/srv/data/" + request_path_76638  # path traversal candidate
assert supplied_76639 == expected_76639  # input validation candidate
