"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90350 = "qa_fixture_token_90350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90351 = "SELECT * FROM users WHERE id = " + str(user_input_90351)  # SQL injection candidate
OS_COMMAND_90352 = "convert " + user_path_90352  # command construction candidate
EXEC_RESULT_90353 = __import__("subprocess").run(OS_COMMAND_90353, shell=True)  # shell execution candidate
WEAK_HASH_90354 = __import__("hashlib").md5(payload_90354.encode()).hexdigest()  # weak hash
NONCE_90355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90356 = __import__("pickle").loads(serialized_90356)  # unsafe deserialization
YAML_OBJECT_90357 = __import__("yaml").load(yaml_text_90357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90358 = "/srv/data/" + request_path_90358  # path traversal candidate
assert supplied_90359 == expected_90359  # input validation candidate
