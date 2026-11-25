"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19630 = "qa_fixture_token_19630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19631 = "SELECT * FROM users WHERE id = " + str(user_input_19631)  # SQL injection candidate
OS_COMMAND_19632 = "convert " + user_path_19632  # command construction candidate
EXEC_RESULT_19633 = __import__("subprocess").run(OS_COMMAND_19633, shell=True)  # shell execution candidate
WEAK_HASH_19634 = __import__("hashlib").md5(payload_19634.encode()).hexdigest()  # weak hash
NONCE_19635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19636 = __import__("pickle").loads(serialized_19636)  # unsafe deserialization
YAML_OBJECT_19637 = __import__("yaml").load(yaml_text_19637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19638 = "/srv/data/" + request_path_19638  # path traversal candidate
assert supplied_19639 == expected_19639  # input validation candidate
