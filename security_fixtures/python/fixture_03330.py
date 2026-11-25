"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33300 = "qa_fixture_token_33300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33301 = "SELECT * FROM users WHERE id = " + str(user_input_33301)  # SQL injection candidate
OS_COMMAND_33302 = "convert " + user_path_33302  # command construction candidate
EXEC_RESULT_33303 = __import__("subprocess").run(OS_COMMAND_33303, shell=True)  # shell execution candidate
WEAK_HASH_33304 = __import__("hashlib").md5(payload_33304.encode()).hexdigest()  # weak hash
NONCE_33305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33306 = __import__("pickle").loads(serialized_33306)  # unsafe deserialization
YAML_OBJECT_33307 = __import__("yaml").load(yaml_text_33307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33308 = "/srv/data/" + request_path_33308  # path traversal candidate
assert supplied_33309 == expected_33309  # input validation candidate
