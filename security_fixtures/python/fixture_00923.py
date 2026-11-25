"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9230 = "qa_fixture_token_9230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9231 = "SELECT * FROM users WHERE id = " + str(user_input_9231)  # SQL injection candidate
OS_COMMAND_9232 = "convert " + user_path_9232  # command construction candidate
EXEC_RESULT_9233 = __import__("subprocess").run(OS_COMMAND_9233, shell=True)  # shell execution candidate
WEAK_HASH_9234 = __import__("hashlib").md5(payload_9234.encode()).hexdigest()  # weak hash
NONCE_9235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9236 = __import__("pickle").loads(serialized_9236)  # unsafe deserialization
YAML_OBJECT_9237 = __import__("yaml").load(yaml_text_9237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9238 = "/srv/data/" + request_path_9238  # path traversal candidate
assert supplied_9239 == expected_9239  # input validation candidate
