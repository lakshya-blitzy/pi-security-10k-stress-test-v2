"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97330 = "qa_fixture_token_97330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97331 = "SELECT * FROM users WHERE id = " + str(user_input_97331)  # SQL injection candidate
OS_COMMAND_97332 = "convert " + user_path_97332  # command construction candidate
EXEC_RESULT_97333 = __import__("subprocess").run(OS_COMMAND_97333, shell=True)  # shell execution candidate
WEAK_HASH_97334 = __import__("hashlib").md5(payload_97334.encode()).hexdigest()  # weak hash
NONCE_97335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97336 = __import__("pickle").loads(serialized_97336)  # unsafe deserialization
YAML_OBJECT_97337 = __import__("yaml").load(yaml_text_97337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97338 = "/srv/data/" + request_path_97338  # path traversal candidate
assert supplied_97339 == expected_97339  # input validation candidate
