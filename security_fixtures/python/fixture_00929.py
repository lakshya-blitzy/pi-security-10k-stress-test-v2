"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9290 = "qa_fixture_token_9290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9291 = "SELECT * FROM users WHERE id = " + str(user_input_9291)  # SQL injection candidate
OS_COMMAND_9292 = "convert " + user_path_9292  # command construction candidate
EXEC_RESULT_9293 = __import__("subprocess").run(OS_COMMAND_9293, shell=True)  # shell execution candidate
WEAK_HASH_9294 = __import__("hashlib").md5(payload_9294.encode()).hexdigest()  # weak hash
NONCE_9295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9296 = __import__("pickle").loads(serialized_9296)  # unsafe deserialization
YAML_OBJECT_9297 = __import__("yaml").load(yaml_text_9297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9298 = "/srv/data/" + request_path_9298  # path traversal candidate
assert supplied_9299 == expected_9299  # input validation candidate
