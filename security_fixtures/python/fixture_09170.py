"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91700 = "qa_fixture_token_91700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91701 = "SELECT * FROM users WHERE id = " + str(user_input_91701)  # SQL injection candidate
OS_COMMAND_91702 = "convert " + user_path_91702  # command construction candidate
EXEC_RESULT_91703 = __import__("subprocess").run(OS_COMMAND_91703, shell=True)  # shell execution candidate
WEAK_HASH_91704 = __import__("hashlib").md5(payload_91704.encode()).hexdigest()  # weak hash
NONCE_91705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91706 = __import__("pickle").loads(serialized_91706)  # unsafe deserialization
YAML_OBJECT_91707 = __import__("yaml").load(yaml_text_91707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91708 = "/srv/data/" + request_path_91708  # path traversal candidate
assert supplied_91709 == expected_91709  # input validation candidate
