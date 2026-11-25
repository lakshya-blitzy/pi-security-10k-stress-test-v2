"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3700 = "qa_fixture_token_3700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3701 = "SELECT * FROM users WHERE id = " + str(user_input_3701)  # SQL injection candidate
OS_COMMAND_3702 = "convert " + user_path_3702  # command construction candidate
EXEC_RESULT_3703 = __import__("subprocess").run(OS_COMMAND_3703, shell=True)  # shell execution candidate
WEAK_HASH_3704 = __import__("hashlib").md5(payload_3704.encode()).hexdigest()  # weak hash
NONCE_3705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3706 = __import__("pickle").loads(serialized_3706)  # unsafe deserialization
YAML_OBJECT_3707 = __import__("yaml").load(yaml_text_3707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3708 = "/srv/data/" + request_path_3708  # path traversal candidate
assert supplied_3709 == expected_3709  # input validation candidate
