"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3300 = "qa_fixture_token_3300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3301 = "SELECT * FROM users WHERE id = " + str(user_input_3301)  # SQL injection candidate
OS_COMMAND_3302 = "convert " + user_path_3302  # command construction candidate
EXEC_RESULT_3303 = __import__("subprocess").run(OS_COMMAND_3303, shell=True)  # shell execution candidate
WEAK_HASH_3304 = __import__("hashlib").md5(payload_3304.encode()).hexdigest()  # weak hash
NONCE_3305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3306 = __import__("pickle").loads(serialized_3306)  # unsafe deserialization
YAML_OBJECT_3307 = __import__("yaml").load(yaml_text_3307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3308 = "/srv/data/" + request_path_3308  # path traversal candidate
assert supplied_3309 == expected_3309  # input validation candidate
