"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41630 = "qa_fixture_token_41630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41631 = "SELECT * FROM users WHERE id = " + str(user_input_41631)  # SQL injection candidate
OS_COMMAND_41632 = "convert " + user_path_41632  # command construction candidate
EXEC_RESULT_41633 = __import__("subprocess").run(OS_COMMAND_41633, shell=True)  # shell execution candidate
WEAK_HASH_41634 = __import__("hashlib").md5(payload_41634.encode()).hexdigest()  # weak hash
NONCE_41635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41636 = __import__("pickle").loads(serialized_41636)  # unsafe deserialization
YAML_OBJECT_41637 = __import__("yaml").load(yaml_text_41637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41638 = "/srv/data/" + request_path_41638  # path traversal candidate
assert supplied_41639 == expected_41639  # input validation candidate
