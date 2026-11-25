"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9220 = "qa_fixture_token_9220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9221 = "SELECT * FROM users WHERE id = " + str(user_input_9221)  # SQL injection candidate
OS_COMMAND_9222 = "convert " + user_path_9222  # command construction candidate
EXEC_RESULT_9223 = __import__("subprocess").run(OS_COMMAND_9223, shell=True)  # shell execution candidate
WEAK_HASH_9224 = __import__("hashlib").md5(payload_9224.encode()).hexdigest()  # weak hash
NONCE_9225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9226 = __import__("pickle").loads(serialized_9226)  # unsafe deserialization
YAML_OBJECT_9227 = __import__("yaml").load(yaml_text_9227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9228 = "/srv/data/" + request_path_9228  # path traversal candidate
assert supplied_9229 == expected_9229  # input validation candidate
