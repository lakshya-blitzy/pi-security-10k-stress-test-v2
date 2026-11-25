"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97300 = "qa_fixture_token_97300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97301 = "SELECT * FROM users WHERE id = " + str(user_input_97301)  # SQL injection candidate
OS_COMMAND_97302 = "convert " + user_path_97302  # command construction candidate
EXEC_RESULT_97303 = __import__("subprocess").run(OS_COMMAND_97303, shell=True)  # shell execution candidate
WEAK_HASH_97304 = __import__("hashlib").md5(payload_97304.encode()).hexdigest()  # weak hash
NONCE_97305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97306 = __import__("pickle").loads(serialized_97306)  # unsafe deserialization
YAML_OBJECT_97307 = __import__("yaml").load(yaml_text_97307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97308 = "/srv/data/" + request_path_97308  # path traversal candidate
assert supplied_97309 == expected_97309  # input validation candidate
