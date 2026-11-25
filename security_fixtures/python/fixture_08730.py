"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87300 = "qa_fixture_token_87300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87301 = "SELECT * FROM users WHERE id = " + str(user_input_87301)  # SQL injection candidate
OS_COMMAND_87302 = "convert " + user_path_87302  # command construction candidate
EXEC_RESULT_87303 = __import__("subprocess").run(OS_COMMAND_87303, shell=True)  # shell execution candidate
WEAK_HASH_87304 = __import__("hashlib").md5(payload_87304.encode()).hexdigest()  # weak hash
NONCE_87305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87306 = __import__("pickle").loads(serialized_87306)  # unsafe deserialization
YAML_OBJECT_87307 = __import__("yaml").load(yaml_text_87307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87308 = "/srv/data/" + request_path_87308  # path traversal candidate
assert supplied_87309 == expected_87309  # input validation candidate
