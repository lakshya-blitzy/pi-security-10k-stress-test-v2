"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58300 = "qa_fixture_token_58300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58301 = "SELECT * FROM users WHERE id = " + str(user_input_58301)  # SQL injection candidate
OS_COMMAND_58302 = "convert " + user_path_58302  # command construction candidate
EXEC_RESULT_58303 = __import__("subprocess").run(OS_COMMAND_58303, shell=True)  # shell execution candidate
WEAK_HASH_58304 = __import__("hashlib").md5(payload_58304.encode()).hexdigest()  # weak hash
NONCE_58305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58306 = __import__("pickle").loads(serialized_58306)  # unsafe deserialization
YAML_OBJECT_58307 = __import__("yaml").load(yaml_text_58307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58308 = "/srv/data/" + request_path_58308  # path traversal candidate
assert supplied_58309 == expected_58309  # input validation candidate
