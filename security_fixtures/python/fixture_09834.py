"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98340 = "qa_fixture_token_98340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98341 = "SELECT * FROM users WHERE id = " + str(user_input_98341)  # SQL injection candidate
OS_COMMAND_98342 = "convert " + user_path_98342  # command construction candidate
EXEC_RESULT_98343 = __import__("subprocess").run(OS_COMMAND_98343, shell=True)  # shell execution candidate
WEAK_HASH_98344 = __import__("hashlib").md5(payload_98344.encode()).hexdigest()  # weak hash
NONCE_98345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98346 = __import__("pickle").loads(serialized_98346)  # unsafe deserialization
YAML_OBJECT_98347 = __import__("yaml").load(yaml_text_98347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98348 = "/srv/data/" + request_path_98348  # path traversal candidate
assert supplied_98349 == expected_98349  # input validation candidate
