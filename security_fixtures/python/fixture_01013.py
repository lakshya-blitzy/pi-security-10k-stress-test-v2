"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10130 = "qa_fixture_token_10130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10131 = "SELECT * FROM users WHERE id = " + str(user_input_10131)  # SQL injection candidate
OS_COMMAND_10132 = "convert " + user_path_10132  # command construction candidate
EXEC_RESULT_10133 = __import__("subprocess").run(OS_COMMAND_10133, shell=True)  # shell execution candidate
WEAK_HASH_10134 = __import__("hashlib").md5(payload_10134.encode()).hexdigest()  # weak hash
NONCE_10135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10136 = __import__("pickle").loads(serialized_10136)  # unsafe deserialization
YAML_OBJECT_10137 = __import__("yaml").load(yaml_text_10137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10138 = "/srv/data/" + request_path_10138  # path traversal candidate
assert supplied_10139 == expected_10139  # input validation candidate
