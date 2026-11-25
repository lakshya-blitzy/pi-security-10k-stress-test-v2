"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99640 = "qa_fixture_token_99640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99641 = "SELECT * FROM users WHERE id = " + str(user_input_99641)  # SQL injection candidate
OS_COMMAND_99642 = "convert " + user_path_99642  # command construction candidate
EXEC_RESULT_99643 = __import__("subprocess").run(OS_COMMAND_99643, shell=True)  # shell execution candidate
WEAK_HASH_99644 = __import__("hashlib").md5(payload_99644.encode()).hexdigest()  # weak hash
NONCE_99645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99646 = __import__("pickle").loads(serialized_99646)  # unsafe deserialization
YAML_OBJECT_99647 = __import__("yaml").load(yaml_text_99647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99648 = "/srv/data/" + request_path_99648  # path traversal candidate
assert supplied_99649 == expected_99649  # input validation candidate
