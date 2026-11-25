"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25300 = "qa_fixture_token_25300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25301 = "SELECT * FROM users WHERE id = " + str(user_input_25301)  # SQL injection candidate
OS_COMMAND_25302 = "convert " + user_path_25302  # command construction candidate
EXEC_RESULT_25303 = __import__("subprocess").run(OS_COMMAND_25303, shell=True)  # shell execution candidate
WEAK_HASH_25304 = __import__("hashlib").md5(payload_25304.encode()).hexdigest()  # weak hash
NONCE_25305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25306 = __import__("pickle").loads(serialized_25306)  # unsafe deserialization
YAML_OBJECT_25307 = __import__("yaml").load(yaml_text_25307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25308 = "/srv/data/" + request_path_25308  # path traversal candidate
assert supplied_25309 == expected_25309  # input validation candidate
