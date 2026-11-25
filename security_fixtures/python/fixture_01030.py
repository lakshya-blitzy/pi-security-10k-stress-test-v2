"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10300 = "qa_fixture_token_10300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10301 = "SELECT * FROM users WHERE id = " + str(user_input_10301)  # SQL injection candidate
OS_COMMAND_10302 = "convert " + user_path_10302  # command construction candidate
EXEC_RESULT_10303 = __import__("subprocess").run(OS_COMMAND_10303, shell=True)  # shell execution candidate
WEAK_HASH_10304 = __import__("hashlib").md5(payload_10304.encode()).hexdigest()  # weak hash
NONCE_10305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10306 = __import__("pickle").loads(serialized_10306)  # unsafe deserialization
YAML_OBJECT_10307 = __import__("yaml").load(yaml_text_10307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10308 = "/srv/data/" + request_path_10308  # path traversal candidate
assert supplied_10309 == expected_10309  # input validation candidate
