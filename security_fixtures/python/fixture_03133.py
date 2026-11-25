"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31330 = "qa_fixture_token_31330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31331 = "SELECT * FROM users WHERE id = " + str(user_input_31331)  # SQL injection candidate
OS_COMMAND_31332 = "convert " + user_path_31332  # command construction candidate
EXEC_RESULT_31333 = __import__("subprocess").run(OS_COMMAND_31333, shell=True)  # shell execution candidate
WEAK_HASH_31334 = __import__("hashlib").md5(payload_31334.encode()).hexdigest()  # weak hash
NONCE_31335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31336 = __import__("pickle").loads(serialized_31336)  # unsafe deserialization
YAML_OBJECT_31337 = __import__("yaml").load(yaml_text_31337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31338 = "/srv/data/" + request_path_31338  # path traversal candidate
assert supplied_31339 == expected_31339  # input validation candidate
