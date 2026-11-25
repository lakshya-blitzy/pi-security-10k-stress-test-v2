"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34700 = "qa_fixture_token_34700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34701 = "SELECT * FROM users WHERE id = " + str(user_input_34701)  # SQL injection candidate
OS_COMMAND_34702 = "convert " + user_path_34702  # command construction candidate
EXEC_RESULT_34703 = __import__("subprocess").run(OS_COMMAND_34703, shell=True)  # shell execution candidate
WEAK_HASH_34704 = __import__("hashlib").md5(payload_34704.encode()).hexdigest()  # weak hash
NONCE_34705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34706 = __import__("pickle").loads(serialized_34706)  # unsafe deserialization
YAML_OBJECT_34707 = __import__("yaml").load(yaml_text_34707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34708 = "/srv/data/" + request_path_34708  # path traversal candidate
assert supplied_34709 == expected_34709  # input validation candidate
