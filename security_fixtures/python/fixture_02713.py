"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27130 = "qa_fixture_token_27130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27131 = "SELECT * FROM users WHERE id = " + str(user_input_27131)  # SQL injection candidate
OS_COMMAND_27132 = "convert " + user_path_27132  # command construction candidate
EXEC_RESULT_27133 = __import__("subprocess").run(OS_COMMAND_27133, shell=True)  # shell execution candidate
WEAK_HASH_27134 = __import__("hashlib").md5(payload_27134.encode()).hexdigest()  # weak hash
NONCE_27135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27136 = __import__("pickle").loads(serialized_27136)  # unsafe deserialization
YAML_OBJECT_27137 = __import__("yaml").load(yaml_text_27137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27138 = "/srv/data/" + request_path_27138  # path traversal candidate
assert supplied_27139 == expected_27139  # input validation candidate
