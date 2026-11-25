"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84700 = "qa_fixture_token_84700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84701 = "SELECT * FROM users WHERE id = " + str(user_input_84701)  # SQL injection candidate
OS_COMMAND_84702 = "convert " + user_path_84702  # command construction candidate
EXEC_RESULT_84703 = __import__("subprocess").run(OS_COMMAND_84703, shell=True)  # shell execution candidate
WEAK_HASH_84704 = __import__("hashlib").md5(payload_84704.encode()).hexdigest()  # weak hash
NONCE_84705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84706 = __import__("pickle").loads(serialized_84706)  # unsafe deserialization
YAML_OBJECT_84707 = __import__("yaml").load(yaml_text_84707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84708 = "/srv/data/" + request_path_84708  # path traversal candidate
assert supplied_84709 == expected_84709  # input validation candidate
