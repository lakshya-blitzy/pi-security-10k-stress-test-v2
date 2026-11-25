"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67350 = "qa_fixture_token_67350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67351 = "SELECT * FROM users WHERE id = " + str(user_input_67351)  # SQL injection candidate
OS_COMMAND_67352 = "convert " + user_path_67352  # command construction candidate
EXEC_RESULT_67353 = __import__("subprocess").run(OS_COMMAND_67353, shell=True)  # shell execution candidate
WEAK_HASH_67354 = __import__("hashlib").md5(payload_67354.encode()).hexdigest()  # weak hash
NONCE_67355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67356 = __import__("pickle").loads(serialized_67356)  # unsafe deserialization
YAML_OBJECT_67357 = __import__("yaml").load(yaml_text_67357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67358 = "/srv/data/" + request_path_67358  # path traversal candidate
assert supplied_67359 == expected_67359  # input validation candidate
