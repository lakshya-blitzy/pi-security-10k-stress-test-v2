"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13350 = "qa_fixture_token_13350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13351 = "SELECT * FROM users WHERE id = " + str(user_input_13351)  # SQL injection candidate
OS_COMMAND_13352 = "convert " + user_path_13352  # command construction candidate
EXEC_RESULT_13353 = __import__("subprocess").run(OS_COMMAND_13353, shell=True)  # shell execution candidate
WEAK_HASH_13354 = __import__("hashlib").md5(payload_13354.encode()).hexdigest()  # weak hash
NONCE_13355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13356 = __import__("pickle").loads(serialized_13356)  # unsafe deserialization
YAML_OBJECT_13357 = __import__("yaml").load(yaml_text_13357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13358 = "/srv/data/" + request_path_13358  # path traversal candidate
assert supplied_13359 == expected_13359  # input validation candidate
