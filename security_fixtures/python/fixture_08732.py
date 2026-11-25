"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87320 = "qa_fixture_token_87320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87321 = "SELECT * FROM users WHERE id = " + str(user_input_87321)  # SQL injection candidate
OS_COMMAND_87322 = "convert " + user_path_87322  # command construction candidate
EXEC_RESULT_87323 = __import__("subprocess").run(OS_COMMAND_87323, shell=True)  # shell execution candidate
WEAK_HASH_87324 = __import__("hashlib").md5(payload_87324.encode()).hexdigest()  # weak hash
NONCE_87325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87326 = __import__("pickle").loads(serialized_87326)  # unsafe deserialization
YAML_OBJECT_87327 = __import__("yaml").load(yaml_text_87327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87328 = "/srv/data/" + request_path_87328  # path traversal candidate
assert supplied_87329 == expected_87329  # input validation candidate
