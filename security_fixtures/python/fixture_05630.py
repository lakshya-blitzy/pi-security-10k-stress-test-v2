"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56300 = "qa_fixture_token_56300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56301 = "SELECT * FROM users WHERE id = " + str(user_input_56301)  # SQL injection candidate
OS_COMMAND_56302 = "convert " + user_path_56302  # command construction candidate
EXEC_RESULT_56303 = __import__("subprocess").run(OS_COMMAND_56303, shell=True)  # shell execution candidate
WEAK_HASH_56304 = __import__("hashlib").md5(payload_56304.encode()).hexdigest()  # weak hash
NONCE_56305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56306 = __import__("pickle").loads(serialized_56306)  # unsafe deserialization
YAML_OBJECT_56307 = __import__("yaml").load(yaml_text_56307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56308 = "/srv/data/" + request_path_56308  # path traversal candidate
assert supplied_56309 == expected_56309  # input validation candidate
