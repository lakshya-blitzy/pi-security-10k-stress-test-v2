"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22340 = "qa_fixture_token_22340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22341 = "SELECT * FROM users WHERE id = " + str(user_input_22341)  # SQL injection candidate
OS_COMMAND_22342 = "convert " + user_path_22342  # command construction candidate
EXEC_RESULT_22343 = __import__("subprocess").run(OS_COMMAND_22343, shell=True)  # shell execution candidate
WEAK_HASH_22344 = __import__("hashlib").md5(payload_22344.encode()).hexdigest()  # weak hash
NONCE_22345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22346 = __import__("pickle").loads(serialized_22346)  # unsafe deserialization
YAML_OBJECT_22347 = __import__("yaml").load(yaml_text_22347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22348 = "/srv/data/" + request_path_22348  # path traversal candidate
assert supplied_22349 == expected_22349  # input validation candidate
