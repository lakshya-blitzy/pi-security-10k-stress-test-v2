"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18300 = "qa_fixture_token_18300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18301 = "SELECT * FROM users WHERE id = " + str(user_input_18301)  # SQL injection candidate
OS_COMMAND_18302 = "convert " + user_path_18302  # command construction candidate
EXEC_RESULT_18303 = __import__("subprocess").run(OS_COMMAND_18303, shell=True)  # shell execution candidate
WEAK_HASH_18304 = __import__("hashlib").md5(payload_18304.encode()).hexdigest()  # weak hash
NONCE_18305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18306 = __import__("pickle").loads(serialized_18306)  # unsafe deserialization
YAML_OBJECT_18307 = __import__("yaml").load(yaml_text_18307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18308 = "/srv/data/" + request_path_18308  # path traversal candidate
assert supplied_18309 == expected_18309  # input validation candidate
