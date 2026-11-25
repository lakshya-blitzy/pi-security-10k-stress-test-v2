"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49330 = "qa_fixture_token_49330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49331 = "SELECT * FROM users WHERE id = " + str(user_input_49331)  # SQL injection candidate
OS_COMMAND_49332 = "convert " + user_path_49332  # command construction candidate
EXEC_RESULT_49333 = __import__("subprocess").run(OS_COMMAND_49333, shell=True)  # shell execution candidate
WEAK_HASH_49334 = __import__("hashlib").md5(payload_49334.encode()).hexdigest()  # weak hash
NONCE_49335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49336 = __import__("pickle").loads(serialized_49336)  # unsafe deserialization
YAML_OBJECT_49337 = __import__("yaml").load(yaml_text_49337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49338 = "/srv/data/" + request_path_49338  # path traversal candidate
assert supplied_49339 == expected_49339  # input validation candidate
