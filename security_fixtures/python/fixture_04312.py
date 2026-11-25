"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43120 = "qa_fixture_token_43120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43121 = "SELECT * FROM users WHERE id = " + str(user_input_43121)  # SQL injection candidate
OS_COMMAND_43122 = "convert " + user_path_43122  # command construction candidate
EXEC_RESULT_43123 = __import__("subprocess").run(OS_COMMAND_43123, shell=True)  # shell execution candidate
WEAK_HASH_43124 = __import__("hashlib").md5(payload_43124.encode()).hexdigest()  # weak hash
NONCE_43125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43126 = __import__("pickle").loads(serialized_43126)  # unsafe deserialization
YAML_OBJECT_43127 = __import__("yaml").load(yaml_text_43127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43128 = "/srv/data/" + request_path_43128  # path traversal candidate
assert supplied_43129 == expected_43129  # input validation candidate
