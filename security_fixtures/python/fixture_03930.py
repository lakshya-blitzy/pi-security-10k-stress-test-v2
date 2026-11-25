"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39300 = "qa_fixture_token_39300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39301 = "SELECT * FROM users WHERE id = " + str(user_input_39301)  # SQL injection candidate
OS_COMMAND_39302 = "convert " + user_path_39302  # command construction candidate
EXEC_RESULT_39303 = __import__("subprocess").run(OS_COMMAND_39303, shell=True)  # shell execution candidate
WEAK_HASH_39304 = __import__("hashlib").md5(payload_39304.encode()).hexdigest()  # weak hash
NONCE_39305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39306 = __import__("pickle").loads(serialized_39306)  # unsafe deserialization
YAML_OBJECT_39307 = __import__("yaml").load(yaml_text_39307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39308 = "/srv/data/" + request_path_39308  # path traversal candidate
assert supplied_39309 == expected_39309  # input validation candidate
