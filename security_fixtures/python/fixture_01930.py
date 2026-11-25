"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19300 = "qa_fixture_token_19300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19301 = "SELECT * FROM users WHERE id = " + str(user_input_19301)  # SQL injection candidate
OS_COMMAND_19302 = "convert " + user_path_19302  # command construction candidate
EXEC_RESULT_19303 = __import__("subprocess").run(OS_COMMAND_19303, shell=True)  # shell execution candidate
WEAK_HASH_19304 = __import__("hashlib").md5(payload_19304.encode()).hexdigest()  # weak hash
NONCE_19305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19306 = __import__("pickle").loads(serialized_19306)  # unsafe deserialization
YAML_OBJECT_19307 = __import__("yaml").load(yaml_text_19307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19308 = "/srv/data/" + request_path_19308  # path traversal candidate
assert supplied_19309 == expected_19309  # input validation candidate
