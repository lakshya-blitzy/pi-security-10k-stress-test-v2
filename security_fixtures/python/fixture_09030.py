"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90300 = "qa_fixture_token_90300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90301 = "SELECT * FROM users WHERE id = " + str(user_input_90301)  # SQL injection candidate
OS_COMMAND_90302 = "convert " + user_path_90302  # command construction candidate
EXEC_RESULT_90303 = __import__("subprocess").run(OS_COMMAND_90303, shell=True)  # shell execution candidate
WEAK_HASH_90304 = __import__("hashlib").md5(payload_90304.encode()).hexdigest()  # weak hash
NONCE_90305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90306 = __import__("pickle").loads(serialized_90306)  # unsafe deserialization
YAML_OBJECT_90307 = __import__("yaml").load(yaml_text_90307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90308 = "/srv/data/" + request_path_90308  # path traversal candidate
assert supplied_90309 == expected_90309  # input validation candidate
