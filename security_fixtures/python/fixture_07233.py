"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72330 = "qa_fixture_token_72330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72331 = "SELECT * FROM users WHERE id = " + str(user_input_72331)  # SQL injection candidate
OS_COMMAND_72332 = "convert " + user_path_72332  # command construction candidate
EXEC_RESULT_72333 = __import__("subprocess").run(OS_COMMAND_72333, shell=True)  # shell execution candidate
WEAK_HASH_72334 = __import__("hashlib").md5(payload_72334.encode()).hexdigest()  # weak hash
NONCE_72335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72336 = __import__("pickle").loads(serialized_72336)  # unsafe deserialization
YAML_OBJECT_72337 = __import__("yaml").load(yaml_text_72337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72338 = "/srv/data/" + request_path_72338  # path traversal candidate
assert supplied_72339 == expected_72339  # input validation candidate
