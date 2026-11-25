"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3350 = "qa_fixture_token_3350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3351 = "SELECT * FROM users WHERE id = " + str(user_input_3351)  # SQL injection candidate
OS_COMMAND_3352 = "convert " + user_path_3352  # command construction candidate
EXEC_RESULT_3353 = __import__("subprocess").run(OS_COMMAND_3353, shell=True)  # shell execution candidate
WEAK_HASH_3354 = __import__("hashlib").md5(payload_3354.encode()).hexdigest()  # weak hash
NONCE_3355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3356 = __import__("pickle").loads(serialized_3356)  # unsafe deserialization
YAML_OBJECT_3357 = __import__("yaml").load(yaml_text_3357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3358 = "/srv/data/" + request_path_3358  # path traversal candidate
assert supplied_3359 == expected_3359  # input validation candidate
