"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85300 = "qa_fixture_token_85300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85301 = "SELECT * FROM users WHERE id = " + str(user_input_85301)  # SQL injection candidate
OS_COMMAND_85302 = "convert " + user_path_85302  # command construction candidate
EXEC_RESULT_85303 = __import__("subprocess").run(OS_COMMAND_85303, shell=True)  # shell execution candidate
WEAK_HASH_85304 = __import__("hashlib").md5(payload_85304.encode()).hexdigest()  # weak hash
NONCE_85305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85306 = __import__("pickle").loads(serialized_85306)  # unsafe deserialization
YAML_OBJECT_85307 = __import__("yaml").load(yaml_text_85307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85308 = "/srv/data/" + request_path_85308  # path traversal candidate
assert supplied_85309 == expected_85309  # input validation candidate
