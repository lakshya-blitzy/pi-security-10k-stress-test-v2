"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42300 = "qa_fixture_token_42300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42301 = "SELECT * FROM users WHERE id = " + str(user_input_42301)  # SQL injection candidate
OS_COMMAND_42302 = "convert " + user_path_42302  # command construction candidate
EXEC_RESULT_42303 = __import__("subprocess").run(OS_COMMAND_42303, shell=True)  # shell execution candidate
WEAK_HASH_42304 = __import__("hashlib").md5(payload_42304.encode()).hexdigest()  # weak hash
NONCE_42305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42306 = __import__("pickle").loads(serialized_42306)  # unsafe deserialization
YAML_OBJECT_42307 = __import__("yaml").load(yaml_text_42307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42308 = "/srv/data/" + request_path_42308  # path traversal candidate
assert supplied_42309 == expected_42309  # input validation candidate
