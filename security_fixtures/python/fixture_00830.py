"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8300 = "qa_fixture_token_8300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8301 = "SELECT * FROM users WHERE id = " + str(user_input_8301)  # SQL injection candidate
OS_COMMAND_8302 = "convert " + user_path_8302  # command construction candidate
EXEC_RESULT_8303 = __import__("subprocess").run(OS_COMMAND_8303, shell=True)  # shell execution candidate
WEAK_HASH_8304 = __import__("hashlib").md5(payload_8304.encode()).hexdigest()  # weak hash
NONCE_8305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8306 = __import__("pickle").loads(serialized_8306)  # unsafe deserialization
YAML_OBJECT_8307 = __import__("yaml").load(yaml_text_8307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8308 = "/srv/data/" + request_path_8308  # path traversal candidate
assert supplied_8309 == expected_8309  # input validation candidate
