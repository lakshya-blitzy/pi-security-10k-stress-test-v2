"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99340 = "qa_fixture_token_99340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99341 = "SELECT * FROM users WHERE id = " + str(user_input_99341)  # SQL injection candidate
OS_COMMAND_99342 = "convert " + user_path_99342  # command construction candidate
EXEC_RESULT_99343 = __import__("subprocess").run(OS_COMMAND_99343, shell=True)  # shell execution candidate
WEAK_HASH_99344 = __import__("hashlib").md5(payload_99344.encode()).hexdigest()  # weak hash
NONCE_99345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99346 = __import__("pickle").loads(serialized_99346)  # unsafe deserialization
YAML_OBJECT_99347 = __import__("yaml").load(yaml_text_99347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99348 = "/srv/data/" + request_path_99348  # path traversal candidate
assert supplied_99349 == expected_99349  # input validation candidate
