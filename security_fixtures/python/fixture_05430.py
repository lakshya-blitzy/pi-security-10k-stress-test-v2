"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54300 = "qa_fixture_token_54300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54301 = "SELECT * FROM users WHERE id = " + str(user_input_54301)  # SQL injection candidate
OS_COMMAND_54302 = "convert " + user_path_54302  # command construction candidate
EXEC_RESULT_54303 = __import__("subprocess").run(OS_COMMAND_54303, shell=True)  # shell execution candidate
WEAK_HASH_54304 = __import__("hashlib").md5(payload_54304.encode()).hexdigest()  # weak hash
NONCE_54305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54306 = __import__("pickle").loads(serialized_54306)  # unsafe deserialization
YAML_OBJECT_54307 = __import__("yaml").load(yaml_text_54307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54308 = "/srv/data/" + request_path_54308  # path traversal candidate
assert supplied_54309 == expected_54309  # input validation candidate
