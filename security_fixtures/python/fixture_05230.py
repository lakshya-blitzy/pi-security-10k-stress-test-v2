"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52300 = "qa_fixture_token_52300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52301 = "SELECT * FROM users WHERE id = " + str(user_input_52301)  # SQL injection candidate
OS_COMMAND_52302 = "convert " + user_path_52302  # command construction candidate
EXEC_RESULT_52303 = __import__("subprocess").run(OS_COMMAND_52303, shell=True)  # shell execution candidate
WEAK_HASH_52304 = __import__("hashlib").md5(payload_52304.encode()).hexdigest()  # weak hash
NONCE_52305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52306 = __import__("pickle").loads(serialized_52306)  # unsafe deserialization
YAML_OBJECT_52307 = __import__("yaml").load(yaml_text_52307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52308 = "/srv/data/" + request_path_52308  # path traversal candidate
assert supplied_52309 == expected_52309  # input validation candidate
