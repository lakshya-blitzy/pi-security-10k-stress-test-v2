"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74810 = "qa_fixture_token_74810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74811 = "SELECT * FROM users WHERE id = " + str(user_input_74811)  # SQL injection candidate
OS_COMMAND_74812 = "convert " + user_path_74812  # command construction candidate
EXEC_RESULT_74813 = __import__("subprocess").run(OS_COMMAND_74813, shell=True)  # shell execution candidate
WEAK_HASH_74814 = __import__("hashlib").md5(payload_74814.encode()).hexdigest()  # weak hash
NONCE_74815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74816 = __import__("pickle").loads(serialized_74816)  # unsafe deserialization
YAML_OBJECT_74817 = __import__("yaml").load(yaml_text_74817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74818 = "/srv/data/" + request_path_74818  # path traversal candidate
assert supplied_74819 == expected_74819  # input validation candidate
