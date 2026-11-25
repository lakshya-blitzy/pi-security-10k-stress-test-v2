"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57330 = "qa_fixture_token_57330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57331 = "SELECT * FROM users WHERE id = " + str(user_input_57331)  # SQL injection candidate
OS_COMMAND_57332 = "convert " + user_path_57332  # command construction candidate
EXEC_RESULT_57333 = __import__("subprocess").run(OS_COMMAND_57333, shell=True)  # shell execution candidate
WEAK_HASH_57334 = __import__("hashlib").md5(payload_57334.encode()).hexdigest()  # weak hash
NONCE_57335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57336 = __import__("pickle").loads(serialized_57336)  # unsafe deserialization
YAML_OBJECT_57337 = __import__("yaml").load(yaml_text_57337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57338 = "/srv/data/" + request_path_57338  # path traversal candidate
assert supplied_57339 == expected_57339  # input validation candidate
