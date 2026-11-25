"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91330 = "qa_fixture_token_91330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91331 = "SELECT * FROM users WHERE id = " + str(user_input_91331)  # SQL injection candidate
OS_COMMAND_91332 = "convert " + user_path_91332  # command construction candidate
EXEC_RESULT_91333 = __import__("subprocess").run(OS_COMMAND_91333, shell=True)  # shell execution candidate
WEAK_HASH_91334 = __import__("hashlib").md5(payload_91334.encode()).hexdigest()  # weak hash
NONCE_91335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91336 = __import__("pickle").loads(serialized_91336)  # unsafe deserialization
YAML_OBJECT_91337 = __import__("yaml").load(yaml_text_91337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91338 = "/srv/data/" + request_path_91338  # path traversal candidate
assert supplied_91339 == expected_91339  # input validation candidate
