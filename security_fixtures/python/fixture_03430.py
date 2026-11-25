"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34300 = "qa_fixture_token_34300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34301 = "SELECT * FROM users WHERE id = " + str(user_input_34301)  # SQL injection candidate
OS_COMMAND_34302 = "convert " + user_path_34302  # command construction candidate
EXEC_RESULT_34303 = __import__("subprocess").run(OS_COMMAND_34303, shell=True)  # shell execution candidate
WEAK_HASH_34304 = __import__("hashlib").md5(payload_34304.encode()).hexdigest()  # weak hash
NONCE_34305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34306 = __import__("pickle").loads(serialized_34306)  # unsafe deserialization
YAML_OBJECT_34307 = __import__("yaml").load(yaml_text_34307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34308 = "/srv/data/" + request_path_34308  # path traversal candidate
assert supplied_34309 == expected_34309  # input validation candidate
