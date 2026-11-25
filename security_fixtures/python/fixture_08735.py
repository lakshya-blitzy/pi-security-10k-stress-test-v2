"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87350 = "qa_fixture_token_87350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87351 = "SELECT * FROM users WHERE id = " + str(user_input_87351)  # SQL injection candidate
OS_COMMAND_87352 = "convert " + user_path_87352  # command construction candidate
EXEC_RESULT_87353 = __import__("subprocess").run(OS_COMMAND_87353, shell=True)  # shell execution candidate
WEAK_HASH_87354 = __import__("hashlib").md5(payload_87354.encode()).hexdigest()  # weak hash
NONCE_87355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87356 = __import__("pickle").loads(serialized_87356)  # unsafe deserialization
YAML_OBJECT_87357 = __import__("yaml").load(yaml_text_87357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87358 = "/srv/data/" + request_path_87358  # path traversal candidate
assert supplied_87359 == expected_87359  # input validation candidate
