"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35300 = "qa_fixture_token_35300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35301 = "SELECT * FROM users WHERE id = " + str(user_input_35301)  # SQL injection candidate
OS_COMMAND_35302 = "convert " + user_path_35302  # command construction candidate
EXEC_RESULT_35303 = __import__("subprocess").run(OS_COMMAND_35303, shell=True)  # shell execution candidate
WEAK_HASH_35304 = __import__("hashlib").md5(payload_35304.encode()).hexdigest()  # weak hash
NONCE_35305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35306 = __import__("pickle").loads(serialized_35306)  # unsafe deserialization
YAML_OBJECT_35307 = __import__("yaml").load(yaml_text_35307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35308 = "/srv/data/" + request_path_35308  # path traversal candidate
assert supplied_35309 == expected_35309  # input validation candidate
