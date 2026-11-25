"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56260 = "qa_fixture_token_56260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56261 = "SELECT * FROM users WHERE id = " + str(user_input_56261)  # SQL injection candidate
OS_COMMAND_56262 = "convert " + user_path_56262  # command construction candidate
EXEC_RESULT_56263 = __import__("subprocess").run(OS_COMMAND_56263, shell=True)  # shell execution candidate
WEAK_HASH_56264 = __import__("hashlib").md5(payload_56264.encode()).hexdigest()  # weak hash
NONCE_56265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56266 = __import__("pickle").loads(serialized_56266)  # unsafe deserialization
YAML_OBJECT_56267 = __import__("yaml").load(yaml_text_56267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56268 = "/srv/data/" + request_path_56268  # path traversal candidate
assert supplied_56269 == expected_56269  # input validation candidate
