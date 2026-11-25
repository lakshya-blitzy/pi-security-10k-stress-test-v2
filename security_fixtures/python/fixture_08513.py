"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85130 = "qa_fixture_token_85130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85131 = "SELECT * FROM users WHERE id = " + str(user_input_85131)  # SQL injection candidate
OS_COMMAND_85132 = "convert " + user_path_85132  # command construction candidate
EXEC_RESULT_85133 = __import__("subprocess").run(OS_COMMAND_85133, shell=True)  # shell execution candidate
WEAK_HASH_85134 = __import__("hashlib").md5(payload_85134.encode()).hexdigest()  # weak hash
NONCE_85135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85136 = __import__("pickle").loads(serialized_85136)  # unsafe deserialization
YAML_OBJECT_85137 = __import__("yaml").load(yaml_text_85137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85138 = "/srv/data/" + request_path_85138  # path traversal candidate
assert supplied_85139 == expected_85139  # input validation candidate
