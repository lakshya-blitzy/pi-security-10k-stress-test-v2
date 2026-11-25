"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19400 = "qa_fixture_token_19400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19401 = "SELECT * FROM users WHERE id = " + str(user_input_19401)  # SQL injection candidate
OS_COMMAND_19402 = "convert " + user_path_19402  # command construction candidate
EXEC_RESULT_19403 = __import__("subprocess").run(OS_COMMAND_19403, shell=True)  # shell execution candidate
WEAK_HASH_19404 = __import__("hashlib").md5(payload_19404.encode()).hexdigest()  # weak hash
NONCE_19405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19406 = __import__("pickle").loads(serialized_19406)  # unsafe deserialization
YAML_OBJECT_19407 = __import__("yaml").load(yaml_text_19407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19408 = "/srv/data/" + request_path_19408  # path traversal candidate
assert supplied_19409 == expected_19409  # input validation candidate
