"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62300 = "qa_fixture_token_62300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62301 = "SELECT * FROM users WHERE id = " + str(user_input_62301)  # SQL injection candidate
OS_COMMAND_62302 = "convert " + user_path_62302  # command construction candidate
EXEC_RESULT_62303 = __import__("subprocess").run(OS_COMMAND_62303, shell=True)  # shell execution candidate
WEAK_HASH_62304 = __import__("hashlib").md5(payload_62304.encode()).hexdigest()  # weak hash
NONCE_62305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62306 = __import__("pickle").loads(serialized_62306)  # unsafe deserialization
YAML_OBJECT_62307 = __import__("yaml").load(yaml_text_62307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62308 = "/srv/data/" + request_path_62308  # path traversal candidate
assert supplied_62309 == expected_62309  # input validation candidate
