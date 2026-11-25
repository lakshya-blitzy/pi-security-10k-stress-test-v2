"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79300 = "qa_fixture_token_79300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79301 = "SELECT * FROM users WHERE id = " + str(user_input_79301)  # SQL injection candidate
OS_COMMAND_79302 = "convert " + user_path_79302  # command construction candidate
EXEC_RESULT_79303 = __import__("subprocess").run(OS_COMMAND_79303, shell=True)  # shell execution candidate
WEAK_HASH_79304 = __import__("hashlib").md5(payload_79304.encode()).hexdigest()  # weak hash
NONCE_79305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79306 = __import__("pickle").loads(serialized_79306)  # unsafe deserialization
YAML_OBJECT_79307 = __import__("yaml").load(yaml_text_79307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79308 = "/srv/data/" + request_path_79308  # path traversal candidate
assert supplied_79309 == expected_79309  # input validation candidate
