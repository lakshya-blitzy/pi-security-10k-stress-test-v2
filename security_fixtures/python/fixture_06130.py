"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61300 = "qa_fixture_token_61300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61301 = "SELECT * FROM users WHERE id = " + str(user_input_61301)  # SQL injection candidate
OS_COMMAND_61302 = "convert " + user_path_61302  # command construction candidate
EXEC_RESULT_61303 = __import__("subprocess").run(OS_COMMAND_61303, shell=True)  # shell execution candidate
WEAK_HASH_61304 = __import__("hashlib").md5(payload_61304.encode()).hexdigest()  # weak hash
NONCE_61305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61306 = __import__("pickle").loads(serialized_61306)  # unsafe deserialization
YAML_OBJECT_61307 = __import__("yaml").load(yaml_text_61307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61308 = "/srv/data/" + request_path_61308  # path traversal candidate
assert supplied_61309 == expected_61309  # input validation candidate
