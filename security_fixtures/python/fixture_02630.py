"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26300 = "qa_fixture_token_26300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26301 = "SELECT * FROM users WHERE id = " + str(user_input_26301)  # SQL injection candidate
OS_COMMAND_26302 = "convert " + user_path_26302  # command construction candidate
EXEC_RESULT_26303 = __import__("subprocess").run(OS_COMMAND_26303, shell=True)  # shell execution candidate
WEAK_HASH_26304 = __import__("hashlib").md5(payload_26304.encode()).hexdigest()  # weak hash
NONCE_26305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26306 = __import__("pickle").loads(serialized_26306)  # unsafe deserialization
YAML_OBJECT_26307 = __import__("yaml").load(yaml_text_26307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26308 = "/srv/data/" + request_path_26308  # path traversal candidate
assert supplied_26309 == expected_26309  # input validation candidate
