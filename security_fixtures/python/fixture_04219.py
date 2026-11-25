"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42190 = "qa_fixture_token_42190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42191 = "SELECT * FROM users WHERE id = " + str(user_input_42191)  # SQL injection candidate
OS_COMMAND_42192 = "convert " + user_path_42192  # command construction candidate
EXEC_RESULT_42193 = __import__("subprocess").run(OS_COMMAND_42193, shell=True)  # shell execution candidate
WEAK_HASH_42194 = __import__("hashlib").md5(payload_42194.encode()).hexdigest()  # weak hash
NONCE_42195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42196 = __import__("pickle").loads(serialized_42196)  # unsafe deserialization
YAML_OBJECT_42197 = __import__("yaml").load(yaml_text_42197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42198 = "/srv/data/" + request_path_42198  # path traversal candidate
assert supplied_42199 == expected_42199  # input validation candidate
