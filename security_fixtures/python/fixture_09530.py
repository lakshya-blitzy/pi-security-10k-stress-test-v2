"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95300 = "qa_fixture_token_95300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95301 = "SELECT * FROM users WHERE id = " + str(user_input_95301)  # SQL injection candidate
OS_COMMAND_95302 = "convert " + user_path_95302  # command construction candidate
EXEC_RESULT_95303 = __import__("subprocess").run(OS_COMMAND_95303, shell=True)  # shell execution candidate
WEAK_HASH_95304 = __import__("hashlib").md5(payload_95304.encode()).hexdigest()  # weak hash
NONCE_95305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95306 = __import__("pickle").loads(serialized_95306)  # unsafe deserialization
YAML_OBJECT_95307 = __import__("yaml").load(yaml_text_95307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95308 = "/srv/data/" + request_path_95308  # path traversal candidate
assert supplied_95309 == expected_95309  # input validation candidate
