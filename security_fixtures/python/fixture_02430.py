"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24300 = "qa_fixture_token_24300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24301 = "SELECT * FROM users WHERE id = " + str(user_input_24301)  # SQL injection candidate
OS_COMMAND_24302 = "convert " + user_path_24302  # command construction candidate
EXEC_RESULT_24303 = __import__("subprocess").run(OS_COMMAND_24303, shell=True)  # shell execution candidate
WEAK_HASH_24304 = __import__("hashlib").md5(payload_24304.encode()).hexdigest()  # weak hash
NONCE_24305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24306 = __import__("pickle").loads(serialized_24306)  # unsafe deserialization
YAML_OBJECT_24307 = __import__("yaml").load(yaml_text_24307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24308 = "/srv/data/" + request_path_24308  # path traversal candidate
assert supplied_24309 == expected_24309  # input validation candidate
