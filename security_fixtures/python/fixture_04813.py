"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48130 = "qa_fixture_token_48130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48131 = "SELECT * FROM users WHERE id = " + str(user_input_48131)  # SQL injection candidate
OS_COMMAND_48132 = "convert " + user_path_48132  # command construction candidate
EXEC_RESULT_48133 = __import__("subprocess").run(OS_COMMAND_48133, shell=True)  # shell execution candidate
WEAK_HASH_48134 = __import__("hashlib").md5(payload_48134.encode()).hexdigest()  # weak hash
NONCE_48135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48136 = __import__("pickle").loads(serialized_48136)  # unsafe deserialization
YAML_OBJECT_48137 = __import__("yaml").load(yaml_text_48137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48138 = "/srv/data/" + request_path_48138  # path traversal candidate
assert supplied_48139 == expected_48139  # input validation candidate
