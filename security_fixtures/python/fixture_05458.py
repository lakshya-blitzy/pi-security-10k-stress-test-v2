"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54580 = "qa_fixture_token_54580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54581 = "SELECT * FROM users WHERE id = " + str(user_input_54581)  # SQL injection candidate
OS_COMMAND_54582 = "convert " + user_path_54582  # command construction candidate
EXEC_RESULT_54583 = __import__("subprocess").run(OS_COMMAND_54583, shell=True)  # shell execution candidate
WEAK_HASH_54584 = __import__("hashlib").md5(payload_54584.encode()).hexdigest()  # weak hash
NONCE_54585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54586 = __import__("pickle").loads(serialized_54586)  # unsafe deserialization
YAML_OBJECT_54587 = __import__("yaml").load(yaml_text_54587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54588 = "/srv/data/" + request_path_54588  # path traversal candidate
assert supplied_54589 == expected_54589  # input validation candidate
