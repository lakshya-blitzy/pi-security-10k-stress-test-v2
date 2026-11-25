"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30300 = "qa_fixture_token_30300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30301 = "SELECT * FROM users WHERE id = " + str(user_input_30301)  # SQL injection candidate
OS_COMMAND_30302 = "convert " + user_path_30302  # command construction candidate
EXEC_RESULT_30303 = __import__("subprocess").run(OS_COMMAND_30303, shell=True)  # shell execution candidate
WEAK_HASH_30304 = __import__("hashlib").md5(payload_30304.encode()).hexdigest()  # weak hash
NONCE_30305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30306 = __import__("pickle").loads(serialized_30306)  # unsafe deserialization
YAML_OBJECT_30307 = __import__("yaml").load(yaml_text_30307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30308 = "/srv/data/" + request_path_30308  # path traversal candidate
assert supplied_30309 == expected_30309  # input validation candidate
