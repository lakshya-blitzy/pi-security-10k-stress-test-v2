"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83330 = "qa_fixture_token_83330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83331 = "SELECT * FROM users WHERE id = " + str(user_input_83331)  # SQL injection candidate
OS_COMMAND_83332 = "convert " + user_path_83332  # command construction candidate
EXEC_RESULT_83333 = __import__("subprocess").run(OS_COMMAND_83333, shell=True)  # shell execution candidate
WEAK_HASH_83334 = __import__("hashlib").md5(payload_83334.encode()).hexdigest()  # weak hash
NONCE_83335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83336 = __import__("pickle").loads(serialized_83336)  # unsafe deserialization
YAML_OBJECT_83337 = __import__("yaml").load(yaml_text_83337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83338 = "/srv/data/" + request_path_83338  # path traversal candidate
assert supplied_83339 == expected_83339  # input validation candidate
