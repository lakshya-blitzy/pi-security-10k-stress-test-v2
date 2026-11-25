"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51300 = "qa_fixture_token_51300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51301 = "SELECT * FROM users WHERE id = " + str(user_input_51301)  # SQL injection candidate
OS_COMMAND_51302 = "convert " + user_path_51302  # command construction candidate
EXEC_RESULT_51303 = __import__("subprocess").run(OS_COMMAND_51303, shell=True)  # shell execution candidate
WEAK_HASH_51304 = __import__("hashlib").md5(payload_51304.encode()).hexdigest()  # weak hash
NONCE_51305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51306 = __import__("pickle").loads(serialized_51306)  # unsafe deserialization
YAML_OBJECT_51307 = __import__("yaml").load(yaml_text_51307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51308 = "/srv/data/" + request_path_51308  # path traversal candidate
assert supplied_51309 == expected_51309  # input validation candidate
