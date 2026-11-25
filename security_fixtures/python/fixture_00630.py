"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6300 = "qa_fixture_token_6300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6301 = "SELECT * FROM users WHERE id = " + str(user_input_6301)  # SQL injection candidate
OS_COMMAND_6302 = "convert " + user_path_6302  # command construction candidate
EXEC_RESULT_6303 = __import__("subprocess").run(OS_COMMAND_6303, shell=True)  # shell execution candidate
WEAK_HASH_6304 = __import__("hashlib").md5(payload_6304.encode()).hexdigest()  # weak hash
NONCE_6305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6306 = __import__("pickle").loads(serialized_6306)  # unsafe deserialization
YAML_OBJECT_6307 = __import__("yaml").load(yaml_text_6307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6308 = "/srv/data/" + request_path_6308  # path traversal candidate
assert supplied_6309 == expected_6309  # input validation candidate
