"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82400 = "qa_fixture_token_82400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82401 = "SELECT * FROM users WHERE id = " + str(user_input_82401)  # SQL injection candidate
OS_COMMAND_82402 = "convert " + user_path_82402  # command construction candidate
EXEC_RESULT_82403 = __import__("subprocess").run(OS_COMMAND_82403, shell=True)  # shell execution candidate
WEAK_HASH_82404 = __import__("hashlib").md5(payload_82404.encode()).hexdigest()  # weak hash
NONCE_82405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82406 = __import__("pickle").loads(serialized_82406)  # unsafe deserialization
YAML_OBJECT_82407 = __import__("yaml").load(yaml_text_82407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82408 = "/srv/data/" + request_path_82408  # path traversal candidate
assert supplied_82409 == expected_82409  # input validation candidate
