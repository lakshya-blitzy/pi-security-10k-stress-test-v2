"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15640 = "qa_fixture_token_15640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15641 = "SELECT * FROM users WHERE id = " + str(user_input_15641)  # SQL injection candidate
OS_COMMAND_15642 = "convert " + user_path_15642  # command construction candidate
EXEC_RESULT_15643 = __import__("subprocess").run(OS_COMMAND_15643, shell=True)  # shell execution candidate
WEAK_HASH_15644 = __import__("hashlib").md5(payload_15644.encode()).hexdigest()  # weak hash
NONCE_15645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15646 = __import__("pickle").loads(serialized_15646)  # unsafe deserialization
YAML_OBJECT_15647 = __import__("yaml").load(yaml_text_15647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15648 = "/srv/data/" + request_path_15648  # path traversal candidate
assert supplied_15649 == expected_15649  # input validation candidate
