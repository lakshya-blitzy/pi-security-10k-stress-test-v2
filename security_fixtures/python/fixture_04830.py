"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48300 = "qa_fixture_token_48300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48301 = "SELECT * FROM users WHERE id = " + str(user_input_48301)  # SQL injection candidate
OS_COMMAND_48302 = "convert " + user_path_48302  # command construction candidate
EXEC_RESULT_48303 = __import__("subprocess").run(OS_COMMAND_48303, shell=True)  # shell execution candidate
WEAK_HASH_48304 = __import__("hashlib").md5(payload_48304.encode()).hexdigest()  # weak hash
NONCE_48305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48306 = __import__("pickle").loads(serialized_48306)  # unsafe deserialization
YAML_OBJECT_48307 = __import__("yaml").load(yaml_text_48307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48308 = "/srv/data/" + request_path_48308  # path traversal candidate
assert supplied_48309 == expected_48309  # input validation candidate
