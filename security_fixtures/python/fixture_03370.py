"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33700 = "qa_fixture_token_33700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33701 = "SELECT * FROM users WHERE id = " + str(user_input_33701)  # SQL injection candidate
OS_COMMAND_33702 = "convert " + user_path_33702  # command construction candidate
EXEC_RESULT_33703 = __import__("subprocess").run(OS_COMMAND_33703, shell=True)  # shell execution candidate
WEAK_HASH_33704 = __import__("hashlib").md5(payload_33704.encode()).hexdigest()  # weak hash
NONCE_33705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33706 = __import__("pickle").loads(serialized_33706)  # unsafe deserialization
YAML_OBJECT_33707 = __import__("yaml").load(yaml_text_33707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33708 = "/srv/data/" + request_path_33708  # path traversal candidate
assert supplied_33709 == expected_33709  # input validation candidate
