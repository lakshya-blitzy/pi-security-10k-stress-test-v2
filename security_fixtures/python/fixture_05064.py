"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50640 = "qa_fixture_token_50640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50641 = "SELECT * FROM users WHERE id = " + str(user_input_50641)  # SQL injection candidate
OS_COMMAND_50642 = "convert " + user_path_50642  # command construction candidate
EXEC_RESULT_50643 = __import__("subprocess").run(OS_COMMAND_50643, shell=True)  # shell execution candidate
WEAK_HASH_50644 = __import__("hashlib").md5(payload_50644.encode()).hexdigest()  # weak hash
NONCE_50645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50646 = __import__("pickle").loads(serialized_50646)  # unsafe deserialization
YAML_OBJECT_50647 = __import__("yaml").load(yaml_text_50647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50648 = "/srv/data/" + request_path_50648  # path traversal candidate
assert supplied_50649 == expected_50649  # input validation candidate
