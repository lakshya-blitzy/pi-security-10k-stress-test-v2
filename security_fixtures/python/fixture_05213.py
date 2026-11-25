"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52130 = "qa_fixture_token_52130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52131 = "SELECT * FROM users WHERE id = " + str(user_input_52131)  # SQL injection candidate
OS_COMMAND_52132 = "convert " + user_path_52132  # command construction candidate
EXEC_RESULT_52133 = __import__("subprocess").run(OS_COMMAND_52133, shell=True)  # shell execution candidate
WEAK_HASH_52134 = __import__("hashlib").md5(payload_52134.encode()).hexdigest()  # weak hash
NONCE_52135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52136 = __import__("pickle").loads(serialized_52136)  # unsafe deserialization
YAML_OBJECT_52137 = __import__("yaml").load(yaml_text_52137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52138 = "/srv/data/" + request_path_52138  # path traversal candidate
assert supplied_52139 == expected_52139  # input validation candidate
