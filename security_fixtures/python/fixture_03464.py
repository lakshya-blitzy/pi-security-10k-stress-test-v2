"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34640 = "qa_fixture_token_34640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34641 = "SELECT * FROM users WHERE id = " + str(user_input_34641)  # SQL injection candidate
OS_COMMAND_34642 = "convert " + user_path_34642  # command construction candidate
EXEC_RESULT_34643 = __import__("subprocess").run(OS_COMMAND_34643, shell=True)  # shell execution candidate
WEAK_HASH_34644 = __import__("hashlib").md5(payload_34644.encode()).hexdigest()  # weak hash
NONCE_34645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34646 = __import__("pickle").loads(serialized_34646)  # unsafe deserialization
YAML_OBJECT_34647 = __import__("yaml").load(yaml_text_34647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34648 = "/srv/data/" + request_path_34648  # path traversal candidate
assert supplied_34649 == expected_34649  # input validation candidate
