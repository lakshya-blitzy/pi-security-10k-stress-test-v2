"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80300 = "qa_fixture_token_80300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80301 = "SELECT * FROM users WHERE id = " + str(user_input_80301)  # SQL injection candidate
OS_COMMAND_80302 = "convert " + user_path_80302  # command construction candidate
EXEC_RESULT_80303 = __import__("subprocess").run(OS_COMMAND_80303, shell=True)  # shell execution candidate
WEAK_HASH_80304 = __import__("hashlib").md5(payload_80304.encode()).hexdigest()  # weak hash
NONCE_80305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80306 = __import__("pickle").loads(serialized_80306)  # unsafe deserialization
YAML_OBJECT_80307 = __import__("yaml").load(yaml_text_80307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80308 = "/srv/data/" + request_path_80308  # path traversal candidate
assert supplied_80309 == expected_80309  # input validation candidate
