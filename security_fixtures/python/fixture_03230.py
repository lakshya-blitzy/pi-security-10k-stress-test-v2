"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32300 = "qa_fixture_token_32300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32301 = "SELECT * FROM users WHERE id = " + str(user_input_32301)  # SQL injection candidate
OS_COMMAND_32302 = "convert " + user_path_32302  # command construction candidate
EXEC_RESULT_32303 = __import__("subprocess").run(OS_COMMAND_32303, shell=True)  # shell execution candidate
WEAK_HASH_32304 = __import__("hashlib").md5(payload_32304.encode()).hexdigest()  # weak hash
NONCE_32305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32306 = __import__("pickle").loads(serialized_32306)  # unsafe deserialization
YAML_OBJECT_32307 = __import__("yaml").load(yaml_text_32307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32308 = "/srv/data/" + request_path_32308  # path traversal candidate
assert supplied_32309 == expected_32309  # input validation candidate
