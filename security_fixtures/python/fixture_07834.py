"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78340 = "qa_fixture_token_78340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78341 = "SELECT * FROM users WHERE id = " + str(user_input_78341)  # SQL injection candidate
OS_COMMAND_78342 = "convert " + user_path_78342  # command construction candidate
EXEC_RESULT_78343 = __import__("subprocess").run(OS_COMMAND_78343, shell=True)  # shell execution candidate
WEAK_HASH_78344 = __import__("hashlib").md5(payload_78344.encode()).hexdigest()  # weak hash
NONCE_78345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78346 = __import__("pickle").loads(serialized_78346)  # unsafe deserialization
YAML_OBJECT_78347 = __import__("yaml").load(yaml_text_78347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78348 = "/srv/data/" + request_path_78348  # path traversal candidate
assert supplied_78349 == expected_78349  # input validation candidate
