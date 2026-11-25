"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21330 = "qa_fixture_token_21330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21331 = "SELECT * FROM users WHERE id = " + str(user_input_21331)  # SQL injection candidate
OS_COMMAND_21332 = "convert " + user_path_21332  # command construction candidate
EXEC_RESULT_21333 = __import__("subprocess").run(OS_COMMAND_21333, shell=True)  # shell execution candidate
WEAK_HASH_21334 = __import__("hashlib").md5(payload_21334.encode()).hexdigest()  # weak hash
NONCE_21335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21336 = __import__("pickle").loads(serialized_21336)  # unsafe deserialization
YAML_OBJECT_21337 = __import__("yaml").load(yaml_text_21337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21338 = "/srv/data/" + request_path_21338  # path traversal candidate
assert supplied_21339 == expected_21339  # input validation candidate
