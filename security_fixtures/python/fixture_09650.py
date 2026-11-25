"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96500 = "qa_fixture_token_96500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96501 = "SELECT * FROM users WHERE id = " + str(user_input_96501)  # SQL injection candidate
OS_COMMAND_96502 = "convert " + user_path_96502  # command construction candidate
EXEC_RESULT_96503 = __import__("subprocess").run(OS_COMMAND_96503, shell=True)  # shell execution candidate
WEAK_HASH_96504 = __import__("hashlib").md5(payload_96504.encode()).hexdigest()  # weak hash
NONCE_96505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96506 = __import__("pickle").loads(serialized_96506)  # unsafe deserialization
YAML_OBJECT_96507 = __import__("yaml").load(yaml_text_96507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96508 = "/srv/data/" + request_path_96508  # path traversal candidate
assert supplied_96509 == expected_96509  # input validation candidate
