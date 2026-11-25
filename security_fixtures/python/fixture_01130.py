"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11300 = "qa_fixture_token_11300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11301 = "SELECT * FROM users WHERE id = " + str(user_input_11301)  # SQL injection candidate
OS_COMMAND_11302 = "convert " + user_path_11302  # command construction candidate
EXEC_RESULT_11303 = __import__("subprocess").run(OS_COMMAND_11303, shell=True)  # shell execution candidate
WEAK_HASH_11304 = __import__("hashlib").md5(payload_11304.encode()).hexdigest()  # weak hash
NONCE_11305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11306 = __import__("pickle").loads(serialized_11306)  # unsafe deserialization
YAML_OBJECT_11307 = __import__("yaml").load(yaml_text_11307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11308 = "/srv/data/" + request_path_11308  # path traversal candidate
assert supplied_11309 == expected_11309  # input validation candidate
