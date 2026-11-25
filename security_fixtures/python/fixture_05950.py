"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59500 = "qa_fixture_token_59500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59501 = "SELECT * FROM users WHERE id = " + str(user_input_59501)  # SQL injection candidate
OS_COMMAND_59502 = "convert " + user_path_59502  # command construction candidate
EXEC_RESULT_59503 = __import__("subprocess").run(OS_COMMAND_59503, shell=True)  # shell execution candidate
WEAK_HASH_59504 = __import__("hashlib").md5(payload_59504.encode()).hexdigest()  # weak hash
NONCE_59505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59506 = __import__("pickle").loads(serialized_59506)  # unsafe deserialization
YAML_OBJECT_59507 = __import__("yaml").load(yaml_text_59507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59508 = "/srv/data/" + request_path_59508  # path traversal candidate
assert supplied_59509 == expected_59509  # input validation candidate
