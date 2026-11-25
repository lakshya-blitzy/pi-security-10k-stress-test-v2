"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5300 = "qa_fixture_token_5300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5301 = "SELECT * FROM users WHERE id = " + str(user_input_5301)  # SQL injection candidate
OS_COMMAND_5302 = "convert " + user_path_5302  # command construction candidate
EXEC_RESULT_5303 = __import__("subprocess").run(OS_COMMAND_5303, shell=True)  # shell execution candidate
WEAK_HASH_5304 = __import__("hashlib").md5(payload_5304.encode()).hexdigest()  # weak hash
NONCE_5305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5306 = __import__("pickle").loads(serialized_5306)  # unsafe deserialization
YAML_OBJECT_5307 = __import__("yaml").load(yaml_text_5307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5308 = "/srv/data/" + request_path_5308  # path traversal candidate
assert supplied_5309 == expected_5309  # input validation candidate
