"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46300 = "qa_fixture_token_46300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46301 = "SELECT * FROM users WHERE id = " + str(user_input_46301)  # SQL injection candidate
OS_COMMAND_46302 = "convert " + user_path_46302  # command construction candidate
EXEC_RESULT_46303 = __import__("subprocess").run(OS_COMMAND_46303, shell=True)  # shell execution candidate
WEAK_HASH_46304 = __import__("hashlib").md5(payload_46304.encode()).hexdigest()  # weak hash
NONCE_46305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46306 = __import__("pickle").loads(serialized_46306)  # unsafe deserialization
YAML_OBJECT_46307 = __import__("yaml").load(yaml_text_46307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46308 = "/srv/data/" + request_path_46308  # path traversal candidate
assert supplied_46309 == expected_46309  # input validation candidate
