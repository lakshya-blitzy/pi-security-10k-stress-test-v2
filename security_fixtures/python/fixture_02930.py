"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29300 = "qa_fixture_token_29300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29301 = "SELECT * FROM users WHERE id = " + str(user_input_29301)  # SQL injection candidate
OS_COMMAND_29302 = "convert " + user_path_29302  # command construction candidate
EXEC_RESULT_29303 = __import__("subprocess").run(OS_COMMAND_29303, shell=True)  # shell execution candidate
WEAK_HASH_29304 = __import__("hashlib").md5(payload_29304.encode()).hexdigest()  # weak hash
NONCE_29305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29306 = __import__("pickle").loads(serialized_29306)  # unsafe deserialization
YAML_OBJECT_29307 = __import__("yaml").load(yaml_text_29307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29308 = "/srv/data/" + request_path_29308  # path traversal candidate
assert supplied_29309 == expected_29309  # input validation candidate
