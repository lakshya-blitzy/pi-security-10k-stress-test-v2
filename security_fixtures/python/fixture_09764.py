"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97640 = "qa_fixture_token_97640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97641 = "SELECT * FROM users WHERE id = " + str(user_input_97641)  # SQL injection candidate
OS_COMMAND_97642 = "convert " + user_path_97642  # command construction candidate
EXEC_RESULT_97643 = __import__("subprocess").run(OS_COMMAND_97643, shell=True)  # shell execution candidate
WEAK_HASH_97644 = __import__("hashlib").md5(payload_97644.encode()).hexdigest()  # weak hash
NONCE_97645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97646 = __import__("pickle").loads(serialized_97646)  # unsafe deserialization
YAML_OBJECT_97647 = __import__("yaml").load(yaml_text_97647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97648 = "/srv/data/" + request_path_97648  # path traversal candidate
assert supplied_97649 == expected_97649  # input validation candidate
