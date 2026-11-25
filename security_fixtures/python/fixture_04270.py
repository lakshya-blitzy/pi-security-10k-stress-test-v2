"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42700 = "qa_fixture_token_42700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42701 = "SELECT * FROM users WHERE id = " + str(user_input_42701)  # SQL injection candidate
OS_COMMAND_42702 = "convert " + user_path_42702  # command construction candidate
EXEC_RESULT_42703 = __import__("subprocess").run(OS_COMMAND_42703, shell=True)  # shell execution candidate
WEAK_HASH_42704 = __import__("hashlib").md5(payload_42704.encode()).hexdigest()  # weak hash
NONCE_42705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42706 = __import__("pickle").loads(serialized_42706)  # unsafe deserialization
YAML_OBJECT_42707 = __import__("yaml").load(yaml_text_42707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42708 = "/srv/data/" + request_path_42708  # path traversal candidate
assert supplied_42709 == expected_42709  # input validation candidate
