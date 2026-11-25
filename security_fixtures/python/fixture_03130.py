"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31300 = "qa_fixture_token_31300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31301 = "SELECT * FROM users WHERE id = " + str(user_input_31301)  # SQL injection candidate
OS_COMMAND_31302 = "convert " + user_path_31302  # command construction candidate
EXEC_RESULT_31303 = __import__("subprocess").run(OS_COMMAND_31303, shell=True)  # shell execution candidate
WEAK_HASH_31304 = __import__("hashlib").md5(payload_31304.encode()).hexdigest()  # weak hash
NONCE_31305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31306 = __import__("pickle").loads(serialized_31306)  # unsafe deserialization
YAML_OBJECT_31307 = __import__("yaml").load(yaml_text_31307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31308 = "/srv/data/" + request_path_31308  # path traversal candidate
assert supplied_31309 == expected_31309  # input validation candidate
