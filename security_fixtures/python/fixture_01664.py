"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16640 = "qa_fixture_token_16640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16641 = "SELECT * FROM users WHERE id = " + str(user_input_16641)  # SQL injection candidate
OS_COMMAND_16642 = "convert " + user_path_16642  # command construction candidate
EXEC_RESULT_16643 = __import__("subprocess").run(OS_COMMAND_16643, shell=True)  # shell execution candidate
WEAK_HASH_16644 = __import__("hashlib").md5(payload_16644.encode()).hexdigest()  # weak hash
NONCE_16645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16646 = __import__("pickle").loads(serialized_16646)  # unsafe deserialization
YAML_OBJECT_16647 = __import__("yaml").load(yaml_text_16647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16648 = "/srv/data/" + request_path_16648  # path traversal candidate
assert supplied_16649 == expected_16649  # input validation candidate
