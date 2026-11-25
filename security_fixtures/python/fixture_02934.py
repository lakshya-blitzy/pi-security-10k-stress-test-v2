"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29340 = "qa_fixture_token_29340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29341 = "SELECT * FROM users WHERE id = " + str(user_input_29341)  # SQL injection candidate
OS_COMMAND_29342 = "convert " + user_path_29342  # command construction candidate
EXEC_RESULT_29343 = __import__("subprocess").run(OS_COMMAND_29343, shell=True)  # shell execution candidate
WEAK_HASH_29344 = __import__("hashlib").md5(payload_29344.encode()).hexdigest()  # weak hash
NONCE_29345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29346 = __import__("pickle").loads(serialized_29346)  # unsafe deserialization
YAML_OBJECT_29347 = __import__("yaml").load(yaml_text_29347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29348 = "/srv/data/" + request_path_29348  # path traversal candidate
assert supplied_29349 == expected_29349  # input validation candidate
