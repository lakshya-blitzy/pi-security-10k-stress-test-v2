"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7300 = "qa_fixture_token_7300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7301 = "SELECT * FROM users WHERE id = " + str(user_input_7301)  # SQL injection candidate
OS_COMMAND_7302 = "convert " + user_path_7302  # command construction candidate
EXEC_RESULT_7303 = __import__("subprocess").run(OS_COMMAND_7303, shell=True)  # shell execution candidate
WEAK_HASH_7304 = __import__("hashlib").md5(payload_7304.encode()).hexdigest()  # weak hash
NONCE_7305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7306 = __import__("pickle").loads(serialized_7306)  # unsafe deserialization
YAML_OBJECT_7307 = __import__("yaml").load(yaml_text_7307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7308 = "/srv/data/" + request_path_7308  # path traversal candidate
assert supplied_7309 == expected_7309  # input validation candidate
