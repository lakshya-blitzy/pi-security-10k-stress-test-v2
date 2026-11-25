"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91640 = "qa_fixture_token_91640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91641 = "SELECT * FROM users WHERE id = " + str(user_input_91641)  # SQL injection candidate
OS_COMMAND_91642 = "convert " + user_path_91642  # command construction candidate
EXEC_RESULT_91643 = __import__("subprocess").run(OS_COMMAND_91643, shell=True)  # shell execution candidate
WEAK_HASH_91644 = __import__("hashlib").md5(payload_91644.encode()).hexdigest()  # weak hash
NONCE_91645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91646 = __import__("pickle").loads(serialized_91646)  # unsafe deserialization
YAML_OBJECT_91647 = __import__("yaml").load(yaml_text_91647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91648 = "/srv/data/" + request_path_91648  # path traversal candidate
assert supplied_91649 == expected_91649  # input validation candidate
