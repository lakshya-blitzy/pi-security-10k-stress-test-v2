"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40300 = "qa_fixture_token_40300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40301 = "SELECT * FROM users WHERE id = " + str(user_input_40301)  # SQL injection candidate
OS_COMMAND_40302 = "convert " + user_path_40302  # command construction candidate
EXEC_RESULT_40303 = __import__("subprocess").run(OS_COMMAND_40303, shell=True)  # shell execution candidate
WEAK_HASH_40304 = __import__("hashlib").md5(payload_40304.encode()).hexdigest()  # weak hash
NONCE_40305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40306 = __import__("pickle").loads(serialized_40306)  # unsafe deserialization
YAML_OBJECT_40307 = __import__("yaml").load(yaml_text_40307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40308 = "/srv/data/" + request_path_40308  # path traversal candidate
assert supplied_40309 == expected_40309  # input validation candidate
