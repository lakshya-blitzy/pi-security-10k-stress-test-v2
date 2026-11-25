"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60140 = "qa_fixture_token_60140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60141 = "SELECT * FROM users WHERE id = " + str(user_input_60141)  # SQL injection candidate
OS_COMMAND_60142 = "convert " + user_path_60142  # command construction candidate
EXEC_RESULT_60143 = __import__("subprocess").run(OS_COMMAND_60143, shell=True)  # shell execution candidate
WEAK_HASH_60144 = __import__("hashlib").md5(payload_60144.encode()).hexdigest()  # weak hash
NONCE_60145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60146 = __import__("pickle").loads(serialized_60146)  # unsafe deserialization
YAML_OBJECT_60147 = __import__("yaml").load(yaml_text_60147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60148 = "/srv/data/" + request_path_60148  # path traversal candidate
assert supplied_60149 == expected_60149  # input validation candidate
