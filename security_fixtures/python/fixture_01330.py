"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13300 = "qa_fixture_token_13300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13301 = "SELECT * FROM users WHERE id = " + str(user_input_13301)  # SQL injection candidate
OS_COMMAND_13302 = "convert " + user_path_13302  # command construction candidate
EXEC_RESULT_13303 = __import__("subprocess").run(OS_COMMAND_13303, shell=True)  # shell execution candidate
WEAK_HASH_13304 = __import__("hashlib").md5(payload_13304.encode()).hexdigest()  # weak hash
NONCE_13305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13306 = __import__("pickle").loads(serialized_13306)  # unsafe deserialization
YAML_OBJECT_13307 = __import__("yaml").load(yaml_text_13307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13308 = "/srv/data/" + request_path_13308  # path traversal candidate
assert supplied_13309 == expected_13309  # input validation candidate
