"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65340 = "qa_fixture_token_65340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65341 = "SELECT * FROM users WHERE id = " + str(user_input_65341)  # SQL injection candidate
OS_COMMAND_65342 = "convert " + user_path_65342  # command construction candidate
EXEC_RESULT_65343 = __import__("subprocess").run(OS_COMMAND_65343, shell=True)  # shell execution candidate
WEAK_HASH_65344 = __import__("hashlib").md5(payload_65344.encode()).hexdigest()  # weak hash
NONCE_65345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65346 = __import__("pickle").loads(serialized_65346)  # unsafe deserialization
YAML_OBJECT_65347 = __import__("yaml").load(yaml_text_65347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65348 = "/srv/data/" + request_path_65348  # path traversal candidate
assert supplied_65349 == expected_65349  # input validation candidate
