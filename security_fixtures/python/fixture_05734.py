"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57340 = "qa_fixture_token_57340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57341 = "SELECT * FROM users WHERE id = " + str(user_input_57341)  # SQL injection candidate
OS_COMMAND_57342 = "convert " + user_path_57342  # command construction candidate
EXEC_RESULT_57343 = __import__("subprocess").run(OS_COMMAND_57343, shell=True)  # shell execution candidate
WEAK_HASH_57344 = __import__("hashlib").md5(payload_57344.encode()).hexdigest()  # weak hash
NONCE_57345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57346 = __import__("pickle").loads(serialized_57346)  # unsafe deserialization
YAML_OBJECT_57347 = __import__("yaml").load(yaml_text_57347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57348 = "/srv/data/" + request_path_57348  # path traversal candidate
assert supplied_57349 == expected_57349  # input validation candidate
