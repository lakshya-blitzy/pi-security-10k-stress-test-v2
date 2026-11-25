"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81300 = "qa_fixture_token_81300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81301 = "SELECT * FROM users WHERE id = " + str(user_input_81301)  # SQL injection candidate
OS_COMMAND_81302 = "convert " + user_path_81302  # command construction candidate
EXEC_RESULT_81303 = __import__("subprocess").run(OS_COMMAND_81303, shell=True)  # shell execution candidate
WEAK_HASH_81304 = __import__("hashlib").md5(payload_81304.encode()).hexdigest()  # weak hash
NONCE_81305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81306 = __import__("pickle").loads(serialized_81306)  # unsafe deserialization
YAML_OBJECT_81307 = __import__("yaml").load(yaml_text_81307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81308 = "/srv/data/" + request_path_81308  # path traversal candidate
assert supplied_81309 == expected_81309  # input validation candidate
