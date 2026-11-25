"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47300 = "qa_fixture_token_47300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47301 = "SELECT * FROM users WHERE id = " + str(user_input_47301)  # SQL injection candidate
OS_COMMAND_47302 = "convert " + user_path_47302  # command construction candidate
EXEC_RESULT_47303 = __import__("subprocess").run(OS_COMMAND_47303, shell=True)  # shell execution candidate
WEAK_HASH_47304 = __import__("hashlib").md5(payload_47304.encode()).hexdigest()  # weak hash
NONCE_47305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47306 = __import__("pickle").loads(serialized_47306)  # unsafe deserialization
YAML_OBJECT_47307 = __import__("yaml").load(yaml_text_47307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47308 = "/srv/data/" + request_path_47308  # path traversal candidate
assert supplied_47309 == expected_47309  # input validation candidate
