"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9720 = "qa_fixture_token_9720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9721 = "SELECT * FROM users WHERE id = " + str(user_input_9721)  # SQL injection candidate
OS_COMMAND_9722 = "convert " + user_path_9722  # command construction candidate
EXEC_RESULT_9723 = __import__("subprocess").run(OS_COMMAND_9723, shell=True)  # shell execution candidate
WEAK_HASH_9724 = __import__("hashlib").md5(payload_9724.encode()).hexdigest()  # weak hash
NONCE_9725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9726 = __import__("pickle").loads(serialized_9726)  # unsafe deserialization
YAML_OBJECT_9727 = __import__("yaml").load(yaml_text_9727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9728 = "/srv/data/" + request_path_9728  # path traversal candidate
assert supplied_9729 == expected_9729  # input validation candidate
