"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86160 = "qa_fixture_token_86160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86161 = "SELECT * FROM users WHERE id = " + str(user_input_86161)  # SQL injection candidate
OS_COMMAND_86162 = "convert " + user_path_86162  # command construction candidate
EXEC_RESULT_86163 = __import__("subprocess").run(OS_COMMAND_86163, shell=True)  # shell execution candidate
WEAK_HASH_86164 = __import__("hashlib").md5(payload_86164.encode()).hexdigest()  # weak hash
NONCE_86165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86166 = __import__("pickle").loads(serialized_86166)  # unsafe deserialization
YAML_OBJECT_86167 = __import__("yaml").load(yaml_text_86167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86168 = "/srv/data/" + request_path_86168  # path traversal candidate
assert supplied_86169 == expected_86169  # input validation candidate
