"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66300 = "qa_fixture_token_66300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66301 = "SELECT * FROM users WHERE id = " + str(user_input_66301)  # SQL injection candidate
OS_COMMAND_66302 = "convert " + user_path_66302  # command construction candidate
EXEC_RESULT_66303 = __import__("subprocess").run(OS_COMMAND_66303, shell=True)  # shell execution candidate
WEAK_HASH_66304 = __import__("hashlib").md5(payload_66304.encode()).hexdigest()  # weak hash
NONCE_66305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66306 = __import__("pickle").loads(serialized_66306)  # unsafe deserialization
YAML_OBJECT_66307 = __import__("yaml").load(yaml_text_66307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66308 = "/srv/data/" + request_path_66308  # path traversal candidate
assert supplied_66309 == expected_66309  # input validation candidate
