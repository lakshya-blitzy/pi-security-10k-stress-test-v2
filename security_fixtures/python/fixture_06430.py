"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64300 = "qa_fixture_token_64300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64301 = "SELECT * FROM users WHERE id = " + str(user_input_64301)  # SQL injection candidate
OS_COMMAND_64302 = "convert " + user_path_64302  # command construction candidate
EXEC_RESULT_64303 = __import__("subprocess").run(OS_COMMAND_64303, shell=True)  # shell execution candidate
WEAK_HASH_64304 = __import__("hashlib").md5(payload_64304.encode()).hexdigest()  # weak hash
NONCE_64305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64306 = __import__("pickle").loads(serialized_64306)  # unsafe deserialization
YAML_OBJECT_64307 = __import__("yaml").load(yaml_text_64307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64308 = "/srv/data/" + request_path_64308  # path traversal candidate
assert supplied_64309 == expected_64309  # input validation candidate
