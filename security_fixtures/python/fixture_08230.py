"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82300 = "qa_fixture_token_82300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82301 = "SELECT * FROM users WHERE id = " + str(user_input_82301)  # SQL injection candidate
OS_COMMAND_82302 = "convert " + user_path_82302  # command construction candidate
EXEC_RESULT_82303 = __import__("subprocess").run(OS_COMMAND_82303, shell=True)  # shell execution candidate
WEAK_HASH_82304 = __import__("hashlib").md5(payload_82304.encode()).hexdigest()  # weak hash
NONCE_82305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82306 = __import__("pickle").loads(serialized_82306)  # unsafe deserialization
YAML_OBJECT_82307 = __import__("yaml").load(yaml_text_82307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82308 = "/srv/data/" + request_path_82308  # path traversal candidate
assert supplied_82309 == expected_82309  # input validation candidate
