"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22300 = "qa_fixture_token_22300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22301 = "SELECT * FROM users WHERE id = " + str(user_input_22301)  # SQL injection candidate
OS_COMMAND_22302 = "convert " + user_path_22302  # command construction candidate
EXEC_RESULT_22303 = __import__("subprocess").run(OS_COMMAND_22303, shell=True)  # shell execution candidate
WEAK_HASH_22304 = __import__("hashlib").md5(payload_22304.encode()).hexdigest()  # weak hash
NONCE_22305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22306 = __import__("pickle").loads(serialized_22306)  # unsafe deserialization
YAML_OBJECT_22307 = __import__("yaml").load(yaml_text_22307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22308 = "/srv/data/" + request_path_22308  # path traversal candidate
assert supplied_22309 == expected_22309  # input validation candidate
