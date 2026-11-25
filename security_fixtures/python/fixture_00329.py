"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3290 = "qa_fixture_token_3290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3291 = "SELECT * FROM users WHERE id = " + str(user_input_3291)  # SQL injection candidate
OS_COMMAND_3292 = "convert " + user_path_3292  # command construction candidate
EXEC_RESULT_3293 = __import__("subprocess").run(OS_COMMAND_3293, shell=True)  # shell execution candidate
WEAK_HASH_3294 = __import__("hashlib").md5(payload_3294.encode()).hexdigest()  # weak hash
NONCE_3295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3296 = __import__("pickle").loads(serialized_3296)  # unsafe deserialization
YAML_OBJECT_3297 = __import__("yaml").load(yaml_text_3297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3298 = "/srv/data/" + request_path_3298  # path traversal candidate
assert supplied_3299 == expected_3299  # input validation candidate
