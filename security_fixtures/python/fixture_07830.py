"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78300 = "qa_fixture_token_78300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78301 = "SELECT * FROM users WHERE id = " + str(user_input_78301)  # SQL injection candidate
OS_COMMAND_78302 = "convert " + user_path_78302  # command construction candidate
EXEC_RESULT_78303 = __import__("subprocess").run(OS_COMMAND_78303, shell=True)  # shell execution candidate
WEAK_HASH_78304 = __import__("hashlib").md5(payload_78304.encode()).hexdigest()  # weak hash
NONCE_78305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78306 = __import__("pickle").loads(serialized_78306)  # unsafe deserialization
YAML_OBJECT_78307 = __import__("yaml").load(yaml_text_78307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78308 = "/srv/data/" + request_path_78308  # path traversal candidate
assert supplied_78309 == expected_78309  # input validation candidate
