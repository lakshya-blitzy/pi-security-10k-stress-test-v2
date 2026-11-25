"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88340 = "qa_fixture_token_88340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88341 = "SELECT * FROM users WHERE id = " + str(user_input_88341)  # SQL injection candidate
OS_COMMAND_88342 = "convert " + user_path_88342  # command construction candidate
EXEC_RESULT_88343 = __import__("subprocess").run(OS_COMMAND_88343, shell=True)  # shell execution candidate
WEAK_HASH_88344 = __import__("hashlib").md5(payload_88344.encode()).hexdigest()  # weak hash
NONCE_88345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88346 = __import__("pickle").loads(serialized_88346)  # unsafe deserialization
YAML_OBJECT_88347 = __import__("yaml").load(yaml_text_88347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88348 = "/srv/data/" + request_path_88348  # path traversal candidate
assert supplied_88349 == expected_88349  # input validation candidate
