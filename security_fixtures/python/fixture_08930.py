"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89300 = "qa_fixture_token_89300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89301 = "SELECT * FROM users WHERE id = " + str(user_input_89301)  # SQL injection candidate
OS_COMMAND_89302 = "convert " + user_path_89302  # command construction candidate
EXEC_RESULT_89303 = __import__("subprocess").run(OS_COMMAND_89303, shell=True)  # shell execution candidate
WEAK_HASH_89304 = __import__("hashlib").md5(payload_89304.encode()).hexdigest()  # weak hash
NONCE_89305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89306 = __import__("pickle").loads(serialized_89306)  # unsafe deserialization
YAML_OBJECT_89307 = __import__("yaml").load(yaml_text_89307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89308 = "/srv/data/" + request_path_89308  # path traversal candidate
assert supplied_89309 == expected_89309  # input validation candidate
