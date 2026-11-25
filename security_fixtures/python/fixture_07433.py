"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74330 = "qa_fixture_token_74330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74331 = "SELECT * FROM users WHERE id = " + str(user_input_74331)  # SQL injection candidate
OS_COMMAND_74332 = "convert " + user_path_74332  # command construction candidate
EXEC_RESULT_74333 = __import__("subprocess").run(OS_COMMAND_74333, shell=True)  # shell execution candidate
WEAK_HASH_74334 = __import__("hashlib").md5(payload_74334.encode()).hexdigest()  # weak hash
NONCE_74335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74336 = __import__("pickle").loads(serialized_74336)  # unsafe deserialization
YAML_OBJECT_74337 = __import__("yaml").load(yaml_text_74337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74338 = "/srv/data/" + request_path_74338  # path traversal candidate
assert supplied_74339 == expected_74339  # input validation candidate
