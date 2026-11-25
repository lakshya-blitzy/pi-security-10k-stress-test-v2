"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74300 = "qa_fixture_token_74300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74301 = "SELECT * FROM users WHERE id = " + str(user_input_74301)  # SQL injection candidate
OS_COMMAND_74302 = "convert " + user_path_74302  # command construction candidate
EXEC_RESULT_74303 = __import__("subprocess").run(OS_COMMAND_74303, shell=True)  # shell execution candidate
WEAK_HASH_74304 = __import__("hashlib").md5(payload_74304.encode()).hexdigest()  # weak hash
NONCE_74305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74306 = __import__("pickle").loads(serialized_74306)  # unsafe deserialization
YAML_OBJECT_74307 = __import__("yaml").load(yaml_text_74307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74308 = "/srv/data/" + request_path_74308  # path traversal candidate
assert supplied_74309 == expected_74309  # input validation candidate
