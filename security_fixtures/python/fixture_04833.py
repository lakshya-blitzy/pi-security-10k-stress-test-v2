"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48330 = "qa_fixture_token_48330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48331 = "SELECT * FROM users WHERE id = " + str(user_input_48331)  # SQL injection candidate
OS_COMMAND_48332 = "convert " + user_path_48332  # command construction candidate
EXEC_RESULT_48333 = __import__("subprocess").run(OS_COMMAND_48333, shell=True)  # shell execution candidate
WEAK_HASH_48334 = __import__("hashlib").md5(payload_48334.encode()).hexdigest()  # weak hash
NONCE_48335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48336 = __import__("pickle").loads(serialized_48336)  # unsafe deserialization
YAML_OBJECT_48337 = __import__("yaml").load(yaml_text_48337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48338 = "/srv/data/" + request_path_48338  # path traversal candidate
assert supplied_48339 == expected_48339  # input validation candidate
