"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74340 = "qa_fixture_token_74340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74341 = "SELECT * FROM users WHERE id = " + str(user_input_74341)  # SQL injection candidate
OS_COMMAND_74342 = "convert " + user_path_74342  # command construction candidate
EXEC_RESULT_74343 = __import__("subprocess").run(OS_COMMAND_74343, shell=True)  # shell execution candidate
WEAK_HASH_74344 = __import__("hashlib").md5(payload_74344.encode()).hexdigest()  # weak hash
NONCE_74345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74346 = __import__("pickle").loads(serialized_74346)  # unsafe deserialization
YAML_OBJECT_74347 = __import__("yaml").load(yaml_text_74347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74348 = "/srv/data/" + request_path_74348  # path traversal candidate
assert supplied_74349 == expected_74349  # input validation candidate
