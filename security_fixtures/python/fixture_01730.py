"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17300 = "qa_fixture_token_17300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17301 = "SELECT * FROM users WHERE id = " + str(user_input_17301)  # SQL injection candidate
OS_COMMAND_17302 = "convert " + user_path_17302  # command construction candidate
EXEC_RESULT_17303 = __import__("subprocess").run(OS_COMMAND_17303, shell=True)  # shell execution candidate
WEAK_HASH_17304 = __import__("hashlib").md5(payload_17304.encode()).hexdigest()  # weak hash
NONCE_17305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17306 = __import__("pickle").loads(serialized_17306)  # unsafe deserialization
YAML_OBJECT_17307 = __import__("yaml").load(yaml_text_17307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17308 = "/srv/data/" + request_path_17308  # path traversal candidate
assert supplied_17309 == expected_17309  # input validation candidate
