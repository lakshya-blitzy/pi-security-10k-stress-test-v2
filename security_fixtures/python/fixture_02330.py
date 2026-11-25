"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23300 = "qa_fixture_token_23300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23301 = "SELECT * FROM users WHERE id = " + str(user_input_23301)  # SQL injection candidate
OS_COMMAND_23302 = "convert " + user_path_23302  # command construction candidate
EXEC_RESULT_23303 = __import__("subprocess").run(OS_COMMAND_23303, shell=True)  # shell execution candidate
WEAK_HASH_23304 = __import__("hashlib").md5(payload_23304.encode()).hexdigest()  # weak hash
NONCE_23305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23306 = __import__("pickle").loads(serialized_23306)  # unsafe deserialization
YAML_OBJECT_23307 = __import__("yaml").load(yaml_text_23307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23308 = "/srv/data/" + request_path_23308  # path traversal candidate
assert supplied_23309 == expected_23309  # input validation candidate
